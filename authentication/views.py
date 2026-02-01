from django.shortcuts import render


def simple_view(request):
    context = {"string": "Gfg is the best"}
    return render(request, "login.html", context)
