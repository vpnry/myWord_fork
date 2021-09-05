# myWord
syllable, word and phrase segmenter for Burmese (Myanmar language)  
(Plan to release soon & please wait...)   

ဗမာစာ စာလုံးတွေကို ပေါ့ပေါ့ပါးပါးနဲ့ ဖြတ်ပေးနိုင်ပြီး developer တွေက လွယ်လွယ်ကူကူ ယူသုံးနိုင်တဲ့ ပြီးတော့လည်း မြန်မြန်ဆန်ဆန်နဲ့ ကိုယ့်စက်ထဲမှာ extend လုပ်နိုင်တဲ့ "syllable, word, phrase segmentation" လုပ်ပေးနိုင်တဲ့ segmentation tool က ဒီနေ့အထိ မရှိသေးဘူးလို့ နားလည်ထားတယ်။ အဲဒီ ကွက်လပ်ကိုဖြည့်နိုင်ဖို့ရည်ရွယ်ပြီးတော့ myWord ကို R&D လုပ်ခဲ့ပါတယ်။  

အားလုံး ပြီးစီးနေပေမဲ့ coding မှာ comment တွေ လိုက်ဖြည့်ဖို့နဲ့ final evaluation လုပ်ဖို့ကျန်နေသေးတာနဲ့ ပြီးတော့တခြား အလုပ်တွေနဲ့မအားတာနဲ့ မတင်ပေးနိုင်သေးဘူး ဖြစ်နေတယ်...  

Note: WAT2021 Machine Translation Share Task အလုပ်မှာ word segmentation လုပ်ဖို့အတွက် myWord ကိုသုံးထားတဲ့အတွက် စာတမ်းထဲမှာ link ထည့်ပေးလိုက်နိုင်ဖို့အတွက် repository ကို အရင်ဆောက်ထားလိုက်တာ။ ဒီလထဲမှာ release လုပ်ပေးနိုင်အောင် အချိန်လုမယ်...

Draft Writing ...  

## Regular Expression based Syllable Segmentation

xxx

[https://github.com/ye-kyaw-thu/sylbreak](https://github.com/ye-kyaw-thu/sylbreak) ထဲက Regular Expression ကိုပဲ သုံးထားပါတယ်။  

```python
myConsonant = r"က-အ"
enChar = r"a-zA-Z0-9"
otherChar = r"ဣဤဥဦဧဩဪဿ၌၍၏၀-၉၊။!-/:-@[-`{-~\s"
ssSymbol = r'္'
aThat = r'်'


#Regular expression pattern for Myanmar syllable breaking
#*** a consonant not after a subscript symbol AND a consonant is not followed by a-That character or a subscript symbol
BreakPattern = re.compile(r"((?<!" + ssSymbol + r")["+ myConsonant + r"](?![" + aThat + ssSymbol + r"])" + r"|[" + enChar + otherChar + r"])", re.UNICODE)
```


input file က အောက်ပါအတိုင်းရှိတယ်လို့ ဆိုကြပါစို့...  

```
$ cat test.txt 
ကျွန်တော်ကသုတေသနသမားပါ။
နေ့ရောညရောမြန်မာစာနဲ့ကွန်ပျူတာနဲ့ပဲအလုပ် များ ပါ တယ်
မင်းကကောဘာအလုပ်လုပ်တာလဲ။
ပြောပြပါအုံး
ကောဖီလည်းထပ်သောက်ချင်ရင်ပြောကွာ
မန္တလေးမှာဒေါ်အောင်ဆန်းစုကြည်မိန့်ခွန်းပြောမယ်တဲ့။
```

syllable segmentation လုပ်ဖို့အတွက်က command line argument ကို syllable လို့ ပေးပြီးနောက် <input-file> နဲ့ <output-file> တွေရဲ့ နာမည်တွေကို ရိုက်ထည့်ပေးလိုက်ယုံပါပဲ။  
 
```
$ python ./myword.py syllable ./test.txt ./test.syllable
$ cat ./test.syllable 
ကျွန် တော် က သု တေ သ န သ မား ပါ ။
နေ့ ရော ည ရော မြန် မာ စာ နဲ့ ကွန် ပျူ တာ နဲ့ ပဲ အ လုပ် များ ပါ တယ်
မင်း က ကော ဘာ အ လုပ် လုပ် တာ လဲ ။
ပြော ပြ ပါ အုံး
ကော ဖီ လည်း ထပ် သောက် ချင် ရင် ပြော ကွာ
မန္တ လေး မှာ ဒေါ် အောင် ဆန်း စု ကြည် မိန့် ခွန်း ပြော မယ် တဲ့ ။
```

## Vitabi Word Segmentation

myword မှာ သုံးထားတဲ့ Word Segmentation က manual word segmentation လုပ်ထားတဲ့ corpus ကနေ unigram, bigram dictionary တွေကို ကြိုဆောက်ထားပြီးတော့ Viterbi algorithm နဲ့ စာလုံးဖြတ်တဲ့ နည်းလမ်းပါ။    

xxx draft theory explanation  

ကိုယ့်မှာ manual word segmentation လုပ်ထားပြီးသား corpus က အဆင့်သင့်ရှိတယ်ဆိုရင် myword နဲ့ n-gram dictionary ဆောက်ဖို့အတွက်က အောက်ပါအတိုင်း command ပေးပါ။  
ဒီနေရာမှာ myword က unigram, bigram အဘိဓာန်တွေကို text file format အနေနဲ့ရော binary file format အနေနဲ့ရော ဆောက်ပေးသွားမှာမို့ အဲဒီ output filename တွေကို ```--unigram_word_txt unigram-word.txt```, ``` --bigram_word_txt bigram-word.txt```,  ```--unigram_word_bin unigram-word.bin```, ``` --bigram_word_bin bigram-word.bin``` ဆိုပြီး ကိုယ်ပေးချင်တဲ့ ဖိုင်နာမည်တွေကို  assign လုပ်သွားလို့ ရပါတယ်။  

Word n-gram dictionary building with full dictionary filenames parameters:  
 ```
 $ python ./myword.py build_dict --unigram_word_txt unigram-word.txt --bigram_word_txt bigram-word.txt --unigram_word_bin unigram-word.bin --bigram_word_bin bigram-word.bin ./corpus2.1k 
 ```
 
 တကယ်လို့ default ngram dictionary နာမည်တွေနဲ့ပဲ ဆောက်သွားမယ်၊ ဖိုင်နာမည်တွေကို သီးသန့် assign လုပ်တာမျိုး မလုပ်ဘူး ဆိုရင်တော့ အောက်ပါအတိုင်း command အတိုနဲ့ပဲ ngram အဘိဓာန်တွေကို ဆောက်သွားလို့ ရပါတယ်။  
Word n-gram dictionary building with default filenames:  
 ```
 $ python ./myword.py build_dict ./corpus2.1k 
 ```
 
 myword နဲ့ word segmentation လုပ်တာကို default n-gram dictionary တွေကိုပဲ သုံးပြီး စာလုံးဖြတ်မယ်ဆိုရင်တော့ အောက်ပါအတိုင်း command ပေးရပါတယ်။  
 ဒီနေရာမှာ ./test.txt ဖိုင်က input file ဖြစ်ပြီးတော့ ./test.word ကတော့ စာလုံးဖြတ်ပြီး ထွက်လာတဲ့ ဖိုင်ကိုသိမ်းစေချင်တဲ့ နာမည်ပါ။  
 
 Word segmentation with default n-gram dictionaries:  
 ```
 python ./myword.py word ./test.txt ./test.word
 ```

input ဖိုင်က အောက်ပါအတိုင်း သုံးထားပါတယ်။  
(space တွေပါနေလည်း myword က auto remove လုပ်ပေးသွားမှာမို့ တကူးတက space တွေကို ဖြုတ်ပြီးမှ input လုပ်စရာမလိုပါဘူး။ ခုက ဥပမာအနေနဲ့ မြင်သာအောင်သာ ပြထားတာပါ)  
```
(base) ye@administrator-HP-Z2-Tower-G4-Workstation:~/tool/word-seg-tool/python-wordsegment/wordsegment/y-test/ref/viterbi/dev4github/4release$ cat test.txt
ကျွန်တော်ကသုတေသနသမားပါ။
နေ့ရောညရောမြန်မာစာနဲ့ကွန်ပျူတာနဲ့ပဲအလုပ် များ ပါ တယ်
မင်းကကောဘာအလုပ်လုပ်တာလဲ။
ပြောပြပါအုံး
ကောဖီလည်းထပ်သောက်ချင်ရင်ပြောကွာ
မန္တလေးမှာဒေါ်အောင်ဆန်းစုကြည်မိန့်ခွန်းပြောမယ်တဲ့။

 ```

word segmented လုပ်ပြီး ထွက်လာတဲ့ output ဖိုင်က အောက်ပါအတိုင်းပါ။  

 ```
$ cat test.word
ကျွန်တော် က သုတေသန သမား ပါ ။
နေ့ ရော ည ရော မြန်မာ စာ နဲ့ ကွန်ပျူတာ နဲ့ ပဲ အလုပ် များ ပါ တယ်
မင်း က ကော ဘာ အလုပ် လုပ် တာ လဲ ။
ပြော ပြ ပါ အုံး
ကောဖီ လည်း ထပ် သောက် ချင် ရင် ပြော ကွာ
မန္တလေး မှာ ဒေါ်အောင်ဆန်းစုကြည် မိန့်ခွန်း ပြော မယ် တဲ့ ။
```

 **unigram, bigram dictionary တွေကို ဆောက်တဲ့အခါမှာ text file format အနေနဲ့ရော binary file format အနေနဲ့ရော ဆောက်ပေးသွားပေမဲ့ word segmentation လုပ်တဲ့အခါမှာတော့ binary dictionary နှစ်ခုပဲ လိုအပ်ပါတယ်။ text file format အဘိဓာန်တွေက developer/researcher တွေအနေနဲ့ မျက်လုံးနဲ့ စစ်ကြည့်ပြီး corpus ကို update လုပ်တာ သို့မဟုတ် အဘိဓာန်ကို update လုပ်ပြီး binary အဖြစ် ပြောင်းတာတွေ လုပ်နိုင်အောင်လို့ facility အနေနဲ့ ထည့်ပေးထားတာပါ။**  
 
 word segmentation လုပ်တဲ့ အခါမှာ unigram, bigram အဘိဓာန်တွေကို assign လုပ်ပြီး ဖြတ်မယ်ဆိုရင်တော့ အောက်ပါအတိုင်း command ပေးပြီး run ပါ။  
 (Word segmentation with unigram, binary n-gram dictionaries)
 ```
 $ python ./myword.py word --unigram_word_bin ./unigram-word.bin --bigram_word_bin ./bigram-word.bin ./test.txt ./test.word
 ```
 
 Word Segmentation ဖြတ်တဲ့အခါမှာ default က space နဲ့ခြားပေးမှာ ဖြစ်ပေမဲ့ delimiter ကိုလည်း အမျိုးမျိုး ပြောင်းလို့ ရပါတယ်။ ဥပမာ delimiter ကို pipe အဖြစ်ထားပြီး word segmentation လုပ်ချင်တယ် ဆိုရင်တော့ အောက်ပါအတိုင်း command ပေး run ပါ။  
 
 (Word segmentation with delimiter "pipe")
 ```
 $ python ./myword.py word --delimiter "|" ./test.txt ./test.word
```

ထွက်လာတဲ့ segmented output ဖိုင်က အောက်ပါအတိုင်းပါ။  

```
ကျွန်တော်|က|သုတေသန|သမား|ပါ|။
နေ့|ရော|ည|ရော|မြန်မာ|စာ|နဲ့|ကွန်ပျူတာ|နဲ့|ပဲ|အလုပ်|များ|ပါ|တယ်
မင်း|က|ကော|ဘာ|အလုပ်|လုပ်|တာ|လဲ|။
ပြော|ပြ|ပါ|အုံး
ကောဖီ|လည်း|ထပ်|သောက်|ချင်|ရင်|ပြော|ကွာ
မန္တလေး|မှာ|ဒေါ်အောင်ဆန်းစုကြည်|မိန့်ခွန်း|ပြော|မယ်|တဲ့|။
```

## Unsupervised Phrase Segmentation with NPMI

Phrase Segmentation လုပ်တာက Normalized pointwise mutual information (NPMI) နဲ့ပါ။  
[Assoc. Prof. Daichi Mochihashi](http://chasen.org/~daiti-m/diary/) ရဲ့ ဂျပန်လိုရေးထားတဲ့ blog ကို တွေ့ပြီး မြန်မာစာအတွက် စမ်းကြည့်ဖို့ အိုက်ဒီယာ ရခဲ့ပါတယ်။ သူ ရှင်းပြထားတာကိုပဲ အခြေခံပြီး ဗမာစာအတွက် စမ်းခဲ့တဲ့ အပိုင်းကို ရှင်းပြသွားပါမယ်။   

Wrod2Vec နဲ့ ပတ်သက်တဲ့ နာမည်ကြီး စာတမ်းနှစ်စောင် ကို အရင်ဆုံး refer လုပ်ကြမှ အသေးစိတ် ဇာတ်ရည်လည်ပါလိမ့်မယ်။  

ပထမစာတမ်း ဖြစ်တဲ့ [Efficient Estimation of Word Representations in Vector Space, (Mikolov et al., 2013)](https://arxiv.org/pdf/1310.4546.pdf) စာတမ်းထဲမှာ အောက်ပါအတိုင်း ဖော်ပြထားတာကို တွေ့ရပါလိမ့်မယ်။

```We have included in our test set only single token words, thus multi-word entities are not present (such as New York).```

ပထမစာတမ်းရဲ့ test set မှာ single token word တွေပဲ သုံးထားကြောင်း ဖော်ပြထားပါတယ်။ ဆိုလိုတာက "New York", "ice cream", "high school", "hot dog", "living room", "full moon", "up to date", "part-time work", "state of the art" တို့လို စာလုံး နှစ်လုံးနဲ့ အထက်တွဲနေတဲ့ စကားလုံးတွေ (word) တွေကို word2vec အနေနဲ့ train လုပ်မယ်ဆိုရင် အရင်ဆုံး အမြဲတမ်း တွဲပြီးသုံးနေတဲ့ စာလုံးတွဲတွေ တနည်းအားဖြင့် phrase တွေကို ငါတို့က ကြိုသိဖို့ လိုအပ်ပါတယ်။ အဲဒီလို သိပြီးမှသာ word2vec ကို train မလုပ်ခင်မှာ preprocessing အနေနဲ့ ဥပမာ "new_york", "ice_cream", ..., "up_to_date", "part_time_work", "state_of_the_art" အဖြစ် underscore နဲ့ တွဲတာမျိုး လုပ်ပြီး စာလုံးတစ်လုံးအနေနဲ့ training corpus ထဲမှာ ကြိုပြင်ထားဖို့ လိုအပ်ပါလိမ့်မယ်။ အဲဒီ လိုမျိုး NLP task အတွက်က supervised approach နဲ့ ဆိုရင် NER (Name Entity Recognition) model နဲ့ လုပ်လို့ ရပေမဲ့ NER model ဆောက်ဖို့အတွက်က NER corpus က ရှိနေမှ ဖြစ်ပါလိမ့်မယ်။ အဲဒါကြောင့် NER corpus ကို မသုံးပဲနဲ့ unsupervised approach အနေနဲ့ သွားမယ်ဆိုရင် ဘယ်လို လုပ်လို့ ရနိုင်တယ် ဆိုတာကို Word2Vec ရဲ့ဒုတိယစာတမ်းလို့ ပြောလို့ရတဲ့ [Distributed Representations of Words and Phrases and their Compositionality, (Mikolov et al., 2013)](https://arxiv.org/pdf/1310.4546.pdf) စာတမ်းရဲ့ Section 4. Learning Phrases မှာ Formula No. 6 အနေနဲ့ အောက်ပါအတိုင်း ဖော်ပြထားတာကို တွေ့ရပါလိမ့်မယ်။  


<img src="https://github.com/ye-kyaw-thu/myWord/blob/main/documentation/formula-6.png" />

ဒီနေရာမှာ ပြောနေတဲ့ n (v, w), n (v), n (w) တွေက bigram နဲ့ unigram frequency တွေ ဖြစ်ပြီးတော့ δ က frequency နိမ့်တဲ့ စကားလုံးတွဲတွေက ထိပ်ပိုင်းကို ရောက်မလာဖို့အတွက် ထိန်းညှိတဲ့ discount factor ပါ။ Phrase တွေကို ဆွဲထုတ်နိုင်ဖို့အတွက်က threshold တစ်ခု သတ်မှတ်ထားပြီး အဲဒီ threshold value အထက်မှာ ရှိတဲ့ bigram စကားလုံးတွဲတွေကို ရွေးယူလိုက်ယုံပါပဲ။ Threshold value အထက် ဆိုတာကို probability အနေနဲ့ စဉ်းစားကြည့်ရင် p (v, w) = n (v, w) / N, p (v) = n (v) / N, p (w) = n ဆိုပြီး ဖော်မြူလာအနေနဲ့ ရေးလို့ ရပါတယ်။ ဒီနေရာမှာ "N" ဆိုတာက unigram စုစုပေါင်းတန်ဖိုးပါ။ δ ကို ဖယ်ပြီးတော့ score တွက်ဖို့အတွက် စဉ်းစားရင် အောက်ပါအတိုင်း ရေးလို့ ရပါတယ်

score (v, w) = n (v, w) / (n (v) * n (w)) = (p (v, w) * N) / (p (v) * N * p (w) * N) = p (v, w) / (p (v) * p (w) * N)

ဒါကြောင့် ဒီ score တွက်တဲ့ အပိုင်းက self-mutual information PMI တွက်တဲ့ PMI (v, w) = log p (v, w) / (p (v) * p (w)) ဆိုတဲ့ ဖော်မြူလာနဲ့ အကုန်လုံးလိုလို ဆင်တူဖြစ်တာကို တွေ့ရပါလိမ့်မယ်။ ဒါပေမဲ့ သေသေချာချာ ပြန် နှိုင်းယှဉ်ကြည့်တဲ့ အခါမှာ၊ အော်ရဂျင်နယ် ဖော်မြူလာမှာက 1/N ဆိုတဲ့ factor က ပါဝင်ပြီးတော့ အဲဒါက corpus အပေါ်မှာ မူတည်နေလို့ ထွက်လာမယ့် score က အခြေခံအားဖြင့် corpus ရဲ့ length ပေါ်မှာ သွားပြီး မူတည်နေပါတယ်။ corpus ကို အပြောင်းအလဲ ထပ်တိုးတာမျိုး မလုပ်ပဲ fixed လုပ်ထားပြီးတော့ threshold တန်ဖိုးကို search လုပ်တာမျိုးလုပ်ရင်တော့ အတိုင်းအတာ တစ်ခုအထိ ပြေလည်ပေမဲ့ threshold ရဲ့ အဓိပ္ပါယ်က နားလည်ရခက်တဲ့အပြင် length မတူတဲ့ စာကြောင်းတွေကို သုံးပြီးတော့ score တွေကို နှိုင်းယှဉ်ကြည့်ပြီးသွားမယ်ဆိုရင် ရလာတဲ့ phrase တွေက ပုံမှန် လူတွေက သုံးနေကြတဲ့ phrase နဲ့တော့ တထပ်တည်း ကျမှာ မဟုတ်ပါဘူး။  

corpus ကို independent ဖြစ်ဖို့အတွက်က original score တန်ဖိုးကို N နဲ့ မြှောက်လို့ ရပါတယ်။ သို့သော် အခုပြောနေတဲ့ score ဆိုတာက PMI ကို တွက်တာ ဖြစ်တာကြောင့်   

- PMI ရဲ့က အားနည်းချက်က low frequency word တွေကို အားနည်းတာ  
- PMI scale ကလည်း ဒေတာပေါ်မူတည်ပြီးနေတာ  
 
စတဲ့ အချက်တွေလည်း ရှိတာကြောင့် Normalized PMI (NPMI) (Bouma 2009) ကို သုံးသင့်တယ်လို့ ထင်ပါတယ်။   
NPMI ဆိုတာက အောက်ပါအတိုင်း သတ်မှတ်ထားပါတယ်။  

NPMI (v, w) = log p (v, w) / (p (v) * p (w)) / (-log p (v, w))  

NPMI ကို -1≦NPMI(v,w)≦1 ဆိုတဲ့ range အတွင်းမှာ သတ်မှတ်ထားတာကြောင့် 1 ဖြစ်နေတဲ့ အချိန်မှာ v နဲ့ w တို့ဟာ တိုက်ရိုက် correlation ဖြစ်နေပြီး -1 ဖြစ်နေတဲ့ အချိန်မှာတော့ inverse correlation ဖြစ်နေကြောင်းကို နားလည်ရ လွယ်ကူပါတယ်။ ပြီးတော့ PMI မှာတုန်းက ရှိခဲ့တဲ့ "p(v)" တို့  "p(w)" တို့ရဲ့ တန်ဖိုးတွေက အရမ်း သေးငယ်တဲ့ အခါမှာ score ကို ဖောင်းပွစေနိုင်တဲ့ အားနည်းချက်ကိုလည်း ရှောင်ပြီးသွား ဖြစ်သွားပါလိမ့်မယ်။ အဲဒီလိုသာဆိုရင် Word2vec ရဲ့ အော်ရဂျင်နယ်စာတမ်းမှာ သုံးခဲ့တဲ့ heuristic discount coefficient တန်ဖိုး ဖြစ်တဲ့ δ လည်း မလိုအပ်တော့ပါဘူး။  

အဲဒါကြောင့် script တစ်ပုဒ် ရေးပြီးတော့ phrase အော်တိုဖြတ်တာကို စမ်း ကြည့်ဖြစ်ခဲ့ပါတယ်။ Phrase recognition သို့မဟုတ် phrase segmentation လုပ်တဲ့ core အပိုင်းကိုပဲ ရေးဖို့အတွက် unigram, bigram frequency တွေကို dictionary နှစ်ခုအနေနဲ့ သိမ်းထားခဲ့ပြီး၊ word bigram (v, w) က phrase ဖြစ်မဖြစ်ကို ဆုံးဖြတ်တဲ့ အပိုင်းကိုပဲ Python script နဲ့ ရေးပြရရင် အောက်ပါအတိုင်း ဖြစ်ပါလိမ့်မယ်။  

```
def compute_phrase (unigram, bigram, threshold = 0.5):
    N = sum (list (unigram.values ​​()))
    phrases = {}
    for bi, freq in bigram.items ():
        if freq> 1:
            v = bi [0]; w = bi [1]
            npmi = (log (N) + log (freq) --log (unigram [v]) --log (unigram [w])) \
                    / (log (N) --log (freq))
            if npmi> threshold:
                phrases [bi] = npmi
    return phrases
``` 
    
Threshold တန်ဖိုးက ဂျပန်စာအတွက်က 0.5 ထားပြီး စမ်းခဲ့ပေမဲ့ မြန်မာစာအတွက်က (0.1...0.5) ထားပြီး အမျိုးမျိုး စမ်းကြည့်ခဲ့ပါတယ်။  
အထက်ပါ algorithm ကို word segmentation လုပ်ထားတဲ့ မြန်မာစာ corpus တစ်ခုလုံးကို pass လုပ်ပြီးသွားတဲ့ အခါမှာ စာလုံးနှစ်လုံးတွဲ စကားစု (two-word phrase) တွေကို ရရှိလာမှာ ဖြစ်ပါတယ်။ တကယ်လို့ ဒုတိယအကြိမ် pass လုပ်ပြီးသွားရင်တော့ စာလုံး နှစ်လုံး ကနေ လေးလုံးအထိ တွဲလျက်ရှိနေတတ်တဲ့ စကားစု (two- to four-word phrase) တွေကို ရရှိလာမှာ ဖြစ်ပါတယ်။ အဲဒါကြောင့် သီအိုရီအရကတော့ passing ကို n pass အထိ လုပ်မယ် ဆိုရင် 2 ကနေ 2^n စာလုံးတွဲ phrase တွေကို ရရှိနိုင်မှာ ဖြစ်ပါတယ်။  

လက်နဲ့စာလုံး ဖြတ်ထားတဲ့ (i.e. manual word segmentation) လုပ်ထားတဲ့ စာကြောင်းရေ ၅သိန်းကျော် ရှိတဲ့ မြန်မာစာ corpus ကို သုံးပြီး phrase segmentation experiment တချို့ လုပ်ကြည့်ကြရအောင်။  

Threshold value=0.1, frequency=3, 1 time pass အနေနဲ့ run ကြည့်ထားပါတယ်။  
```
$ time python ./myword.py train_phrase -l 1 -t 0.1 -f 3 --unigram_phrase_txt unigram.l1.t0.1f3.txt --bigram_phrase_txt bigram.l1.t0.1f3.txt --unigram_phrase_bin unigram.l1.t0.1f3.bin --bigram_phrase_bin bigram.l1.t0.1f3.bin ./corpus2 ./train.l1t0.1f3.out
{'command': 'train_phrase', 'iteration': 1, 'threshold': 0.1, 'minfreq': 3, 'unigram_phrase_txt': 'unigram.l1.t0.1f3.txt', 'bigram_phrase_txt': 'bigram.l1.t0.1f3.txt', 'unigram_phrase_bin': 'unigram.l1.t0.1f3.bin', 'bigram_phrase_bin': 'bigram.l1.t0.1f3.bin', 'input': './corpus2', 'output': './train.l1t0.1f3.out'}
computing phrases: threshold = 0.1 minfreq = 3
pass [1/1]..
- computing phrases..
- writing output..
done.

real	1m4.555s
user	1m3.892s
sys	0m0.484s
```

pass က တစ်ခါပဲ လုပ်တာမို့ corpus ထဲမှာ ပါဝင်တဲ့ bigram စာလုံးတွဲတွေရဲ့ frequency ပေါ်မူတည်ပြီး threshold value ပေါ်ကို မူတည်ပြီး ဆွဲထုတ်လို့ ရလာတဲ့ မြန်မာစာ phrase ဥပမာ တချို့က အောက်ပါအတိုင်းပါ။  

```
$ tail ./train.l1t0.1f3.out
သူ_ဟာ လက်ဝှေ့ပွဲ မှာ အနိုင်_ရ နိုင် စရာ_ရှိ တယ်
သူ_ဟာ လက်ဝှေ့ ထိုးသတ်ပွဲ မှာ_ရှုံးနိမ့် ဖို့_မ ဖြစ်_နိုင် လောက် ဘူး
သူငယ်_ကလေး ဟာ ငါး_မျှား နေ_တယ်
သူ ကံကောင်း ရင် ငါး တစ်_ကောင် မိ နိုင် တယ်
သစ်ကိုင်း ဟာ သိပ်_မ ခိုင် ဘူး
၎င်း ဟာ‍ ကျိုး ချင် ကျိုး_သွား နိုင် တယ်
သစ်ကိုင်း_ကျိုး ကျ_သွား ရင်_ကောင်ကလေး ဟာ မြစ်_ထဲ ကို ကျ_သွား ဖို့ အလားအလာ_ရှိ တယ်
သူ မြစ်_ထဲ ကို ကျ_သွား ရင် သူ ရေစို ဖို့ ဖြစ် ကောင်း ဖြစ်_နိုင် လိမ့်_မယ်
ရုပ်ပုံ ထဲ_မှာ ပျား တစ်_ကောင် ရှိ_တယ်
၎င်း ဘာ_လုပ် နိုင် မယ်_လို့ ခင်ဗျား ထင်_သလဲ
```

Threshold value=0.1, frequency=3, 2 time pass ထားပြီး run ထားပါတယ်။  
```
$ time python ./myword.py train_phrase -l 2 -t 0.1 -f 3 --unigram_phrase_txt unigram.l2.t0.1f3.txt --bigram_phrase_txt bigram.l2.t0.1f3.txt --unigram_phrase_bin unigram.l2.t0.1f3.bin --bigram_phrase_bin bigram.l2.t0.1f3.bin ./corpus2 ./train.l2t0.1f3.out
{'command': 'train_phrase', 'iteration': 2, 'threshold': 0.1, 'minfreq': 3, 'unigram_phrase_txt': 'unigram.l2.t0.1f3.txt', 'bigram_phrase_txt': 'bigram.l2.t0.1f3.txt', 'unigram_phrase_bin': 'unigram.l2.t0.1f3.bin', 'bigram_phrase_bin': 'bigram.l2.t0.1f3.bin', 'input': './corpus2', 'output': './train.l2t0.1f3.out'}
computing phrases: threshold = 0.1 minfreq = 3
pass [1/2]..
- computing phrases..
- writing output..
pass [2/2]..
- computing phrases..
- writing output..
done.

real	1m38.575s
user	1m37.342s
sys	0m1.125s
```

ဒီတစ်ခါတော့ passing ကို နှစ်ခါ လုပ်ထားတာမို့ စာလုံး နှစ်လုံးတွဲ phrase တွေသာမကပဲ သုံးလုံးတွဲ၊ လေးလုံးတွဲ phrase တွေလည်း ဆွဲထုတ်လာနိုင်တာကို တွေ့ရပါလိမ့်မယ်။  

```
$ tail ./train.l2t0.1f3.out 
သူ_ဟာ လက်ဝှေ့ပွဲ မှာ အနိုင်_ရ နိုင် စရာ_ရှိ_တယ်
သူ_ဟာ လက်ဝှေ့ ထိုးသတ်ပွဲ မှာ_ရှုံးနိမ့် ဖို့_မ_ဖြစ်_နိုင် လောက်_ဘူး
သူငယ်_ကလေး ဟာ ငါး_မျှား နေ_တယ်
သူ ကံကောင်း_ရင် ငါး_တစ်_ကောင် မိ နိုင်_တယ်
သစ်ကိုင်း ဟာ သိပ်_မ ခိုင် ဘူး
၎င်း ဟာ‍ ကျိုး ချင် ကျိုး_သွား နိုင်_တယ်
သစ်ကိုင်း_ကျိုး ကျ_သွား ရင်_ကောင်ကလေး ဟာ မြစ်_ထဲ_ကို ကျ_သွား ဖို့_အလားအလာ_ရှိ တယ်
သူ မြစ်_ထဲ_ကို ကျ_သွား ရင် သူ ရေစို ဖို့ ဖြစ် ကောင်း_ဖြစ်_နိုင် လိမ့်_မယ်
ရုပ်ပုံ_ထဲ_မှာ ပျား_တစ်_ကောင် ရှိ_တယ်
၎င်း ဘာ_လုပ် နိုင်_မယ်_လို့ ခင်ဗျား ထင်_သလဲ
```

Threshold value=0.1, frequency=1, 2 time pass ထားပြီး run ထားပါတယ်။  
```
$ time python ./myword.py train_phrase -l 2 -t 0.1 -f 1 --unigram_phrase_txt unigram.l2.t0.1f1.txt --bigram_phrase_txt bigram.l2.t0.1f1.txt --unigram_phrase_bin unigram.l2.t0.1f1.bin --bigram_phrase_bin bigram.l2.t0.1f1.bin ./corpus2 ./train.l2t0.1f1.out
{'command': 'train_phrase', 'iteration': 2, 'threshold': 0.1, 'minfreq': 1, 'unigram_phrase_txt': 'unigram.l2.t0.1f1.txt', 'bigram_phrase_txt': 'bigram.l2.t0.1f1.txt', 'unigram_phrase_bin': 'unigram.l2.t0.1f1.bin', 'bigram_phrase_bin': 'bigram.l2.t0.1f1.bin', 'input': './corpus2', 'output': './train.l2t0.1f1.out'}
computing phrases: threshold = 0.1 minfreq = 1
pass [1/2]..
- computing phrases..
- writing output..
pass [2/2]..
- computing phrases..
- writing output..
done.

real	1m57.006s
user	1m55.366s
sys	0m1.373s
```

ဒီ တစ်ခါတော့ frequency ကို တစ်ကြိမ်ပါတာနဲ့ phrase အဖြစ် ထည့်သွင်းစဉ်းစားတဲ့အုပ်စုအထဲကို ဝင်လာမှာမို့ ဆွဲထုတ်ပြီး ရလာတဲ့ phrase တွဲတွေမှာ အပြောင်းအလဲ ဖြစ်လာတာကိုလည်း မြင်တွေ့ရမှာ ဖြစ်ပါတယ်။ ဥပမာ "ခင်ဗျား_ထင်_သလဲ" ကို phrase တစ်ခုအနေနဲ့ တွဲပေးသွားတာမျိုးပါ။  

```
$ tail ./train.l2t0.1f1.out 
သူ_ဟာ_လက်ဝှေ့ပွဲ မှာ အနိုင်_ရ နိုင် စရာ_ရှိ_တယ်
သူ_ဟာ လက်ဝှေ့_ထိုးသတ်ပွဲ_မှာ_ရှုံးနိမ့် ဖို့_မ_ဖြစ်_နိုင် လောက်_ဘူး
သူငယ်_ကလေး_ဟာ ငါး_မျှား_နေ_တယ်
သူ_ကံကောင်း ရင် ငါး_တစ်_ကောင် မိ နိုင်_တယ်
သစ်ကိုင်း_ဟာ သိပ်_မ_ခိုင် ဘူး
၎င်း_ဟာ‍_ကျိုး ချင်_ကျိုး_သွား နိုင်_တယ်
သစ်ကိုင်း_ကျိုး ကျ_သွား_ရင်_ကောင်ကလေး ဟာ_မြစ်_ထဲ ကို ကျ_သွား ဖို့_အလားအလာ_ရှိ တယ်
သူ_မြစ်_ထဲ ကို ကျ_သွား ရင် သူ ရေစို_ဖို့ ဖြစ် ကောင်း_ဖြစ်_နိုင် လိမ့်_မယ်
ရုပ်ပုံ_ထဲ_မှာ ပျား_တစ်_ကောင် ရှိ_တယ်
၎င်း ဘာ_လုပ် နိုင်_မယ်_လို့ ခင်ဗျား_ထင်_သလဲ

```
Threshold value=0.1, frequency=3, 2 time pass ဆိုတဲ့ training နဲ့ပဲ corpus ထဲကနေ ရှည်တဲ့ စာကြောင်းတွေကို ကနေ ရလာတဲ့ phrase တွေကိုလည်း လေ့လာကြည့်ရင် အောက်ပါလိုမျိုး စိတ်ဝင်စားစရာကောင်းတဲ့ မြန်မာစာ phrase အတွဲတွေ ရနိုင်တာကို မြင်တွေ့ရပါလိမ့်မယ်။  

```
$ shuf ./train.l2t0.1f3.out | head
ဒါ_ကြောင့်_က_ကျွန်တော် ဟာ ဩဇာ_လွှမ်းမိုး ရေး_လမ်းကြောင်း_ကို ပဲ လိုက် ခဲ့_တယ်_။
သီးခြား အကောင့်_တစ်_ခု နှင့်_ပူးတွဲ စာရင်း အကောင့်_ဖွင့် ထား_ခြင်း_သည် ငွေကြေး ပြဿနာ_အနည်းငယ် ကို_ကျော်လွှား ရန်_အမှန်တကယ် အထောက်အကူ_ပြု_နိုင် ပါ_တယ်_။
ဘယ်_သန် ဆို_ရင်_ကော 😝_😝_😜
မိန်းကလေး အတွက် လား_ဒါမှမဟုတ် ယောက်ျားလေး_အတွက် လား
ဝမ်းသာ_လိုက်_တာ ကိုရင်_တို့ ရယ်_၊ ဆွမ်း_ကွမ်း အပြင်_မှာ အခြား_ပစ္စည်း လေး_ပါး လည်း_လိုအပ် သမျှ_မိန့် ကြ_ပါ ၊_တပည့်တော်မ ကို ကုသိုလ် ပေး_ကြ_ပါ
ပျား ဆို_တဲ့_သတ္တဝါ လေး_တွေ_ဟာ သူ့_ဘာသာ_ဆို ဘာ_မှ_မ_လုပ် ပေ_မယ့် သူ နေ_တဲ့ အုံ_ကို များ သွား ထိမိ လိုက် လို့_က_တော့ အပြုံလိုက် ထွက်_လာ ပြီး_တုပ် တယ်_ဆို_တာ အားလုံး_သိ_ကြ မှာ_ပါ_။
နှုတ်ခမ်းနီ_လေး ဘယ်တော့_ရ_မလဲ ခု_လေး_တင် ဝယ်_လာ_တာ ပါ ကုန်_သွား မှာ_ဆိုး_လို့ ဘူး သေး ရော ဘူး ကြီး ရော_ဝယ် ခဲ့_တယ် ချစ်_သွား_ပြီ အဆင်ပြေ_လား_ကြိုက် လား_ရှင့် အသား_လတ် တယ်_ဆို နံပါတ်_၂၀_သုံး နော်
Football_Observatory ဆွန်ဟောင်မင် ကို_ယူရို_သန်း ၇ဝ_အနိမ့်ဆုံး_အပြောင်းအရွှေ့_ဈေး အဖြစ်_သတ်မှတ်_ဖော်ပြ_ထား ပါ_တယ်_။
ဟံသာဝတီ မြေ ကို_နင်း_မိ ပေ_ပြီ_။
၂၀၁၈_ခုနှစ် တရားမကြီး_မှု_အမှတ်_- ၃၅
```

ကိုယ်မှာက manual word segmentation လုပ်ထားတဲ့ corpus လည်း မရှိဘူး ဆိုရင်တော့ myword က version အလိုက် default အနေနဲ့ training လုပ်ပြီး သုံးထားတဲ့ dictionary ကိုပဲ သုံးပြီး phrase segmentation လုပ်ချင်တယ် ဆိုရင်တော့ အောက်ပါအတိုင်း command ပေးပါ။  

```
$ python ./myword.py phrase ./test.space.txt ./test.phrase
{'command': 'phrase', 'threshold': 0.1, 'minfreq': 1, 'unigram_phrase_bin': 'unigram-phrase.bin', 'bigram_phrase_bin': 'bigram-phrase.bin', 'input': './test.space.txt', 'output': './test.phrase'}
computing phrases: threshold = 0.1 minfreq = 1
phrase segmentation...
- read unigram dictionary
- read bigram dictionary
- computing phrases..
- writing output..., filename:  ./test.phrase
done.
```

လက်ရှိ default ထားထားတဲ့ dictionary နဲ့ ဖြတ်ပြီး ရလာတဲ့ output က အောက်ပါအတိုင်းပါ။  

```
$ cat ./test.phrase
ကျွန်တော်_က သုတေသန သမား ပါ_။
နေ့ ရော ည ရော_မြန်မာစာ နဲ့ ကွန်ပျူတာ_နဲ့ ပဲ အလုပ် များ ပါ_တယ်
မင်း_က ကော_ဘာ အလုပ်_လုပ် တာ_လဲ ။
ပြော_ပြ ပါ_အုံး
ကောဖီ လည်း ထပ်_သောက် ချင်_ရင် ပြော ကွာ
မန္တလေး_မှာ ဒေါ်_အောင်ဆန်းစုကြည် မိန့်ခွန်း_ပြော မယ် တဲ့ ။
```

**တစ်ခု သတိထားရမှာက input ဖိုင်က word ဖြတ်ထားတဲ့ ဖိုင်ကိုပေးမှသာ phrase အဖြစ် ဖြတ်ပေးမှာပါ**  

```
$ cat test.space.txt 
ကျွန်တော် က သုတေသန သမား ပါ ။
နေ့ ရော ည ရော မြန်မာစာ နဲ့ ကွန်ပျူတာ နဲ့ ပဲ အလုပ် များ ပါ တယ်
မင်း က ကော ဘာ အလုပ် လုပ် တာ လဲ ။
ပြော ပြ ပါ အုံး
ကောဖီ လည်း ထပ် သောက် ချင် ရင် ပြော ကွာ
မန္တလေး မှာ ဒေါ် အောင်ဆန်းစုကြည် မိန့်ခွန်း ပြော မယ် တဲ့ ။
```

တကယ်လို့ ကိုယ့် word segmented corpus နဲ့ အမျိုးမျိုး training/experiment လုပ်ထားပြီး ကိုယ်သုံးချင်တဲ့ dictionary ကို command line argument အနေနဲ့ assign လုပ်ပြီး သုံးချင်တယ် ဆိုရင်တော့ အောက်ပါအတိုင်း run ပါ။  

```
python ./myword.py phrase --unigram_phrase_bin ./unigram-phrase.bin --bigram_phrase_bin ./bigram-phrase.bin ./test2.txt ./test2.phrase
```

## Reference
 
1. Viterbi, Andrew. Error bounds for convolutional codes and an asymptotically optimum decoding algorithm. <i>IEEE transactions on Information Theory</i>, 13(2):260–269, 1967 [[Paper]](https://ieeexplore.ieee.org/document/1054010)
2. Slade, George. (2013). The Viterbi algorithm demystified. Link:[https://www.researchgate.net/publication/235958269_The_Viterbi_algorithm_demystified](https://www.researchgate.net/publication/235958269_The_Viterbi_algorithm_demystified) 
3. The Viterbi Algorithm Demystified, By Andrew J. Viterbi, March 16, 2017, Link: [https://viterbischool.usc.edu/news/2017/03/viterbi-algorithm-demystified/](https://viterbischool.usc.edu/news/2017/03/viterbi-algorithm-demystified/)
 4. Forney, G David. The Viterbi algorithm. <i>Proceedings of the IEEE</i>, 61(3):268–278, 1973, [https://www2.isye.gatech.edu/~yxie77/ece587/viterbi_algorithm.pdf](https://www2.isye.gatech.edu/~yxie77/ece587/viterbi_algorithm.pdf)
5. The Viterbi Algorithm at 50: [https://viterbischool.usc.edu/news/2017/03/viterbi-algorithm-50/](https://viterbischool.usc.edu/news/2017/03/viterbi-algorithm-50/)
6. Backurs, A. &amp; Tzamos, C.. (2017). Improving Viterbi is Hard: Better Runtimes Imply Faster Clique Algorithms. <i>Proceedings of the 34th International Conference on Machine Learning</i>, in <i>Proceedings of Machine Learning Research</i>, 70:311-321 [http://proceedings.mlr.press/v70/backurs17a/backurs17a.pdf](http://proceedings.mlr.press/v70/backurs17a/backurs17a.pdf)
7. Python implementation of Viterbi algorithm for word segmentation
A clean-up of this: [(http://norvig.com/ngrams/ch14.pdf)](http://norvig.com/ngrams/ch14.pdf), [https://gist.github.com/markdtw/e2a4e2ee7cef8ea6aed33bb47a97fba6](https://gist.github.com/markdtw/e2a4e2ee7cef8ea6aed33bb47a97fba6)
8. 
