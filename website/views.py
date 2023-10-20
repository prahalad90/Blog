from django.shortcuts import render,HttpResponse
from .models import blog

# Create your views here.
def home(request):
    post = blog.objects.all().filter(status='2').order_by('-date')
    return render(request,'index.html',{'data':post})

def search(request):
    if request.method == "GET":
        query = request.GET.get('search')
        result = blog.objects.filter(content__contains = query)
    return render(request,'search.html',{'data':result})


def post(request,slg):
    result = blog.objects.get(slug = slg)
    return render(request,'post.html',{'data':result})

def about(request):
    return render(request,'about.html')