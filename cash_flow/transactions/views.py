from .forms import TransactionForm, TransactionFilterForm, StatusForm, TypeForm, CategoryForm, SubCategoryForm
from django.shortcuts import redirect, render, get_object_or_404
from .models import Transaction, Status, Type, Category, SubCategory


def transaction_create(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm()
    return render(request, 'transactions/transaction_form.html', {'form': form})

def transaction_edit(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'transactions/transaction_form.html', {'form': form, 'is_edit': True})

def transaction_delete(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)
    if request.method == 'POST':
        transaction.delete()
        return redirect('transaction_list')
    return render(request, 'transactions/transaction_confirm_delete.html', {'transaction': transaction})

def transaction_list(request):
    transactions = Transaction.objects.all().order_by('-date')

    filter_form = TransactionFilterForm(request.GET)
    if filter_form.is_valid():
        if filter_form.cleaned_data['date_from']:
            transactions = transactions.filter(date__gte=filter_form.cleaned_data['date_from'])

        if filter_form.cleaned_data['date_to']:
            transactions = transactions.filter(date__lte=filter_form.cleaned_data['date_to'])

        if filter_form.cleaned_data['status']:
            transactions = transactions.filter(status=filter_form.cleaned_data['status'])

        if filter_form.cleaned_data['type']:
            transactions = transactions.filter(type=filter_form.cleaned_data['type'])

        if filter_form.cleaned_data['category']:
            transactions = transactions.filter(category=filter_form.cleaned_data['category'])

        if filter_form.cleaned_data['subcategory']:
            transactions = transactions.filter(subcategory=filter_form.cleaned_data['subcategory'])

    return render(request, 'transactions/transaction_list.html', {
        'transactions': transactions,
        'filter_form': filter_form
    })


def reference_list(request):
    statuses = Status.objects.all()
    types = Type.objects.all()
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()

    return render(request, 'transactions/reference_management.html', {
        'statuses': statuses,
        'types': types,
        'categories': categories,
        'subcategories': subcategories,
    })

def status_create(request):
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reference_list')
    else:
        form = StatusForm()
    return render(request, 'transactions/status_form.html', {'form': form})

def status_edit(request, status_id):
    status = get_object_or_404(Status, id=status_id)
    if request.method == 'POST':
        form = StatusForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            return redirect('reference_list')
    else:
        form = StatusForm(instance=status)
    return render(request, 'transactions/status_form.html', {'form': form, 'is_edit': True})

def status_delete(request, status_id):
    status = get_object_or_404(Status, id=status_id)
    if request.method == 'POST':
        status.delete()
        return redirect('reference_list')
    return render(request, 'transactions/status_confirm_delete.html', {'status': status})

def type_create(request):
    if request.method == 'POST':
        form = TypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reference_list')
    else:
        form = TypeForm()
    return render(request, 'transactions/type_form.html', {'form': form})

def type_edit(request, type_id):
    type_obj = get_object_or_404(Type, id=type_id)
    if request.method == 'POST':
        form = TypeForm(request.POST, instance=type_obj)
        if form.is_valid():
            form.save()
            return redirect('reference_list')
    else:
        form = TypeForm(instance=type_obj)
    return render(request, 'transactions/type_form.html', {'form': form, 'is_edit': True})

def type_delete(request, type_id):
    type_obj = get_object_or_404(Type, id=type_id)
    if request.method == 'POST':
        type_obj.delete()
        return redirect('reference_list')
    return render(request, 'transactions/type_confirm_delete.html', {'type': type_obj})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reference_list')
    else:
        form = CategoryForm()
    return render(request, 'transactions/category_form.html', {'form': form})

def category_edit(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('reference_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'transactions/category_form.html', {'form': form, 'is_edit': True})

def category_delete(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        category.delete()
        return redirect('reference_list')
    return render(request, 'transactions/category_confirm_delete.html', {'category': category})

def subcategory_create(request):
    if request.method == 'POST':
        form = SubCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reference_list')
    else:
        form = SubCategoryForm()
    return render(request, 'transactions/subcategory_form.html', {'form': form})

def subcategory_edit(request, subcategory_id):
    subcategory = get_object_or_404(SubCategory, id=subcategory_id)
    if request.method == 'POST':
        form = SubCategoryForm(request.POST, instance=subcategory)
        if form.is_valid():
            form.save()
            return redirect('reference_list')
    else:
        form = SubCategoryForm(instance=subcategory)
    return render(request, 'transactions/subcategory_form.html', {'form': form, 'is_edit': True})

def subcategory_delete(request, subcategory_id):
    subcategory = get_object_or_404(SubCategory, id=subcategory_id)
    if request.method == 'POST':
        subcategory.delete()
        return redirect('reference_list')
    return render(request, 'transactions/subcategory_confirm_delete.html', {'subcategory': subcategory})

def home(request):
    return render(request, 'transactions/home.html')