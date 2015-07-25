## 1: (Task 1) Movie Review
## Task 1
from random import *
def movie_review(name):
    """
    Input: the name of a movie
    Output: a string (one of the review options), selected at random using randint
    """
    L = ["A gem","See it!","Ideologial claptrap!"]
    return L[randint(0,2)]


## 2: (Task 2) Make Inverse Index
def makeInverseIndex(strlist):
    """
    Input: a list of documents as strings
    Output: a dictionary that maps each word in any document to the set consisting of the
            document ids (ie, the index in the strlist) for all documents containing the word.
    Distinguish between an occurence of a string (e.g. "use") in the document as a word
    (surrounded by spaces), and an occurence of the string as a substring of a word (e.g. "because").
    Only the former should be represented in the inverse index.
    Feel free to use a loop instead of a comprehension.

    Example:
    >>> makeInverseIndex(['hello world','hello','hello cat','hellolot of cats']) == {'hello': {0, 1, 2}, 'cat': {2}, 'of': {3}, 'world': {0}, 'cats': {3}, 'hellolot': {3}}
    True
    """
    #create an empty dictionary first
    inverseindex = { }
    for (ii,doc) in enumerate(strlist):
    	for word in doc.split() :
    		if word not in inverseindex:
    			inverseindex[word] = set()
    			inverseindex[word].add(ii)
    		else:
    			inverseindex[word].add(ii)
    return inverseindex


## 3: (Task 3) Or Search
def orSearch(inverseindex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of document ids that contain _any_ of the specified words
    Feel free to use a loop instead of a comprehension.
    
    >>> idx = makeInverseIndex(['Johann Sebastian Bach', 'Johannes Brahms', 'Johann Strauss the Younger', 'Johann Strauss the Elder', ' Johann Christian Bach',  'Carl Philipp Emanuel Bach'])
    >>> orSearch(idx, ['Bach','the'])
    {0, 2, 3, 4, 5}
    >>> orSearch(idx, ['Johann', 'Carl'])
    {0, 2, 3, 4, 5}
    """
    doc_ids_set = set()
    for word in query:
    	if word in inverseindex:
    		for id in inverseindex[word]:
    			doc_ids_set.add(id)
    return doc_ids_set		



## 4: (Task 4) And Search
def andSearch(inverseindex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of all document ids that contain _all_ of the specified words
    Feel free to use a loop instead of a comprehension.

    >>> idx = makeInverseIndex(['Johann Sebastian Bach', 'Johannes Brahms', 'Johann Strauss the Younger', 'Johann Strauss the Elder', ' Johann Christian Bach',  'Carl Philipp Emanuel Bach'])
    >>> andSearch(idx, ['Johann', 'the'])
    {2, 3}
    >>> andSearch(idx, ['Johann', 'Bach'])
    {0, 4}
    """
    contain_all = set()
    for word in query:
    	if word in inverseindex:
    		if not contain_all:
    			#the case in which contain_all is the empty set
    			contain_all = inverseindex[word]
    		else:
    			contain_all = contain_all & inverseindex[word]
    return contain_all
# -----------------------------------end----------------------------------    
