while True:
    print("File Handling Operations:")
    print("1.Add a content into file")
    print("2.Read a content from file")
    print("3.Append some content into file")
    print("4.Exit")
  
    ch=input("Enter your choice:") 
    
    if ch=='1':
    #write a file
      print("kkk")
      f=open("mydata.txt","w")
      f.write("welcome to python programming")
      f.close()
    elif ch=='2':
      f=open("mydata.txt","r")
      print(f.read())
      f.close()
    elif ch=='3':
      f=open("mydata.txt","a")
      f.write("\n hello world")
      f.close()
    elif ch=='4':
        print("exiting....")
        break
    else:
        print("Invalid choice!!!!!") 
           
