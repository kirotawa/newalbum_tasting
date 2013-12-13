# oreate your mport datetime
from django.http import HttpResponse
from django.contrib import messages, auth
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, redirect
from tasting.utils import *

def main(request):
    artist_songs = load_artist_songs()         
    # casa = " rua"
    return render_to_response('page.html', locals(), 
            context_instance=RequestContext(request))
        
