# class info():
#     def __init__(self,name,age,address):
#         self.name=name
#         self.age=age
#         self.address=address
#     def __str__(self):
#         return self.name
# name=input("enter the name= ")
# age=int(input("enter the age= "))
# address=input("enter the address= ")
# obj =info(name,age,address)
# print(obj)
# print(str(obj))



# class total():
#     def __init__(self,a):
    
#         self.a=a
#         print("this is init method",self.a)
#     def __str__(self):
#         print("this is str method",self.a)
#         return str(self.a)
#     def __add__(self,others):
#         a=self.a+ others.a
#         print("this is add method",self.a)
#         return total(a)

# obj = total(1000)
# obj1=total(2000)
# obj2=total(3000)
# print(obj+obj1+obj2)
# type(obj+obj1+obj2)




# def add():
#         n=int(input("Enter n= "))
#         for i in range(n):
#             english=int(input("enter the score of english= "))
#             nepali=int(input("enter the score of nepali= "))
#             maths=int(input("enter the score of maths= "))
#             science=int(input("enter the score of science= "))
#             data =english+nepali+maths+science
#             per=data/4
#             print(data) 
#             print(per)
# add()    


1
2
3
4
5
6
7
8
9
10
class Dog:                
 
    def __init__(self, dogBreed,dogEyeColor): 
  
        self.breed = dogBreed   
        self.eyeColor = dogEyeColor
 
tomita = Dog("Fox Terrier","brown")
 
print("This dog is a",tomita.breed,"and his eyes are",tomita.eyeColor)
    



