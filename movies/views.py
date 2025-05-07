from django.shortcuts import render

context = {"movies": ["Sonic", "Thor", "Matrix"]}


def index(request):
    return render(request, "movies/index.html", context)


def about(request):
    return render(request, "movies/about.html")
