import firebase_admin
from firebase_admin import credentials, firestore


cred = credentials.Certificate("./to-do-635cd-firebase-adminsdk-c24ws-e424a54dda.json") 
default_app = firebase_admin.initialize_app(cred)

db = firestore.client()


def get_users():
    return db.collection('users').get()


def get_user(user_id):
    return db.collection('users').document(user_id).get()


def get_todos(user_id):
    return db.collection('users')\
        .document(user_id)\
        .collection('todos').get()