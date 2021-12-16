a=int(input("Enter the beggining number: "))
b=int(input("Enter the ending number:  "))
c=0
e=0
f=0
for i in range(a,b+1):
    c=i%2
    if c==0:
        e=e+1
    else:
       f=f+1
print("even number",e)
print("odd number",f)