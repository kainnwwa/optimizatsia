from django.shortcuts import render

def start_page(request):
    return render(request, 'time.html')

def timer_page(request):
    return render(request, 'timer.html')