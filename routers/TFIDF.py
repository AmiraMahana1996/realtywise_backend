from sklearn.feature_extraction.text import TfidfVectorizer
from fastapi import Depends, HTTPException, status, APIRouter, Response
from database import Property
from sklearn.metrics.pairwise import cosine_similarity
import json
from bson import json_util

router = APIRouter()
def TFIDF(term:str):
    Documents = Property.find()
    documents=[doc for doc in Documents]
    # create a list of all document texts
    texts = [doc["advertising"] for doc in documents]
    # create a TfidfVectorizer object and fit it to the documents
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(texts)
    print(tfidf_matrix)
    # # compute the cosine similarity matrix
    # cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)  
    # define a query
    query = term
    # transform the query using the TfidfVectorizer object
    query_vector = vectorizer.transform([query])
     # compute the cosine similarity between the query and the documents
    similarity_scores = cosine_similarity(query_vector, tfidf_matrix)
    # sort the documents by their similarity score
    similarity_scores = similarity_scores[0]
    document_indices = [i for i in range(len(similarity_scores))]
    sorted_indices = sorted(document_indices, key=lambda i: similarity_scores[i], reverse=True)
    # print the top 10 documents
    rankingDocs=list()
    if  len(sorted_indices) == 0:
        for i in range(10):
            doc_index = sorted_indices[i]
            _id=documents[doc_index]["_id"]
            str_id = _id
            doc = Property.find_one({"_id": str_id})
            rankingDocs.append(doc)
        return json.loads(json_util.dumps(rankingDocs))
    else :
     return "There is no posts related with this term"
# TFIDF Search Engine
@router.get('/{term}')
def get_properties(term: str):
 TFIDF(term)


# get appartments
@router.get('/residential/appartment')
def get_appartment():
   TFIDF('appartment')


#   get villas
@router.get('/residential/villa')
def get_villa():
   TFIDF('villa')

# get castel
@router.get('/residential/castle')
def get_castle():
   TFIDF('castle')

# get chalets
@router.get('/residential/chalets')
def get_chalets():
   TFIDF('chalets')

#  GET INDUSTRIAL PROPERTIES
# get factory
@router.get('/industrial/factory')
def get_factory():
   TFIDF('factory')


# get stores
@router.get('/industrial/stores')
def get_stores():
   TFIDF('stores')


# GET COMMERCIAL PROPERTIES
# get administrative
@router.get('/commercial/administrative')
def get_administrative():
   TFIDF('administrative')


# get shopping_center
@router.get('/commercial/shopping_center')
def get_shopping_center():
   TFIDF('shopping center')

# GET argricultural PROPERTIES
# get farm
@router.get('/argricultural/farm')
def get_farm():
   TFIDF('farm')

# get orchards
@router.get('/argricultural/orchards')
def get_orchards():
   TFIDF('orchards')

#  GET LAND
# get orchards
@router.get('/land')
def get_land():
   TFIDF('land')



# MARKET PLACE
# chance,cheap,favorite city for user,user location
# first section
@router.get('/first_section')
def get_first_section():
   TFIDF('cheap chance')

# chance,cheap,favorite city for user,user location
# second section
@router.get('/second_section')
def get_second_section():
   TFIDF('cheap villa')

# chance,cheap,favorite city for user,user location
# third section
@router.get('/third_section')
def get_third_section():
   TFIDF('factory')

# fourth section
# land
@router.get('/fourth_section')
def get_fourth_section():
   TFIDF('land')

