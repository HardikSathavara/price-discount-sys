# Price discount systerm

A Django REST Framework-based Price discount systerm API with Product, Discount, Order CRUD Operations.

---

## Tech Stack

- Python 3.10+
- Django 4.x
- Django REST Framework
- SQLite (default DB)

---

## Setup Instructions

Create & Activate a Virtual Environment

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```


Install Dependencies

```bash
pip install -r requirements.txt
```

Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

Create Superuser (optional)

```bash
python manage.py createsuperuser
```

Run the Server

```bash
python manage.py runserver
```


## API Endpoints

### Products

```bash
Method: POST
Endpoint: api/products
Description: Create a new product
```

```bash
Method: GET
Endpoint: api/products
Description: List all products
```

```bash
Method: GET
Endpoint: api/products/<id>
Description: Get a product details
```

```bash
Method: PUT
Endpoint: api/products/<id>
Description: Update product
```

```bash
Method: DELETE
Endpoint: api/product/<id>
Description: Delete product
```



### Discounts

```bash
Method: POST
Endpoint: api/discounts
Description: Create a new discount
```

```bash
Method: GET
Endpoint: api/discounts
Description: List all discounts
```

```bash
Method: GET
Endpoint: api/discounts/<id>
Description: Get a discount details
```

```bash
Method: PUT
Endpoint: api/discounts/<id>
Description: Update discount
```

```bash
Method: DELETE
Endpoint: api/discounts/<id>
Description: Delete discount
```



### Orders

```bash
Method: POST
Endpoint: api/orders
Description: Create a new order
```

```bash
Method: GET
Endpoint: api/orders
Description: List all orders
```

```bash
Method: GET
Endpoint: api/orders/<id>
Description: Get a order details
```

```bash
Method: PUT
Endpoint: api/orders/<id>
Description: Update order
```

```bash
Method: DELETE
Endpoint: api/orders/<id>
Description: Delete order
```