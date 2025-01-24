from django.shortcuts import render
from .models import Category,Photo
# Create your views here.
def gallary(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()
    context = {'categories':categories , 'photos':photos}
    return render(request,'photos/gallary.html',context)

def viewPhoto(request,pk):
    return render(request,'photos/photo.html')

def addPhoto(request):
    return render(request,'photos/add.html')