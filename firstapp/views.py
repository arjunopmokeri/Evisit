from django.shortcuts import render, HttpResponse, redirect
from .models import register, ProductModel
from .forms import ProductForm

# Create your views here.


def home(request):
    reg = register.objects.all()
    context = {
        'reg': reg
    }
    return render(request, "index.html", context)


def registration(request):
    if request.method == "POST":
        user_name = request.POST.get("name")
        reason = request.POST.get("purpose")
        time = request.POST.get("time")

        reg = register(name=user_name, reason=reason, time=time)
        reg.save()
        return HttpResponse("successfull")
    else:
        return render(request, 'register.html')


def edit_user(request, id):
    reg = register.objects.get(id=id)
    context = {
        'reg': reg
    }
    return render(request, 'edit_user.html', context)


def add_product(request):
    if request.method == "POST":
        forms = ProductForm(request.POST)
        if forms.is_valid():
            name = forms.cleaned_data.get("name")
            price = forms.cleaned_data.get("price")
            seller = forms.cleaned_data.get("seller")
            category = forms.cleaned_data.get("category")

            product = ProductModel(
                name=name, price=price, seller=seller, category=category)
            product.save()
            return HttpResponse("product added")
        else:
            forms = ProductForm()
            context = {
                'forms': forms
            }
            return render(request, "add_product.html", context)

    else:
        forms = ProductForm()
        context = {
            'forms': forms
        }
        return render(request, "add_product.html", context)
