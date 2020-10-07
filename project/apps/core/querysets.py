from django.db.models import QuerySet


class ModeloBaseQuerySet(QuerySet):
    def activos(self, estado=True):
        return self.filter(activo=estado)
