import logging

from django.conf import settings

from multitenancy.models import MultiTenancyModel

MULTITENANCY_SUBJECT = getattr(
    settings, 
    'MULTITENANCY_SUBJECT', 
    'subject')

class MultiTenancyMiddleware(object):
    """
    Multi tenancy Middleware
    ========================

    This middleware warranty the existence of a tenan in every request.

    The detection of the tenant depends on the kind of request, and it has several fallbacks.

    1) The most priority tenant container is the profile of the actual user authenticated.

    2) Tenant given by the subdomain of the request.

    3) Tenant given by the domain GET/POST request.

    4) None Tenant

    """

    def process_request(self, request):

        # Default value
        request.tenant = None 

        # Check for user in session
        if hasattr(request, MULTITENANCY_SUBJECT):
            # Get the subject
            subject = getattr(request, MULTITENANCY_SUBJECT)

            # Check if it is a multitenancy model
            if isinstance(subject, MultiTenancyModel):                
                request.tenant = subject.tenant
                
        else:
            if hasattr(request, 'session'):
                if 'tenant' in request.session:
                    request.tenant = request.sessioon['tenant']

        if hasattr(request, 'session'):
            request.session['tenant'] = request.tenant
            

