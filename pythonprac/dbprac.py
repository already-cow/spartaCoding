# pymongo 코드 요약
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# insert
# doc = {'name':'Jane','age':21}
# db.users.insert_one(doc)
#
# find
# same_ages = list(db.users.find({'age':21},{'_id':False}))
# user = db.users.find_one({'name':'bobby'},{'_id':False}) -> 하나를 찾을 때는 list X
#
# update
# db.users.update_one({'name':'bobby'},{'$set':{'age':21}})
# db.users.update_many({'age':25},{'$set':{'age':21}}) -> 한 번에 모든 데이터 변경
#
# delete
# db.users.delete_one({'name':'bobby'})