def fileSwapper():
    fileName1 = input("ENTER THE FILE NAME : ")
    fileName2 = input("ENTER THE NAME OF THE 2nd FILE : ")
    with open(fileName1,'r') as a:
        data_1 = a.read()
    with open(fileName2,'r') as b:
        data_2 = b.read()

    with open(fileName1,'w') as a:
        a.write(data_2)
    with open(fileName2,'w') as b:
        b.write(data_1)



fileSwapper()