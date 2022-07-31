from unittest.mock import MagicMock, patch

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .factory_boy import UserFactory

# Create your tests here.


class TestUserAPIs(APITestCase):
    """
    Test the Employee api
    GET, POST, PUT, PATCH, DELETE
    """

    headers = {"Authorization": "Token token_key"}

    @patch(
        "rest_framework.authtoken.models.Token",
        MagicMock(return_value=headers["Authorization"]),
    )
    def test_employee_create(self):
        # method to test the creation of employee
        data = {
            "username": "string",
            "first_name": "string",
            "last_name": "string",
            "email": "user@example.com",
            "password": "string",
        }
        res = self.client.post(
            reverse("user-list"),
            data=data,
            format="json",
            HTTP_AUTHORIZATION="Token token_key",
        )
        result_data = res.json()
        assert res.status_code == status.HTTP_201_CREATED
        assert result_data["username"] == data["username"]
        assert result_data["first_name"] == data["first_name"]
        assert result_data["last_name"] == data["last_name"]
        assert result_data["email"] == data["email"]
        assert result_data["password"] == data["password"]

    @patch(
        "rest_framework.authtoken.models.Token",
        MagicMock(return_value=headers["Authorization"]),
    )
    def test_employee_list(self):
        # method to test the getting employee list
        created_employee = [UserFactory() for i in range(3)]
        res = self.client.get(
            reverse("user-list"),
            format="json",
            HTTP_AUTHORIZATION="Token token_key",
        )

        result_data = res.json()
        assert res.status_code == status.HTTP_200_OK
        assert len(result_data) == len(created_employee)
        for employee, result in zip(created_employee, result_data):

            assert str(employee.id) == result["id"]
            assert employee.first_name == result["first_name"]
            assert employee.last_name == result["last_name"]
            assert employee.email == result["email"]
            assert employee.password == result["password"]

    @patch(
        "rest_framework.authtoken.models.Token",
        MagicMock(return_value=headers["Authorization"]),
    )
    def test_employee_detail(self):
        # method to test the employee detail
        employee = UserFactory()
        res = self.client.get(
            reverse("user-detail", args=[str(employee.id)]),
            format="json",
            HTTP_AUTHORIZATION="Token token_key",
        )
        result_data = res.json()
        assert res.status_code == status.HTTP_200_OK
        assert str(employee.id) == result_data["id"]
        assert employee.first_name == result_data["first_name"]
        assert employee.last_name == result_data["last_name"]
        assert employee.email == result_data["email"]
        assert employee.password == result_data["password"]

    @patch(
        "rest_framework.authtoken.models.Token",
        MagicMock(return_value=headers["Authorization"]),
    )
    def test_employee_partial_update(self):
        # method to test the prtial update of emplyee detail
        employee = UserFactory()
        res = self.client.patch(
            reverse("user-detail", args=[str(employee.id)]),
            format="json",
            HTTP_AUTHORIZATION="Token token_key",
        )
        expected_result = {"message": "Update function is not offered in this path."}
        result_data = res.json()
        assert res.status_code == status.HTTP_403_FORBIDDEN
        assert expected_result == result_data

    @patch(
        "rest_framework.authtoken.models.Token",
        MagicMock(return_value=headers["Authorization"]),
    )
    def test_employee_update(self):
        # method to test the update of employee detail
        employee = UserFactory()
        res = self.client.put(
            reverse("user-detail", args=[str(employee.id)]),
            format="json",
            HTTP_AUTHORIZATION="Token token_key",
        )
        expected_result = {"message": "Update function is not offered in this path."}
        result_data = res.json()
        assert res.status_code == status.HTTP_403_FORBIDDEN
        assert expected_result == result_data

    @patch(
        "rest_framework.authtoken.models.Token",
        MagicMock(return_value=headers["Authorization"]),
    )
    def test_employee_delete(self):
        # method to test the deletion of employee
        employee = UserFactory()
        res = self.client.delete(
            reverse("user-detail", args=[str(employee.id)]),
            format="json",
            HTTP_AUTHORIZATION="Token token_key",
        )
        expected_result = {"message": "Delete function is not offered in this path."}
        result_data = res.json()
        assert res.status_code == status.HTTP_403_FORBIDDEN
        assert expected_result == result_data
