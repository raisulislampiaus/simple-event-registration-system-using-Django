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
  
 

  
  
![2023-12-31_155800](https://github.com/raisulislampiaus/simple-event-registration-system-using-Django/assets/54791396/f06051d0-dd9e-4c68-81ff-15d7dde6daff)
![2023-12-31_155622](https://github.com/raisulislampiaus/simple-event-registration-system-using-Django/assets/54791396/dad181e9-43f9-4e36-b6fb-eba4d9331dff)
![2023-12-31_155949](https://github.com/raisulislampiaus/simple-event-registration-system-using-Django/assets/54791396/f531e5cc-628b-44b7-a008-2424a3bdb12d)
![2023-12-31_155922](https://github.com/raisulislampiaus/simple-event-registration-system-using-Django/assets/54791396/b9b1c165-9115-4b2d-9cd5-4477c9563baf)
![2023-12-31_155904](https://github.com/raisulislampiaus/simple-event-registration-system-using-Django/assets/54791396/0f6b1482-c174-4631-9d64-c9ec109d80bf)
![2023-12-31_155823](https://github.com/raisulislampiaus/simple-event-registration-system-using-Django/assets/54791396/269b64a0-dfc5-45c0-bf3f-e8523e1b6fd7)
