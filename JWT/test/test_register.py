import pytest
from rest_framework.test import APIClient
from django.urls import reverse

client = APIClient()


@pytest.mark.django_db
def test_register_user():
    payload = {
        "email": "test@gmail.com",
        "password": "nagarani",
        "password2": "nagarani",
    }
    response = client.post(reverse("register"), payload)
    print(response)

    assert response.status_code == 200