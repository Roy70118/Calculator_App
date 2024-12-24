from django.shortcuts import render

# Create your views here.


def cal_view(request):
    return render(request, 'index.html')
