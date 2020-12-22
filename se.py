import tkinter as tk
import pandas as pd
import sqlite3
from tkinter import ttk

#Assignment: HW 3
#   Name: Andre Puddie, Simon Irwin, Domingo Esparza
#   INST 326 :  Prof Cruz
#   Due Date: 12/21/2020
# How to run the Code
#Open it up in Github Desktop
#Once it's up, clone the file
#Press the Respository Button at the top
#Press Open in Visiual Studios
#Then once it's open in Visiual Studio
#Make Sure everything has been imported
#Before then running with the play button or from the terminal 

class Moviechecker(tk.Frame):
    """ This classes holds the database, search function, list function for the Moviechcker
    
    
    Attributes:
        list_fa (list of favorite): A list that contains and adds the search results to the favorite window
        
        may_lis (list of maybe): A list that contains and adds the search result to the maybe window

        home (method): The method that will initilize the home window
    
    """
    
    def __init__(self, parent):
        
     #    tk.Frame.__init__(self, parent)
        # The functions that are all being initilized and called
        # self.parent = parent
        self.home()
        # self.el()
        # self.sea_rc()
        # self.sea_b()
     #    self.data_base()  # -Commented out since were done making the database
        # self.submit()
        self.list_fa = []
        self.may_lis = []

     # Commented out because this was function was being used to make the database and is kept if we need to make anymore extra adjustments

    def data_base(self):
        """ This method will hold the values of the database
        
        Args:
            TOM_ACT (str): Entering the genere value for the Movie
            Name_Movie (str): Entering the name of the Movie
            
            Actors(str): Entering the first Actors of the Movie
            
            Actor_2 (str): Entering the second Actors of the Movie
            
            Actor_3 (str): Entering the third Actors of the Movie
           
            Actor_4 (str): Entering the fourth Actors of the Movie
            
            Came_out (int): Entering the date of when the Movie came out
            
            Rate_S (int): Entering the rating of the Movie
            
            Director (str): Entering the name of the Director of the Movie
            
            submit_btn(Button): A button that will submit the values into the database
        
        """

        self.comn = sqlite3.connect("Movie_Log.db")
        self.root = tk.Tk()
        self.root.geometry("400x400")
        self.root.title("dsds")
        self.comn = self.comn.cursor()

        #   Making a database table for the movie logs

        self.comn.execute(""" CREATE TABLE movies (
        TOM_ACT text, 
        Name_Movie text, 
        Actors text,
        Actor_2 text,
        Actor_3 text,
        Actor_4 text,
        Came_out integer, 
        Rate_S integer,
        Director text
    )""")

        self.TOM_ACT = tk.Entry(self.root, width=50)
        self.TOM_ACT.grid(row=0, column=3, padx=20)

        self.Name_Movie = tk.Entry(self.root, width=50)
        self.Name_Movie.grid(row=1, column=3)

        self.Actors = tk.Entry(self.root, width=50)
        self.Actors.grid(row=2, column=3)

        self.Actor_2 = tk.Entry(self.root, width=50)
        self.Actor_2.grid(row=3, column=3)

        self.Actor_3 = tk.Entry(self.root, width=50)
        self.Actor_3.grid(row=4, column=3)

        self.Actor_4 = tk.Entry(self.root, width=50)
        self.Actor_4.grid(row=5, column=3)

        self.Came_out = tk.Entry(self.root, width=50)
        self.Came_out.grid(row=6, column=3)

        self.Rate_S = tk.Entry(self.root, width=50)
        self.Rate_S.grid(row=7, column=3)

        self.Director = tk.Entry(self.root, width=50)
        self.Director.grid(row=8, column=3)
        # create text box lables

        self.TOM_ACT_label = tk.Label(self.root, text="The name of the genre")
        self.TOM_ACT_label.grid(row=0, column=1)

        self.Name_Movie_label = tk.Label(
            self.root, text="The name of the Move Title")
        self.Name_Movie_label.grid(row=1, column=1)

        self.Actors_label = tk.Label(
            self.root, text="The name of the First Actor")
        self.Actors_label.grid(row=2, column=1)

        self.Actors_2_label = tk.Label(
            self.root, text="The name of the Second Actor")
        self.Actors_2_label.grid(row=3, column=1)

        self.Actors_3_label = tk.Label(
            self.root, text="The name of the Third Actor")
        self.Actors_3_label.grid(row=4, column=1)

        self.Actors_4_label = tk.Label(
            self.root, text="The name of the Fourth Actor")
        self.Actors_4_label.grid(row=5, column=1)

        self.Came_out_label = tk.Label(
            self.root, text="The time when the movie came out")
        self.Came_out_label.grid(row=6, column=1)

        self.Rate_S_label = tk.Label(
            self.root, text="The is the rating of the movie")
        self.Rate_S_label.grid(row=7, column=1)

        self.Director_label = tk.Label(
            self.root, text="This is the Director of the Movie")
        self.Director_label.grid(row=8, column=1)

        # Making the submit button for the code
        self.submit_btn = tk.Button(self.root, text="Add", command=self.submit)
        self.submit_btn.grid(row=9, column=3)

        # Comit changes
        self.comn.commit()

        # Close connection
        self.comn.close()

        # f"SELECT {dropdownselection} FROM table_name"

        # Home function and the first window that should appear

    def home(self):
        
        """This method is the home window
            
        Args:
            
            tit_sc (str): represent the title label of the program
            
            list_cus_se (button): represent the button for the Favorite List
            
            search_mov (button): represent the button for the search function
            
            exi_button (button): represent the exit button to leave the program
            
            
        """         

        self.parent = tk.Tk()
        # The size of the window
        self.parent.geometry("600x600")
        # The title of the window
        self.parent.title("Movie checker")

        self.tit_sc = tk.Label(self.parent, width=40, text="My Project")
        self.tit_sc.grid(row=0, column=0)

        # Button for the list of movies that are saved
        self.list_cus_se = tk.Button(
            self.parent, text="Favorite List", width=25, pady=10, command=self.el)
        self.list_cus_se.grid(row=1, column=0)

        # Button for the search function of the movies
        self.search_mov = tk.Button(
            self.parent, text="Search", width=25, pady=10, command=self.sea_rc)
        self.search_mov.grid(row=2, column=0)
        # Exit button to leave the progra,
        self.exi_button = tk.Button(
            self.parent, text="Exit", width=25, pady=10, command=self.parent.quit)
        self.exi_button.grid(row=3, column=0)

        # self.ad_base = tk.Button(self.parent, text = "Add To Data", command = self.data_base)
        # self.ad_base.grid()

    # Uneeded code for now, but was used for inserting the values of the database table

    def submit(self):

        self.comn = sqlite3.connect("Movie_Log.db")

        self.comn = self.comn.cursor()

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

        # Comit changes
        # self.comn.commit()

        # Close connection
        # self.comn.close()

        # Clear text boxes
        # self.TOM_ACT.delete(0, "end")
        # self.Name_Movie.delete(0, "end")
        # self.Actors.delete(0, "end")
        # self.Actor_2.delete(0, "end")
        # self.Actor_3.delete(0, "end")
        # self.Actor_4.delete(0, "end")
        # self.Came_out.delete(0, "end")
        # self.Rate_S.delete(0, "end")
        # self.Director.delete(0, "end")

    def sea_rc(self):
        """ The search method for the program
        
        Args:
            search_box (entry): represent the entry box of the search program

            searc_but (button): represent the button for the search program
            
            submit_btn (button): represent the add button for the search program
            
            subt_btn (button): represent the maybe button for the search program
            
            back (button): represent the back button for the search program
            
            drop (dropdown-box): repsents the dropdown box for the search program
        
        """
        self.search_ad = tk.Tk()
        # Size of the window
        self.search_ad.geometry("600x600")
        # Title of the Window
        self.search_ad.title("Movie checker")

        # The database of the movie and where the logs are kept
        self.comn = sqlite3.connect("Movie_Log.db")
        # The function that searches through the database

        # Search box input field
        self.search_box = tk.Entry(self.search_ad)
        self.search_box.grid(row=2, column=1, padx=10, pady=10)
        # The labeling the button search
        self.search_box_label = tk.Label(
            self.search_ad, text="Type name of movie")
        self.search_box_label.grid(row=2, column=0, padx=5, pady=10)

        # The search button which we place it on the screen using grid
        self.searc_but = tk.Button(
            self.search_ad, text="Search", command=self.sea_b)
        self.searc_but.grid(row=0, column=1, padx=10)
        #The add button to add the selected search result to the favorite list
        self.submit_btn = tk.Button(
            self.search_ad, text="Add", command=self.add_s)
        self.submit_btn.grid(row=2, column=2)
        # The may button to add the selected search result to the Maybe List
        self.subt_btn = tk.Button(
            self.search_ad, text="Maybe", command=self.maybe_s)
        self.subt_btn.grid(row=3, column=2)
        #The listbox to hold the all of the search results
        self.sea_list = tk.Listbox(self.search_ad, width=50, height=20)
        self.sea_list.grid(row=1, columnspan=3)
        #The drop down tab for all of the values in the drop-down list
        self.drop = tk.ttk.Combobox(self.search_ad, value=[
                                    "Search by genre...", "Action", "Romance", "Horror"])
        self.drop.current(0)
        self.drop.grid(row=0, column=0)
        #The back button to return back to the home page
        self.back = tk.Button(self.search_ad, text="Back", command=self.search_ad.destroy)
        self.back.grid(row=4, columnspan=4)

        # Close the database
        self.comn.close()

    def sea_b(self):
        """ The search method results
        
        Args:

            selected(str): The selected value of the dropdown box
            
            sea_list (str): Represent inserting the value into the listbox
        
            test (str): Represent the label of the Dropdown box text
        
        """
        # opening up the databse
        self.comn = sqlite3.connect("Movie_Log.db")

        # Selecting and fetching the code from the databse
        #Selecting it from the drop down box
        self.selected = self.drop.get()
        if self.selected == "Search by genre...":
            self.test = tk.Label(
                self.search_ad, text="Select some option first...")
            self.test.grid(row=3, column=0)
        if self.selected == "Action":
            self.result = self.comn.execute(
                "SELECT *, oid FROM movies WHERE TOM_ACT = 'Action'")
            self.sea_list.delete(0, tk.END)
            for row in self.result:
                self.sea_list.insert(0, row[1])
            self.test = tk.Label(self.search_ad, text="Type in a Action Movie")
            self.test.grid(row=3, column=0)
        if self.selected == "Horror":
            self.result = self.comn.execute(
                "SELECT *, oid FROM movies WHERE TOM_ACT = 'Horror'")
            self.sea_list.delete(0, tk.END)
            for row in self.result:
                self.sea_list.insert(0, row[1])
            self.test = tk.Label(self.search_ad, text="Type in a Horror movie")
            self.test.grid(row=3, column=0)
        if self.selected == "Romance":
            self.result = self.comn.execute(
                "SELECT *, oid FROM movies WHERE TOM_ACT = 'Romance'")
            self.sea_list.delete(0, tk.END)
            for row in self.result:
                self.sea_list.insert(0, row[1])
            self.test = tk.Label(
                self.search_ad, text="Type in a Romance Movie")
            self.test.grid(row=3, column=0)

        # Close connection
        self.comn.close()

    def add_s(self):
        # opening up the databse
        
        """ The method to add the results to the Favorite Drop box
        
        Args:
            search_box(str): representing the function of getting the result
        
        """

        self.con = sqlite3.connect('Movie_Log.db')
        #Getting the results out of the search box
        name = self.search_box.get()
        name = name.replace("'", "''")

        res = self.con.execute(
            "SELECT *, oid FROM movies WHERE Name_Movie like '{}'".format(name))
        #Fetching one of the results
        res = res.fetchone()
        #Printing it and inserting it into the Favorite List, listbox
        if res:
            print(res)
            self.list_fa.insert(0, res)
        # self.list_fa.insert(self.results)

        # Commit to the database
    def maybe_s(self):
        """ The method to add the results to the Maybe List
        
        Args:
            search_box(str): representing the function of getting the result
            
            lit_myBox(Listbox): represent the Listbox of the Maybe function
            
                    
        """
        
        self.list_may = tk.Tk()
        
        self.con = sqlite3.connect('Movie_Log.db')

        #Grabbing the searh results out of the search bar        
        name = self.search_box.get()
        name = name.replace("'", "''")

        may = self.con.execute(
            "SELECT *, oid FROM movies WHERE Name_Movie like '{}'".format(name))
        #Fetching one of the results from the listbox
        may = may.fetchone()
        if may:
            print(may)
            self.may_lis.insert(0, may)
        #Making a listbox
        self.lit_myBox = tk.Listbox(self.list_may, width=50, height=20)
        self.lit_myBox.grid(column=1)    
        #inserting the results into the Listbox
        for row in self.may_lis:
            self.lit_myBox.insert(0, ', '.join(
                [row[1], row[0], str(row[6]), str(row[7]), row[8]]))
        
        
        
    def el(self):
        """ This method is for the Favorie List function
        
        Args:
            list_faBox(Listbox): Represent the listbox for the Favorite List

            list_faDe (button): Represent the back button
        
        """
        self.list_cus = tk.Tk()
        #    self.list_cus.geometry("600x600")
        self.list_cus.title("Movie checker")
        #The listbox for the Favorite List
        self.list_faBox = tk.Listbox(self.list_cus, width=50, height=20)
        self.list_faBox.grid(column=1)

        for row in self.list_fa:
            self.list_faBox.insert(0, ', '.join(
                [row[1], row[0], str(row[6]), str(row[7]), row[8]]))
        #The back Button
        self.list_faDe = tk.Button(
            self.list_cus, text="Back", command=self.list_cus.destroy)
        self.list_faDe.grid(row=2, column=1)
        
        self.lis_k = tk.Button(
            self.list_cus, text = "Delete", command = self.list_cus.delete)
        self.lis_k.grid(row=3, column=1)    


if __name__ == '__main__':

    root = tk.Tk()
    Moviechecker(root)
    root.mainloop()
