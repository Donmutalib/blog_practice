from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from urllib import request 
from django.shortcuts import render, redirect
from .models import Blog
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_protect



def index(request):
    return render(request, 'blog_practice_app/index.html')


class BlogList(LoginRequiredMixin, ListView):
    
    model = Blog

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = context['object_list'].filter(user=self.request.user)
        return context


class BlogDetail(LoginRequiredMixin, DetailView):
    model = Blog


class BlogCreate(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ['title', 'text']
    success_url = reverse_lazy('blog_practice_app:blogs')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BlogCreate, self).form_valid(form)


class BlogUpdate(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ['title', 'text']
    success_url = reverse_lazy('blog_practice_app:blogs')


class BlogDelete(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('blog_practice_app:blogs')


class CustomLoginView(LoginView):
    template_name = 'blog_practice_app/login.html'
    fields = '__all__'
    redirect_authenticated_user  = True

    def get_success_url(self):
        return reverse_lazy('blog_practice_app:index')


@csrf_protect
def register(request):
    
    if request.method != 'POST':
        form = UserCreationForm()

    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('blog_practice_app:index')

        
    context = {'form': form}
    return render(request, 'blog_practice_app/register.html', context)

        

        







