# Travel Planning Backend

This is the backend service for the **Travel Planning App**, built with Django REST Framework and PostgreSQL.  
It provides APIs for trip planning, hotel booking, and transport booking.

---

## 🚀 Tech Stack
- **Backend Framework:** Django REST Framework
- **Database:** PostgreSQL
- **API:** RESTful endpoints
- **Frontend (separate repo):** React.js + TailwindCSS

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/MKdir75/Travel-Planning-Backend.git
cd travel-planning-backend

2. Create virtual environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3. Install dependencies
pip install -r requirements.txt

4. Run migrations
python manage.py migrate

5. Start development server
python manage.py runserver

📡 API Endpoints
Trips: /api/trips/
Hotels: /api/hotels/
Transport: /api/transport/
