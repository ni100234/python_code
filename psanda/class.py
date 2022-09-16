# class cal:   
# # it there is not self we can use (@srtaticmethod)

#     def hello(self):
#         x=int(input("enter for x= "))
#         y=int(input("enter for y= "))
#         z=int(input("enter for z= "))
#         a=x*y
#         b=a*z
#         print("the multiplication is= ",a)
#         print("the multiplication is= ",b)
# obj=cal()
# obj.hello()







# class cal:   

#     def area(self,x,y):

#         e=a*b
#         print("the area is ",e)
        

#     def vol(self,x,y,z):
#         f=a*b*c
#         print("the vol is ",f)
# a=int(input("enter for x= "))
# b=int(input("enter for y= "))
# c=int(input("enter for z= "))


     
# obj=cal()
# obj.area(a,b)
# obj.vol(a,b,c)


# class cal:
#     def __init__(self):
#         self.a=int(input("enter for x= "))
#         self.b=int(input("enter for y= "))
#         self.c=int(input("enter for z= "))


#     def area(self):

     
#         self.e = self.a*self.b
#         print("the area is ",self.e)
        

#     def vol(self):
#         self.f=self.a*self.b*self.c
#         print("the vol is ",self.f)





     
# obj=cal()
# obj.area()
# obj.vol()



# class info:
#     def __init__(self):
#         self.name=input("enter for x= ")
#         self.age=int(input("enter for y= "))
#         self.add=input("enter for z= ")
          

#     def my_info(self):

#         print(f"my name is {self.name}. Im {self.age} old and im from {self.add}")
     
# obj=info()
# obj.my_info()



class Area():
    def __init__(self,x,y):
        self.x,self.y=x,y
    def area(self):
        a=self.x*self.y
        print("the area is ",a)
class Volume():
    def __init__(self,x,y,z):
        self.x,self.y,self.z=x,y,z
        
    def volume(self):
        vol=self.x*self.y*self.z
        print("the volume is ",vol)
l=int(input("enter the length= "))
b=int(input("emter te breath= "))
h=int(input("enter the height= "))
obj1=Area(l,b)
obj=Volume(l,b,h)
obj1.area()
obj.volume()

