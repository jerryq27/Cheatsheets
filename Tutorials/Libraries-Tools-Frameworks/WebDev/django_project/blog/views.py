from django.shortcuts import render

posts = [
    {
        'author': 'John Smith',
        'title': 'Post 1',
        'content': 'Example content',
        'date_posted': 'August 27, 2018',
    },
    {
        'author': 'John Smith',
        'title': 'Post 2',
        'content': 'Example content',
        'date_posted': 'August 28, 2018',
    },
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }

    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', { 'title': 'About' })