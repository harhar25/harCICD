import sys
import os

# Ensure 'src/' is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from app import app  # Import your Flask app
import pytest

# Sample test case
def test_home_route():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello, CI/CD!" in response.data  # Update expected response content
