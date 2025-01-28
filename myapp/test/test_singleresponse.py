import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from myapp.models import AiResponse

client = APIClient()

@pytest.mark.django_db
def testgetmethod():
    AiResponse.objects.create(prompt = 'hii',response_text = 'hello',model_used = 'gpt',status='success',processing_time = 4)
    url = reverse('single-response', kwargs={'pk': 1})
    print(url)
    response = client.get(url)
    print(response)
    assert response.status_code == 200
