import tkinter as tk 
import pandas as pd
import xlrd
import mysql.connector
import sqlite3 

#Note the program keep bringing up all of the screens on play, not sure how to not make that happen
#Having trouble adding the movies that were searched into the list
#Having trouble trying to have the code search for similar movies, as well as hold the one that is selectced as maybe

 #Creates the open widget frame for the home screen

#The Class for the program
class Moviechecker(tk.Frame):
   def __init__(self, parent):
       tk.Frame.__init__(self, parent)
       #The functions that are all being initilized and called
       self.parent = parent
       self.home()
       #self.el()
       #self.sea_rc()
       #self.sea_b()
       #self.data_base()-Commented out since were done making the database
       #self.submit()
  
       
    

    #Commented out because this was function was being used to make the database and is kept if we need to make anymore extra adjustments
   #def data_base(self):
        
    #   self.comn = sqlite3.connect("Movie_Log.db")
     #  self.root = tk.Tk()
      # self.root.geometry("400x400")
       #self.root.title("dsds")
       #self.c = self.comn.cursor()
      
      #Making a database table for the movie logs

       #self.c.execute(""" CREATE TABLE movies (
        #   TOM_ACT text, 
        #   Name_Movie text, 
        #   Actors text,
        #   Actor_2 text,
        #   Actor_3 text,
        #   Actor_4 text,
        #   Came_out integer, 
        #   Rate_S integer,
        #   Director text
        # )""")
      
       #self.TOM_ACT = tk.Entry(self.root, width = 50)
       #self.TOM_ACT.grid(row=0, column=3, padx=20)

       #self.Name_Movie = tk.Entry(self.root, width = 50)
       #self.Name_Movie.grid(row= 1, column=3)

       #self.Actors = tk.Entry(self.root, width = 50)
       #self.Actors.grid(row = 2, column = 3)

       #self.Actor_2 = tk.Entry(self.root, width = 50)
       #self.Actor_2.grid(row = 3, column=3)

       #self.Actor_3 = tk.Entry(self.root, width = 50)
       #self.Actor_3.grid(row=4, column = 3)

       #self.Actor_4 = tk.Entry(self.root, width = 50)
       #self.Actor_4.grid(row = 5, column = 3)

       #self.Came_out = tk.Entry(self.root, width = 50)
       #self.Came_out.grid(row = 6, column = 3)

       #self.Rate_S = tk.Entry(self.root, width = 50)
       #self.Rate_S.grid(row = 7, column = 3)

       #self.Director = tk.Entry(self.root, width = 50)
       #self.Director.grid(row = 8, column = 3)
       #create text box lables

       #self.TOM_ACT_label= tk.Label(self.root, text ="The name of the genre")
       #self.TOM_ACT_label.grid(row = 0, column = 1)

       #self.Name_Movie_label= tk.Label(self.root, text ="The name of the Move Title")
       #self.Name_Movie_label.grid(row = 1, column = 1)

       #self.Actors_label= tk.Label(self.root, text ="The name of the First Actor")
       #self.Actors_label.grid(row = 2, column = 1)

       #self.Actors_2_label= tk.Label(self.root, text ="The name of the Second Actor")
       #self.Actors_2_label.grid(row = 3, column=1)

       #self.Actors_3_label= tk.Label(self.root, text ="The name of the Third Actor")
       #self.Actors_3_label.grid( row = 4, column =1)

       #self.Actors_4_label= tk.Label(self.root, text ="The name of the Fourth Actor")
       #self.Actors_4_label.grid(row = 5, column = 1)

       #self.Came_out_label= tk.Label(self.root, text ="The time when the movie came out")
       #self.Came_out_label.grid(row = 6, column = 1)

       #self.Rate_S_label = tk.Label (self.root, text ="The is the rating of the movie")
       #self.Rate_S_label.grid(row = 7, column= 1)

       #self.Director_label = tk.Label (self.root, text ="This is the Director of the Movie")
       #self.Director_label.grid(row = 8, column = 1)
       
       
       #Making the submit button for the code
       #self.submit_btn = tk.Button(self.root, text= "Add", command = self.submit)
       #self.submit_btn.grid(row =9, column = 3)
       
      
      #Comit changes
       #self.comn.commit()


       #Close connection
       #self.comn.close()
    
    #f"SELECT {dropdownselection} FROM table_name"

    
    #Home function and the first window that should appear
   def home(self):
      
       self.parent = tk.Tk()
       #The size of the window
       self.parent.geometry("400x400")
       #The title of the window 
       self.parent.title("Movie checker")

           
    
       
       #Button for the list of movies that are saved
       self.list_cus_se=tk.Button(self.parent,text="List", command=self.el)
       self.list_cus_se.grid()
       
       #Button for the search function of the movies
       self.search_mov = tk.Button(self.parent, text="Search", command=self.sea_rc)
       self.search_mov.grid()
       #Exit button to leave the progra,
       self.exi_button = tk.Button(self.parent, text="Exit", command = self.parent.quit)
       self.exi_button.grid()
       
       #self.ad_base = tk.Button(self.parent, text = "Add To Data", command = self.data_base)
       #self.ad_base.grid()
       
       
      
       
   #Uneeded code for now, but was used for inserting the values of the database table 
   def submit(self):
       
       
       self.comn = sqlite3.connect("movie_log.db")

       self.c = self.comn.cursor()
    
      # self.c.execute("INSERT INTO movies VALUES (:TOM_ACT, :Name_Movie, :Actors, :Actor_2, :Actor_3, :Actor_4, :Came_out, :Rate_S, :Director)",
                     # {
       #                   'TOM_ACT': self.TOM_ACT.get(),
       #                   'Name_Movie': self.Name_Movie.get(),
       #                   'Actors': self.Actors.get(),
       #                   'Actor_2': self.Actor_2.get(),
       #                   'Actor_3': self.Actor_3.get(),
       #                   'Actor_4': self.Actor_4.get(),
       #                   'Came_out': self.Came_out.get(),
       #                   'Rate_S': self.Rate_S.get(),
       #                   'Director': self.Director.get()
       #                   
       #                   })
    
    
       #Comit changes
       #self.comn.commit()


       #Close connection
       #self.comn.close()
    
       #Clear text boxes
       #self.TOM_ACT.delete(0, "end")
       #self.Name_Movie.delete(0, "end")
       #self.Actors.delete(0, "end")
       #self.Actor_2.delete(0, "end")
       #self.Actor_3.delete(0, "end")
       #self.Actor_4.delete(0, "end")
       #self.Came_out.delete(0, "end")
       #self.Rate_S.delete(0, "end")
       #self.Director.delete(0, "end")

  
   def sea_rc(self):
       self.search_ad = tk.Tk() 
       #Size of the window
       self.search_ad.geometry("400x400")
       #Title of the Window
       self.search_ad.title("Movie checker")
  
       #The database of the movie and where the logs are kept
       self.comn = sqlite3.connect("Movie_Log.db")
       #The function that searches through the database
       
    
       #Search box input field
       self.search_box = tk.Entry(self.search_ad)
       self.search_box.grid(row= 0, column=1, padx=10, pady=10)
       #The labeling the button search
       self.search_box_label = tk.Label (self.search_ad, text ="Search")
       self.search_box_label.grid(row=0, column=0, padx=10, pady=10)
    
       #The search button which we place it on the screen using grid
       self.searc_but = tk.Button(self.search_ad, text = "Searching", command = self.sea_b)
       self.searc_but.grid(row = 1, column=0, padx=10)
  
       self.sea_list = tk.Listbox(self.search_ad)
       self.sea_list.grid()
    
       #Comit changes
       self.comn.commit()
       #Close the database
       self.comn.close()
    
   def sea_b (self):
        #opening up the databse
        self.comn = sqlite3.connect("Movie_Log.db")
        #Make cursor
        self.c = self.comn.cursor()
        #Selecting and fetching the code from the databse
        self.result = self.c.execute("SELECT *, oid FROM movies WHERE TOM_ACT = 'Action'")
        self.results = self.result.fetchone()
        
        self.searc_label = tk.Label(self.search_ad, text = self.results)
        self.searc_label.grid(row = 8, column= 8, columnspan = 2)
        
           #Inserting it into the listbox
        self.sea_list.insert("0", self.results)
     
           
           #Commit to the database
        self.comn.commit()
    
           #Close connection
        self.comn.close()    
       
   def el(self):
       self.list_cus = tk.Tk() 
       self.list_cus.geometry("500x500")
       self.list_cus.title("Movie checker")
       self.comn = sqlite3.connect("movie_log.db")
       
       def de_lis(self):
           #Opening the databse
           self.comn = sqlite3.connect("Movie_Log.db")
            #Make cursor
           self.c = self.comn.cursor()
           #selecting from the database and fetching all of the ones that were save
           self.c.execute("SELECT *, oid FROM movies")
           self.records = self.c.fetchall()
           #print(records)

           #Loop through result
           #To fetch all of the records that were saved
           self.print_records = ''
           for self.record in self.records[0]:
               self.print_records +=str(self.record) + "\n"
        
           self.list_Fav_label =tk.Label(self.list_cus, text = self.print_records)
           self.list_Fav_label.grid()
        
           self.lis_box = tk.Listbox(self.list_cus)
           self.lis_box.grid()
          #inserting the records into the listbox
           self.lis_box.insert("0", self.print_records)


           
           self.list_faBox.delete(self.ANCHOR)
           #Commiting to the databse
           self.comn.commit ()
           
           #Closing the database
           self.comn.close()
       
       #List box for the listo favorite movies
       self.list_faBox = tk.Listbox(self.list_cus)
       self.list_faBox.grid()
       #Making the delete button
       self.list_faDe = tk.Button(self.list_cus, text ="Delete", command = de_lis)
       self.list_faDe.grid()
       #Showing the list button
       self.sho_btn = tk.Button(self.list_cus, text= "Show the list", command = de_lis)
       self.sho_btn.grid()
    
    
        #Comit changes
       self.comn.commit()


       #Close connection
       self.comn.close()
   
   
  

if __name__ == '__main__':

   root = tk.Tk()
   run = Moviechecker(root)
   root.mainloop()

        