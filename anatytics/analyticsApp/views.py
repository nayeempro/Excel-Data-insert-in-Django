from django.shortcuts import render
import pandas as pd

from .models import StudentCourse
# Create your views here.
def home(request):
    return render(request, 'analyticsApp/home.html')

def upload(request):
    if request.method == "POST":
        files = request.FILES.getlist('excel_files')

        if not files:
            #  if no file uploaded, send an error message to template
            return render(request, 'analyticsApp/upload.html', {'error': 'Please upload at least one Excel file.'})

        try:
            dataframes = []
            for f in files:
                df = pd.read_excel(f)
                # print(df.head,"print")
                dataframes.append(df)

            merged = pd.concat(dataframes, ignore_index=True)
            dup_num = merged.duplicated().sum()
            print(f"total duplicates num is : {dup_num}")
            data_unique = merged.drop_duplicates().reset_index(drop=True)
            # merged.drop_duplicates(inplace=True)
            def insert_data(dt,model):
                for _, row in dt.iterrows():
                    model.objects.create(
                        # id=row['id'],
                        StudentName=row['StudentName'],
                        CourseName=row['CourseName'],
                        Email=row['Email'],
                        Price=row['Price'],
                        )
            insert_data(data_unique,StudentCourse)
            # Send a "success" flag to the template(upload.html file)
            return render(request, 'analyticsApp/upload.html', {'success': True,'duplicates':dup_num})

        except Exception as e:
            # Send the error message to the template
            return render(request, 'analyticsApp/upload.html', {'error': str(e)})

    # when start--> GET request → Just show the empty form
    return render(request,'analyticsApp/upload.html')

def showTable(request):
    data = StudentCourse.objects.all()
    return render(request,'analyticsApp/table.html',{'data':data})

def analytics(request):
     # Get all records from DB
    queryset = StudentCourse.objects.all().values()
    
    # Convert to pandas DataFrame
    df = pd.DataFrame(list(queryset))
    course_analysis = df.groupby('CourseName').agg(
    total_sales=('Price', 'sum'),
    course_count=('CourseName', 'count')
    )
    course_analysis_dict = course_analysis.to_dict(orient='index')
    print(course_analysis_dict)

    
    return render(request,'analyticsApp/analytics.html', {'data': course_analysis_dict})

