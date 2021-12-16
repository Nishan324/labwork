for i in range (1500,2701):
    a=i%7
    b=1%5
    if a==0 and b==0:
        print(f"{i} is mutilple of 5 and 7")
    else:
        print(f"{i} is not mulyiple of 5 and 7")