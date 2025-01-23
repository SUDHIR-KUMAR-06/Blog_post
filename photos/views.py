from django.shortcuts import render

# Create your views here.
def gallary(request):
    return render(request,'photos/gallary.html')

def viewPhoto(request,pk):
    return render(request,'photos/photo.html')

def addPhoto(request):
    return render(request,'photos/add.html')