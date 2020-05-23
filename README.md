# CRUD_SERVER
This is a API Server created in Python using the Django REST Framework. This Server is created for the registration of student.

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

The **/student** is a link dedicated to add a single record on the database and retrieiving all records in the database

**Sample Response for the link /student:**

### GET Method

**200 response**

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

**400 response**
```json
 { "details": "No student is currently registered" }
```

### POST Method

**201 response**
```json
 {
   "details": "Request Success"
 }
```

**400 response**

```json
 {
   "details": "Request Failed, please double check youe inputs"
 }

```

The **/student/<<int:student_number>>** is a link dedicated for retrieiving, updating and deleting a single record on the database the link requires a integer called student_number to be used in the query later.

**Sample Response for the link /student/<<int:student_number>>:**

### GET Method

**200 response (/student/1510688)**

```json
 {
   "student_number": "1510688",
   "first_name": "Joshua",
   "middle_initial": "C.",
   "last_name": "Bacani",
   "year_level": "5th",
   "program": "BSCPE",
   "password": "test123",
 }
```

**400 response (/student/10000)**

```json
{ "details": "No Data found" }
```

### PUT Method

**200 response(/student/1510688)**

```json
{ "details": "Update Success", 
  "updated_data": 
  { 
    "student_number": "1510622", 
    "first_name": "joshua", 
    "middle_initial": "D.", 
    "last_name": "Roger", 
    "year_level": "4th", 
    "program": "BSCE", 
    "password": "dsa12312333" 
   } 
}
```

**400 response (/student/10000)**
```json
{ "details": "No Data found" }
```

### DELETE Method

**204 response (/student/1510688)**
```json
 {}
```










