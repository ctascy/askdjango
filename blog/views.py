from django.shortcuts import render
from django.views.generic import TemplateView
from blog.models import Post
from blog.forms import CommentForm
from django.shortcuts import redirect

# Create your views here.
# index = TemplateView.as_view(template_name='blog/index.html')

# def index(request):
#     #blog.templates/blog/index.html
#     return render(request,'blog/index.html') #앱별로 중복이 되지 않도록 blog를 사용. index.html은 다른 곳에도 있을 수 있다

class MyTemplateView(object):
    @staticmethod
    def as_view(template_name):
        def view(request):
            return render(request, template_name)
        return view

index = MyTemplateView.as_view(template_name="blog/index.html")


def index(request):
    return render(request, 'blog/index.html')

def post_list(request):
    return render(request, 'blog/post_list.html',{
        'post_list':Post.objects.all()
    })

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html',{
        'post':post
    })

def comment_new(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            # comment.author = request.user
            comment.save()
            print('redirect!')
            return redirect('blog.views.post_detail',post_pk)
    else:
        form = CommentForm()
    # print(form)
    # print(form.errors)
    return render(request, 'blog/comment_form.html',{
        'form':form
    })
