from django.http import HttpResponse
from django.shortcuts import render
from .models import Student, Course
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def create_course(request):
    if request.method == 'POST':
       courseid = request.POST.get('courseid')
       name = request.POST.get('name')
       course = Course(courseid=courseid, name=name)
       course.save()
       return HttpResponse('Course created successfully')
    else:
        return render(request, 'create_course.html')
   
@csrf_exempt
def create_student(request):
    if request.method == 'POST':
        cms = request.POST.get('cms')
        name = request.POST.get('name')
        email = request.POST.get('email')
        father_name = request.POST.get('fatherName')
        dept = request.POST.get('dept')

        course = Course.objects.get(courseid=2)
        course = Course()
        student = Student(cms=cms, name=name, email=email, father_name=father_name, dept=dept, course=course)
        student.save()
        return HttpResponse('Student created successfully')
    else:
        return render(request, 'create_student.html')
    
def get_students(request):
    students = Student.objects.all()
    for student in students:
        print(student.course.name)
    return HttpResponse('Students fetched successfully')

def get_students_by_course(request):
    course = Course.objects.get(courseid=1)
    students = course.student_set.all()    
    for student in students:
        print(student.name)
    return HttpResponse('Students fetched successfully')

    

# #To get data from student table.
# def get_students(request):
#     students = Student.objects.all()

#     for student in students:
#         print("CMS:", student.cms)
#         print("Name:", student.name)
#         print("Email:", student.email)
#         print("Father's Name:", student.father_name)
#         print("Department:", student.dept)
#         print("Course ID:", student.courseid)
#         print("----------------------")

#     return HttpResponse("Data printed in console")
# # To delete all students.


# def delete_all_students(request):
#     Student.objects.all().delete()
#     return HttpResponse("All students deleted successfully")


   
