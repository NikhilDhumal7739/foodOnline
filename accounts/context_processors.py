from vendor.models import Vendor
from django.conf import settings
#context processor :- is a function which takes one argument that is request, and return a dictionary that gets added to the request context.
#Inshort it is used here so All modeules which are present on sidebar (eg. Dashboard, myRestarent and so on..) can access  the current user_profile in one go from cover.html.

def get_vendor(request):
    try:
        vendor = Vendor.objects.get(user=request.user)
    except:
        vendor = None
    return dict(vendor = vendor)

def get_google_api(request):
    return {'GOOGLE_API_KEY': settings.GOOGLE_API_KEY}