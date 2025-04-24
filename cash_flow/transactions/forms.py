from django import forms
from django.core.exceptions import ValidationError
from .models import Transaction, Status, Type, Category, SubCategory

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['created_at', 'date', 'status', 'type', 'category', 'subcategory', 'amount', 'comment']
        widgets = {
            'created_at': forms.DateInput(attrs={'type': 'date'}),
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        type = cleaned_data.get('type')
        category = cleaned_data.get('category')
        subcategory = cleaned_data.get('subcategory')
        amount = cleaned_data.get('amount')

        if not type or not category or not subcategory or amount is None:
            raise ValidationError("Поля 'сумма', 'тип', 'категория' и 'подкатегория' обязательны.")

        if category.type != type:
            raise ValidationError("Категория не относится к выбранному типу.")

        if subcategory.category != category:
            raise ValidationError("Подкатегория не связана с выбранной категорией.")

class TransactionFilterForm(forms.Form):
    date_from = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Дата с'
    )
    date_to = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Дата по'
    )
    status = forms.ModelChoiceField(
        queryset=Status.objects.all(),
        required=False,
        label='Статус'
    )
    type = forms.ModelChoiceField(
        queryset=Type.objects.all(),
        required=False,
        label='Тип'
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        label='Категория'
    )
    subcategory = forms.ModelChoiceField(
        queryset=SubCategory.objects.all(),
        required=False,
        label='Подкатегория'
    )

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']

class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['name']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'type']

class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ['name', 'category']