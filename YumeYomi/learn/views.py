from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from .import views
from django.http import HttpResponse, JsonResponse
from .models import Post, Radical, Character, CharacterEdit
from django.contrib.auth.decorators import login_required
#from .forms import CharacterEditForm
from django.db.models import Q
from gtts import gTTS
import io


def fetch_characters(request):
    selected_radicals = request.GET.getlist('radicals[]')
    if not selected_radicals:
        return JsonResponse({'characters': []})

    try:
        radical_ids = [int(id) for id in selected_radicals if id.isdigit()]
        if not radical_ids:
            return JsonResponse({'characters': []})

        radicals = Radical.objects.filter(radical_id__in=radical_ids)
        characters = Character.objects.filter(radicals__in=radicals).distinct()
        character_data = list(characters.values('name', 'meaning', 'readings'))
        return JsonResponse({'characters': character_data})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    

def character_detail(request, name):
    character = get_object_or_404(Character, name=name)
    return render(request, 'learn/character_detail.html', {
        'character': character
    })


def radical_selection(request):
    radicals = Radical.objects.all()
    return render(request, 'learn/radical_selection.html', {
        'radicals': radicals
    })
    



def radicals(request):
    radicals = Radical.objects.all()
    return render(request, "learn/radicals.html", {'radicals': radicals})

def radical_detail(request, radical):
    radical_obj = get_object_or_404(Radical, radical=radical)
    readings_hiragana = radical_obj.reading_hiragana.split(", ")
    readings_romanji = radical_obj.reading_romanji.split(", ")
    other_forms = radical_obj.other_forms.split(", ")

    readings = zip(readings_hiragana, readings_romanji)

    context = {
        'radical' : radical_obj,
        'readings': readings,
        'other_forms': other_forms
    }

    return render(request, 'learn/radical_detail.html', context)

def home(request):
    context = {"title" : "Home Page!!"}

    return render(request, "learn/base.html", context=context)

def post(request):
    context = {'posts': Post.objects.all()}
    return render(request, "learn/posts.html", context=context)

def generate_audio(request):
    if request.method == 'GET':
        # Get the kana character from the request
        character = request.GET.get('character', '')

        # Generate the audio using gtts
        tts = gTTS(text=character, lang='ja')
        audio_stream = io.BytesIO()
        tts.write_to_fp(audio_stream)
        audio_stream.seek(0)  # Reset stream position to the beginning

        # Return the audio as a streaming response
        response = HttpResponse(audio_stream, content_type='audio/mpeg')
        # response['Content-Disposition'] = 'attachment; filename="{}.mp3"'.format(character)
        return response
