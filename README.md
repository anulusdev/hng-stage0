# HNG Stage 0 - Name Gender Classifier API

A REST API that classifies the gender of a name using the Genderize API.

## Endpoint

GET /api/classify?name={name}

## Example Request
GET https://yourapp.up.railway.app/api/classify?name=john

## Example Response
{
  "status": "success",
  "data": {
    "name": "john",
    "gender": "male",
    "probability": 0.99,
    "sample_size": 1234,
    "is_confident": true,
    "processed_at": "2026-04-01T12:00:00Z"
  }
}

## Tech Stack
- Python / Django
- Django REST Framework
- Requests
- Django CORS Headers

## Setup
pip install -r requirements.txt
python manage.py runserver