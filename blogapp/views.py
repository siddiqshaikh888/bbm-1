from .models import BlogModel,CommentModel
from .forms import SearchForm,CommentForm,PostForm
from django.views.generic import ListView, DetailView, CreateView #, UpdateView
from django.shortcuts import render,redirect
 
def BlogListView(request):
    dataset = BlogModel.objects.all()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            blog_title = form.cleaned_data['blog_title']
            blog = BlogModel.objects.get(blog_title)
            return redirect(f'/blog/{blog.id}')
    else:
        form = SearchForm()
        context = {
            'dataset':dataset,
            'form':form,
        }
    return render(request,'blogapp/listview.html',context)

def Blog(request): 
    return render(request,'blog.html')   
#def BlogListView(request):
    #dataset = None
    #categories = Category.get_all_categories()
    #categoryID = request.GET.get('category')
    #if categoryID:
    #    categories = Category.get_all_categories_by_id(categoryID)
    #else:
    #    dataset = BlogModel.objects.all()
   # if request.method == 'POST':
       # form = SearchForm(request.POST)
       # if form.is_valid():
            
      #      title = form.cleaned_data['title']
     #       blog = BlogModel.objects.get(blog_title=title)
     #       return redirect(f'/blog/{blog.id}')
    #else:
    #    form = SearchForm()
    #    context = {
    #        'dataset':dataset,
   #         'form':form,
  #      }
    
 #   return render(request,'blogapp/listview.html',context)
  
 
def BlogDetailView(request,_id):
    try:
        data =BlogModel.objects.get(id =_id)
        comments = CommentModel.objects.filter(blog = data)
        blog_object=BlogModel.objects.get(id = _id)
        #blog_object=blog_views=blog_object.blog_views+1
        blog_object.save()
    except BlogModel.DoesNotExist:
         raise Http404('Data does not exist')
     
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment = CommentModel(your_name= form.cleaned_data['your_name'],
            comment_text=form.cleaned_data['comment_text'],
            blog=data)
            Comment.save()
            return redirect(f'/{_id}')
    else:
        form = CommentForm()
 
    context = {
            'data':data,
            'form':form,
            'comments':comments,
        }
    return render(request,'blogapp/detailview.html',context)
    
class AddPostView(CreateView):
    form_class = PostForm
    model = BlogModel
    template_name = 'blogapp/addblog.html'
    #fields = '__all__'
    #fields = ('blog_title','blog','Category_name','header_image')

#class BlogDetailView(DetailView):
#    model = BlogModel
#    template_name = 'blogapp/details.html'

class HomeView(ListView):
    model = BlogModel
    template_name = 'blogapp/all_blogs.html'


#class UpdatePostView(UpdateView):
 #   model = BlogModel
 #   template_name = 'editblog.html'
 #   fields = ['blog_title','blog','author','Category_name','blog_views']
