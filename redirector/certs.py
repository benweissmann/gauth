EMAIL_HEADER = 'SSL_CLIENT_S_DN_Email'

def get_email(request):
    if EMAIL_HEADER in request.META:
        return request.META[EMAIL_HEADER]
    else:
        return None