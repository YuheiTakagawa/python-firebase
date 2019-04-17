import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate(os.environ['FIREBASE_AUTH_KEY'])
firebase_admin.initialize_app(cred)

db = firestore.client()
docs = db.collection('messages').where('name', '==', "aaaa").get()
for doc in docs:
    print(doc.to_dict()['text'])
