students={}
student={'민영':1,'연재':2,'기태':3,'명은':4,'성일':5,'연수':6,'재일':7,'도현':8,'가미':9,'규환':10,'성빈':11,'시형':12,'의용':13,'송화':14,
          '범규':15,'보라':16,'소윤':17,'여름':18,'지혜':19,'현도':20,'성경':21,'영효':22,'홍선':23,'은희':24,'연우':25,'철우':26,'민석':27,'지혁':28}
i=0
m=0
num=[]
key=0
for i in range(0,3):
    key=i+1
    students[key]=input()

for j,k in students.items():
    print("{}학생의 가입순서={},출석변호:%d".format(k,j) %(student[k]))
    m+=1