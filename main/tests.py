from django.test import TestCase
from django.contrib.auth.models import User
from django import forms
from .models import Transaction
from .forms import TransactionForm

# Модель Transaction
class Transaction(models.Model):
    INCOME = 'income'
    EXPENSE = 'expense'
    TYPE_CHOICES = [
        (INCOME, 'Income'),
        (EXPENSE, 'Expense'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=7, choices=TYPE_CHOICES)
    category = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return f"{self.type} - {self.amount} - {self.category}"

# Форма TransactionForm
class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'type', 'category', 'date']

# Тесты для модели Transaction
class TransactionModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.transaction = Transaction.objects.create(
            user=self.user,
            amount=100.00,
            type='income',
            category='salary',
            date='2023-10-01'
        )

    def test_transaction_creation(self):
        self.assertEqual(self.transaction.amount, 100.00)
        self.assertEqual(self.transaction.type, 'income')
        self.assertEqual(self.transaction.category, 'salary')
        self.assertEqual(self.transaction.date.strftime('%Y-%m-%d'), '2023-10-01')
        self.assertEqual(self.transaction.user.username, 'testuser')

    def test_transaction_str(self):
        self.assertEqual(str(self.transaction), 'income - 100.00 - salary')

# Тесты для формы TransactionForm
class TransactionFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            'amount': 100.00,
            'type': 'income',
            'category': 'salary',
            'date': '2023-10-01'
        }
        form = TransactionForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {
            'amount': '',  # Поле обязательно для заполнения
            'type': 'income',
            'category': 'salary',
            'date': '2023-10-01'
        }
        form = TransactionForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('amount', form.errors)  # Проверяем, что есть ошибка в поле amount

# Тесты для представлений (views)
from django.urls import reverse

class TransactionViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.transaction = Transaction.objects.create(
            user=self.user,
            amount=100.00,
            type='income',
            category='salary',
            date='2023-10-01'
        )

    def test_transaction_list_view(self):
        response = self.client.get(reverse('transaction_list'))  # Замените 'transaction_list' на ваш URL
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'income - 100.00 - salary')

    def test_transaction_create_view(self):
        response = self.client.post(reverse('transaction_create'), {  # Замените 'transaction_create' на ваш URL
            'amount': 200.00,
            'type': 'expense',
            'category': 'food',
            'date': '2023-10-02'
        })
        self.assertEqual(response.status_code, 302)  # Проверяем редирект после успешного создания
        self.assertEqual(Transaction.objects.count(), 2)  # Проверяем, что транзакция создалась
