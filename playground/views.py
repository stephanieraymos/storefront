from django.shortcuts import render

def calculate():
    x = 1
    y = 2
    return x

def say_hello(request):
    x = calculate()
    y = 2
    return render(request, 'hello.html', { 'name': 'Stephanie' }) # Request, template, dictionary
