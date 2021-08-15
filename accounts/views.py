from accounts.decorators import allowed_users, unauthorized_user, admin_only
from accounts.models import Customer, Order, Product
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.forms import inlineformset_factory
from .forms import OrderForm, CreateUserForm
from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# Create your views here.


@unauthorized_user
def registerPage(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='user')
            user.groups.add(group)
            messages.success(
                request, "User registered Successfully!!!. as {}".format(username))
            return redirect('accounts:login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


@unauthorized_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('accounts:dashboard')
        else:
            messages.info(request, "Username or Password Incorrect")
            return redirect('accounts:login')

    context = {}
    return render(request, 'accounts/login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('accounts:login')


@login_required(login_url='accounts:login')
@admin_only
def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    last_five_orders = orders.order_by('-date_created')[:5]

    context = {
        'orders': orders,
        'customers': customers,
        'total_customers': total_customers,
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending,
        'last_five_orders': last_five_orders
    }
    return render(request, 'accounts/dashboard.html', context)


@login_required(login_url='accounts:login')
def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'accounts/products.html', context)


@login_required(login_url='accounts:login')
def customer(request, pk):
    customer_details = Customer.objects.get(pk=pk)

    orders = customer_details.order_set.all()
    total_orders = orders.count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {
        'customer': customer_details,
        'order_count': total_orders,
        'orders': orders,
        'myfilters': myFilter,
    }
    return render(request, 'accounts/customers.html', context)


@login_required(login_url='accounts:login')
def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(
        Customer, Order, fields=('product', 'status'), extra=3)
    customer = Customer.objects.get(pk=pk)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    # form = OrderForm(initial={'customer': customer})
    if request.method == 'POST':
        # print(request.POST)
        #form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('accounts:dashboard')

    context = {'formset': formset}
    return render(request, 'accounts/order_form.html', context)


@login_required(login_url='accounts:login')
def updateOrder(request, pk):
    order = Order.objects.get(pk=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        # print(request.POST)
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('accounts:dashboard')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)


@login_required(login_url='accounts:login')
def deleteOrder(request, pk):
    order = Order.objects.get(pk=pk)

    if request.method == 'POST':
        order.delete()
        return redirect('accounts:dashboard')

    context = {'item': order}
    return render(request, 'accounts/delete_form.html', context)


@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
    orders = request.user.customer.order_set.all()
    print(orders)
    context = {"orders": orders}
    return render(request, 'accounts/user.html', context)
