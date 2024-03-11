from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Invoice, InvoiceDetail

class InvoiceAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.invoice_data = {'date': '2024-03-11', 'customer_name': 'Test Customer'}
        self.invoice = Invoice.objects.create(**self.invoice_data)
        self.invoice_detail_data = {'invoice': self.invoice, 'description': 'Test Description', 'quantity': 1, 'unit_price': 10, 'price': 10}
        self.invoice_detail = InvoiceDetail.objects.create(**self.invoice_detail_data)

    def test_create_invoice(self):
        url = reverse('invoice-list')
        response = self.client.post(url, self.invoice_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Similar test methods for other CRUD operations

    def test_retrieve_invoice_detail(self):
        url = reverse('invoice-detail', kwargs={'pk': self.invoice_detail.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
