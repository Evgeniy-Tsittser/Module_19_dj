from django import forms

class ContactForm(forms.Form):
    username = forms.CharField(max_length=30, label='Введите логин')
    password = forms.CharField(max_length=8, label='Введите пароль')
    repeat_password = forms.CharField(max_length=8, label='Повторите пароль')
    age = forms.IntegerField(label='Введите свой возраст')
    email = forms.EmailField(max_length=100, label='Введите свой email')
    balance = forms.DecimalField(max_digits=10, decimal_places=2, label='Укажите внесенную сумму')