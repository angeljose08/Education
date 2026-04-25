# Election Education Platform

An interactive Django-based platform designed to break down the complexities of the election process. This project provides personalized, easy-to-understand insights into voting procedures, candidate information, voter registration requirements, and polling locations.

## 🎯 Features

### 1. **Voting Procedures** 📋
- State-specific voting methods and procedures
- Information about voting methods (in-person, mail-in, early voting, provisional)
- Accessibility features and accommodations
- Detailed procedural guides by category

### 2. **Candidate Information & Comparison** 👥
- Comprehensive candidate profiles with bio and contact information
- Policy positions and stances on key issues
- Side-by-side candidate comparisons
- Search and filter by position, state, election year

### 3. **Voter Registration Information** 📝
- State-specific registration requirements
- Multiple registration methods (online, mail, in-person, automatic)
- Registration deadlines and important dates
- Eligibility and identification requirements

### 4. **Polling & Early Voting Locations** 📍
- Find polling locations by state, city, or proximity
- Early voting location information with dates/hours
- Accessibility information
- Location search with nearby feature

## 🛠️ Tech Stack

- **Backend**: Django 4.2
- **API**: Django REST Framework
- **Database**: SQLite (default, configurable)
- **Frontend**: HTML/CSS/JavaScript (vanilla)
- **Additional Libraries**: CORS support, Pillow for image handling

## 📋 Prerequisites

- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
cd /workspaces/Education
```

### 2. Create Virtual Environment
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Copy Environment Variables
```bash
cp .env.example .env
# Edit .env with your configuration if needed
```

### 5. Run Migrations
```bash
python manage.py migrate
```

### 6. Create Superuser (Admin)
```bash
python manage.py createsuperuser
```
Follow the prompts to create an admin account.

### 7. Load Sample Data (Optional)
```bash
python manage.py collectstatic --noinput
```

### 8. Start Development Server
```bash
python manage.py runserver
```

The application will be available at `http://localhost:8000`

## 📚 Project Structure

```
Education/
├── config/                 # Django configuration
│   ├── settings.py        # Main settings file
│   ├── urls.py            # URL routing
│   ├── wsgi.py            # WSGI application
│   └── asgi.py            # ASGI application
├── apps/                   # Django applications
│   ├── core/              # Core shared functionality
│   ├── voting/            # Voting procedures
│   ├── candidates/        # Candidate information
│   ├── registration/      # Voter registration
│   └── polling/           # Polling locations
├── templates/             # HTML templates
├── static/                # Static files (CSS, JS, images)
├── media/                 # User-uploaded media
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## 🔌 API Documentation

### Base URL
```
http://localhost:8000/api
```

### Voting Procedures

#### Get All Voting Procedures
```
GET /api/voting/procedures/
```
Query parameters:
- `search`: Search by title or description
- `category`: Filter by category (registration, voting_methods, day_of_voting, accessibility, requirements)

#### Get Voting Procedures by State
```
GET /api/voting/procedures/by_state/?state=CA
```

#### Get Voting Methods
```
GET /api/voting/methods/
```

---

### Candidates

#### Get All Candidates
```
GET /api/candidates/
```
Query parameters:
- `search`: Search by name, position, or office sought
- `ordering`: Sort by field (name, position)

#### Get Candidates by Position
```
GET /api/candidates/by_position/?position=Governor
```

#### Get Candidates by State
```
GET /api/candidates/by_state/?state=TX
```

#### Get Candidates by Election Year
```
GET /api/candidates/by_year/?year=2024
```

#### Create Candidate Comparison
```
POST /api/candidates/comparisons/
```
Body:
```json
{
  "candidate_ids": [1, 2, 3],
  "position": "Governor",
  "election_year": 2024
}
```

---

### Voter Registration

#### Get Registration Requirements
```
GET /api/registration/requirements/
```

#### Get Registration Requirements by State
```
GET /api/registration/requirements/by_state/?state=NY
```

#### Get Registration Methods
```
GET /api/registration/methods/
```

#### Get Registration Methods by State
```
GET /api/registration/methods/by_state/?state=FL
```

#### Get Registration Deadlines
```
GET /api/registration/deadlines/
```

#### Get Deadlines by State
```
GET /api/registration/deadlines/by_state/?state=PA
```

---

### Polling Locations

#### Get All Polling Locations
```
GET /api/polling/locations/
```
Query parameters:
- `search`: Search by name, city, or address

#### Get Polling Locations by State
```
GET /api/polling/locations/by_state/?state=CA
```

#### Get Polling Locations by City
```
GET /api/polling/locations/by_city/?city=Los+Angeles&state=CA
```

#### Find Nearby Polling Locations
```
GET /api/polling/locations/nearby/?lat=37.7749&lon=-122.4194&radius=5
```
Parameters:
- `lat`: Latitude
- `lon`: Longitude
- `radius`: Search radius in miles (default: 5)

#### Get Early Voting Locations
```
GET /api/polling/early-voting/
```

#### Get Early Voting Locations by State
```
GET /api/polling/early-voting/by_state/?state=NV
```

---

## 👨‍💼 Admin Panel

Access the Django admin panel at:
```
http://localhost:8000/admin
```

The admin panel allows you to:
- Manage voting procedures and methods
- Add and edit candidate information and policies
- Manage registration requirements and methods
- Add polling locations and early voting sites
- Create and organize content

## 🎨 Customization

### Adding Custom Content

1. **Add Voting Procedures**: Jump to Admin > Voting > Voting Procedures
2. **Add Candidates**: Go to Admin > Candidates > Candidates
3. **Add Registration Info**: Visit Admin > Registration > Requirements/Methods/Deadlines
4. **Add Polling Locations**: Access Admin > Polling > Polling Locations

### Styling

The main template uses inline CSS. To customize:
1. Edit `templates/index.html` for structure and styles
2. Add custom CSS to the `<style>` section
3. Create additional templates in `templates/` directory

## 🔐 Security

for production deployment:
1. Set `DEBUG = False` in settings.py
2. Update `SECRET_KEY` in `.env`
3. Configure `ALLOWED_HOSTS` properly
4. Use a production database (PostgreSQL recommended)
5. Enable HTTPS
6. Set secure cookie flags

## 📁 Database Models

### Voting App
- `VotingProcedure`: Voting procedures and guidelines
- `VotingMethod`: Different voting methods with pros/cons

### Candidates App
- `Candidate`: Candidate information
- `CandidatePolicy`: Candidate positions on issues
- `CandidateComparison`: User-created candidate comparisons

### Registration App
- `RegistrationRequirement`: State-specific registration requirements
- `RegistrationMethod`: Available registration methods by state
- `RegistrationDeadline`: Important dates and deadlines

### Polling App
- `PollingLocation`: Physical polling place locations
- `PollingDistrict`: Polling districts/precincts
- `EarlyVotingLocation`: Early voting sites with dates

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🆘 Support & Contact

For questions, issues, or suggestions:
- Create an issue in the repository
- Contact the project maintainers

## 🗳️ Mission

Making voting information accessible, easy to understand, and personalized for every voter, breaking down election complexities one feature at a time.
