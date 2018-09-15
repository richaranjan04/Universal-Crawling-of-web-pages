from bs4 import BeautifulSoup
import urllib2
import requests
import re,math
import os
from sklearn.feature_extraction.text import CountVectorizer
import codecs
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

#This function crawls the hyperlinks fron the list and writes the data into a text file
def func(i,name):                                
        html = requests.get(i).content
        #1 Recoding
        unicode_str = html.decode("ISO-8859-1")
        encoded_str = unicode_str.encode("ascii",'ignore')
        news_soup = BeautifulSoup(encoded_str, "html.parser")
        a_text = news_soup.find_all('p')
        #2 Removing
        y=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]

        file1 = open('test.txt', 'w')
        for item in y:
            file1.write("%s\n" % item)
        os.rename("test.txt",name)

#This function calculates the csoine similarity between the querry and the documents
def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

def text_to_vector(text):
     words = WORD.findall(text)
     #print(Counter(words)
     return Counter(words)
        
WORD = re.compile(r'\w+')


#TASK -1
#The URL od the wikipedia page of IIT Delhi is taken
url = "https://en.wikipedia.org/wiki/Indian_Institute_of_Technology_Delhi"
response = requests.get(url)
data = response.text
soup = BeautifulSoup(data, 'lxml')
links = []

# A list named 'links' is created and the crawler crawls the website and stoores all the hyperlnks in this list 
for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
    links.append(link.get('href'))
print('\n')
print('The hyperlinks found on the wikiperia page of IIT Delhi: ')
print(links)
print('\n')

#TASK -2
#All the hyperlinks are opened one by one and the content is stored in the text file.
name=[]
for i in range(50):
    s = "file"+ str(i) +".txt" 
    name.append(s)
x=0
for i in links:
    func(i,name[x])
    x=x+1

# The stop words are removed and tokenization of the content of tct file takes place
stop_words = set(stopwords.words('english'))
filtered_sentence = []

main =[]
i=0
for item in name:
    file1 = codecs.open(item, encoding='utf-8')
    word_tokens = word_tokenize(file1.read())
    for w in word_tokens:
        if w not in stop_words:
            s = s + " "+w
    main.append(s)

#TASK-3 
# vectorisation for documents and terms take place
vectorizer = CountVectorizer()
p = vectorizer.fit_transform(main)
print('The matrix after vectorization of the documents :')
print('\n')
print(p.toarray())
print('\n')

#Task-4
#The querry is taken fron the user and cosine similarity is calculated between wuerry and every document
print('Enter a query: ')

all_cos=[]
rank=[]
text1 = raw_input()
vector1 = text_to_vector(text1)
for i in range(50):
    text2 = codecs.open(name[i], encoding='ISO-8859-1').read()
    vector2 = text_to_vector(text2)
    cosine = get_cosine(vector1, vector2)
    all_cos.append(cosine)
    rank.append(cosine)
    print 'Cosine:', i, cosine

rank.sort(reverse=True)

#TASK-5
# The rank od document based on similarity and the url of top 10 documents are displayed 
print('Rank of documents based on similarity is as follows:')
print('\n')
for i in range(50):
    print 'Rank:', i,': ', rank[i]

j = 1
while j < 11:
    maxpos= all_cos.index(max(all_cos)) 
    s = all_cos[maxpos]
    print('\n')
    print 'Document ',j
    print'Value of similarity :',s
    print 'URL for that page is :',links[maxpos]
    print('\n')
    all_cos.remove(s)
    j += 1
    

