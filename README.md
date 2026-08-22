# AI-Assisted Box Selection System

## 1. Project Overview

This project is a Django-based box selection system for an ecommerce platform. It recommends the most suitable shipping box for an order based on product dimensions, product weight, box dimensions, maximum box weight, and box cost.

The system allows boxes, products, orders, and order items to be managed through Django Admin. A user can select an order from the web interface and get a recommended shipping box.

## 2. Problem Statement

In an ecommerce warehouse, different products have different dimensions and weights, while shipping boxes have different internal dimensions, weight capacities, and costs.

The goal of this system is to determine which available box can accommodate an order and recommend the most suitable option while considering the constraints of the products and the cost of the box.

## 3. Features

- Manage shipping boxes using Django Admin
- Manage products using Django Admin
- Create orders and order items
- Check product dimensions against box dimensions
- Allow products to fit in different orientations
- Check total order weight against box capacity
- Check total product volume against box volume
- Consider product quantities
- Support orders containing multiple products
- Recommend the lowest-cost suitable box
- Return "No Suitable Box Found" when no box can accommodate the order
- Automated test cases using Django's test framework
- Simple web interface for selecting an order and viewing the recommendation

## 4. Technology Stack

- Python 3.11
- Django 5.2.17
- SQLite
- HTML
- Django Templates
- Django Admin
- Django Test Framework

## 5. Project Structure


```text
box_selection_system/
├── box_selection/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── box_selector/
│   ├── migrations/
│   ├── templates/
│   │   └── box_selector/
│   │       └── home.html
│   ├── admin.py
│   ├── models.py
│   ├── service.py
│   ├── tests.py
│   └── views.py
├── db.sqlite3
├── manage.py
└── README.md

## 6. How the System Works


Boxes and products are created using Django Admin.
An order is created and products are added to the order as order items.
The user selects an order from the web interface.
The system calculates the total weight and total volume of the order.
Each available box is checked against the order constraints.
Product dimensions are checked in all possible orientations.
Boxes that cannot accommodate the order are rejected.
Among the suitable boxes, the lowest-cost box is recommended.
If no box is suitable, the system displays "No Suitable Box Found".

 ##7. Box Selection Logic

A box is considered suitable when:

The total order weight does not exceed the box maximum weight.
The total product volume does not exceed the box volume.
Every product can fit within the box dimensions in at least one orientation.

For each product, all possible rotations of its length, width, and height are checked.

After filtering unsuitable boxes, the system selects the box with the lowest cost. If multiple boxes have the same cost, the box with the smaller volume is preferred.

##8. Assumptions and Limitations

Dimensions are assumed to use the same unit for both products and boxes.
Weight is assumed to use the same unit for products and box capacity.
Product rotation is allowed.
The system uses total volume as a feasibility check for multiple products.
The implementation does not perform complete 3D bin-packing or determine the exact physical arrangement of multiple products inside a box.
Boxes are selected from the boxes available in the database.

Clone the repository
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd box_selection_system
Create a virtual environment
python -m venv venv
Activate the virtual environment

Windows PowerShell:

venv\Scripts\Activate.ps1
Install Django
pip install django
Apply migrations
python manage.py migrate
Create an admin user
python manage.py createsuperuser


##10. Running the Application

Start the Django development server:

python manage.py runserver

Open:

http://127.0.0.1:8000/

Django Admin is available at:

http://127.0.0.1:8000/admin/
11. Running Tests

Run the automated tests using:

python manage.py test

The project currently contains 7 automated tests covering box selection, product size, weight, quantity, multiple products, product rotation, and no suitable box scenarios.


##12. Test Cases

The test suite covers:

Test	Expected Result
Small product fits	Small Box is recommended
Product too large	No box is returned
Medium-sized product	Medium Box is recommended
Multiple products	Suitable box is recommended
Multiple quantities	Larger suitable box is selected
Weight exceeds small box capacity	Medium Box is recommended
Product rotation required	Small Box is recommended


##13. Example

Example order:

Product: Laptop
Dimensions: 15 × 10 × 5
Weight: 2
Quantity: 1

Available boxes include:

Small Box:  20 × 15 × 10, Max Weight 5, Cost 30
Medium Box: 30 × 20 × 15, Max Weight 10, Cost 50
Large Box:  50 × 40 × 30, Max Weight 20, Cost 80

The laptop fits inside the Small Box and its weight is within the box capacity.

Therefore, the system recommends:

Small Box
Cost: 30


##14. Future Improvements

Possible future improvements include:

Implementing true 3D bin-packing for multiple products
Adding authentication for warehouse users
Adding a REST API
Adding better input validation
Adding more detailed recommendation explanations


