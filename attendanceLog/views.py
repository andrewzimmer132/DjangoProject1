from django.shortcuts import render
from django.views import View
from .models import Attendance
from datetime import datetime

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

    def post(self, request):
        name = request.POST.get('student_name')
        course = request.POST.get('course')
        date_str = request.POST.get('attendance_date')

        try:
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
            Attendance.objects.create(student_name=name, course=course, attendance_date=date)
            msg = "Record inserted successfully"
        except Exception as e:
            msg = f"Error: {e}"

        return render(request, 'home.html', {'message': msg})


class AttendanceLogView(View):
    def get(self, request):
        records = Attendance.objects.all()
        return render(request, 'log.html', {'records': records})

    def post(self, request):
        course = request.POST.get('course_filter')
        date = request.POST.get('date_filter')
        records = Attendance.objects.all()

        if course:
            records = records.filter(course__icontains=course)
        if date:
            records = records.filter(attendance_date=date)

        return render(request, 'log.html', {
            'records': records,
            'course_filter_value': course,
            'date_filter_value': date
        })
