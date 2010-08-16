#from django import forms
#import mongoengine as mongo

class MultiTenancyModel(object):
    """
    Multi Tenancy Model
    ===================

    This class defines an abstract class 
    that let define others models in a 
    multitenancy environment.

    It only define a tenant field, as a 
    char field with the reference field that 
    uniquely identify the model defined as tenant.
    """

#    tenant = mongo.GenericReferenceField()
