# Flask Products

Implementation of a GET API to list products stored in a TinyDB database.

## Getting Started

Clone the repository:
```bash
git clone https://github.com/Trowsing/flask-products.git
cd flask_products/
``` 
Create and execute a virtual environment:
```bash
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
```

Or use Pipenv (recommended):
```bash
pipenv install
pipenv shell
```

Run the development server:

```bash
python products/handler.py

# Or use the flask run command:
export FLASK_APP=products/handler.py
flask run
```

Or run the `gunicorn` server:

```bash
gunicorn --chdir products/ handler:app
```

## Available endpoints

---

`GET` */products/* 

Returns a list of all products.

`curl http://localhost:5000/products`

---

`GET` */products/\<id>*

Returns a list of products matching the ID parameter.

`curl http://localhost:5000/products/1`


---

`GET` */products/filter?\<name>*

Returns a list of products matching the search keywords.

- `name` (str): product name search query 

`curl http://localhost:5000/products/filter?name=kingston`


---

`GET` */products/filter/price?\<min>&\<max>*

Returns a list of products in a price range.

- `min` (int): minumum desired price
- `max` (int): maximum desired value

`curl http://localhost:5000/products/filter/price?min=150&max=500`

`curl http://localhost:5000/products/filter/price?min=150`


`curl http://localhost:5000/products/filter/price?max=800`


---
