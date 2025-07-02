#Real Estate Portfolio Analyzer

This is a web application that allows users to input a portfolio of real estate properties as a csv file, analyze key financial metrics such as income, expenses, tax, and EMI payments, and visualize the data using interactive charts.

#Features

Add and manage a portfolio of real estate properties
Input income, expenses, tax, and EMI data for each property
Automated calculations and financial summaries
Interactive charts to visualize performance

#Tech Stack

Backend: Django
Frontend Styling: Tailwind CSS
Charts: Chart.js

#Setup Instructions

Clone the repository:
```
git clone https://github.com/Anugragha/Properties_webapp.git
cd Properties_webapp
```

Create a virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

Install dependencies:
```
pip install -r requirements.txt
```

Apply migrations:
```
python manage.py migrate
```

Run the development server:
```
python manage.py runserver
```

Open your browser and go to http://127.0.0.1:8000/
