import datetime
import pprint
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.pythondb
posts = db.posts

print("posts count is = ", posts.count())

print("posts's author is Maxsu count is =",
      posts.find({
          "author": "Maxsu"
      }).count())
