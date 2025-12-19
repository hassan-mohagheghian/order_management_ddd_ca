# Order Management App

## Overview

This is a simple order management Python project following **Clean Architecture** and **DDD** principles.

For run you could follow any oth below path:

    - running in local
    - running with docker

## Feature Status

Until now, all CRUD operation for orders are implemented. but following endpoint have been released:

    - create order
    - list order (return all for manager user and owned for customer)

User management has not been implemented yet. but as an start follow below steps to create user:

    - for login to admin panel: use admin user with similar for pass.
    - two groups created: manager and user
    - two user created (admin, customer) and moved to respectively groups:
    - you can add another user and assign them in any of manager or customer group

## Project Structure

    ```bash
    root/
    ├── src/
    │    └── order_app/
    │        ├── domain/
    │        │   ├─── entities/ --> entities and their related value objects
    │        │   └─── value_objects --> common value objects
    │        ├── application/
    │        │   └─── use_cases/
    │        ├── interface/
    │        │   ├─── controllers/
    │        │   ├─── presenters/
    │        │   └─── view_models/
    │        └── infrastructure/
    │            └─── web_app/
    │                 └─── django_order_app/ --> django app with repositories implementation.
    │    
    └── tests/ --> test with similar folder structure to src folder
    ```

    ```bash
    HTTP Request (Django)
            ↓
    Interface Layer
    └── Controller
            ↓
    Application Layer
    └── Use Case
            ↓
    Domain Layer
    └── Entities / Value Objects
            ↓
    Application Layer
    └── Use Case Result
            ↓
    Interface Layer
    └── Presenter
            ↓
    ViewModel
            ↓
    HTTP Response (Django)
    ```

## Setup / Installation (Local)

1. clone the repository

    ```bash
    git clone https://github.com/hassan-mohagheghian/oder_management_ddd_ca
    cd oder_management_ddd_ca
    ```

1. Create a virtual environment in the root folder

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Linux/macOS
    ```

1. Use PYTHONPATH

    ```bash
    export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"  # Linux/macOS
    ```

1. Install dependencies

    ```bash
    pip install -r requirements.txt
    ```

1. Running the Application

    ```bash
    python -m src.main
    ```

1. Running Tests

    ```bash
    pytest
    ```

## Run with Docker

    ```bash
    docker compose up
    ```
