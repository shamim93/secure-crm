from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden,HttpResponseNotAllowed
from .forms import (
    CustomUserCreationForm,
    LoginForm,
    CustomerProfileForm,
    OrderForm,
    OrderStatusForm
)
from .models import Order


def home_view(request):
    if request.method == "GET":
        return render(request, 'users/home.html')
    return HttpResponseNotAllowed(['GET'])



def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                response = redirect('dashboard')
                response.set_cookie(
                    key='ui_theme',
                    value='dark', 
                    max_age=60 * 60 * 24 * 30,
                    secure=False,
                    httponly=True,
                    samesite='Lax'
                )
                return response
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard_view(request):
    first_visit = request.COOKIES.get('first_visit', 'true') == 'true'
    response = render(request, 'users/dashboard.html', {
        'user_type': request.user.user_type,
        'show_welcome': first_visit
    })

    if first_visit:
        response.set_cookie(
            'first_visit',
            'false',
            max_age=3600,
            secure=False,
            httponly=True,
            samesite='Lax'
        )
    return response


@login_required
def edit_profile_view(request):
    user = request.user
    if request.method == 'POST':
        form = CustomerProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CustomerProfileForm(instance=user)
    return render(request, 'users/edit_profile.html', {'form': form})


@login_required
def view_orders(request):
    user = request.user
    if user.user_type == 'customer':
        orders = Order.objects.filter(customer=user).order_by('-created_at')
    elif user.user_type == 'superadmin':
        orders = Order.objects.all().order_by('-created_at')
    else:
        return redirect('dashboard')
    return render(request, 'users/order_list.html', {'orders': orders})


@login_required
def create_order(request):
    if request.user.user_type == 'subscriber':
        return HttpResponseForbidden("Subscribers are not allowed to create orders.")

    if request.user.user_type not in ['customer', 'superadmin']:
        return redirect('dashboard')

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = request.user
            order.save()
            return redirect('view_orders')
    else:
        form = OrderForm()
    return render(request, 'users/create_order.html', {'form': form})



@login_required
def update_order(request, order_id):
    user = request.user
    order = get_object_or_404(Order, id=order_id)
    if user.user_type not in ['customer', 'superadmin']:
        return redirect('dashboard')
    if user.user_type == 'customer' and order.customer != user:
        return redirect('dashboard')

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('view_orders')
    else:
        form = OrderForm(instance=order)
    return render(request, 'users/update_order.html', {'form': form, 'order': order})


@login_required
def delete_order(request, order_id):
    user = request.user
    order = get_object_or_404(Order, id=order_id)

    if user.user_type not in ['superadmin', 'customer']:
        return redirect('dashboard')
    if user.user_type == 'customer' and order.customer != user:
        return redirect('dashboard')

    if request.method == "POST":
        order.delete()
        return redirect('view_orders')
    return render(request, 'users/delete_order.html', {'order': order})


@login_required
def update_order_status(request, order_id):
    if request.user.user_type != 'superadmin':
        return HttpResponseForbidden('Only Superadmin can update the status.')

    order = get_object_or_404(Order, id=order_id)

    if request.method == "POST":
        form = OrderStatusForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('all_orders')
    else:
        form = OrderStatusForm(instance=order)
    return render(request, 'users/update_order_status.html', {'form': form, 'order': order})


@login_required
def all_orders_view(request):
    if request.user.user_type != 'superadmin':
        return redirect('dashboard')
    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'users/all_orders.html', {'orders': orders})
