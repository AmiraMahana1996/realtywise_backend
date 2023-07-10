from sklearn.feature_extraction.text import TfidfVectorizer
from fastapi import Depends, HTTPException, status, APIRouter, Response
from database import Property
from sklearn.metrics.pairwise import cosine_similarity
import json
from bson import json_util

router = APIRouter()

# TFIDF Search Engine
@router.get('/{term}')
def get_posts(term: str):
    Documents = Property.find()
    documents=[doc for doc in Documents]
    # create a list of all document texts
    texts = [doc["advertising"] for doc in documents]
    # create a TfidfVectorizer object and fit it to the documents
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(texts)
    print(tfidf_matrix)
    # compute the cosine similarity matrix
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)  
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

