from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import SotibOlish


# Create your views here.
def get_func(request):
    products = SotibOlish.objects.all().order_by("-id")

    context = {
        'products':products,

    }

    return render(request, "template.html", context)

