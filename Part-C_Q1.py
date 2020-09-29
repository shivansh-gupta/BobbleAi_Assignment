from string import punctuation
import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
#-------------------------------------------------------------------------------------------------#
with open('file.txt', 'r') as file:
    data = file.read().replace('\n', '')
print(data)
#-------------------------------------------------------------------------------------------------#
#1. Text_lowercase

data_lower=data.lower()
print(data_lower)
#-------------------------------------------------------------------------------------------------#
#2. Change numerals to their counter names

import re
ones = ["", "one ","two ","three ","four ", "five ", "six ","seven ","eight ","nine ","ten ","eleven ","twelve ", "thirteen ", "fourteen ", "fifteen ","sixteen ","seventeen ", "eighteen ","nineteen "]
twenties = ["","","twenty ","thirty ","forty ", "fifty ","sixty ","seventy ","eighty ","ninety "]
thousands = ["","thousand ","million ", "billion ", "trillion ", "quadrillion ", "quintillion ", "sextillion ", "septillion ","octillion ", "nonillion ", "decillion ", "undecillion ", "duodecillion ", "tredecillion ", "quattuordecillion ", "quindecillion", "sexdecillion ", "septendecillion ", "octodecillion ", "novemdecillion ", "vigintillion "]

def num999(n):
    c = n % 10
    b = ((n % 100) - c) / 10
    a = ((n % 1000) - (b * 10) - c) / 100
    t = ""
    h = ""
    if a != 0 and b == 0 and c == 0:
        t = ones[int(a)] + "hundred "
    elif a != 0:
        t = ones[int(a)] + "hundred and "
    if b <= 1:
        h = ones[n%100]
    elif b > 1:
        h = twenties[int(b)] + ones[int(c)]
    st = t + h
    return st

def num2word(num):
    if num == 0: return 'zero'
    i = 3
    n = str(num)
    word = "" 
    k = 0 
    while(i == 3): 
        nw = n[-i:] 
        n = n[:-i] 
        if int(nw) == 0: 
            word = num999(int(nw)) + thousands[int(nw)] + word 
        else: 
            word = num999(int(nw)) + thousands[k] + word 
        if n == '': 
            i = i+1 
        k += 1 
    return word[:-1]

text=data

text = re.sub(r"(\d+)", lambda x: num2word(int(x.group(0))), text)
print(text)
#-------------------------------------------------------------------------------------------------#

#3. remove_punctuation

print(''.join(c for c in data if c not in punctuation))
#-------------------------------------------------------------------------------------------------#
#4. remove_spaces

print(data.replace(" ",""))
#-------------------------------------------------------------------------------------------------#
#5. remove_stopwords
nltk.download('stopwords')
text =data
text = ' '.join([word for word in text.split() if word not in (stopwords.words('english'))])
print(text)
#-------------------------------------------------------------------------------------------------#
#6. stemming

nltk.download('punkt')
stopword = stopwords.words('english')
snowball_stemmer = SnowballStemmer('english')
text =data
word_tokens = nltk.word_tokenize(text)
stemmed_word = [snowball_stemmer.stem(word) for word in word_tokens]
print (stemmed_word)
#-------------------------------------------------------------------------------------------------#
#7. lemmatize
nltk.download('wordnet')
stopword = stopwords.words('english')
wordnet_lemmatizer = WordNetLemmatizer()
text = data
word_tokens = nltk.word_tokenize(text)
lemmatized_word = [wordnet_lemmatizer.lemmatize(word) for word in word_tokens]
print (lemmatized_word)
#-------------------------------------------------------------------------------------------------#