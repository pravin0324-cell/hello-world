from django.test import TestCase
import pytest
from django.urls import reverse
# Create your tests here.
@pytest.mark.django_db
def test_index_view(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200
    assert response.content == b"Hello, world!\n"
