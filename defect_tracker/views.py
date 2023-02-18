from django.shortcuts import render, HttpResponse
from .forms import DefectForm
# Create your views here.


def home(request):
    context = {}
    if request.method == "POST":
        form = DefectForm(request.POST)
        if form.is_valid():
            form.save()
            print("form is valid and saved!")
            return HttpResponse("Thanks for submitting the form!!")
        else:
            print(form.errors)  # print form errors to the console

            print("form is not valid ")
    else:
        form = DefectForm()
        context["form"] = form

    return render(request, "get_defects.html", context)


def show_defects(request):
    context = {}
    return render(request, "defect_metrics.html", context)
