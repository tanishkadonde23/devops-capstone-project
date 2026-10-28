"""Tests for the Customer Accounts REST API."""

import unittest

from service.routes import app, accounts


class TestAccountRoutes(unittest.TestCase):
    """Test account CRUD operations."""

    def setUp(self):
        self.client = app.test_client()
        accounts.clear()

    def test_index(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_create_account(self):
        response = self.client.post(
            "/accounts",
            json={
                "name": "John Doe",
                "email": "john@example.com",
                "address": "123 Main Street",
                "phone_number": "555-0100",
                "date_joined": "2023-01-15",
            },
        )
        self.assertEqual(response.status_code, 201)

    def test_list_accounts(self):
        response = self.client.get("/accounts")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), [])

    def test_read_missing_account(self):
        response = self.client.get("/accounts/999")
        self.assertEqual(response.status_code, 404)

    def test_update_missing_account(self):
        response = self.client.put("/accounts/999", json={})
        self.assertEqual(response.status_code, 404)

    def test_delete_missing_account(self):
        response = self.client.delete("/accounts/999")
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
