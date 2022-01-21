import os
import tempfile

import pytest

from server import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    yield client

def test_english_to_french(client):
    rv = client.get("englishToFrench?textToTranslate=small")    
    assert "Petit" == rv.get_json().get("translated")    
    assert "Grand" != rv.get_json().get("translated")

def test_french_to_english(client):
    rv = client.get("frenchToEnglish?textToTranslate=petit")    
    assert "Small" == rv.get_json().get("translated")
    assert "Big" != rv.get_json().get("translated")
