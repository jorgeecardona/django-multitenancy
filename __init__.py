from multitenancy.models import MultiTenancyModel

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
        request.domain = None 

        # Check for user in session
        if hasattr(request, 'user') and isinstance(request.user, MultiTenancyModel):
            try:
                request.domain = request.user.get_tenant()
                return
            except EntityNotFoundException:
                pass

        # Check for subdomain
        if len(request.get_host().split('.')) > 1:

            # Split host.
            subdomain, domain = host.split('.',1)
        
            # Search domain with this name.
            try:
                request.domain = Domain.get_by_name(subdomain)
                return
            except EntityNotFoundException:
                pass
                
        if 'domain' in request.REQUEST:
            try:
                request.domain = Domain.get_by_uuid(request.REQUEST['domain'])
                return
            except EntityNotFoundException:
                pass
