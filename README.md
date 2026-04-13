# HNG Internship Stage 0 — Name Gender Classifier API

A lightweight REST API built with Django that predicts the gender of a given name by integrating with the [Genderize.io](https://genderize.io) API. It processes the raw response and returns a structured, enriched result including a confidence flag and a UTC timestamp.

---

## Overview

This API receives a name as a query parameter, calls the Genderize.io API, and returns a processed JSON response that includes:
- The predicted gender and probability
- A renamed `sample_size` field (from Genderize's `count`)
- A computed `is_confident` flag based on probability and sample size thresholds
- A dynamically generated `processed_at` UTC timestamp

---

## Tech Stack

- **Language:** Python 3.11
- **Framework:** Django
- **External API:** [Genderize.io](https://api.genderize.io)
- **Libraries:**
  - `requests` — for calling the Genderize API
  - `django-cors-headers` — for enabling CORS on all origins
- **Deployment:** Railway

---

## Project Structure
hng-stage0/
├── core/                  # Django project settings and root URLs
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── classifier/            # App containing the API logic
│   ├── views.py           # Main endpoint logic
│   └── urls.py            # App-level URL routing
├── requirements.txt       # Project dependencies
├── manage.py
└── README.md

---

## Setup & Installation

### Prerequisites
- Python 3.11+
- pip

### Steps

**1. Clone the repository**
```bash
git clone https://github.com/YOURUSERNAME/hng-stage0.git
cd hng-stage0
```

**2. Create and activate a virtual environment**
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Run the development server**
```bash
python manage.py runserver
```

**5. Test the endpoint**
http://127.0.0.1:8000/api/classify?name=john

---

## API Documentation

### Classify Name
Predicts the gender of a given name.

## Deployment

This API is deployed on Railway and publicly accessible at:
https://YOURAPP.up.railway.app

**Live endpoint example:**
https://YOURAPP.up.railway.app/api/classify?name=john