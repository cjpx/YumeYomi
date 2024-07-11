from django.shortcuts import render, redirect
from django.http import HttpResponse
from learn .models import Radicals
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

katakana_dict = {
    "ア": "a", "イ": "i", "ウ": "u", "エ": "e", "オ": "o",
    "カ": "ka", "キ": "ki", "ク": "ku", "ケ": "ke", "コ": "ko",
    "サ": "sa", "シ": "shi", "ス": "su", "セ": "se", "ソ": "so",
    "タ": "ta", "チ": "chi", "ツ": "tsu", "テ": "te", "ト": "to",
    "ナ": "na", "ニ": "ni", "ヌ": "nu", "ネ": "ne", "ノ": "no",
    "ハ": "ha", "ヒ": "hi", "フ": "fu", "ヘ": "he", "ホ": "ho",
    "マ": "ma", "ミ": "mi", "ム": "mu", "メ": "me", "モ": "mo",
    "ヤ": "ya", "ユ": "yu", "ヨ": "yo",
    "ラ": "ra", "リ": "ri", "ル": "ru", "レ": "re", "ロ": "ro",
    "ワ": "wa", "ヲ": "wo",
    "ン": "n",
    "ガ": "ga", "ギ": "gi", "グ": "gu", "ゲ": "ge", "ゴ": "go",
    "ザ": "za", "ジ": "ji", "ズ": "zu", "ゼ": "ze", "ゾ": "zo",
    "ダ": "da", "ヂ": "dji", "ヅ": "dzu", "デ": "de", "ド": "do",
    "バ": "ba", "ビ": "bi", "ブ": "bu", "ベ": "be", "ボ": "bo",
    "パ": "pa", "ピ": "pi", "プ": "pu", "ペ": "pe", "ポ": "po",
    "キャ": "kya", "キュ": "kyu", "キョ": "kyo",
    "シャ": "sha", "シュ": "shu", "ショ": "sho",
    "チャ": "cha", "チュ": "chu", "チョ": "cho",
    "ニャ": "nya", "ニュ": "nyu", "ニョ": "nyo",
    "ヒャ": "hya", "ヒュ": "hyu", "ヒョ": "hyo",
    "ミャ": "mya", "ミュ": "myu", "ミョ": "myo",
    "リャ": "rya", "リュ": "ryu", "リョ": "ryo",
    "ギャ": "gya", "ギュ": "gyu", "ギョ": "gyo",
    "ジャ": "ja", "ジュ": "ju", "ジョ": "jo",
    "ビャ": "bya", "ビュ": "byu", "ビョ": "byo",
    "ピャ": "pya", "ピュ": "pyu", "ピョ": "pyo",
}

def random_word(request):
    if request.method == 'GET':
        return render(request, 'jp_word_guess/random.html')

    elif request.method == 'POST':
        # Handle character set selection
        if 'character_set' in request.POST:
            selected_set = request.POST.get('character_set')
            request.session['selected_set'] = selected_set
            # Reset session values for new character set
            request.session['character'] = None
            request.session['correct_romanji'] = None
            request.session['random_reading'] = None
            request.session['radical_meaning'] = None
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
        elif selected_set == 'katakana':
            character = random.choice(list(katakana_dict.keys()))
            correct_romanji = katakana_dict[character]
            random_reading = ''  # Initialize as empty for consistency
            radical_char_meaning = ''
        elif selected_set == 'kanas':
            # Merge hiragana and katakana dictionaries
            merged_dict = {**hiragana_dict, **katakana_dict}
            character = random.choice(list(merged_dict.keys()))
            correct_romanji = merged_dict[character]
            random_reading = character  # Store the selected character for display
            radical_char_meaning = ''
        elif selected_set == 'radical':
            # Fetch a random radical instance
            radical = Radicals.objects.order_by('?').first()

            # Split readings into lists
            readings_hiragana = radical.reading_hiragana.split(",")
            readings_romanji = radical.reading_romanji.split(",")

            # Ensure hiragana and romanji readings are matched correctly
            if len(readings_hiragana) != len(readings_romanji) or len(readings_hiragana) == 0:
                return HttpResponse("Error: Invalid data in database", status=500)

            # Randomly select an index to display
            random_index = random.randint(0, len(readings_hiragana) - 1)
            random_hiragana = readings_hiragana[random_index].strip()
            correct_romanji = readings_romanji[random_index].strip()

            # Store selected values in session
            request.session['character'] = radical.radical
            request.session['correct_romanji'] = correct_romanji
            request.session['random_reading'] = random_hiragana
            request.session['radical_meaning'] = radical.radical_meaning

            # Display only one reading and its corresponding romanji
            radical_char_meaning = f"{radical.radical} meaning: {radical.radical_meaning}, hiragana reading: {random_hiragana}, romanji reading {correct_romanji}"

            character = radical.radical
            random_reading = random_hiragana
        else:
            return HttpResponse("Invalid character set selected", status=400)

        # Store the correct romanji value in session
        request.session['correct_romanji'] = correct_romanji

        # Prepare context for rendering the template
        context = {
            'character_display': character,
            'random_reading': random_reading,
            'radical_char_meaning': radical_char_meaning,
        }

        return render(request, 'jp_word_guess/random.html', context)

    return HttpResponse("Method not allowed", status=405)