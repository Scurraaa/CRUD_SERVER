from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from central.models import Student
from central.serializers import StudentSerializers
client = APIClient()


class post_single_student(APITestCase):
	"""
	Test Module for Post Method
	"""
	def setUp(self):
		self.student = Student.objects.create(
		student_number='1510688',
		first_name='Joshua',
		middle_initial='C.',
		last_name='Bacani',
		year_level='5th',
		program='BSCPE',
		password='joshua123'
		)
		
		self.valid_payload = {
		"student_number": "1510001",
		"first_name": "owa",
		"middle_initial": "D.",
		"last_name": "roger",
		"year_level": "1st",
		"program": "bscs",
		"password": "onep!ece"
		}
		
		self.invalid_payload = {
		"student_number": "1510688",
		"first_name": "joshua",
		"middle_initial": "C.",
		"last_name": "Bacani",
		"year_level": "5th",
		"program": "BSCPE",
		"password": "joshua123"
		}
	#test with valid inputs	
	def test_201_student(self):
		response = self.client.post("/student", data=self.valid_payload)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
	#test with invalid inputs
	def test_400_student(self):
		response = self.client.post("/student", data=self.invalid_payload)
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
		
class retrieve_all_student(APITestCase):
	"""
	Test Module for Retrieving ALL data
	"""
	def setUp(self):
		Student.objects.create(
		student_number='1510688',
		first_name='Joshua',
		middle_initial='C.',
		last_name='Bacani',
		year_level='5th',
		program='BSCPE',
		password='joshua123'
		)
		
		Student.objects.create(
		student_number='151001',
		first_name='owa',
		middle_initial='A.',
		last_name='Roger',
		year_level='4th',
		program='BSCE',
		password='joshua321'
		)
	
	def test_200_student(self):
		#retrieve API response
		response = self.client.get("/student")
		#retrieve database data
		students = Student.objects.all()
		serializer = StudentSerializers(students, many=True)
		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		
class get_single_student(APITestCase):
	"""
	Test Module for Retrieiving Single Data
	"""
	
	def setUp(self):
		self.joshua = Student.objects.create(
		student_number='1510688',
		first_name='Joshua',
		middle_initial='C.',
		last_name='Bacani',
		year_level='5th',
		program='BSCPE',
		password='joshua123'
		)
		
		self.owa = Student.objects.create(
		student_number='151001',
		first_name='owa',
		middle_initial='A.',
		last_name='Roger',
		year_level='4th',
		program='BSCE',
		password='joshua321'
		)
		
	def test_200_single_student(self):
		response = self.client.get("/student/1510688")
		student = Student.objects.get(student_number=self.joshua.student_number)
		serializer = StudentSerializers(student)
		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		
class delete_single_student(APITestCase):
	"""
	Test Module for Deleting single data
	"""
	def setUp(self):
		self.joshua = Student.objects.create(
		student_number='1510688',
		first_name='Joshua',
		middle_initial='C.',
		last_name='Bacani',
		year_level='5th',
		program='BSCPE',
		password='joshua123')
		
		self.owa = Student.objects.create(
		student_number='151001',
		first_name='owa',
		middle_initial='A.',
		last_name='Roger',
		year_level='4th',
		program='BSCE',
		password='joshua321')
		
	def test_204_delete_student(self):
		response = self.client.delete("/student/1510688")
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
		
	def test_404_delete_student(self):
		response = self.client.delete("/student/151111")
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class update_single_student(APITestCase):
	"""
	Test Module for Updating a single data
	"""
	def setUp(self):
		self.joshua = Student.objects.create(
		student_number='1510688',
		first_name='Joshua',
		middle_initial='C.',
		last_name='Bacani',
		year_level='5th',
		program='BSCPE',
		password='joshua123')
		
		self.owa = Student.objects.create(
		student_number='151001',
		first_name='owa',
		middle_initial='A.',
		last_name='Roger',
		year_level='4th',
		program='BSCE',
		password='joshua321')
		
		self.valid_payload = {
		"student_number": "1510688",
		"first_name": "owa",
		"middle_initial": "D.",
		"last_name": "roger",
		"year_level": "1st",
		"program": "bscs",
		"password": "onep!ece"
		}
		
		self.invalid_payload = {
		"student_number": "",
		"first_name": "joshua",
		"middle_initial": "C.",
		"last_name": "Bacani",
		"year_level": "5th",
		"program": "BSCPE",
		"password": "joshua123"
		}
		
	def test_200_update_student(self):
		response = self.client.put("/student/1510688", data=self.valid_payload)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		
	def test_400_update_student(self):
		response = self.client.put("/student/1510688", data=self.invalid_payload)
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
		
		
	