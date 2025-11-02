from concurrent.futures import ThreadPoolExecutor
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

def hello_world(request):
    return HttpResponse("Hello, World! 🌍")

def home(req):
    return render(req,'helloapp/home.html')

def about(req):
    return render(req,'helloapp/about.html')

import pandas as pd
from .models import Book, Customers1
from .models import Customers2
from .models import Customers3
def test(req):
    # dt1 = pd.read_excel("G:/AI_Backend/Django_class/myproject/customers_file_1.xlsx", engine="openpyxl")
    # dt2 = pd.read_excel("G:/AI_Backend/Django_class/myproject/customers_file_2.xlsx", engine="openpyxl")
    # dt3 = pd.read_excel("G:/AI_Backend/Django_class/myproject/customers_file_3.xlsx", engine="openpyxl")

    # convert these dataframe into dictionary
    # data_dict1 = dt1.to_dict(orient='records')
    # data_dict2 = dt2.to_dict(orient='records')
    # data_dict3 = dt3.to_dict(orient='records')

    #need a function for insert
    # def insert_data(dt,model):
    #     for _, row in dt.iterrows():
    #         model.objects.create(
    #             customer_id=row['customer_id'],
    #             name=row['name'],
    #             email=row['email'],
    #             phone=row['phone'],
    #             age=row['age'],
    #             city=row['city']
    #             )
    # Database a Data Insert korlam alada table alada model
    # insert_data(dt1, Customers1)
    # insert_data(dt2, Customers2)
    # insert_data(dt3, Customers3)

    # Ebar database data gula nibo
    data1 = Customers1.objects.all()
    data2 = Customers2.objects.all()
    data3 = Customers3.objects.all()
    # frontend a pathay dilam
    return render(req,'helloapp/test.html', {
        'data1':data1,
        'data2':data2,
        'data3':data3,
        })

def loading(req):

    # --- Example file paths (replace with your actual file paths) ---
    files = {
        "file1":"G:/AI_Backend/Django_class/myproject/customers_file_1.xlsx",
        "file2":"G:/AI_Backend/Django_class/myproject/customers_file_2.xlsx",
        "file3":"G:/AI_Backend/Django_class/myproject/customers_file_3.xlsx"
    }
    # --- Model mapping for each file ---
    model_map = {
        "file1": Customers1,
        "file2": Customers2,
        "file3": Customers3,
    }
        # --- Function to load Excel and insert into database ---
    def load_and_insert(file_key):
        path = files[file_key]
        model = model_map[file_key]
        print(f"Loading {path}...")
        df = pd.read_excel(path, engine="openpyxl")

        # Convert and insert into DB
        objs = [
            model(
                customer_id=row['customer_id'],
                name=row['name'],
                email=row['email'],
                phone=row['phone'],
                age=row['age'],
                city=row['city'],
            )
            for _, row in df.iterrows()
        ]
        model.objects.bulk_create(objs, batch_size=1000)
        print(f"Inserted {len(objs)} rows into {model.__name__}")
        return f"{file_key} completed"
        # --- Run all three concurrently ---
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(load_and_insert, files.keys())

    # --- Now fetch all data from DB ---
    data1 = Customers1.objects.all()
    data2 = Customers2.objects.all()
    data3 = Customers3.objects.all()

    return render(req, 'helloapp/loading.html', {
        'data1': data1,
        'data2': data2,
        'data3': data3,
    })
    

from .models import Customer1 
# Insert a new customer record directly into the database
def insert_customer_Data_1(req):
    cusData = Customer1(
        name="Mayeem",
        email="mdnam@gmail.com",
        phone="18827727"
    )
     
    # Save the customer to the database
    cusData.save()

    return HttpResponse("Customer data insert Successfully")

# Insert a new customer using .create() method
def insert_customer_Data_2(req):
    var_name="Mayeem"
    var_email="ekn@gmail.com"
    var_phone="18827727"
    
    Customer1.objects.create(
          name = var_name,
          email=var_email,
          phone=var_phone
     )
    return HttpResponse("Customer data insert Successfully using create method")

#Bulk Insert
def bulk_insert(req):
      
    customers_data = [
        Customer1(name="Alice Brown", email="alice.brown@example.com", phone="2345678901"),
        Customer1(name="Bob White", email="bob.white@example.com", phone="3456789012"),
        Customer1(name="Charlie Green", email="charlie.green@example.com", phone="4567890123"),
        Customer1(name="David Black", email="david.black@example.com", phone="5678901234"),
        Customer1(name="Emily Blue", email="emily.blue@example.com", phone="6789012345"),
        Customer1(name="Frank Harris", email="frank.harris@example.com", phone="7890123456"),
        Customer1(name="Grace Johnson", email="grace.johnson@example.com", phone="8901234567"),
        Customer1(name="Henry King", email="henry.king@example.com", phone="9012345678"),
        Customer1(name="Ivy Lee", email="ivy.lee@example.com", phone="0123456789"),
        Customer1(name="Jack Miller", email="jack.miller@example.com", phone="1234509876"),
        Customer1(name="Kathy Moore", email="kathy.moore@example.com", phone="2345612345"),
        Customer1(name="Liam Walker", email="liam.walker@example.com", phone="3456723456"),
        Customer1(name="Mia Davis", email="mia.davis@example.com", phone="4567834567"),
        Customer1(name="Nathan Scott", email="nathan.scott@example.com", phone="5678945678"),
        Customer1(name="Olivia Carter", email="olivia.carter@example.com", phone="6789056789"),
        Customer1(name="Paul Turner", email="paul.turner@example.com", phone="7890167890"),
        Customer1(name="Quincy Mitchell", email="quincy.mitchell@example.com", phone="8901278901"),
        Customer1(name="Rachel Adams", email="rachel.adams@example.com", phone="9012389012"),
        Customer1(name="Samuel Clark", email="samuel.clark@example.com", phone="0123490123"),
        Customer1(name="Tina Martinez", email="tina.martinez@example.com", phone="1234501234"),
        Customer1(name="Ursula Allen", email="ursula.allen@example.com", phone="2345612347"),
        Customer1(name="Victor Perez", email="victor.perez@example.com", phone="3456723459"),
        Customer1(name="Wendy Wilson", email="wendy.wilson@example.com", phone="4567834569"),
        Customer1(name="Xander Rodriguez", email="xander.rodriguez@example.com", phone="5678945679"),
        Customer1(name="Yvonne King", email="yvonne.king@example.com", phone="6789056790"),
        Customer1(name="Zack Wright", email="zack.wright@example.com", phone="7890167900"),
        # Add more customers here as needed
    ]
    # Perform the bulk insert
    Customer1.objects.bulk_create(customers_data)
    return HttpResponse("Bulk insert successfully")

def show_data(req):
    all_data = Customer1.objects.all()
    data_dict = {"data": all_data}

    return render(req, 'helloapp/table.html', data_dict )


def bookList(req):
    books = Book.objects.all()
    return render(req, 'helloapp/booklist.html', {'books': books})
   

def create_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        description = request.POST['description']
        pic = request.FILES.get('pic')  # Handle the uploaded file
        Book.objects.create(title=title, author=author, description=description, pic=pic)
        return redirect('book_list')
    return render(request, 'helloapp/book_form.html', {'action': 'Create'})

def book_details(req,id):
    # Assignment Backend AI Night 
    book = Book.objects.get(id=id)
    # Here I calculate size / I can do it in create_book function

    size_title = len(book.title.encode("utf-8"))
    size_author = len(book.author.encode("utf-8"))
    size_description = len(book.description.encode("utf-8"))
    size_pic_kb = round(book.pic.size / 1024,2) # 2 ghor after point

    context = {
        'book': book,
        'size_title': size_title,
        'size_author': size_author,
        'size_description':size_description,
        'size_pic_kb': size_pic_kb
    }
    return render(req, 'helloapp/book_details.html' ,context)

def book_delete(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return redirect('book_list')

def book_edit(request, id):
    book = get_object_or_404(Book, id=id)
    
    if request.method == "POST":
        # Update book attributes based on form input
        book.title = request.POST.get('title', book.title)
        book.author = request.POST.get('author', book.author)
        book.description = request.POST.get('description', book.description)
        if 'pic' in request.FILES:
            book.pic = request.FILES['pic']
        book.save()
        return redirect('book_details', id=book.id)
    
    return render(request, 'helloapp/book_details_edit.html', {'book': book})