# Dream Car Bazaar

A web application for buying and selling used cars, built with Django 4.1.3.

## Prerequisites

- Python 3.12+
- PostgreSQL 15+
- Git

## Installation

1. Clone the repository :
git clone <your-repository-url>

cd dream_car_bazaar

cd DCB_Project

2. Create and activate virtual environment

3. Install dependencies :
pip install -r requirements.txt

4. Install and Configure PostgreSQL:

psql -U postgres

CREATE DATABASE dreamcar_dreamcarbazaar;

5. Update Database Configuration Update settings.py

6. Environment Setup Create .env in project root

7. Initialize Database

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

## Running the Project
1. Start development server:
python manage.py runserver

2. Access the application:
Main site: http://127.0.0.1:8000

Admin panel: http://127.0.0.1:8000/admin
