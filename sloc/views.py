from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from models import Segment, Language, Sloc, SlocType
from forms import SlocForm

def index(request):
    segments = Segment.objects.all()
    languages = Language.objects.all()
    return render_to_response('sloc/index.html', {'segments': segments, 'languages': languages})

def segment_detail(request, segment_id):
    segment = get_object_or_404(Segment, pk=segment_id)
    slocs = Sloc.objects.filter(segment=segment_id).order_by('-created_date')[:20]
    return render_to_response('sloc/segment_detail.html', {'segment': segment, 'slocs': slocs})

def segment_detail_csv(request, segment_id):
    segment = get_object_or_404(Segment, pk=segment_id)
    slocs = Sloc.objects.filter(segment=segment_id)
    return render_to_response('sloc/segment_detail.csv', {'segment': segment, 'slocs': slocs})

def language_detail(request, language_id):
    language = get_object_or_404(Language, pk=language_id)
    slocs = Sloc.objects.filter(language=language_id).order_by('-created_date')[:20]
    return render_to_response('sloc/language_detail.html', {'language': language, 'slocs': slocs})

def language_detail_csv(request, language_id):
    language = get_object_or_404(Language, pk=language_id)
    slocs = Sloc.objects.filter(language=language_id)
    return render_to_response('sloc/language_detail.csv', {'language': language, 'slocs': slocs})

def sloc_add(request):
    def errorHandle(error):
        form = SlocForm()
        return render_to_response('sloc/sloc_add.html', {
                'error' : error,
                'form' : form,
        })
    if request.method == 'POST':
        form = SlocForm(request.POST)
        if form.is_valid():
            sloc = form.cleaned_data['sloc']
            segment = form.cleaned_data['segment']
            language = form.cleaned_data['language']
            generated_date = form.cleaned_data['generated_date']
            reported_by = form.cleaned_data['reported_by']
            sloc_type = form.cleaned_data['sloc_type']
            new_sloc = Sloc(source_lines_of_code=sloc, segment=segment,
                language=language, generated_date=generated_date, reported_by=reported_by, sloc_type=sloc_type)
            
            new_sloc.save()

            if new_sloc:
                error = u'Sloc successfully saved'
                return errorHandle(error)
            else:
                error = u'Could not save sloc entry'
                return errorHandle(error)
        else:
            error = u'The form is not filled in correctly (are all fields filled in?)'
            return errorHandle(error)
    else:
        form = SlocForm()
        return render_to_response('sloc/sloc_add.html', {'form': form})

