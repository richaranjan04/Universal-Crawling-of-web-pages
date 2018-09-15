# Universal-Crawling-of-web-pages

The following code crawls the web pages and calculates the cosine similarity between the given query and the web pages .

The sequence in which the tasks are performed are as follows:

Task #1 – perform universal crawling 

Task #2 – store the crawled page (at least 50) in a folder 

Task #3 – vectorisation for documents and term 

Task#4 – get a query and find cosine similarity between the given query and every document.

Task #5 – rank the documents based on the similarity and display the url of first 10 documents


LIBRARIES USED:

BeautifulSoup ,urllib2 : Crawling through the webpage and storing the
hyperlinks in a list.

NLTK: Removing the stop words and tokenisation.

sklearn.feature_extraction.txt : For vectorisation and calculation the cosine
similarity between the documents.
