from django.shortcuts import render
from .import views
from django.http import HttpResponse
from .models import Post
from gtts import gTTS
import io



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