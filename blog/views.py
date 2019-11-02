from django.shortcuts import render , reverse
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Blog

# Create your views here.
def index(request):
    context = {
        'blogs' : Blog.objects.all()
    }
    return render(request, 'blog/home.html', context)

class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'

    ordering = ['-published_date']

class BlogDetailedView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ['blog_title','blog_type','feautured_image','blog_content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blogdetail', kwargs={'pk': self.object.id})

class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    fields = ['blog_title','blog_type','feautured_image','blog_content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        blog = self.get_object()
        return self.request.user.id == blog.author.id

    def get_success_url(self):
        return reverse('blogdetail', kwargs={'pk': self.object.id})

class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    success_url = '/blog'

    def test_func(self):
        blog = self.get_object()
        return self.request.user.id == blog.author.id
