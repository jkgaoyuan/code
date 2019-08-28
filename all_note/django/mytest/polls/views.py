from django.shortcuts import render, HttpResponse

def index(request):
    # django将会把http请求作为参数传递给函数，因此，函数必须至少有一个参数
    return render(request,'index.html')