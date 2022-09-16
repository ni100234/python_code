# filesyntx
# file=open('<fiolename>','<modes>')
# <operation>
# file.close()

# with open('<file name>','<modes>'):
#     <operation>


# Modes 
# r->read
# x->create
# w-write
# a-append


# try:
#    file=open('data.txt','r')
#    file.close()
# except:
#     print("f")

# with open('data.txt','r') as file:
#    x=file.read()
#    x=x.split('\n')
# #    n=int(input("enter number= "))
#    print(x[1])
#    print(type(x),x)


# with open('data.txt','a') as file:
#     file.write("\n hello my dost ko abn haru")

# print()


n=int(input("enter the quantity number= "))
s=str()
for  i in range(n):
    name=input("enter the name = ")
    price=int(input("enter the price= "))
    quantity=int(input("enter the quamtity= "))
    total=price+quantity
    s=s+f'{name},{price},{quantity},{total}\n'
    
print(s)

with open('data.csv','w') as file:
    file.write(s)
    print(s)
 

# import os
# try:
#     os.remove("dataa.txt")
# except:
#     print("the file is remove")