import random
from datetime import datetime, timedelta
from decimal import Decimal
from django.utils import timezone
from transactions.models import Status, Type, Category, SubCategory, Transaction

# Очистка базы данных (опционально)
# Status.objects.all().delete()
# Type.objects.all().delete()
# Category.objects.all().delete()
# SubCategory.objects.all().delete()
# Transaction.objects.all().delete()


statuses = [
    Status.objects.get_or_create(name="Активен")[0],
    Status.objects.get_or_create(name="Завершен")[0],
    Status.objects.get_or_create(name="В ожидании")[0],
    Status.objects.get_or_create(name="Отменен")[0]
]

income_type = Type.objects.get_or_create(name="Доход")[0]
expense_type = Type.objects.get_or_create(name="Расход")[0]


income_categories = [
    Category.objects.get_or_create(name="Зарплата", type=income_type)[0],
    Category.objects.get_or_create(name="Инвестиции", type=income_type)[0],
    Category.objects.get_or_create(name="Подарки", type=income_type)[0],
    Category.objects.get_or_create(name="Прочие доходы", type=income_type)[0]
]

expense_categories = [
    Category.objects.get_or_create(name="Продукты", type=expense_type)[0],
    Category.objects.get_or_create(name="Транспорт", type=expense_type)[0],
    Category.objects.get_or_create(name="Развлечения", type=expense_type)[0],
    Category.objects.get_or_create(name="Жилье", type=expense_type)[0]
]


subcategories = []

SubCategory.objects.get_or_create(name="Оклад", category=income_categories[0])
SubCategory.objects.get_or_create(name="Премия", category=income_categories[0])
SubCategory.objects.get_or_create(name="Подработка", category=income_categories[0])

SubCategory.objects.get_or_create(name="Дивиденды", category=income_categories[1])
SubCategory.objects.get_or_create(name="Проценты по вкладам", category=income_categories[1])

SubCategory.objects.get_or_create(name="Деньги на праздники", category=income_categories[2])
SubCategory.objects.get_or_create(name="Наследство", category=income_categories[2])

SubCategory.objects.get_or_create(name="Возврат долга", category=income_categories[3])
SubCategory.objects.get_or_create(name="Выигрыши", category=income_categories[3])


SubCategory.objects.get_or_create(name="Супермаркет", category=expense_categories[0])
SubCategory.objects.get_or_create(name="Рынок", category=expense_categories[0])
SubCategory.objects.get_or_create(name="Кафе и рестораны", category=expense_categories[0])

SubCategory.objects.get_or_create(name="Общественный транспорт", category=expense_categories[1])
SubCategory.objects.get_or_create(name="Такси", category=expense_categories[1])
SubCategory.objects.get_or_create(name="Бензин", category=expense_categories[1])

SubCategory.objects.get_or_create(name="Кино", category=expense_categories[2])
SubCategory.objects.get_or_create(name="Концерты", category=expense_categories[2])
SubCategory.objects.get_or_create(name="Походы в бары", category=expense_categories[2])

SubCategory.objects.get_or_create(name="Аренда", category=expense_categories[3])
SubCategory.objects.get_or_create(name="Коммунальные платежи", category=expense_categories[3])
SubCategory.objects.get_or_create(name="Ремонт", category=expense_categories[3])


def random_date(start_date, end_date):
    time_between = end_date - start_date
    days_between = time_between.days
    random_days = random.randrange(days_between)
    return start_date + timedelta(days=random_days)


all_subcategories = list(SubCategory.objects.all())

today = timezone.now().date()
start_date = today - timedelta(days=60)
end_date = today + timedelta(days=30)

comments = [
    "Ежемесячный платеж", "Срочная покупка", "Запланированная трата",
    "Непредвиденные расходы", "Регулярный платеж", "Подарок",
    "Стипендия", "Квартальная премия", "ДМС от компании",
    "Возмещение расходов", "Корпоративные расходы", "На отпуск",
    "Праздничный бонус", "Налоговый вычет", "Кэшбэк"
]

for i in range(15):
    subcategory = random.choice(all_subcategories)
    category = subcategory.category
    transaction_type = category.type

    if transaction_type == income_type:
        amount = Decimal(random.randint(5000, 100000))
    else:
        amount = Decimal(random.randint(100, 10000))

    Transaction.objects.create(
        created_at=random_date(start_date, end_date),
        date=random_date(start_date, end_date),
        status=random.choice(statuses),
        type=transaction_type,
        category=category,
        subcategory=subcategory,
        amount=amount,
        comment=random.choice(comments)
    )

print("База данных успешно заполнена! Создано:")
print(f"- {Status.objects.count()} статусов")
print(f"- {Type.objects.count()} типов")
print(f"- {Category.objects.count()} категорий")
print(f"- {SubCategory.objects.count()} подкатегорий")
print(f"- {Transaction.objects.count()} транзакций")