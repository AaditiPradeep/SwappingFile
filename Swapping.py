def SwapFileData():
    f1 = input("Enter the directory of the file to be swapped : ")
    f2 = input("Enter the directory of file to swap with : ")

    with open(f1 , 'r') as a:
     data_a = a.read()
    with open(f2 , 'r') as b:
     data_b = b.read()
    
    with open(f1 , 'w') as a:
     a.write(data_b)
    with open(f2 , 'w') as b:
      b.write(data_a)
      
    file1 = open(f1 , 'r')
    print(file1.read())
    file2 = open(f2 , 'r')
    print(file2.read())
     
SwapFileData()
"""file1 = open(f1 , 'r')
    data_a = file1.read()
    file1.close()
        
    file2 = open(f2 , 'r')
    data_b = file2.read()
    file2.close()

    file1=open(f1 , 'w')
    file2=open(f2 , 'w')
    
    file1.write(data_b)
    file2.write(data_a)
    file1.close()
    file2.close()"""
    
    
    
