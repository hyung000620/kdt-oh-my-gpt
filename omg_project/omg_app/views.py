from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def chat(request):
    return render(request, 'chat.html')

def write(request):
    return render(request, 'write.html')

def loading(request):
    return render(request, 'loading.html')

def payment(request):
    return render(request, 'payment.html')

def intro(request):
    return render(request, 'intro.html')