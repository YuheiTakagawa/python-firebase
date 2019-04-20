import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def firestore_init():
    cred = credentials.Certificate(os.environ['FIREBASE_AUTH_KEY'])
    firebase_admin.initialize_app(cred)
    return firestore.client()

