from django.shortcuts import render
from django.http import HttpResponse
from .models import Post



# urls module matches the url to the url patterns and sends the request to the
# appropriate view as defined in the module

# Q: where do template files live?
# A: blog -> templates -> blog -> <template>.html
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

