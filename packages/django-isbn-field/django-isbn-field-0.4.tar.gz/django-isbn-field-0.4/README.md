# django-isbn-field

Provides django model field to store and validate ISBN numbers.

## Requirements

It has been tested on

* Python >= 3
* Django 1.7, 1.8, 1.9, 1.10, 1.11

## Installation

From Pypi

```bash
$ pip install django-isbn-field
```

or from the repository

```bash
$ git clone https://github.com/secnot/django-isbn-field
$ python setup.py install
```

## Usage 

Add isbn_field to INSTALLED_APPS

```python
# settings.py
INSTALLED_APPS = (
	...
	'isbn_field',
)
```

Use the field in your model

```python
from django.db import models
from isbn_field import ISBNField

class Book(models.Model):
	isbn = ISBNField()
	...
```

It will raise ValidationError when the number provided is invalid
