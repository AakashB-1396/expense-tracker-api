from django.test import TestCase
from restapi import models


# Create your tests here.
class TestModels(TestCase):
    def test_expense(self):
        expense = models.Expense.objects.create(
            amount=20.99,
            merchant="Funk Pop",
            description="Wanda from WandaVision",
            category="merchandise",
        )
        inserted_expense = models.Expense.objects.get(pk=expense.id)

        self.assertEqual(20.99, inserted_expense.amount)
        self.assertEqual("Wanda from WandaVision", inserted_expense.description)
