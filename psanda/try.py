# import pandas as pd



# data={'name':['ram','sita','hari'],
# "age":[23,34,32],
# 'city':['kathmandu','bhaktapur','laitpur']}
# df=pd.DataFrame(data)
# df.to_csv('clean_data_csv')
# print(df)


# import csv
# data1=[['name','age','add'],
# ['nitin','22','ktm']]
# data2=[['name','age','add'],
# ['subodh','22','pokhara']]
# data=data1+data2
# with open('clean_data_csv','a')as file:
#     x=csv.writer(file)
#     x.writerows(data)


# import csv
# add_data=[]

# with open('clean_data_csv','r')as file:

#     reader=csv.DictReader(file)
#     for data in reader:
#         add_data.append(data)
#     print(add_data)


import csv
li={}
n=int(input("enter the number if list = "))
for i in range(1,n+1):
    name=input("enter the name= ")
    age=input("enter the age= ")
    address=input("enter the address= ")
    data={'name':name,'age':age,'address':address}
    li[i]=data
print(li)
with open('clean_data_csv','a')as file:
    x=csv.writer(file)
    x.writerows(data)