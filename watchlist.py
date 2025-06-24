mywatchlist=[]

while True:
    
      print("Movie watchlist items")
      print("1.Add movie")
      print("2.view movies")
      print("3.remove movies")
      print("4.exit")
      
      choice=input("enter your choice:")
       
      if choice == '1' :
         movie=input("Enter a movie name.")        
         mywatchlist.append(movie)
         print(f"{movie} is added to your watchlist.") 

      elif choice == '2':
          if not mywatchlist:
              print("your watchlist is empty") 
          else:
              print("your watchlist:")
              for i,movie in  enumerate(mywatchlist,1):
                print(f"{i}.{movie}")
                
      elif choice =='3':
          remove_movie=input("Enter a movie name to remove.")
          if remove_movie in mywatchlist: 
              mywatchlist.remove(remove_movie)
              print(f"your '{remove_movie}' removed successfully.")   
          else:
              print("movie is not found in watchlist.")   
              
      elif  choice =='4':  
          print("exit") 
          break  
          
      else:
          print("invalid choice")              