from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404, render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext
from redirector.models import Token, Form
from redirector import certs

def index(request):
    if request.method == 'GET':
        return render_to_response('index.html', {'error': False},
                                  context_instance=RequestContext(request))
    else:
        form = Form(formkey = request.POST['formkey'])
        form.fill_entry_id()
        if not form.entry_id:
            return render_to_response(
                'index.html',
                {'error': True, 'formkey': request.POST['formkey']},
                context_instance=RequestContext(request)
            )

        form.save()

        return render_to_response(
            'created.html',
            {'form': form}
        )

def redirect(request, form_key):
    form = get_object_or_404(Form, key=form_key)
    token = form.token_set.create()
    token.user = certs.get_email(request)
    token.save()

    params = {form.entry_id: ('gauth:'+token.token)}

    return HttpResponseRedirect(form.get_url(params))

def resolve(request, token):
    try:
        token = Token.objects.get(token=token)
        return HttpResponse(token.user)
    except Token.DoesNotExist:
        return HttpResponse('INVALID')
