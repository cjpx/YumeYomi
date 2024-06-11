from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
import json
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import WordList,  Word, Like, Tag
from .forms import WordListForm, WordForm

def list_index(request):
    public_lists = WordList.objects.filter(privacy='public')
    for word_list in public_lists:
        word_list.already_liked = word_list.user_already_liked(request.user) if request.user.is_authenticated else False
    return render(request, 'users_list/list_index.html', {'lists': public_lists})

def list_detail(request, pk):
    word_list = get_object_or_404(WordList, pk=pk)
    words = word_list.words.all()

    if word_list.privacy == 'private' and word_list.author != request.user:
        return render(request, 'users_list/not_authorized.html')
    
    return render(request, 'users_list/list_detail.html', {'word_list': word_list, 'words': words})

@login_required
def create_list(request):
    if request.method == 'POST':
        form = WordListForm(request.POST)
        if form.is_valid():
            word_list = form.save(commit=False)
            word_list.author = request.user
            word_list.save()
            return redirect('list_index')
    else:
        form = WordListForm()
    return render(request, 'users_list/form.html', {'form': form})

@login_required
def add_word(request, list_pk):
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            word = form.save(commit=False)
            word.word_list_id = list_pk
            word.save()
            # Process tags
            tag_names = request.POST.get('tags')
            if tag_names:
                tag_names_list = [tag.strip() for tag in tag_names.split(',') if tag.strip()]
                for tag_name in tag_names_list:
                    tag, _ = Tag.objects.get_or_create(name=tag_name)
                    word.tags.add(tag)
            return redirect('list_detail', pk=list_pk)
    else:
        form = WordForm()
    return render(request, 'users_list/form.html', {'form': form})

@login_required
def add_tag(request):
    if request.method == 'POST' and request.is_ajax():
        tags = request.POST.getlist('tags[]')
        for tag_name in tags:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            # Do something with the tag if needed
        return JsonResponse({'message': 'Tags added successfully'}, status=200)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)


@login_required
def toggle_privacy(request, pk):
    word_list = get_object_or_404(WordList, pk=pk, author=request.user)
    
    # Toggle privacy setting
    if word_list.privacy == 'public':
        word_list.privacy = 'private'
    else:
        word_list.privacy = 'public'
    
    word_list.save()
    
    return redirect('list_index')

@login_required
@csrf_exempt
@require_POST
def like_word_list(request):
    try:
        data = json.loads(request.body)
        word_list_id = data.get('word_list_id')
        action = data.get('action')
        if word_list_id and action:
            word_list = WordList.objects.get(id=word_list_id)
            if action == 'like':
                word_list.like(request.user)
            else:
                word_list.unlike(request.user)
            return JsonResponse({'likes_count': word_list.likes, 'liked': action == 'like'})
    except WordList.DoesNotExist:
        return JsonResponse({'error': 'WordList not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request'}, status=400)

@login_required
def unlike_word_list(request, pk):
    word_list = get_object_or_404(WordList, pk=pk)
    Like.objects.filter(user=request.user, word_list=word_list).delete()
    return redirect('list_index', pk=pk)


def toggle_like(request):
    if request.method == 'POST' and request.is_ajax():
        word_list_id = request.POST.get('word_list_id')
        already_liked = request.POST.get('already_liked')

        # Toggle like status here

        return JsonResponse({'success': True, 'liked': not already_liked})
    else:
        return JsonResponse({'success': False})


def word_detail(request, word_id):
    word = get_object_or_404(Word, id=word_id)
    if request.method == 'POST':
        form = WordForm(request.POST, instance=word)
        if form.is_valid():
            form.save()
            return redirect('word_detail', word_id=word.id)
    else:
        form = WordForm(instance=word)
    return render(request, 'users_list/word.html', {'word': word, 'form': form})