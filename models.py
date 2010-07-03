from django.db import models

from unique_model.models import ReferenceUniqueModel
# Create your models here.
from core.models.domain import Domain

class MultiTenancyModel(models.Model):
    """
    Multi Tenancy Model
    ===================

    This class defines an abstract class that let define others models in
    a multitenancy environment.

    It only define a tenant field, as a char field with the uuid that uniquely identify
    the model defined as tenant.
    """

    tenant = ReferenceUniqueModel(Domain, null=True)
#    tenant = models.CharField(max_length=36, null=True)

    def get_tenant(self):
        return self._tenant_model.get_by_uuid(self.tenant)

    class Meta:
        abstract = True
