# QR Code Payment App

This project is a QR code payment application built using Django for the backend and Vue.js for the frontend.

## Features

- Generate QR codes for payments
- Handle payment transactions
- View payment details
- Merchant and buyer interfaces

## Installation

### Backend (Django)

1. **Clone the repository:**

```bash
https://github.com/nithinmv4u/QR_code_payment.git
cd backend
```

2. **Create and activate a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate
```
3. **Install dependencies:**
```bash
pip install -r requirements.txt
```
4. **Apply database migrations:**
```bash
python manage.py migrate
```
5. **Run the development server:**
```bash
python manage.py runserver
```
The backend server will start running at http://localhost:8000.

### Frontend (Vue.js)

1. **Navigate to the frontend directory:**
```bash
cd frontend
```
2. **Install dependencies:**
```bash
npm install
```
3. **Start the development server:**
```bash
npm run serve
```
The frontend server will start running at http://localhost:8080.

## Usage

1. **Access the backend admin interface at http://localhost:8000/admin/ to manage merchants, buyers, payments, etc.**

2. **Add Merchant and Buyer Dummy Data from admin to start**

3. **Access the frontend interface at http://localhost:8080 to use the application as a merchant or buyer.**

4. **Access merchant page at http://localhost:8080/merchant and the buyer page will be available from QR code**

## API Documentation

Run:

```bash
python manage.py spectacular --color --file schema.yml
```

### UI API documentation: http://localhost:8000/api/schema/swagger-ui/

### DB Schema (ERD)
DB Schema is included in repository as 'ERD_diagram.png'
