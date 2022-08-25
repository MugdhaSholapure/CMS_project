from django.shortcuts import render,redirect
from .forms import DepartmentForm,StudentForm
from .models import DepartmentModel,StudentModel

# Create your views here.
def home(request):
	return render(request,"home.html")

def showdept(request):
	data = DepartmentModel.objects.all()
	return render(request,"showdept.html",{"data":data})

def adddept(request):
	if request.method == "POST":
		data = DepartmentForm(request.POST)
		if data.is_valid():
			data.save()
			fm = DepartmentForm()
			return render(request,"adddept.html",{"fm":fm,"msg":"Dept Added"})
		else:
			return render(request,"adddept.html",{"fm":data,"msg":"Check Errors"})
	else:
		fm = DepartmentForm()
		return render(request,"adddept.html",{"fm":fm})

def deletedept(request,id):
	d = DepartmentModel.objects.get(deptid=id)
	d.delete()
	return redirect("showdept")

def showstudent(request):
	data = StudentModel.objects.all()
	return render(request,"showstudent.html",{"data":data})

def addstudent(request):
	if request.method == "POST":
		data = StudentForm(request.POST)
		if data.is_valid():
			data.save()
			fm = StudentForm()
			return render(request,"addstudent.html",{"fm":fm,"msg":"Student Added"})
		else:
			return render(request,"addstudent.html",{"fm":data,"msg":"Check Errors"})
	else:
		fm = StudentForm()
		return render(request,"addstudent.html",{"fm":fm})

def deletestudent(request,id):
	d = StudentModel.objects.get(rno=id)
	d.delete()
	return redirect("showstudent")

