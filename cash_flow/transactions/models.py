from django.db import models
from django.utils import timezone

# Create your models here.
# Модель статуса транзакции (например, "Проведено", "Черновик" и т.д.)
class Status(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = "Statuses"
    def __str__(self):
        return self.name

# Модель типа транзакции (например, "Доход" или "Расход")
class Type(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

# Модель категории, связана с типом (например, "Зарплата" для дохода)
class Category(models.Model):
    name = models.CharField(max_length=50)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='categories')

    class Meta:
        verbose_name_plural = "Categories"
    def __str__(self):
        return f"{self.name} ({self.type.name})"

# Модель подкатегории, связана с категорией (например, "Премия" для "Зарплата")
class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    class Meta:
        verbose_name_plural = "Subcategories"

    def __str__(self):
        return f"{self.name} ({self.category.name})"

# Основная модель транзакции
class Transaction(models.Model):
    created_at = models.DateField(default=timezone.now)
    date = models.DateField()
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    type = models.ForeignKey(Type, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.date} | {self.amount} | {self.status.name}"