from django.shortcuts import render, get_object_or_404

from .models import Post_blogs


def all_blogs(request):
    blog_count = Post_blogs.objects.count()
    post_list = Post_blogs.objects.order_by('-date')[:5]
    blogs_list = {'post_list': post_list,
                  'blog_count': blog_count}
    return render(request, 'blog/all_blogs.html', blogs_list)


def detail(request, post_id):
    post = get_object_or_404(Post_blogs, pk=post_id)
    return render(request, 'blog/detail.html', {'post': post})
