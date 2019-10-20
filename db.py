from flask_pymongo import PyMongo
import server as s

s.app.config['MONGO_DBNAME'] = 'pictest'
s.app.config['MONGO_URI'] = 'mongodb://localhost:27017/pictest'
mongo = PyMongo(s.app)
