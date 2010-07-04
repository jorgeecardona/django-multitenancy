from django.db import models

from unique_model.models import ReferenceUniqueModel
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

    _tenant_model = None
    tenant = ReferenceUniqueModel(_tenant_model, null=True)

    class Meta:
        abstract = True
