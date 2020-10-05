from django.shortcuts import render, redirect
from .models import Post, Like
from django.contrib.auth.decorators import login_required


# Create your views here.
def post_view(request):
    qs = Post.objects.all()
    user = request.user

    context = {
        'qs': qs,
        'user': user
    }

    return render(request, 'post/main.html', context)


@login_required
def like_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        print(post_id)
        post_obj = Post.objects.get(id=post_id)

        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)

    like, create = Like.objects.get_or_create(user=user, post_id=post_id)

    if not create:
        if like.value == 'Like':
            like.value = 'Unlike'
        else:
            like.value = 'Like'
    like.save()
    return redirect('posts:post-list')


def redirect_view(request):
    return redirect('/admin/login')
