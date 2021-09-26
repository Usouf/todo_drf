from django.shortcuts import render

# Create your views here.
def listView(request):
    context = {}
    return render(request, 'frontend/list.html', context)
