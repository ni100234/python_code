


# class Data:
#     def __init__(self):
#         self.name=input("enter name= ")
#         self.add=input("enter address= ")

# class Info(Data):
#         def info(self):
#             print(f"hello she is {self.name} and she is from {self.add}")
# obj=Info()
# obj.info()


# class Data:
#     def __init__(self,name,add):
#         self.name=name
#         self.add=add
       

# class Info(Data):
#         def info(self):
#             print(f"hello she is {self.name} and she is from {self.add}")


# name=input("enter name= ")
# add=input("enter address= ")
# obj=Info(name,add)
# obj.info()
        


# 

# class Data:
#     def __init__(self,add):
        
#         self.add=add
       

# class Info(Data):
#     def __init__(self,name,add):
#         self.name=name
#         Data. __init__(self,add)
        
#     def info(self):
#         print(f"hello she is {self.name} and she is from {self.add}")


# name=input("enter name= ")
# add=input("enter address= ")
# obj=Info(name,add)
# obj.info()



# 


# class age():
#     def __init__(self,age):
#         self.age=age


# class Data(age):
#     def __init__(self,name,add):
#         self.name=name
#         self.add=add
       

# class Info(Data):
#         def info(self):
#             print(f"hello she is {self.name} and she is from {self.add}")


# name=input("enter name= ")
# add=input("enter address= ")
# obj=Info(name,add)
# obj.info()






# class a():
#     def __init__(self,age):
#         self.age=age


# class Data():
#     def __init__(self,add):
        
#         self.add=add
    
       

# class Info(a,Data):
#     def __init__(self,name,age,add):
#         self.name=name
#         Data. __init__(self,add)
#         a.__init__(self,age)
        
#     def info(self):
#         print(f"hello she is {self.name}.She is {self.age} yrs old and she is from {self.add}")


# name=input("enter name= ")
# add=input("enter address= ")
# age=int(input("enter the age= "))
# obj=Info(name,age,add)
# obj.info()




# public members
# class info:
#     def __init__(self,name,age,add):
#         self.name=name
#         self.age=age
#         self.add=add
# obj=info("ram",33,"ktm")
# print(obj.name)
# print(obj.age)
# print(obj.add)


# protected members
class info:
    def __init__(self,name,age,add):
        self._name=name
        self._age=age
        self._add=add
obj=info("ram",33,"ktm")
print(obj._name)
print(obj._age)
print(obj._add)