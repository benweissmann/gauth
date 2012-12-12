EMAIL_HEADER = 'SSL_CLIENT_S_DN_Email'

def get_email(request):
    return request.META[EMAIL_HEADER]