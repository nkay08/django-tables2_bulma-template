import django_tables2 as tables
from django.views.generic.base import TemplateView
from django_tables2 import SingleTableMixin

TABLE_DATA = [{"name": y, "age": y, "id": y} for y in range(100)]


class DummyTable(tables.Table):
    name = tables.Column()
    age = tables.Column()
    id = tables.Column()


class TableView(SingleTableMixin, TemplateView):
    DEFAULT_TEMPLATE = "django-tables2/bulma.html"

    table_class = DummyTable
    table_data = TABLE_DATA
    template_name = "table.html"

    def get_table(self, **kwargs):
        if self.request.GET is not None:
            if self.request.GET.get("paginate_by", False):
                self.table_pagination = {}
                self.paginate_by = self.request.GET.get("paginate_by")
        return super(TableView, self).get_table(**kwargs)

    def get_table_kwargs(self):
        template_name = self.DEFAULT_TEMPLATE
        kwargs = {"template_name": template_name}
        if self.request.GET is not None:
            if self.request.GET.get("template_name", False):
                kwargs["template_name"] = self.request.GET.get("template_name")
        return kwargs


