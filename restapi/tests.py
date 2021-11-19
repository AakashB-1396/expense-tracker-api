from django.test import TestCase
from restapi import models
from django.urls import reverse

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


class TestViews(TestCase):
    def test_expense_create(self):
        payload = {
            "amount": 25.0,
            "merchant": "Marvel",
            "description": "Spiderman No Way Home Tshirt",
            "category": "Marchandise",
        }

        res = self.client.post(
            reverse("restapi:expense-list-create"), payload, format="json"
        )

        self.assertEqual(201, res.status_code)

        json_res = res.json()

        self.assertEqual(payload["amount"], json_res["amount"])
        self.assertEqual(payload["merchant"], json_res["merchant"])
        self.assertEqual(payload["description"], json_res["description"])
        self.assertEqual(payload["category"], json_res["category"])
        self.assertIsInstance(json_res["id"], int)

    def test_expense_list(self):
        res = self.client.get(reverse("restapi:expense-list-create"), format="json")

        self.assertEqual(200, res.status_code)

        json_res = res.json()

        self.assertIsInstance(json_res, list)

        expenses = models.Expense.objects.all()
        self.assertEqual(len(expenses), len(json_res))

    def test_expense_create_required_fields_missing(self):
        payload = {
            "merchant": "Marvel",
            "description": "Spiderman No Way Home Tshirt",
            "category": "Marchandise",
        }

        res = self.client.post(
            reverse("restapi:expense-list-create"), payload, format="json"
        )

        self.assertEqual(400, res.status_code)
