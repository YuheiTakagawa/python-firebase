import fs_init

db = fs_init.firestore_init()
docs = db.collection('messages').where('name', '==', "aaaa").get()
for doc in docs:
    print(doc.to_dict()['text'])

print("================")
db.collection('messages').add({
    'name': 'aaaa',
    'text': 'oaaaa'
})

docs = db.collection('messages').where('name', '==', "aaaa").get()
for doc in docs:
    print(doc.to_dict()['text'])

