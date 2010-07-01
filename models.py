from django.db import models

# Create your models here.


class MultiTenancyModel(models.Model):
    """
    Multi Tenancy Model
    ===================

    This class defines an abstract class that let define others models in
    a multitenancy environment.

    It only define a tenant field, as a char field with the uuid that uniquely identify
    the model defined as tenant.
    """

    tenant = models.CharField(max_length=36, null=True)

    def get_tenant(self):
        return self.Meta.tenant_model.get_by_uuid(self.tenant)

    class Meta:
        abstract = True
