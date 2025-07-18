1. Clone the repository:
   git clone https://github.com/ramserssesd/Job-Board-Application.git
2. Create virtual environment:
   python -m venv venv && source venv/bin/activate
3. Install dependencies:
4. Run migrations:
   python manage.py migrate
5. Create superuser:
   python manage.py createsuperuser
6. Run the server:
   python manage.py runserver
Docker Setup
1. Build and run containers:
   docker-compose up --build
2. Create superuser inside container:
   docker-compose exec web python manage.py createsuperuser
Access URLs
- Admin Panel: http://localhost:8000/admin/
- API Base: http://localhost:8000/api/
- Swagger Docs: http://localhost:8000/swagger/
- Front ebd user: http://localhost:8000/login/
JWT Authentication
POST /api/login/
Body:
{ "name": "1234", "password": "1234" }
Returns access and refresh tokens.
Use Authorization header: Bearer <access_token>
API Endpoints
- POST auth/token/ — JWT login
- GET/POST /api/jobs/ — List & create jobs
- PUT/DELETE /api/jobs/<id>/ — Update & delete jobs
- GET /api/applications/ — View applicants
- POST /api/applications/ — Submit job application
Frontend
Basic admin panel located in `http://localhost:8000/login/`. Open in browser. all login you will get it all functionlity
Includes login, job management, and applicant viewing.
Postman & Swagger
Use Swagger at http://localhost:8000/swagger/ for API docs.
Import the provided Postman collection for testing endpoints.
