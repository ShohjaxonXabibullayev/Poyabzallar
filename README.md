👟 Poyabzallar Veb Sayti (Django REST Framework)

📌 Ushbu loyiha Django REST Framework yordamida yaratilgan bo‘lib, turli xil poyabzallarni onlayn boshqarish imkoniyatini beradi.  
API orqali poyabzallarni qo‘shish, ko‘rish, tahrirlash va o‘chirish (CRUD) amallarini bajarish mumkin.  

🔑 Shuningdek, foydalanuvchilar uchun authentication (ro‘yxatdan o‘tish, login, profil boshqaruvi) va comment (izoh qoldirish) imkoniyatlari ham mavjud.  

---

 ✨ Asosiy imkoniyatlari
- 👟 Poyabzal qo‘shish (Create)  
- 👁️ Poyabzallarni ko‘rish (Read)  
- 🖊️ Poyabzalni tahrirlash (Update)  
- ❌ Poyabzalni o‘chirish (Delete)  
- 💬 Poyabzallar haqida izoh (comment) qoldirish  
- 🔐 Ro‘yxatdan o‘tish, login qilish va foydalanuvchini boshqarish  

---

 🖥️ Localhost’da ishga tushirish

1️⃣ cmd ni ochib olish kerak

2️⃣ Loyihani yuklab olish cmd iga git clone https://github.com/ShohjaxonXabibullayev/Logitech deb yozasiz

3️⃣Loyiha papkasiga kirish cmd iga cd Logitech deb yozasiz

4️⃣ Virtual muhit yaratish va faollashtirish python -m venv .env

5️⃣Virtual muhitni activlashtirish source .env/bin/activate # Linux/MacOS .env\Scripts\activate # Windows

6️⃣ Kerakli kutubxonalarni o‘rnatish pip install Django 

pip install -r requirements.txt

7️⃣ Serverni ishga tushirish python manage.py runserver

👉 Brauzerda ochish: http://127.0.0.1:8000

Loyiha Poyabzallarni onlayn boshqarish uchun yaratilgan.

postman documentation 👉 https://documenter.getpostman.com/view/47098717/2sB3BHm8xc

swagger documentation 👉 http://127.0.0.1:8000/swagger/

redoc documentation 👉 http://127.0.0.1:8000/redoc/
