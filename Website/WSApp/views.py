from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Article
from .forms import *


def index(request):
    articles = Article.objects.order_by('-created_date')
    context = {
        'articles': articles,
    }
    return render(request, 'WSApp/index.html', context)


def description(request, id_art):
    article = Article.objects.get(id=id_art)
    context = {
        'article': article,
    }
    return render(request, 'WSApp/description.html', context)


class add_post(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Article
    template_name = 'WSApp/add-post.html'
    success_url = reverse_lazy('home')
    form_class = AddPostForm


class update_post(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Article
    template_name = 'WSApp/update-post.html'
    form_class = AddPostForm
    success_url = reverse_lazy('edit_page')
    success_msg = 'Запись успешно обновлена'

    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)


class del_post(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Article
    template_name = 'WSApp/index.html'
    success_url = reverse_lazy('home')
    success_msg = 'Запись удалена'
    def post(self,request,*args,**kwargs):
        messages.success(self.request, self.success_msg)
        return super().post(request)


class MyLoginView(LoginView):
    template_name = 'WSApp/login-page.html'
    success_url = reverse_lazy('home')
    form_class = MyLoginForm

    def get_success_url(self):
        return self.success_url


class MyAuthView(CreateView):
    model = User
    template_name = 'WSApp/auth-page.html'
    success_url = reverse_lazy('home')
    form_class = MyAuthForm
    success_msg = 'User was added'

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        auth_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        login(self.request, auth_user)
        return form_valid


class MyLogOutView(LogoutView):
    next_page = reverse_lazy('home')
