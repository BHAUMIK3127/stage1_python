from PIL import Image

a=input("How much would you rate ur looks out of 10 ? ")
b=input("How much would you rate ur intelligence out of 10 ?")
c=input("How much would you rate ur social skills out of 10 ?")

a=int(a)
b=int(b)
c=int(c)

d = (a+b)*2 - c

print("According to the calculations you should be getting" , d , "BITCHES")
print("but you still get 0")
print("u gon stay bitchless for life ig")

im1 = Image.open("D:\\PYTHON\\variables_datatypes\\no_bitches.png")
im1.show()

