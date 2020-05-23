from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from central.serializers import StudentSerializers
from central.models import Student




@api_view(['POST', 'GET'])
def add_retrieve_all_student(request):	
	"""
	Function for retrieving all records of all students from the database 
	and add single record of student in the database
	"""
	if request.method == 'GET':
		queryset = Student.objects.all()
		if queryset:
			serializer = StudentSerializers(queryset, many=True)
			return Response(serializer.data, status=status.HTTP_200_OK)
		response = {
			'details': 'No student is currently registered'
			}
		return Response(response, status=status.HTTP_400_BAD_REQUEST)
		
	#Add single record of student in the database	
	elif request.method == 'POST':
		serializer = StudentSerializers(data=request.data)
		if serializer.is_valid():
			
			if not Student.objects.filter(student_number=request.data['student_number']).exists():
				
				serializer.save()
				
				response = {
				'details': 'Request Success'
				}
				
				return Response(response, status=status.HTTP_201_CREATED)
			else:
				
				response = {
				'details': ' Request Failed, Student already registered'
				}
				
				return Response(response, status=status.HTTP_400_BAD_REQUEST)
				
		response = {
				'details': 'Request Failed, please double check your inputs'
				}	
				
		return Response(response, status=status.HTTP_400_BAD_REQUEST)
		

@api_view(['GET', 'PUT','DELETE'])
def update_retrieve_delete_single_student(request, student_number):
	"""
	Function for updating, retrieving, deletint single record
	of student in the database
	"""
	#check if the data exist or not
	try: 
		student = Student.objects.get(student_number=student_number)
	except Student.DoesNotExist:
		response = {
		'details': 'No records found'
		}
		return Response(response,status=status.HTTP_404_NOT_FOUND)
	#Retrieve single record of student by its student number
	if request.method == 'GET':
		serializer = StudentSerializers(student)
		return Response(serializer.data, status=status.HTTP_200_OK)
	#Update single record of a student
	elif request.method == 'PUT':
		serializer = StudentSerializers(student, data=request.data)
		if serializer.is_valid():
			serializer.save()
			response = {
				'details': 'Update Success',
				'updated_data': serializer.data
				}
			return Response(response, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	#delete single record of student
	elif request.method == 'DELETE':
		student.delete()		
		return Response(status=status.HTTP_204_NO_CONTENT)
			
		

			
		