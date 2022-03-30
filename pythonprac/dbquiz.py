from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# 매트릭스의 평점 찾기
q1 = db.movies.find_one({'title':'매트릭스'},{'_id':False})
target_star = q1['star']
print(target_star)

# 매트릭스와 평점이 같은 영화 제목
target_movies = list(db.movies.find({'star':target_star},{'_id':False}))
for q2 in target_movies:
    print(q2['title'])

movie = list(db.movies.find({},{'_id':False}))
for i in movie:
    if i['star'] == target_star:
        print(i['title'])

# 매트릭스의 평점 바꾸기 -> 문자열 주의
db.movies.update_one({'title':'매트릭스'},{'$set':{'star':'9.39'}})