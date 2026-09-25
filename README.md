# 🚆 Railway Ticket Booking System

A simple **Railway Ticket Booking System** developed using **Python, Streamlit, and SQLite3**.

The application provides a user-friendly web interface where users can enter passenger and journey details, book tickets, store booking information in an SQLite database, and retrieve previously stored bookings.

---

## 📌 Project Overview

The Railway Ticket Booking System is a Streamlit-based web application designed to manage railway ticket booking details.

The application allows users to:

* Enter passenger details
* Enter journey details
* Select coach type
* Select seat number
* Select meal preferences
* Enter fare details
* Book a ticket
* Store booking information in SQLite3
* Generate a unique Booking ID
* Retrieve and view all bookings

---

## 🛠️ Technologies Used

| Technology | Purpose                   |
| ---------- | ------------------------- |
| Python     | Application development   |
| Streamlit  | Front-end web application |
| SQLite3    | Database management       |
| SQL        | Database operations       |

---

## 📂 Project Structure

```text
railway_booking/
│
├── app.py
├── database.py
├── railway.db
└── README.md
```

### `app.py`

Contains the Streamlit application and user interface.

It handles:

* Passenger input
* Journey details
* Coach and seat selection
* Meal selection
* Fare input
* Ticket booking
* Displaying booking records

### `database.py`

Contains the SQLite database operations.

It handles:

* Database creation
* Table creation
* Inserting booking records
* Retrieving booking records

### `railway.db`

SQLite database file that stores the booking information.

> The database file is automatically created when the application is executed.

---

## 🗄️ Database Structure

The application uses a `bookings` table.

### Bookings Table

| Column         | Data Type | Description           |
| -------------- | --------- | --------------------- |
| booking_id     | INTEGER   | Unique booking ID     |
| passenger_name | TEXT      | Passenger name        |
| age            | INTEGER   | Passenger age         |
| gender         | TEXT      | Passenger gender      |
| marital_status | TEXT      | Marital status        |
| from_date      | TEXT      | Journey starting date |
| boarding_time  | TEXT      | Boarding time         |
| to_date        | TEXT      | Journey ending date   |
| end_time       | TEXT      | Journey ending time   |
| coach          | TEXT      | Selected coach        |
| seat_no        | INTEGER   | Seat number           |
| meal           | TEXT      | Selected meal         |
| fare           | REAL      | Ticket fare           |
| booking_status | TEXT      | Booking status        |

---

## ⚙️ Features

### 1. Passenger Details

The user can enter:

* Passenger name
* Age
* Gender
* Marital status

### 2. Journey Details

The user can enter:

* From date
* Boarding time
* To date
* End journey time

### 3. Travel Details

The user can select:

* Coach type
* Seat number
* Meal preference

Available coach types:

```text
General
3 Tier
2 Tier
First Class
```

### 4. Ticket Booking

After entering all required details, the user can click:

```text
🎟️ Book Ticket
```

The booking information is then stored in the SQLite database.

### 5. Booking ID

SQLite automatically generates a unique `booking_id` for every booking.

Example:

```text
Ticket booked successfully!
Booking ID: 1
```

### 6. View Bookings

The application can retrieve stored booking records from SQLite and display them in Streamlit.

---

## 🔄 Application Workflow

```text
          START
            │
            ▼
   Open Streamlit App
            │
            ▼
   Enter Passenger Details
            │
            ▼
     Enter Journey Details
            │
            ▼
 Select Coach / Seat / Meal
            │
            ▼
       Enter Fare
            │
            ▼
      Book Ticket
            │
            ▼
       Validate Data
            │
            ▼
       Save to SQLite
            │
            ▼
      Generate Booking ID
            │
            ▼
      Display Confirmation
            │
            ▼
       View Bookings
            │
            ▼
           END
```

---

## 💾 Data Flow

```text
User
 │
 ▼
Streamlit Interface
 │
 ▼
Python Application
 │
 ▼
database.py
 │
 ▼
SQLite3
 │
 ▼
railway.db
```

For retrieving information:

```text
railway.db
    │
    ▼
SQLite Query
    │
    ▼
database.py
    │
    ▼
app.py
    │
    ▼
Streamlit
    │
    ▼
Booking Records
```

---

## 🚀 Installation

### Step 1: Install Python

Download and install Python from the official Python website.

Make sure Python is added to PATH during installation.

### Step 2: Install Streamlit

Open Command Prompt or Terminal and run:

```bash
pip install streamlit
```

SQLite3 is included with Python, so no separate SQLite installation is required for this project.

---

## ▶️ How to Run

Navigate to the project folder:

```bash
cd railway_booking
```

Then run:

```bash
streamlit run app.py
```

The Streamlit application will open in your browser.

---

## 🧪 Example Booking

Example input:

```text
Passenger Name : Rahul Sharma
Age             : 25
Gender          : Male
Marital Status  : Single

From Date      : 25-09-2026
Boarding Time  : 10:30 AM

To Date        : 26-09-2026
End Time       : 06:30 AM

Coach          : 3 Tier
Seat Number    : 23
Meal           : Vada Pav
Fare            : ₹850
```

After clicking **Book Ticket**, the information is stored in the SQLite database.

---

## 🔮 Future Enhancements

The following features can be added to make the project more advanced:

* Automatic fare calculation
* Automatic seat allocation
* Real-time seat availability
* PNR generation
* Search booking using PNR
* Search booking using passenger name
* Ticket cancellation
* Cancellation/refund calculation
* Train selection
* Source and destination stations
* Train schedule
* Multiple passengers in one booking
* Payment details
* Booking history
* Admin dashboard
* Login and authentication
* PDF ticket generation
* Improved database design with multiple related tables

---

## 🎯 Future Database Design

The project can later be expanded into a relational railway database containing tables such as:

```text
Passenger
    │
    ▼
Booking ─────── Payment
    │
    ▼
Train ─────── Train Route
    │
    ▼
Coach
    │
    ▼
Seat

Station ─────── Station Route
```

This will make the project more similar to a real-world railway reservation system.

---

## 👩‍💻 Author

**Railway Ticket Booking System**

Developed using:

**Python + Streamlit + SQLite3**

---

## 📄 License

This project is created for **educational and learning purposes**.


[alt text](diagram.png)