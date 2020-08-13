========
Eastwood
========

Employees is a test Django application that allows to display
several tables with the employees data.

Quick start
-----------

1. Add "eastwood" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'eastwood/core',
        'eastwood/employees',
    ]

2. Include the URLconf in your project urls.py like this::

       path('', include('eastwood.core.urls')),
       path('employees/', include('eastwood.employees.urls')),

3. Run ``python manage.py migrate`` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create an employee and/or department records (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/ to view the result.


Docker run[^]
----------
1. Install ``docker`` and ``docker-compose``
2. Navigate to the project root folder

[^] Yet not implemented