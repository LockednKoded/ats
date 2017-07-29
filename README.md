# Airport Terminal Services (ats) system

ATS is a system to digitise the services offered by an airport terminal, for both both passengers and employees.
<br>
Check out [ATS hosted project](https://ats2017.pythonanywhere.com)
<br>
Developed for: [Airports Authority of India](www.aai.aero/) by AAI Interns 2017

### Dependencies
To run this project you need to install these packages/dependencies in your virtual environment(preferrably):

- Python 3
- Django v1.11

- Pillow <br>
`pip install Pillow`

- Django Crispy forms <br>
`pip install django-crispy-forms`

- Django datetime widget <br>
`pip install django-datetime-widget`

- MySQL client <br>
`pip install mysqlclient`

Also, to run locally you need to have a file "local.py" in the following directory: src/ats/settings/ having the following code:
~~~~
# This file is gitignored to keep production and local settings seprate

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True

SECURE_SSL_REDIRECT = False

~~~~

### How to run:
  - Install/satify the above mentioned dependencies, including creating "local.py" file <br>
  - Make migrations, and migrate

### Instructions for collabprators:
  
  - Name your branches in the pattern <br>
    `your_module_name - branch_name`
    
  - Base HTML files are put in <br>
    `src/templates/common/base.html`
    
    And they can be used like:<br>
    `common/base.html`  
  
  - Place your template files in 
    `src/templates/your-module-name/your-file.html`
    
    And then in your views refer to them as:
    `your-module-name/your-file.html`<br>
    Extend your HTML template from base.html:
    `{% extends 'common/base.html' %}` as first statement in your template 
    and write your `{% block content %}`
  
  
  
  - Base static files (css,javascript,images) are placed in eg.<br> 
    `src/static/js/common/base.js`<br>
    `src/static/css/common/base.css`<br>
    `src/static/images/common/base.jpg`<br>
    
    And then in your template refer to them as:<br>
    `{% static 'js/common/base.js' %}`<br>
    `{% static 'css/common/base.css' %}`<br>
    `{% static 'images/common/base.jpg' %}`

  - Place your static files (css,javascript,images) in 
    `src/static/js/your-module-name/your-file.js`<br>
    `src/static/css/your-module-name/your-file.css`
    `src/static/images/your-module-name/your-image.jpg`
    
    And then in your template refer to them as:<br>
    `{% static 'js/your-module-name/your-file.js' %}` within `{% block script %}`<br> 
    `{% static 'css/your-module-name/your-file.css' %}` within `{% block style %}`<br>
    `{% static 'images/your-module-name/your-image.jpg' %}`
    
    also load static files at the top of your template, like so:<br>
    `{% load staticfiles %}` below the `{% extends 'common/base.html' %}`

### Trobleshooting
- If you're facing problems in making migrations after make changes to models or after pulling from GitHub, delete all files in migrations folder in your app, except `__init__.py`, and then tru to make migrations again. You can also try doing this and also deleting the database and then try making migrations, and migrate.

### Development

Want to contribute? Great! Fork me!

### License
MIT

### Say Hi
[LinkedIn Links](https://ats2017.pythonanywhere.com/developedby/)

**If collaborator: Please edit this readme for adding any more important instructions**

*last uplated: 29 July 2017*
