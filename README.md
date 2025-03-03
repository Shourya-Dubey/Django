# ☕ Chai Aur Django

Chai Aur Django is a **Django project** for managing and displaying different varieties of **chai (tea)**.  
The project includes models for **chai varieties, reviews, stores, and certificates** and provides templates to display chai details.

---

## 👤 Project Structure
```
chaiaurDjango/
├── chai/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── templates/
│   │   ├── chai/
│   │   │   ├── all_chai.html
│   │   │   └── chai_detail.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── chaiaurDjango/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
├── media/
│   └── chais/
├── requirements.txt
├── static/
│   ├── about.css
│   └── style.css
├── templates/
│   ├── about.html
│   ├── layout.html
│   └── website/
│       └── index.html
└── theme/
    ├── __init__.py
    ├── apps.py
    ├── static_src/
    └── templates/
        └── base.html
```

---

## 🚀 Installation & Setup  

### **1️⃣ Clone the Repository**
```sh
git clone <repository-url>
cd chaiaurDjango
```

### **2️⃣ Create and Activate a Virtual Environment**
```sh
python -m venv .venv
```
- **On Windows:**  
  ```sh
  .venv\Scripts\activate
  ```
- **On macOS/Linux:**  
  ```sh
  source .venv/bin/activate
  ```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Apply Migrations**
```sh
python manage.py migrate
```

### **5️⃣ Create a Superuser (For Admin Access)**
```sh
python manage.py createsuperuser
```

### **6️⃣ Run the Development Server**
```sh
python manage.py runserver
```

---

## 📊 Usage  

- **Admin Panel**: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)  
  - Manage **chai varieties, reviews, stores, and certificates**.  

- **Main Website**: [http://127.0.0.1:8000](http://127.0.0.1:8000)  
  - View different **chai varieties** and their details.

---

## 📊 Models  

| Model | Description |
|--------|------------|
| `ChaiVarity` | Represents a variety of chai with fields for name, image, date added, type, price, and description. |
| `ChaiReview` | Represents a review for a chai variety with fields for chai, user, rating, comment, and date added. |
| `Store` | Represents a store that sells chai varieties with fields for name, location, and chai varieties. |
| `ChaiCertificate` | Represents a certificate for a chai variety with fields for chai, certificate number, issued date, and valid until. |

---

## 🛠 Admin Panel  

The **admin interface** is configured to manage the following:
- Chai Varieties
- Reviews
- Stores
- Certificates

### **Admin Features**
- The `ChaiVarityAdmin` class includes an **inline for reviews**.
- The `StoreAdmin` class includes a **horizontal filter** for chai varieties.

---

## 🎭 Templates  

| File | Purpose |
|------|---------|
| `all_chai.html` | Displays a list of all chai varieties. |
| `chai_detail.html` | Shows the details of a specific chai variety. |
| `layout.html` | Base template for the website. |
| `index.html` | Home page of the site. |
| `about.html` | About page of the site. |

---

## 🎨 Static Files  

| File | Description |
|------|-------------|
| `about.css` | Styles for the about page. |
| `style.css` | General styles for the site. |

---

## 🎭 Tailwind CSS  

This project uses **Tailwind CSS** for styling. The configuration file is located at:
```
tailwind.config.js
```

To install Tailwind, run:
```sh
python manage.py tailwind install
```
To build styles, run:
```sh
python manage.py tailwind build
```

---

## 📜 License  
This project is licensed under the **MIT License**.
```

