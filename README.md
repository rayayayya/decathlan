# Link deployment
https://pbp.cs.ui.ac.id/rayna.balqis/decathlan

# Soal dan jawaban TI 2

## 1. Cara membuat proyek Django baru
    membuat proyek django dengan perintah "django-admin startproject football-shop"
## 2. Cara membuat aplikasi dengan nama main
    a. menjalankan perintah "python manage.py startapp main"
    b. menambahkan 'main' ke dalam INSTALLED_APPS
## 3.Cara melakukan routing pada agar dapat menjalankan aplikasi main
    Membuat berkas urls.py dan menambahkan app_name = 'main' dan menambah pada ulrpatterns lalu mengimport fungsi include dari django urls dan menginclude path 'main.urls' pada urlpatterns
## 4. Cara membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib 
    Menambahkan class Product pada models.py lalu menambahkan atribut dengan requirements yang tertera
    name sebagai nama item dengan tipe CharField.
    price sebagai harga item dengan tipe IntegerField.
    description sebagai deskripsi item dengan tipe TextField.
    thumbnail sebagai gambar item dengan tipe URLField.
    category sebagai kategori item dengan tipe CharField.
    is_featured sebagai status unggulan item dengan tipe BooleanField.
## 5. Cara membuat fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas 
    Membuat fungsi bernama show main yang diisi dengan variabel yang berisi dengan isinya sesuai dengan permintaan dan menyambungkannya dengan main.html yang berada pada direktori templates
## 6. Cara membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py
    Menambahkan path show main yang ada pada urls.pydan include pada urls.py dan tidak lupa untukmengimpor include
## 7. Cara melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet
    Setelah memastikan bahwa proyek ini sudah diset url dengan link proyek pws, melakukan add, commit dan push kepada keduanya, github dan pws. Secara otomatis aplikasi dideploy melalui PWS
## 8. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
    ![Diagram](images/pbp.png)

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