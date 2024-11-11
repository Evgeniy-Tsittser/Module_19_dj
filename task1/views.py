from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .forms import ContactForm
from .models import Buyer, Game


def home_page(request):
    return render(request, 'first_task/home_page.html')


def shop_page(request):
    products = list(Game.objects.all())
    context = {'products': products}
    return render(request, 'first_task/shop_page.html', context)


def cart_page(request):
    return render(request, 'first_task/cart_page.html')


def sign_up_by_django(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            email = form.cleaned_data['email']
            balance = form.cleaned_data['balance']
            if password != repeat_password:
                form.add_error('password', 'Пароли не совпадают!')
            elif int(age) < 18:
                form.add_error('age', 'Вы должны быть старше 18 лет.')
            elif Buyer.objects.filter(name=username).exists():
                form.add_error('username', 'Пользователь с таким именем уже существует.')
            else:
                Buyer.objects.create(
                    name=username,
                    password=password,
                    age=age,
                    email=email,
                    balance=balance
                )
                #return redirect("hello_message", username=username)
                url = reverse('hello_message', args=[username])
                return redirect(url)
        else:
             form = ContactForm()
    context = {'form': form}
    return render(request, 'first_task/registration_page.html', context)


def hello_message(request, username):
    context = {'username': username}
    return render(request, 'first_task/hello_page.html', context)