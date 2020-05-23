# CRUD_SERVER
This is a API Server created in Python using the Django REST Framework



## :arrow_up: How to Setup
### Requirements
To run this SERVER you must have the following software on your computer
* Python 3.6+
* Django 3.0.6

**Step 1:** git clone this repo:
```bash
  $ https://github.com/Scurraaa/CRUD_SERVER.git
  ````

**Step 2:** change directory to the cloned repo:

**Step 3:** 
To install additional Python Dependencies of the project you can run the following command on the project folder
```python
pip install -r requirements.txt
  ```

## :arrow_forward: How to Run the Server
To run this API Server run the following command on the project folder
```python
python manage.py runserver
  ```
This CRUD Server has two (2) available links
* /student
* /student/<int:student_number>

The **/student** link function is to add a single record on the database and retrieiving all records in the database
Sample output is below:

**200 response (GET Method)**
```json
[
 {
   "student_number": "1510688",
   "first_name": "Joshua",
   "middle_initial": "C.",
   "last_name": "Bacani",
   "year_level": "5th",
   "program": "BSCPE",
   "password": "test123",
 }
 ...
]
```
**400 response (GET Method)**
```json
[
 { "details": "No student is currently registered" }
]
```

** 201 response (POST Method)
```json
[
 {
   "details": "Request Success"
 }
]
```

** 400 response (POST Method)
```json
[
 {
   "details": "Request Failed, please double check youe inputs"
 }

]
```






