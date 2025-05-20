import os
from .models import Post, Website
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import  ListView, DetailView, CreateView, UpdateView,DeleteView,View 
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import logging

logger = logging.getLogger(__name__)

@method_decorator(csrf_exempt, name='dispatch')
class ImageUploadView(View):
    def post(self, request, *args, **kwargs):
        print("ImageUploadView POST request received")
        
        # Use Cloudinary storage directly instead of default_storage
        from cloudinary_storage.storage import MediaCloudinaryStorage
        cloudinary_storage = MediaCloudinaryStorage()
        
        image_file = request.FILES.get('file')
        if image_file:
            try:
                file_path = cloudinary_storage.save(f'images/{image_file.name}', image_file)
                file_url = cloudinary_storage.url(file_path)
                print("Uploaded to Cloudinary:", file_url)
                return JsonResponse({'location': file_url})
            except Exception as e:
                print("Cloudinary upload error:", str(e))
                return JsonResponse({'error': str(e)}, status=500)
        return JsonResponse({'error': 'No file uploaded'}, status=400)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        # Get the search query from the request
        q = self.request.GET.get('q', '')

        if q:
            # Filter posts by title, content, or author's username
            return Post.objects.filter(
                Q(title__icontains=q) |
                Q(content__icontains=q) |
                Q(author__username__icontains=q)
            ).order_by('-date_posted')
        else:
            # If no search query, return all posts ordered by date
            return Post.objects.all().order_by('-date_posted')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')  # Pass 'q' to the template

        # Add the total post count to the context
        context['post_count'] = self.get_queryset().count()
        return context


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'     #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'     
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'}) 


def website(request):
    return render(request, 'blog/pageweb.html')
