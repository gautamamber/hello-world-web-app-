from django.contrib import admin
from .models import Student
from django import forms
import csv
from django.shortcuts import render, redirect
from django.urls import path

class StudentModelForm(forms.Form):
	csv_file = forms.FileField(required = False, label = "Please select a file")

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	change_list_template = "admin/uploadcsvadmin/student/change_list.html"

	def get_urls(self):
		urls = super().get_urls()
		my_urls = [
			path('import-csv/', self.import_csv),
		]
		return my_urls + urls

	def import_csv(self, request):
		if request.method == "POST":
			csv_file = request.FILES["csv_file"]
			file_data = csv_file.read().decode("utf-8")
			lines = file_data.split('\n')
			lines.pop(0)
			for line in lines:
				field = line.split(',')
				if field[0]:
					data = Student.objects.create(
							name = field[0],
							roll_no = field[1],
							stu_class = field[2],
							school = field[3],
							city = field[4],
						)
			self.message_user(request, "Your csv file has been imported")

		form = StudentModelForm()
		payload = {"form":form}
		return render(request, "admin/uploadcsvadmin/student/csv_form.html", payload)



