import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class App(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.wm_title("where is student")  
        #self.root.wm_iconbitmap("@icon2.xbm")   
        self.label = tk.Label(self.root, text="Set ")
        self.label.pack()
        self.enr = tk.StringVar()
        self.hashtable=[[],] * 10
        tk.Entry(self.root, textvariable=self.enr).pack()

        self.buttontext = tk.StringVar()
        self.buttontext.set("Calculate")
        tk.Button(self.root,
                  textvariable=self.buttontext,
                  command=self.clicked1).pack()
    def hashFunction(capacity,key):
        sum=0
        while(key>0):
            sum+=key%1000
            key=key//1000
        return sum % capacity
    def insertData(self,key, data):
        index = self.hashFunction(10,key)
        self.hashTable[index] = [key, data]
        return

    def checkhash(self,n):
        i=self.hashFunction(n,10)
        if self.hashTable[i][1]==0:
            return "CHECKED-OUT"
        else:
            return "CHECKED-IN"

        text_display = checkhash(self.enr)
        self.label = tk.Label(self.root, text=text_display)
        self.label.pack()
        self.root.mainloop()

    def clicked1(self):
        enr = self.enr.get()
        self.label.configure(text=enr)

    def button_click(self, e):
        pass
App.insertData(0,12301032021,0)
App.insertData(0,43201022022,1)
App.insertData(0,21301022020,0)
App()