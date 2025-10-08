

# Link deployment

https://rayna-balqis-decathlan.pbp.cs.ui.ac.id/

# Soal dan jawaban TI 2

## 1. Cara membuat proyek Django baru

1. menginstall django
2. membuat proyek django dengan perintah 
`django-admin startproject [nama proyek]`

## 2. Cara membuat aplikasi dengan nama main

1. menjalankan perintah 
`python manage.py startapp main`
2. menambahkan 'main' ke dalam INSTALLED_APPS pada settings.py
3. menghubungkan direktori main dengan proyek utama melalui urls.py
4. membuat file urls.py di folder main dan menambahkan app_name serta urlpatterns
5. menambahkan fungsi view di views.py untuk menampilkan response
6. menjalankan perintah 
`python manage.py runserver`

## 3.Cara melakukan routing pada agar dapat menjalankan aplikasi main
1. membuat berkas urls.py di dalam folder main
2. menambahkan app_name = 'main' pada main/urls.py
3. menambahkan daftar urlpatterns pada main/urls.py
4. membuat fungsi view di views.py untuk dihubungkan dengan path
5. mengimport include dari django.urls pada urls.py di direktori utama
6. menambahkan path('main/', include('main.urls')) ke dalam urlpatterns di project utama
## 4. Cara membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib 
Menambahkan class Product pada models.py lalu menambahkan atribut dengan requirements yang tertera  
`name sebagai nama item dengan tipe CharField. ` 
`price sebagai harga item dengan tipe IntegerField. ` 
`description sebagai deskripsi item dengan tipe TextField. ` 
`thumbnail sebagai gambar item dengan tipe URLField.  `
`category sebagai kategori item dengan tipe CharField.  `
`is_featured sebagai status unggulan item dengan tipe BooleanField.  `
## 5. Cara membuat fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas 
1. membuat folder templates/main/ di dalam direktori aplikasi main
2. membuat file main.html di dalam folder tersebut
3. menambahkan fungsi bernama show_main pada views.py yang berisi variabel (misalnya app_name, nama, kelas)
4. mengembalikan fungsi tersebut dengan render(request, "main/main.html", context)
5. menambahkan path baru di main/urls.py untuk memanggil fungsi show_main
## 6. Cara membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py
1. membuka atau membuat file urls.py di dalam folder main
2. mengimpor fungsi include dan path dari django.urls
3. mengimpor fungsi show_main dari views.py
4. menambahkan path baru di urlpatterns
## 7. Cara melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet
Setelah memastikan bahwa proyek ini sudah diset url dengan link proyek pws, melakukan add, commit dan push kepada keduanya, github dan pws. Secara otomatis aplikasi dideploy melalui PWS
## 8. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![Diagram](https://github.com/rayayayya/decathlan/raw/master/images/pbp.png)

urls.py menerima request dan menentukan viewmana yang akan bertanggung jawab, lalu views.py akan menjalankan logic dan interact dengan models.py yang akan berkomunikasi dengan database untuk ambil/simpan data, dan template html akan merender halaman dengan data yang sudah berikan

## 9. Jelaskan peran settings.py dalam proyek Django!
Settings.py berfungsi sebagai file konfigurasi pada sebuah proyek django. Pengaturan inti seperikoneksi database, aplikasi apa saja yang digunakan, keamanan, sampai konfigurasi yang statis dilakukan oleh settings.py.
## 10. Bagaimana cara kerja migrasi database di Django?
Dengan cara mentranslate perubahan pada models.py menjadi perubahan pada skema database menggunakan file migrations  

1. Mengubah atau membuat model di models.py  
2. Django melihat ada perubahan model  
3. Menjalankan python manage.py makemigrations  

Intinya step ini dilakukan setiap ada perubahan pada models.py

## 11. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Menurut saya, django cukup cocok dijadikan permulaan bagi seseorang yang ingin belajar pengembangan perangkat lunak karena:
1. Menggunakan python (bahasa yang cukup mudah untuk dipelajari)
2. Fitur bawaan lengkap
3. Menggunakan pola arsitektur yang terorganisi (MVT)

## 12. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
Tidak ada, overall good. Thankyou asdos PBP :D


# Soal dan jawaban TI 2

## 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Karena ada proses pertukaran data dari server ke client. Jadi data delivery yang menjadi jembatan untuk menghubungkan antara backend dengan frontend. Tanpa mekanisme data delivery, frontend tidak bisa tahu data apa yang ada di server.

## 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya, JSON lebih baik :D dibandingkan dengan XML, JSON lebih dapat "dibaca" oleh mata manusia dibandingkan dengan XML yang memiliki banyak tag, walaupun JSON kurang cocok untuk data dengan struktur yang kompleks. JSON lebih populer dibandingkan dengan XML karena lebih ringkas dan efisien, selain itu JSON bisa dipake langsung tanpa parsing tambahan.

## 3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
fungsi dari method `is_valid ` adalah untuk mengecek apakah semua form yang ada sudah terisi sesuai dengan aturan model yang ada. Kita membutuhkan method tersebut untuk mencegah data yang tidak valid masuk ke dalam database.

## 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
csrf_token berfungsi untuk melindungi aplikasi dari serangan cross site request forgery (CSRF). Tanpa csrf_token, attacker bisa mengubah data tanpa seizin user, misal mengganti data-data privasi seperti password, pin ATM, nomor identitas, dan sebagainya yang seharusnya butuh interaksi langsung dari user. Hal ini dilakukan oleh attacker dengan cara mengandalkan cookie session yang biasanya otomatis terkirim oleh browser, jadi walaupun user tidak tahu, requestnya tetap terlihat valid di sisi server, dengan kata lain, dengan adanya csrf_token, server dapat membedakan request asli dan palsu.
## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step 

1. Menambah keempat fungsi tersebut pada views.py dan tidak lupa untuk import productform dan product

```python
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from main.forms import ProductForm
from main.models import Product

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    json_data = serializers.serialize("json", product_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, product_id):
   try:
       news_item = Product.objects.filter(pk=product_id)
       xml_data = serializers.serialize("xml", news_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)
   
def show_json_by_id(request, product_id):
   try:
       product_item = Product.objects.get(pk=product_id)
       json_data = serializers.serialize("json", [product_item])
       return HttpResponse(json_data, content_type="application/json")
   except Product.DoesNotExist:
       return HttpResponse(status=404)
```

2. Menambahkan path API endpoints dari keempat fungsi tersebut di urls.py
``` python
path('xml/', show_xml, name='show_xml'),
path('json/', show_json, name='show_json'),
path('xml/<str:news_id>/', show_xml_by_id, name='show_xml_by_id'),
path('json/<str:news_id>/', show_json_by_id, name='show_json_by_id'),
```

3. Membuat file forms.py yang berisi models dan template yang sesuai
```python
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description","category", "thumbnail", "stock", "brand"]
```
4. Mengubah main.html di dalam templates yang ada di direktori main
```python
<h1>Product List</h1>

<h5>NPM:</h5>
<p>{{ npm }}</p>

<h5>Name:</h5>
<p>{{ name }}</p>

<h5>Class:</h5>
<p>{{ class }}</p>

<a href="{% url 'main:create_product' %}">
  <button>+ Add Product</button>
</a>

<hr>

{% if not product_list %}
  <p>Belum ada data produk.</p>
{% else %}

{% for product in product_list %}
<div>
  <h2>
    <a href="{% url 'main:show_product' product.id %}">
      {{ product.name }}
    </a>
  </h2>

  <p>
    <b>{{ product.get_category_display }}</b>
    {% if product.is_product_hot %} | <b>Hot</b>{% endif %}
    | Views: {{ product.product_views }}
  </p>

  {% if product.thumbnail %}
    <img src="{{ product.thumbnail }}" alt="Product thumbnail" width="150" height="100">
    <br />
  {% endif %}

  <p>{{ product.description|truncatewords:25 }}...</p>

  <p>
    <a href="{% url 'main:show_product' product.id %}">
      <button>View Details</button>
    </a>
  </p>
</div>

<hr>
{% endfor %}

{% endif %}
```
5. Menambah template form dengan nama create_product di templates yang ada di direktori main

```python
{% extends 'base.html' %} 
{% block content %}
<h1>Add New Product</h1>

<form method="POST">
  {% csrf_token %}
  <table>
    {{ form.as_table }}
    <tr>
      <td></td>
      <td>
        <input type="submit" value="Add New Product" />
      </td>
    </tr>
  </table>
</form>

{% endblock %}
```

6. Menambah template detail dengan nama product_detail di templates yang ada di direktori main
```python
{% extends 'base.html' %}
{% block content %}
<p>
  <a href="{% url 'main:show_main' %}">
    <button>← Back to Product List</button>
  </a>
</p>

<h1>{{ product.name }}</h1>

<p>
  <b>{{ product.get_category_display }}</b>
  {% if product.is_product_hot %} | <b>Hot</b>{% endif %}
  | Views: {{ product.product_views }}
</p>

{% if product.thumbnail %}
  <img src="{{ product.thumbnail }}" alt="Product thumbnail" width="300">
  <br /><br />
{% endif %}

<p><b>Brand:</b> {{ product.brand|default:"N/A" }}</p>
<p><b>Price:</b> Rp {{ product.price }}</p>
<p><b>Stock:</b> {{ product.stock }}</p>
<p><b>Description:</b> {{ product.description }}</p>

{% endblock content %}
```
7. Jalankan migrasi
`python manage.py makemigrations`
`python manage.py migrate`

8. Jalankan server

`python manage.py runserver`

## 6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
Tidak


## Lampiran gambar postman
![XML](images/xml.jpg)
![XML_ID](images/xml_id.jpg)
![JSON](images/json.jpg)
![JSON_ID](images/json_id.jpg)

# Soal dan jawaban TI 4

## Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya
Django authentiactionform adalah formulir built in dari Django yang dapat giguanakn untuk menghandle proses autheticate user. Kelebihannya adalah siap pakaijadi tidak perlu membuat dari nol, dan juga mudah untuk disesuaikan dengan tampilan yang diinginkan, namun tidak cocok untuk diaplikasikan pada program yang kompleks, karena jika tidak dibuat dengan benar, bdapat menimbulkan masalah yang besar.

## Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
Autentikasi adalah proses verifikasi identitas pengguna untuk memastikan bahwa pengguna benar-benar pengguna yang diklaim sedankan otorisasi menentukan tingkat akses yang diberikan pada pengguna setelah diautentikasi

## Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
Kelebihan session adalah memiliki keamanan tinggi karena data disimpan di server dan bisa menyimpan data besar sedangkan kekurangannya adalah membutuhkan penyimpanan yang besar.
Kelebihan cookies adalah ringan dan tidak membebani server dan fleksibel sedangkan kekurangan cookie adalah kapaistas penyimpanannya terbatas

## Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
Risiko potensial yang mungkin dihadapi adalah akses tidak sah dan pelacakan privasi, tetapi dihandle oleh django dengan pengaturan atribut `Secure` `HttpOnly` dan `SameSite` serta enkripsi data

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)

### 1. Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna mengakses aplikasi sebelumnya sesuai dengan status login/logoutnya.

Fungsi registrasi
1. Import `UserCreationForm`, `AuthenticationForm`, `messages`, `authenticate`, `login`, `logout` di views.py
```python
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
```
2. Menambahkan fungsi register, login, logout user ke dalam views.py

```python
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```

```python
def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:show_main')

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)
```
```python
def logout_user(request):
    logout(request)
    return redirect('main:login')
```

3. Menambah file html baru bernama `register.html`,`login.html`, `logout.html` di direktori templates yang ada dimain dengan isi

```python
{% extends 'base.html' %}

{% block meta %}
<title>Register</title>
{% endblock meta %}

{% block content %}

<div>
  <h1>Register</h1>

  <form method="POST">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input type="submit" name="submit" value="Daftar" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %}
</div>

{% endblock content %}
```

```python
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="login">
  <h1>Login</h1>

  <form method="POST" action="">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input class="btn login_btn" type="submit" value="Login" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %} Don't have an account yet?
  <a href="{% url 'main:register' %}">Register Now</a>
</div>

{% endblock content %}
```
```python
...
<a href="{% url 'main:logout' %}">
  <button>Logout</button>
</a>
...
```

4. Mengimpor fungsi register,login, dan logout_user ke dalam urls.py yang ada di direktori main dan menambahkan path ketiga url tersebut ke dalam urlpatterns

2. Membuat dua (2) akun pengguna dengan masing-masing tiga (3) dummy data menggunakan model yang telah dibuat sebelumnya untuk setiap akun di lokal.
- Melakukan registrasi dengan mengisi username dan passowrd
- Login ke akun yang sudah dibuat
- Menambahkan masing-masing 3 produk untuk tiap akun

3. Menghubungkan model Product dengan User
- Menimport User di dalam models.py
- Pada model Product menambahkan line user
```python
class News(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
```
- mengubah kode pada fungsi create_product
```python
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "create_product.html", context)
```
- modifikasi fungsi show_main
```python
@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")
    if filter_type =="all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        'npm' : '2406400373',
        'name': 'Rayna Balqis',
        'class': 'PBP D',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')

    }

    return render(request, "main.html", context)
```

- menambahkan tombol filtr pada main.html
- menampilkan nma author di product_details
- migrate

# Soal dan jawaban TI 5

## Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

### urutan prioritas pengambilan CSS selector didasarkan pada spesifisitas, yang menentukan seberapa kuat suatu aturan diterapkan. Urutannya ada pada

1. inline style
2. ID selector
3. classes selector
4. element selector

## Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!

Responive design penting untuk memastikan user experience yang konsisten di berbagai ukuran layar, selain itu bisa meningkatkan SEO karena search engine seperti google mengutamakan situs yang mobile friendly.


## Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
### 
Margin: Jarak antar satu elemen dengan elemen lain di sekitarnya

```css
div {
  margin: 20px; 
}
```
Padding: Jarak antara isi elemen dengan tepi dalam elemen 

```css
div {
  padding: 15px;
}
```

Border: Garis tepi di sekeliling elemen

```css
div {
  border: 2px solid black;
}
```

## Jelaskan konsep flex box dan grid layout beserta kegunaannya!

Flexbox
Mengatur elemen dalam bentuk horizontal atau vertikal

Kegunaan:
1. Menyusun elemen secara horizontal atau vertikal dengan mudah
2. Membuat layout yang responsif terhadap ukuran layar
3. Mengatur aignment

```css
<div class="flex-container">
  <div>Box 1</div>
  <div>Box 2</div>
  <div>Box 3</div>
</div>

<style>
  .flex-container {
    display: flex;            
    justify-content: space-around; 
    align-items: center;         
  }
  .flex-container div {
    background: lightblue;
    padding: 20px;
  }
</style>
```

Grid layout
Untuk mengatur baris dan kolom.

Kegunaan:

1. Membuat layout halaman penuh: header, sidebar, content, footer.
2. Mengatur posisi elemen berdasarkan baris dan kolom.
3. Fleksibel untuk desain kompleks dan responsif.

```css
<div class="grid-container">
  <div class="header">Header</div>
  <div class="sidebar">Sidebar</div>
  <div class="content">Content</div>
  <div class="footer">Footer</div>
</div>

<style>
  .grid-container {
    display: grid; 
    grid-template-columns: 200px 1fr; 
    grid-template-rows: auto 1fr auto; 
    gap: 10px; 
  }
  .header { grid-column: span 2; background: lightgreen; }
  .sidebar { background: lightcoral; }
  .content { background: lightblue; }
  .footer { grid-column: span 2; background: lightgoldenrodyellow; }
</style>
```

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

1. Menambahkan tailwind pada file base.html
2. Menambah fitur edit product dengan menambah fungsi edit produk di views.py, menambah berkas baru bernama edit_product.html, import fungsi edit produk pada urls dan menambahkan path pada urlpattern
3. Menambah fitur hapus produk dengan menambah fungsi hapus produk di views.py, import fungsi hapus produk pada urls dan menambahkan path pada urlpattern
4. Menambahkan navigation bar dengan cara membuat file html di template main root kemudian ditambahkan pada main.html
5. Menambahkan file global.css pada direktori css yang berada pada direktori statis
6. Menghubungkan file global.css dengan tailwind pada file bae.html
`<link rel="stylesheet" href="{% static 'css/global.css' %}"/`
7. Mengatur style pada global.css, dan style pada file html seperti edit produk, add produk, main, login, register, dan detail produk
8. Membuat file card produk pada direktori templates


# Soal dan jawaban TI 6
## Apa perbedaan antara synchronous request dan asynchronous request?
synchronous request dilakukan dengan mengeksekusi setiap request secara berurutan, satu persatu, sedangkan pada asynchornous request, program dapat memulai tugas lain tanpa harus menunggu tugas yang sebelumnya selesai

## Bagaimana AJAX bekerja di Django (alur request–response)?
Saat ada event terjadi, javascript membuat seuat CMLHttpRequest object yang akan mengirimkan request ke server, setelah itu server akan memproses request tersebut, seteah itu server mengembalika response kembali kepada halama web dan response dibaca oleh javascript. Aksi berikutnya akan dipicu oleh javascript sesuai dengan lankah yang dibuat

## Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?
Menggunakan AJAX dapat meningkatkan user experience, kinerja aplikasi lebih cepat, pengurangan penggunaan bandwidth, dan kemampuan untuk membuat web yang lebih dinamis dan interaktif

## Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?
Untuk memastikan keamanan fitur Login dan Register dengan AJAX di Django, Anda wajib mengaktifkan dan menerapkan perlindungan CSRF menggunakan {% csrf_token %} di formulir HTML atau header X-CSRFToken di permintaan AJAX

## Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?
AJAX menciptakan website yang leibh interaktif, responsif, dan cepatkarena data dapat diperbarui tanpa perlu mereload seluruh halaman