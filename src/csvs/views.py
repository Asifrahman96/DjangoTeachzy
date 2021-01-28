from django.shortcuts import render
from django.http import HttpResponse
from .forms import CsvModelForm
from .models import Csvs
import csv, io
from teachers.models import Teachers
from django.contrib.auth.decorators import login_required
from tablib import Dataset
# from teachers.resources import TeachersResource


# Create your views here.
@login_required(login_url="/accounts/login")
def upload_file_view(request):
    template = "csvs/upload-file.html"
    # prompt = {
    #     'order': 'Order of the CSV should be first_name, last_name, profile_picure, email_address, phone_number, room_number, subjects_taken'
    # }


    if request.method == 'GET':
        return render(request, template)

        # teachers_resource = TeachersResource()
        # dataset = Dataset()
    
    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a CSV file !')
    
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)

    for column in csv.reader(io_string, delimiter = ',', quotechar = "|"):
        Teachers.objects.update_or_create(
            first_name = column[0],
            last_name = column[1],
            profile_picture = column[2],
            email = column[3],  
            phone_number = column[4],
            room_number = column[5],
            # subjects_taken = set(column[6]),
        )

    context = {
        
    }

    return render(request, template, context)


    # form = CsvModelForm(request.POST or None, request.FILES or None)
    # if form.is_valid():
    #     form.save()
    #     form = CsvModelForm()
    #     obj = Csvs.objects.get(activated=False)
    #     with open(obj.file_name.path, 'r') as f:
    #         reader = csv.reader(f)

    #         for i, row in enumerate(reader):
    #             if i==0:
    #                 pass
    #             else:
    #                 row = "".join(row)
    #                 # row = row.replace(";", "")
    #                 # row = row.split()

    #                 print(row)
    #                 print(type(row))

    #                 first_name = row[1].upper()
    #                 last_name = row[2].upper()
    #                 profile_picture = row[3].upper()
    #                 email = row[4].upper()
    #                 phone_number = row[5].upper()
    #                 room_number = row[6].upper()


    #         #         Teachers.objects.create(
    #         #             first_name = first_name,
    #         #             last_name = last_name,
    #         #             profile_picture = profile_picture,
    #         #             email = email,
    #         #             phone_number = phone_number,
    #         #             room_number = room_number,
    #         #             subjects_taken = subjects_taken.set(),
    #         #         )
    #         # obj.activated = True   
    #         # obj.save()