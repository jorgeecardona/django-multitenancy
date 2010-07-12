from django.db import models
from django.conf import settings

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

    tenant = ReferenceUniqueModel(settings.MULTITENANCY_MODEL, null=True)

    class Meta:
        abstract = True
