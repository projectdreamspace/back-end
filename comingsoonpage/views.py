from django.shortcuts import render

# Create your views here.

def comingsoonpage(request):
    return render(request, 'comingsoonpage/coming-soon.html', {})