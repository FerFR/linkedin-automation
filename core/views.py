from django.shortcuts import render
from django.http import HttpRequest

class Views():
    def login(request: HttpRequest):
        pass
    def home(request: HttpRequest):
        return render(request, 'home.html')