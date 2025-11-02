import threading
import tempfile
from django.conf import settings
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
import pandas as pd
import os
from .models import CourseInfo
from .google_drive_utils import upload_to_drive
from django.core.files.storage import FileSystemStorage
# Create your views here

# Marge and duplicates
def mergeAndDuplicate(files):
    dataframes = []
    for f in files:
        df = pd.read_excel(f)
        dataframes.append(df)
    merge = pd.concat(dataframes, ignore_index=True)
    # duplicate_num = merge.duplicated().sum()
    # print(f"total duplicates num is : {duplicate_num}")
    # Only compare these meaningful columns
    key_columns = ['name', 'email', 'course_name', 'price', 'city']

    # print(merge.duplicated(subset=key_columns))
    duplicate_num = merge.duplicated(subset=key_columns).sum()
    
    # delete duplicates
    unique_df = merge.drop_duplicates(subset=key_columns).reset_index(drop=True)

    return unique_df , duplicate_num

# name-->email-->course_name-->price-->city-->created_at
# insert data into database
def insert_data(df,status,model):
    for _, row in df.iterrows():
        model.objects.create(
            name = row['name'],
            email = row['email'],
            course_name = row['course_name'],
            price = row['price'],
            city = row['city'],
            enrolled_at = row['created_at'],
            status = status           
            )


def background_upload(file_path):
    try:
        upload_to_drive(file_path)
        print("succeed to upload")
    except Exception as e:
        print("Google Drive upload failed:", e)        



def home(req):
    context = {}  # ✅ initialize context for all cases
    # Part:01 (Merged and Saved data) 
    # Take excel file from frontend form
    if req.method == "POST":
        sts = req.POST.get('status')
        files = req.FILES.getlist("uploaded_files")
        if not files:
            #  if no file uploaded, send an error message to template
            messages.error(req, "❌ Please upload at least one Excel file.")
            return redirect('/')
        # files are merged and drop duplicates and return unique data
        data, dup_num = mergeAndDuplicate(files)
        # insert data into database
        insert_data(data,sts,CourseInfo)

        # Save merged dataframe to a temporary Excel file for uploading
        # Use NamedTemporaryFile so it's cross-platform and safe for concurrency
        # Inside your home view (POST section)
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix='.xlsx')
        tmp_name = tmp.name
        tmp.close()
        data.to_excel(tmp_name, index=False)
        # start background thread to upload the temp file to Google Drive
        
        folder_id = getattr(settings, 'GOOGLE_DRIVE_FOLDER_ID', None)
        t = threading.Thread(target=background_upload, 
                             args=(tmp_name,), 
                             daemon=True)
        t.start()

        # ✅ Success message shown after redirect
        messages.success(req, f"✅ Files saved successfully! (Total {dup_num} duplicates found and removed and also save {len(data)}) data into database")
        return redirect('/')
    
    # Part:02 (get data from DB and send it into frontend)
    data = CourseInfo.objects.filter(status='draft').order_by('-id')
    paginator = Paginator(data,10)
    page_number = req.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    
    return render(req,'excelApp/home.html', context)

def viewInfo(req,id):
    studentInfo = get_object_or_404(CourseInfo,id=id)
    return render(req, 'excelApp/details.html',{'studentInfo':studentInfo})

def edit_stu_info(req,id):
    studentInfo = get_object_or_404(CourseInfo,id=id)

    if req.method == 'POST':
         studentInfo.name = req.POST.get('name')
         studentInfo.email = req.POST.get('email')
         studentInfo.course_name = req.POST.get('course_name')
         studentInfo.price = req.POST.get('price')
         studentInfo.city = req.POST.get('city')
         studentInfo.status = req.POST.get('status')
         studentInfo.save()
         messages.success(req,"✅ Course updated successfully!")
         return redirect('stu_info',id=id)

    return render(req,'excelApp/edit_stu_info.html',{'studentInfo':studentInfo})

def delete_stu(req,id):
    del_item = get_object_or_404(CourseInfo,id=id)
    del_item.delete()
    messages.success(req,"Item deleted successfully! ")
    return redirect('/')

def confirm_student(req,id):
    confirmed_item = get_object_or_404(CourseInfo,id=id)
    confirmed_item.status = "published" 
    confirmed_item.save()
    messages.success(req,"data published")
    return redirect('published_data')

def published(req):
    data = CourseInfo.objects.filter(status='published')
    return render(req,'excelApp/published.html',{'data':data})

def courseStatistics(req):
    # get all data from DB
    data = CourseInfo.objects.all().values()
    # convert them into dataframe
    df = pd.DataFrame(list(data))

    # course wise sell
    course_wise_sell = df.groupby('course_name').agg(
        total_sales = ('price','sum'),
        course_count = ('course_name','count')
    )
    # convert into dictionary
    course_wise_sell_dict = course_wise_sell.to_dict(orient='index')
    # city wise sell
    city_wise_sell = df.groupby('city').agg(
        total_sales = ('price','sum'),
        course_count = ('city','count')
    )
    # convert into dictionary
    city_wise_sell_dict = city_wise_sell.to_dict(orient='index')

    context = {
        'courseWiseSales' : course_wise_sell_dict,
        'cityWiseSales' : city_wise_sell_dict
    }

    return render(req,'excelApp/analyticsPage.html',context)

