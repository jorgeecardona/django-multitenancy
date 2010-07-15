import logging

from django.conf import settings

from multitenancy.models import MultiTenancyModel
from unique_model.models import EntityNotFoundException

__base, __sub = settings.MULTITENANCY_MODEL.rsplit('.',1)
Tenant = getattr(__import__(__base, fromlist=[__sub]), __sub)

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
        if hasattr(request, 'subject') and isinstance(request.subject, MultiTenancyModel):
            try:
                request.tenant = request.subject.tenant
            except EntityNotFoundException:
                logging.info("Tenant not found.")
                pass

        # Check for subdomain
        elif request.get_host().endswith('.ubidots.com'):

            # Split host.
            subdomain = '.'.join(request.get_host().rsplit('.',2)[:-2])

            print subdomain
            # Search domain with this name.
            try:
                request.tenant = Tenant._get_by(subdomain=subdomain)
                print request.tenant
            except EntityNotFoundException:
                logging.info("Tenant not found.")
                pass
                
        elif 'domain' in request.REQUEST:
            try:
                request.tenant = Tenant.get_by_uuid(request.REQUEST['domain'])
            except EntityNotFoundException:
                logging.info("Tenant not found.")
                pass

        else:
            if hasattr(request, 'session'):
                if isinstance(request.session.get('tenant'), Tenant):
                    request.tenant = request.session['tenant']

        if hasattr(request, 'session'):
            request.session['tenant'] = request.tenant
            

