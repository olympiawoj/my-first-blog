from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request, 'blog/post_list.html', {})


#created a function using def, called post-list which takes request
#returns a function, render, that will render (put together) our template blog/post_list.html
