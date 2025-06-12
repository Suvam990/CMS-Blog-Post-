# 📰 CMS-Blog-Post

**CMS-Blog-Post** is a Django-powered blog content management system that allows administrators to create, manage, and publish blog posts through a secure admin interface.
Built with scalability and simplicity in mind, it's perfect for use in personal or small business blogging platforms.

---

## 📌 Project Features

- ✅ Admin dashboard to create, update, and delete blog posts
- 🎨 Template-based frontend rendering
- 🛠️ Modular and scalable Django architecture
- 📂 MYSQL for local development
- 🔐 Secure admin login with Django's built-in auth system

---

## 🚀 Getting Started
2. Create and Activate a Virtual Environment
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

4. Install Dependencies
pip install -r requirements.txt
If requirements.txt is not available, you can manually install Django:


pip install django
4. Apply Database Migrations
python manage.py migrate

5. Create a Superuser
python manage.py createsuperuser
Follow the prompts to set a username and password.

6. Start the Development Server
python manage.py runserver
Visit: http://127.0.0.1:8000



🔐 Admin Login Credentials
Use the following credentials to log in to the admin panel:

Username: admin

Password: admin1234

Access the admin panel at: http://127.0.0.1:8000/admin/


### 1. To Clone the Repository
```bash
git clone https://github.com/your-username/CMS-Blog-Post.git
cd CMS-Blog-Post
