# 🏟️ Stadion Booking API

Django REST Framework (DRF) asosida yaratilgan API bo‘lib, foydalanuvchilar stadionlarni ko‘rishlari, bron qilishlari va faqat **owner** foydalanuvchilar yangi stadion qo‘shishlari mumkin.

---

## 🚀 Texnologiyalar
- Python 3.10+
- Django 5.x
- Django REST Framework (DRF)
- SimpleJWT (Token autentifikatsiya)
- drf-spectacular (Swagger/OpenAPI hujjatlash)
- SQLite (default)

---
<img width="1306" height="842" alt="image" src="https://github.com/user-attachments/assets/c67fa621-36c3-49bc-af62-f15e681e6da4" />


---
## 🔑 Xususiyatlar
- 👤 **User autentifikatsiya** (Ro‘yxatdan o‘tish, login, JWT token)
- 🏟️ **Stadionlar bilan ishlash**
  - Stadion ro‘yxatini ko‘rish
  - Faqat `owner` role foydalanuvchi stadion qo‘shishi mumkin
  - Stadionni yangilash va o‘chirish
- 📅 **Booking (bron qilish)**
  - Stadionni ma’lum kun va vaqt oralig‘ida band qilish
  - Agar vaqt to‘qnashsa → xatolik qaytaradi
  - Stadion bron qilingan vaqtlarini ko‘rish
  - Bo‘sh vaqtlarni tekshirish
- 🔒 JWT orqali xavfsizlik

---

## ⚙️ O‘rnatish

1. Loyihani yuklab olish:
   ```bash
   git clone https://github.com/SardorToirov/Stadion-api.git
   cd Stadion-api ```
