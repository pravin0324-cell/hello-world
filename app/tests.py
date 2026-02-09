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

@pytest.mark.django_db
def test_school_list_view(client):
    url = reverse('school-list')
    response = client.get(url)
    assert response.status_code == 200
    assert response.json() == []

@pytest.mark.django_db
def test_school_create_view(client):
    url = reverse('school-create')
    data = {
        'name': 'Test School',
        'location': 'Test Location'
    }
    response = client.post(url, data, content_type='application/json')
    assert response.status_code == 201
    assert response.json()['name'] == 'Test School'
    assert response.json()['location'] == 'Test Location'