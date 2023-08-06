=======================
Django FilteredListView
=======================

FilteredListView provides a basic class based view for django to easily filter a ListView.
The provided template currently is in german and for bootstrap3.

Quick start
-----------

1. Add "django_filteredlist" to your INSTALLED_APPS::

    INSTALLED_APPS = [
        ...
        'django_filteredlist',
    ]

2. Create a FilteredListView::

    class MyView(FilteredListView, ListView):
        allowed_filters = ('employee_name', 'project')
        lookup_expressions = { 'project': 'projects__name__icontains' }
        verbose_names = (('employee_name', 'Name'), ('project', 'Working on'),)

3. Add search form to your list template::

    {% extends 'base.html' %}

    {% block content %}

        {{ search }}

        <!-- YOUR LIST HERE -->

    {% endblock %}



