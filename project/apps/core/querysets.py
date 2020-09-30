from django.db.models import QuerySet


class ModeloBaseQuerySet(QuerySet):
    def activos(self):
        return self.filter(activo=True)
