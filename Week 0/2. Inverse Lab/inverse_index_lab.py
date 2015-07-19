from random import *
#------------------------------------------------------------------------------
# Task 1
def movie_review(name):
    review_options = ["See it!", "A gem!", "Ideological claptrap!"]
    return review_options[randint(0,2)]

#------------------------------------------------------------------------------
#Task 2
def makeInverseIndex(strlist):
	inverseindex = {}
        for (i,doc) in enumerate(strlist):
        	for word in doc.split():
        		if word not in inverseindex:
        			inverseindex[word] = set()
        		        inverseindex[word].add(i)
                        else:
                        	inverseindex[word].add(i)
        return inverseindex

#------------------------------------------------------------------------------
#Task 3
def orSearch(inverseindex,query):
	doc_id_set = set()
        for word in query:
        	if word in inverseIndex:
        		for id in inverseIndex[word]:
        			doc_id_set.add(id)
        return doc_id_set

#------------------------------------------------------------------------------
#Task 4:
def andSearch(inverseindex, query):
	doc_Ids = set()
        for q in query:
        	if q in inverseindex:
        		if not doc_Ids:
        			doc_Ids = inverseindex[q]
                        else:
                                doc_Ids = doc_Ids & inverseindex[q]
        return doc_Ids
#------------------------------------------------------------------------------
