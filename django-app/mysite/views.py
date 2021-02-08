# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render

def howdy(request):
    user = request.session["user"]
    decoded_token = request.session["decoded_token"]
    return render(request, "howdy.html", {"user":user, "decoded_token":decoded_token})

def post_list(request):
    roles = request.session["decoded_token"]["resource_access"]["djangoclient"]["roles"]
    return render(request, 'post_list.html', {"roles":roles})

def logout(request):
    return render(request, "logout.html", {})
