# django-tables2_bulma-template

## Installation
`pip install django_table2_bulma_template`
Add to `INSTALLED_APPS` in your Django `settings.py`:  
```
INSTALLED_APPS = [
    ...
    'django_tables2_bulma_template',
    ...
]
```

## Setup
In your Django `settings.py` set:  
 `DJANGO_TABLES2_TEMPLATE = "django-tables2/bulma.html"`
 
## Customization

You can extend the template provided by this package and customize it by overriding blocks.
E.g.

```
# templates/my_bulma_table.html
```
```
{% extends 'django-tables2/bulma.html' %}

{% block table %}
    Your custom table html
{% endblock table %}
``` 
Supported blocks you can override:
- `table-wrapper `: Container that wraps the table
- `table`: The actual table html element
- `table.thead`: The table head
- `table.thead.row`: The table head row that contains the column headers
- `table.thead.th`: Individual table `<th>...</th>`
- `table.tbody`: The table body
- `table.tbody.row`: Individual table row
- `table.tbody.td`: Individual data cell
- `table.tbody.empty_text`: Text that is shown if table is empty
- `table.tfoot`: Footer element of table
- `table.tfoot.row`: Footer rows
- `table.tfoot.td`: Footer cells
- `pagination`: Pagination for this table
- `pagination.previous`: Text/Icons shown to navigate to previous page
- `pagination.next`: Text/Icons shown to navigate to next page
- `pagination.range`: Range of pages shown in pagination