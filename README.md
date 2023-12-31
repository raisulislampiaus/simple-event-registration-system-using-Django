Step 1:
  How to Project Run:
  1: .\env\Scripts\activate
  2: cd event
  3.  python manage.py runserver
  4.  python manage.py makemigrations 
  5.  python manage.py migrate 
  6.  python manage.py createsuperuser

Step 2: API Check: Using Postman..
  1. Sigup / POST REQ:  http://127.0.0.1:8000/api/users/register/
  2. Login / POST REQ:  http://127.0.0.1:8000/api/users/login/
  3. GetAll_event / GET REQ: http://127.0.0.1:8000/api/v1/events/
  4. Enroll_event / POST REQ:  http://127.0.0.1:8000/api/v1/events/create/  (only Authenticated user & admin  can create Enroll_even).
  5. Registration_list / GET REQ:  http://127.0.0.1:8000/api/v1/registrations/ (only  admin  can 'GET', 'POST').
  6. Event_detail /GET, PUT, DELETE REQ: http://127.0.0.1:8000/api/v1/events/1/ (only  admin  can GET, PUT, DELETE).
  7. Search Event: http://127.0.0.1:8000/api/v1/events/?title=hi.
  
  
  
  
