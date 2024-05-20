from django.shortcuts import render

# Create your views here.
def hiragana(request):
    title = "ひらがな"
    hiragana_table = {
    # Monographs (gojūon)
    "あ": "a", "い": "i", "う": "u", "え": "e", "お": "o",
    "か": "ka", "き": "ki", "く": "ku", "け": "ke", "こ": "ko",
    "さ": "sa", "し": "shi", "す": "su", "せ": "se", "そ": "so",
    "た": "ta", "ち": "chi", "つ": "tsu", "て": "te", "と": "to",
    "な": "na", "に": "ni", "ぬ": "nu", "ね": "ne", "の": "no",
    "は": "ha", "ひ": "hi", "ふ": "fu", "へ": "he", "ほ": "ho",
    "ま": "ma", "み": "mi", "む": "mu", "め": "me", "も": "mo",
    "や": "ya", "placeholder1": "", "ゆ": "yu", "placeholder2": "", "よ": "yo",
    "ら": "ra", "り": "ri", "る": "ru", "れ": "re", "ろ": "ro",
    "わ": "wa", "placeholder3": "", "placeholder4": "", "placeholder5": "", "を": "wo",
    "ん": "n",
    }

    diacritics_table = {
    "が": "ga", "ぎ": "gi", "ぐ": "gu", "げ": "ge", "ご": "go",
    "ざ": "za", "じ": "ji", "ず": "zu", "ぜ": "ze", "ぞ": "zo",
    "だ": "da", "ぢ": "dji", "づ": "dzu", "で": "de", "ど": "do",
    "ば": "ba", "び": "bi", "ぶ": "bu", "べ": "be", "ぼ": "bo",
    "ぱ": "pa", "ぴ": "pi", "ぷ": "pu", "ぺ": "pe", "ぽ": "po",
    } 

    digraphs_table = {
    "きゃ": "kya", "placeholder6": "", "きゅ": "kyu", "placeholder7": "", "きょ": "kyo",
    "しゃ": "sha", "placeholder8": "", "しゅ": "shu", "placeholder9": "", "しょ": "sho",
    "ちゃ": "cha", "placeholder10": "", "ちゅ": "chu", "placeholder11": "", "ちょ": "cho",
    "にゃ": "nya", "placeholder12": "", "にゅ": "nyu", "placeholder13": "", "にょ": "nyo",
    "ひゃ": "hya", "placeholder14": "", "ひゅ": "hyu", "placeholder15": "", "ひょ": "hyo",
    "みゃ": "mya", "placeholder16": "", "みゅ": "myu", "placeholder17": "", "みょ": "myo",
    "りゃ": "rya", "placeholder18": "", "りゅ": "ryu", "placeholder19": "", "りょ": "ryo",
    "ぎゃ": "gya", "placeholder20": "", "ぎゅ": "gyu", "placeholder21": "", "ぎょ": "gyo",
    "じゃ": "ja", "placeholder22": "", "じゅ": "ju", "placeholder23": "", "じょ": "jo",
    "びゃ": "bya", "placeholder24": "", "びゅ": "byu", "placeholder25": "", "びょ": "byo",
    "ぴゃ": "pya", "placeholder26": "", "ぴゅ": "pyu", "placeholder27": "", "ぴょ": "pyo",
    }   


    context = {"hiragana_table":hiragana_table, "title":title, "diacritics_table":diacritics_table, "digraphs_table":digraphs_table}
    return render(request, 'kanas/hiragana.html', context=context)

def katakana(request):
    title = "カタカナ"
    #context = {"title": title}
    katakana_table= {
    # Monographs (basic katakana)
    "ア": "a", "イ": "i", "ウ": "u", "エ": "e", "オ": "o",
    "カ": "ka", "キ": "ki", "ク": "ku", "ケ": "ke", "コ": "ko",
    "サ": "sa", "シ": "shi", "ス": "su", "セ": "se", "ソ": "so",
    "タ": "ta", "チ": "chi", "ツ": "tsu", "テ": "te", "ト": "to",
    "ナ": "na", "ニ": "ni", "ヌ": "nu", "ネ": "ne", "ノ": "no",
    "ハ": "ha", "ヒ": "hi", "フ": "fu", "ヘ": "he", "ホ": "ho",
    "マ": "ma", "ミ": "mi", "ム": "mu", "メ": "me", "モ": "mo",
    "ヤ": "ya", "placeholder1": "", "ユ": "yu",  "placeholder2": "", "ヨ": "yo",
    "ラ": "ra", "リ": "ri", "ル": "ru", "レ": "re", "ロ": "ro",
    "ワ": "wa",  "placeholder28": "", "placeholder29": "", "placeholder30": "","ヲ": "wo", 
    "ン": "n",
    }  

    dicrits_table = {
        # Diacritics (tenten and maru)
    "ガ": "ga", "ギ": "gi", "グ": "gu", "ゲ": "ge", "ゴ": "go",
    "ザ": "za", "ジ": "ji", "ズ": "zu", "ゼ": "ze", "ゾ": "zo",
    "ダ": "da", "ヂ": "zi", "ヅ": "zu", "デ": "de", "ド": "do",
    "バ": "ba", "ビ": "bi", "ブ": "bu", "ベ": "be", "ボ": "bo",
    "パ": "pa", "ピ": "pi", "プ": "pu", "ペ": "pe", "ポ": "po",
    }

    digraphs_table = {
        # Digraphs (yōon)
    "キャ": "kya",  "placeholder3": "", "キュ": "kyu", "placeholder4": "", "キョ": "kyo",
    "シャ": "sha",  "placeholder5": "",  "シュ": "shu", "placeholder6": "", "ショ": "sho",
    "チャ": "cha",  "placeholder7": "",  "チュ": "chu", "placeholder8": "", "チョ": "cho",
    "ニャ": "nya",  "placeholder9": "", "ニュ": "nyu", "placeholder10": "", "ニョ": "nyo",
    "ヒャ": "hya",  "placeholder11": "", "ヒュ": "hyu", "placeholder12": "",  "ヒョ": "hyo",
    "ミャ": "mya",  "placeholder13": "", "ミュ": "myu",  "placeholder14": "", "ミョ": "myo",
    "リャ": "rya",  "placeholder15": "", "リュ": "ryu",  "placeholder16": "", "リョ": "ryo",
    }

    handukten_table = {
        # Digraphs with diacritics (yōon with (han)dakuten)
    "ギャ": "gya",  "placeholder17": "", "ギュ": "gyu",  "placeholder18": "", "ギョ": "gyo",
    "ジャ": "ja",  "placeholder19": "", "ジュ": "ju",  "placeholder20": "", "ジョ": "jo",
    "ビャ": "bya",  "placeholder21": "", "ビュ": "byu",  "placeholder22": "", "ビョ": "byo",
    "ピャ": "pya",  "placeholder23": "", "ピュ": "pyu",  "placeholder24": "", "ピョ": "pyo",
    }

    extendedkana_table = {
         # Extended katakana
    "イィ": "yi", "placeholder25": "", "イェ": "ye", "placeholder26": "", "イォ": "yo",
    "ウァ": "wa", "ウィ": "wi", "ウゥ": "wu", "ウェ": "we", "ウォ": "wo",
    "ヴァ": "va", "ヴィ": "vi", "ヴ": "vu", "ヴェ": "ve", "ヴォ": "vo",
    "ファ": "fa", "フィ": "fi",  "placeholder27": "", "フェ": "fe", "フォ": "fo",
    "ラ゚": "la", "リ゚": "li", "ル゚": "lu", "レ゚": "le", "ロ゚": "lo"
    }
    
    
    context = {"katakana_table":katakana_table, "title":title, "dicrits_table": dicrits_table, "digraphs_table":digraphs_table, 
               "handukten_table": handukten_table, "extendedkana_table": extendedkana_table}
    return render(request, 'kanas/katakana.html', context=context)
