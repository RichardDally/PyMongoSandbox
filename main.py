import datetime
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client['test-database']
post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

posts = db.posts
post_id = posts.insert_one(post).inserted_id

