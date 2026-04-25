# Quick start guide

## Setup Instructions

1. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

4. **Create superuser**:
   ```bash
   python manage.py createsuperuser
   ```

5. **Start server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the platform**:
   - Home: http://localhost:8000
   - Admin: http://localhost:8000/admin
   - API: http://localhost:8000/api

## Common Commands

- **Makemigrations**: `python manage.py makemigrations`
- **Migrate**: `python manage.py migrate`
- **Create superuser**: `python manage.py createsuperuser`
- **Run tests**: `python manage.py test`
- **Collect static files**: `python manage.py collectstatic`

## API Endpoints Summary

- **Voting**: `/api/voting/procedures/`, `/api/voting/methods/`
- **Candidates**: `/api/candidates/`, `/api/candidates/comparisons/`
- **Registration**: `/api/registration/requirements/`, `/api/registration/methods/`, `/api/registration/deadlines/`
- **Polling**: `/api/polling/locations/`, `/api/polling/districts/`, `/api/polling/early-voting/`
