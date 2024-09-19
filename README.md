# Patient Assessment System

## Overview

The Patient Assessment System is a Django-based web application designed to allow clinicians to administer, track, and manage patient assessments. The application provides a RESTful API for managing patient records and assessments, utilizing Django REST Framework and JWT for authentication.

## Features

- User registration and login
- Patient management (Create, Retrieve, Update, Delete)
- Assessment management (Create, Retrieve, Update, Delete)
- Multi-tenancy support for data isolation between different clinician users
- Filtering, pagination, and sorting for assessments

## Tech Stack

- **Backend**: Django
- **Database**: PostgreSQL
- **API**: Django REST Framework
- **Authentication**: JWT (JSON Web Tokens)

## Installation

### Prerequisites

- Python 3.x
- Django 5.x
- PostgreSQL
- pip

### Steps to Set Up

1. **Clone the repository:**

   ```bash
   git clone https://github.com/crazyGru/patient-assessment-system.git
   cd patient-assessment-system
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database:**

   - Create a PostgreSQL database named `patient_assessment_system`.
   - Update the database settings in `patient_assessment_system/settings.py` with your PostgreSQL credentials.

5. **Run migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser:**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

8. **Access the API:**
   - The API will be available at `http://127.0.0.1:8000/api/`.
   - Admin panel can be accessed at `http://127.0.0.1:8000/admin/`.

## API Endpoints

- **User Registration**: `POST /api/register/`
- **User Login**: `POST /api/login/`
- **Patients**:
  - `GET /api/patients/`
  - `POST /api/patients/`
  - `GET /api/patients/{id}/`
  - `PUT /api/patients/{id}/`
  - `DELETE /api/patients/{id}/`
- **Assessments**:
  - `GET /api/assessments/`
  - `POST /api/assessments/`
  - `GET /api/assessments/{id}/`
  - `PUT /api/assessments/{id}/`
  - `DELETE /api/assessments/{id}/`
