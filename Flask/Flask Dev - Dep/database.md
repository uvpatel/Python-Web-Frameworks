flask sqlachimy

```python
pip install sqlalchemy
```

- provide - orm maper - python thorugh db manuplate 


```pip
from flask_sqlalchemy import SQLAlchemy
```

## Database creation
- We make a database using python oop. we define a schema. 









```powershell
from app import app, db
with app.app_context():
  db.create_all()
  
>>> 
```


```python

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), nullable = False)
    desc = db.Column(db.String(500), nullable = False )
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

```
- [1 - First Todo] for this formated show interminal we write repr 

- in this code we make database schema and also use a method wich reprint. 


- for visualization

[https://inloop.github.io/sqlite-viewer/][SQLite Viewer]
[https://flask-sqlalchemy.readthedocs.io/en/stable/config/#configuration-keys][SQLalchemy]

github.io's link but very powerful link. 

- when you posting the request. give a method in routes. 