from sklearn.feature_extraction.text import TfidfVectorizer
from fastapi import Depends, HTTPException, status, APIRouter, Response
from database import Property
from sklearn.metrics.pairwise import cosine_similarity
import json
from bson import json_util
import numpy as np
import pandas as pd 



router = APIRouter()

# TFIDF Search Engine
@router.get('/{term}')
def get_posts(term: str):
  items = {}
  for item in Property.find():
    items[item['_id']] = item['advertising']
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(items.values())
    query = "villa"
    query_vec = vectorizer.transform([query])
    similarity_scores = cosine_similarity(tfidf_matrix, query_vec)
    item_scores = {}
    for i, item_id in enumerate(items.keys()):
     tf_idf_score = 0
    for term in query.split():
        if term in vectorizer.vocabulary_:
            tf_idf_score += tfidf_matrix[i, vectorizer.vocabulary_[term]]
    item_scores[item_id] = tf_idf_score * similarity_scores[i]

    sorted_items = sorted(item_scores.items(), key=lambda x: x[1], reverse=True)
    relevant_items = [Property.find_one({'_id': item_id}) for item_id, score in sorted_items if score > 0]
    return json.loads(json_util.dumps(relevant_items))
