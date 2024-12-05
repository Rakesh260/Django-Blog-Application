Django Blog Application

Description:
This is a simple blog application built with Django and Django REST Framework. 
It allows users to create, retrieve, update, and delete blog posts and comments. 
The project demonstrates the basic functionality of a blog, with a focus on CRUD operations (Create, Read, Update, Delete) for posts and comments. 
It also incorporates user authentication through token-based authentication, ensuring that only authenticated users can modify the posts and comments.

Features
Post Model: Create, read, update, and delete blog posts. Each post includes a title, content, author, and published date.
Comment Model: Create and view comments for each blog post. Each comment includes an author, text, and creation date.
API Endpoints:
CRUD operations for Post model (Create, Retrieve, Update, Delete).
List and Create operations for Comment model, linked to individual posts.
User Authentication: Token-based authentication to secure create, update, and delete actions.

Installation
Prerequisites:
Ensure you have the following installed:
Python 3.10
pip
Django
Django REST Framework

Steps to Install:
git clone https://github.com/Rakesh260/Django-Blog-Application.git
cd Django-Blog-Application

Create a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install required dependencies:
pip install -r requirements.txt

create a new schema in mysql and connect from settings file
eg:   create database database_name
'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog_app',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'ATOMIC_REQUESTS': True
    },

Run migrations to create the database schema:
python manage.py migrate

Start the development server:
python manage.py runserver

Frontend Installation (Angular):
Prerequisites:
Ensure you have the following installed:

Node.js (which includes npm)
Angular CLI (Command Line Interface)
npm install -g @angular/cli

Install dependencies:
npm install

Create a configuration file to set the API URL for communication with the Django backend. Inside the src/environments folder, edit the environment.ts file to point to your backend server.
export const environment = {
  production: false,
  apiUrl: 'http://localhost:8000/api/' // Ensure this matches your Django API URL
};

Serve the Angular application:
ng serve

