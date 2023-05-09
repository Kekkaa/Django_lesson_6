from django.shortcuts import render


def main_page(request):
    return render(request, 'core/main_page.html')

def employers_list(request):
    return render(request, 'core/employers_list.html')

def employee_of_the_month(request):
    return render(request, 'core/employee_of_the_month.html')

def add_employee(request):
    return render(request, 'core/add_employee.html')
