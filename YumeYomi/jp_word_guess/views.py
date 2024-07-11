from django.shortcuts import render, redirect
from django.http import HttpResponse
import random

# Dictionary mapping Hiragana characters to their romanji equivalents
hiragana_dict = {
    "あ": "a", "い": "i", "う": "u", "え": "e", "お": "o",
    "か": "ka", "き": "ki", "く": "ku", "け": "ke", "こ": "ko",
    "さ": "sa", "し": "shi", "す": "su", "せ": "se", "そ": "so",
    "た": "ta", "ち": "chi", "つ": "tsu", "て": "te", "と": "to",
    "な": "na", "に": "ni", "ぬ": "nu", "ね": "ne", "の": "no",
    "は": "ha", "ひ": "hi", "ふ": "fu", "へ": "he", "ほ": "ho",
    "ま": "ma", "み": "mi", "む": "mu", "め": "me", "も": "mo",
    "や": "ya", "ゆ": "yu", "よ": "yo",
    "ら": "ra", "り": "ri", "る": "ru", "れ": "re", "ろ": "ro",
    "わ": "wa", "を": "wo",
    "ん": "n",
    "が": "ga", "ぎ": "gi", "ぐ": "gu", "げ": "ge", "ご": "go",
    "ざ": "za", "じ": "ji", "ず": "zu", "ぜ": "ze", "ぞ": "zo",
    "だ": "da", "ぢ": "dji", "づ": "dzu", "で": "de", "ど": "do",
    "ば": "ba", "び": "bi", "ぶ": "bu", "べ": "be", "ぼ": "bo",
    "ぱ": "pa", "ぴ": "pi", "ぷ": "pu", "ぺ": "pe", "ぽ": "po",
    "きゃ": "kya", "きゅ": "kyu", "きょ": "kyo",
    "しゃ": "sha", "しゅ": "shu", "しょ": "sho",
    "ちゃ": "cha", "ちゅ": "chu", "ちょ": "cho",
    "にゃ": "nya", "にゅ": "nyu", "にょ": "nyo",
    "ひゃ": "hya", "ひゅ": "hyu", "ひょ": "hyo",
    "みゃ": "mya", "みゅ": "myu", "みょ": "myo",
    "りゃ": "rya", "りゅ": "ryu", "りょ": "ryo",
    "ぎゃ": "gya", "ぎゅ": "gyu", "ぎょ": "gyo",
    "じゃ": "ja", "じゅ": "ju", "じょ": "jo",
    "びゃ": "bya", "びゅ": "byu", "びょ": "byo",
    "ぴゃ": "pya", "ぴゅ": "pyu", "ぴょ": "pyo",
}

def random_word(request):
    if request.method == 'GET':
        return render(request, 'jp_word_guess/random.html')

    elif request.method == 'POST':
        # Handle character set selection
        if 'character_set' in request.POST:
            selected_set = request.POST.get('character_set')
            request.session['selected_set'] = selected_set
        else:
            selected_set = request.session.get('selected_set')

        # Handle user input submission
        if 'user_input' in request.POST:
            correct_romanji = request.session.get('correct_romanji', '')
            user_input = request.POST.get('user_input', '').strip().lower()
            character = request.session.get('character', '')

            if user_input == correct_romanji:
                result_message = f"Correct! {correct_romanji}"
                radical_char_meaning = request.session.get('radical_meaning', '')
            else:
                result_message = f"Incorrect. The correct romanji value is '{correct_romanji}'"
                radical_char_meaning = request.session.get('radical_meaning', '')

            context = {
                'character_display': character,
                'result_message': result_message,
                'radical_char_meaning': radical_char_meaning
            }
            return render(request, 'jp_word_guess/random.html', context)

        # Selecting the character set and preparing context for rendering
        if selected_set == 'hiragana':
            character = random.choice(list(hiragana_dict.keys()))
            correct_romanji = hiragana_dict[character]
            random_reading = ''  # Initialize as empty for consistency
            radical_char_meaning = ''
        else:
            return HttpResponse("Invalid character set selected", status=400)

        # Prepare context for rendering the template
        context = {
            'character_display': character,
            'random_reading': random_reading,
            'radical_char_meaning': radical_char_meaning,
        }

        return render(request, 'jp_word_guess/random.html', context)

    return HttpResponse("Method not allowed", status=405)