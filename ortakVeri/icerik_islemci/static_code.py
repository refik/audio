from django.conf import settings

def static_code_url(context):
   return {'STATIC_CODE': settings.STATIC_CODE}
