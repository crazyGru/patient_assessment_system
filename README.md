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

## Assumptions Made During Development

- The application assumes that users will have a basic understanding of how to use a web application and API.
- It is assumed that the PostgreSQL database is installed and configured correctly on the local machine.
- The application is designed for a single organization, with multi-tenancy support to isolate data between different users.

## Challenges Faced and Solutions

- **Challenge**: Implementing JWT authentication was initially confusing due to the need for token management.
  - **Solution**: I referred to the official Django REST Framework documentation and examples to understand how to implement JWT authentication properly.
- **Challenge**: Ensuring proper validation for user input, especially for phone numbers and final scores.
  - **Solution**: I implemented custom validation methods in the serializers to enforce these rules and tested them thoroughly.

## Additional Features or Improvements

- Added pagination and filtering for assessments to improve the user experience when dealing with large datasets.
- Implemented a user login view to allow users to authenticate and receive JWT tokens for secure access to the API.

## Deployment Process to AWS

1. **Prepare the Environment**: Set up an AWS account and create an EC2 instance with the desired specifications (e.g., Ubuntu server).

2. **Install Dependencies**: SSH into the EC2 instance and install necessary software, including Python, pip, and PostgreSQL.

3. **Clone the Repository**: Use Git to clone the project repository onto the EC2 instance.

4. **Set Up the Database**: Create a PostgreSQL database on the EC2 instance and configure the database settings in the Django project.

5. **Configure Environment Variables**: Set up environment variables for sensitive information like the secret key and database credentials.

6. **Run Migrations**: Execute the database migrations to set up the necessary tables.

7. **Collect Static Files**: Run `python manage.py collectstatic` to gather all static files for production use.

8. **Set Up a Web Server**: Install and configure a web server (e.g., Nginx) to serve the application and handle incoming requests.

9. **Run the Application**: Use a WSGI server (e.g., Gunicorn) to run the Django application.

10. **Configure Security Groups**: Ensure that the EC2 instance's security groups allow traffic on the necessary ports (e.g., 80 for HTTP, 443 for HTTPS).

11. **Monitor and Maintain**: Set up monitoring for the application and database to ensure uptime and performance.

By following these steps, the Patient Assessment System can be successfully deployed on AWS, providing clinicians with a robust tool for managing patient assessments.
