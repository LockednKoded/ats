# Airport Terminal Services (ats) system

ATS is a system to digitise the services offered by an airport terminal, for both both passengers and employees.

### Dependencies
To run this project you need to install these packages/dependencies in your virtual environment(preferrably):

- Python 3
- Django v1.11

- Pillow <br>
`pip install pillow`

- Django Crispy forms <br>
`pip install django-crispy-forms`

- Django datetime widget <br>
`pip install django-datetime-widget`


### Instructions
  
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

**If collaborator: Please edit this readme for adding any more important instructions**
