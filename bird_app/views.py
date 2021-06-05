from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, ListView
from .forms import CustomUserCreationForm, PostForm
from .models import CustomUser, Post
from django.contrib.postgres.search import SearchVector

class UserDetailView(DetailView):
    template_name = 'user_detail.html'
    model = CustomUser
    context_object_name = 'customUser'


# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class PostListView(ListView):
    model = Post
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'home.html'


class PostCreateView(View):
    form_class = PostForm
    template_name = 'postCreate.html'
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            body = form.cleaned_data.get('body')
            authorID = request.user.id
            userC = CustomUser.objects.get(pk=authorID)
            post = Post(authorID=userC, title=title, body=body)
            post.save()
            return redirect('/')
        return render(request, self.template_name, {'form' : form})
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form' : form})

class SearchView(ListView):
    def get(self, request, *args, **kwargs):
        query = request.GET['search']
        results = Post.objects.annotate(search=SearchVector('title', 'body'),).filter(search=query)
        return render(request, 'search_post.html', {'results': results, 'query' : query}, )