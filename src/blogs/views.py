from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.urls import reverse
from .models import Blogs
from .form import BlogsModelForm
from django.views.generic import (
    CreateView,
    DetailView,
    DeleteView,
    ListView,
    UpdateView
)

# Base VIEW class = VIEW
# Raw Function Based
class BlogView(View): 
    template_name="base.html"
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name,{})


# Class based VIEWS
class CreatePostView(CreateView):
    template_name = "blogs/create_post.html"
    form_class = BlogsModelForm
    queryset=Blogs.objects.all()

    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('Blogs:create-post')

class PostDetailView(DetailView):
    template_name = "blogs/check_post.html"
    queryset=Blogs.objects.all()

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Blogs,id=id_)

class UpdatePostView(UpdateView):
    template_name = "blogs/create_post.html"
    form_class = BlogsModelForm
    queryset=Blogs.objects.all()

    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Blogs,id=id_)


class DeletePostView(DeleteView):
    template_name = "blogs/delete_post.html"
    queryset=Blogs.objects.all()    

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Blogs,id=id_)
    def get_success_url(self):
        return reverse('Blogs:list-post')


class ListPostView(ListView):
    template_name = "blogs/list_post.html"
    queryset=Blogs.objects.all()

# raw function based views
class PostDeleteView(View):
    template_name = 'blogs/remove_post.html'
    
    def get_success_url(self):
        return reverse('Blogs:list-post')

    def get_object(self):
        id_ = self.kwargs.get("id")
        obj=None
        if id_ is not None:
            obj=get_object_or_404(Blogs,id=id_)
        return obj
    
    def get(self,request,id=None,*args,**kwargs):
        context={}
        obj=self.get_object()
        if obj is not None:
            context['object']=obj
        return render(request,self.template_name,context)
    
    def post(self,request,id=None,*args,**kwargs):
        context={}
        obj=self.get_object()
        if obj is not None:
            obj.delete()
            context['object'] : obj
            return redirect(self.get_success_url())
        return render(request,self.template_name,context)
    