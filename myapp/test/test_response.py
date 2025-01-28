import pytest
from rest_framework.test import APIClient
from django.urls import reverse

client = APIClient()

@pytest.mark.django_db
def test_get_all_responses():
        url = reverse('all-responses') 
        response = client.get(url)
        assert response.status_code == 200
        
@pytest.mark.django_db
def test_post_responses():
        url = reverse('all-responses') 
        payload = {'input_text':'hii'}
        response = client.post(url,payload)
        assert response.status_code == 200