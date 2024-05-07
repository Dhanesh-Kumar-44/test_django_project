from django.shortcuts import render
import csv
from django.http import JsonResponse
import pandas as pd
from .models import CSVData, RegisterUser
import os


def read_csv(request):
    # csv_file_path = '/home/kumail/Desktop/employ2.csv'  

    current_path = os.getcwd()
    print("Current Working Directory:", current_path)

    csv_file_path = '/app/employ2.csv'
    df = pd.read_csv(csv_file_path)
    sorted_df = df.sort_values(by='salary')
    output_csv_file = '/app/sorted_data.csv'
    sorted_df.to_csv(output_csv_file, index=False)
    # json_data = sorted_df.to_json(orient='records')
    new_count = 0
    same_count = 0
    for index, item in df.iterrows():
        record = CSVData.objects.filter(name=item['name'], age=item['age'],salary=item['salary']).exists()
        if record:
            same_count += 1
            # return JsonResponse({'message': 'Record with the same name and age already exists.'}, status=400)
        else:
            new_record = CSVData(name=item['name'], age=item['age'], salary=item['salary'])
            new_record.save()
            new_count += 1
            # return JsonResponse({'message': 'CSV data added successfully.'}, status=201)
    msg = 'CSV data added ' + str(new_count) + ' new records and found same records: '+ str(same_count)
    return JsonResponse({'message':  msg}, status=201)


def register(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        record = RegisterUser.objects.filter(email=email).exists()
        if record:
            # return JsonResponse({'message':  msg}, status=201)
            return render(request, 'register.html',{'msg': 'user email already exit'})
        new_record = RegisterUser(name=name, email=email, password=password)
        new_record.save()
        return render(request, 'register.html',{'msg': 'user registered'})
    #     form = UserForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('registered_users')
    # else:
    #     form = UserForm()
    # return render(request, 'register.html', {'form': form})
    return render(request, 'register.html')
