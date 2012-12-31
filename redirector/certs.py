from gauth.settings import CLIENT_EMAIL_HEADER

def get_email(request):
    if CLIENT_EMAIL_HEADER in request.META:
        return request.META[CLIENT_EMAIL_HEADER]
    else:
        return None