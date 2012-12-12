from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
import random
import urllib
from redirector import shortener
from redirector import form_parser
from gauth.settings import GAUTH_URL

def gen_token():
    return hex(random.getrandbits(100))[2:-1]

# Create your models here.
class Form(models.Model):
    formkey = models.CharField(max_length=50)
    entry_id = models.CharField(max_length=50, blank=True)
    key = models.CharField(max_length=50, db_index=True, unique=True, default=gen_token)
    short_url = models.CharField(max_length=50, blank=True)

    def fill_short_url(self):
        if self.short_url:
            return

        long_url = GAUTH_URL + "forms/" + self.key
        self.short_url = shortener.shorten(long_url)

    def fill_entry_id(self):
        if self.entry_id:
            return

        self.entry_id = form_parser.get_entry_id(self.get_url())

    def get_url(self, params={}):
        params['formkey'] = self.formkey
        return "https://docs.google.com/spreadsheet/viewform?" + urllib.urlencode(params)

@receiver(pre_save, sender=Form)
def fill_in_form(sender, **kwargs):
    kwargs['instance'].fill_entry_id()
    kwargs['instance'].fill_short_url()

class Token(models.Model):
    form = models.ForeignKey(Form)
    token = models.CharField(max_length=50, db_index=True, unique=True, default=gen_token)
    user = models.CharField(max_length=50)



