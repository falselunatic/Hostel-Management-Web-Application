from tkinter import*
from PIL import Image, ImageTk #pip install pillow
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("hostel management system")
        self.root.geometry("1295x590+230+190")

        #====================variables=================
        self.var_contact = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomavailable = StringVar()
        self.var_meal = StringVar()
        self.var_total = StringVar()

        lbl_title=Label(self.root,text="ROOMBOOKING DETAILS",font=("arial",19,"bold"),bg="purple",fg="yellow",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)
#***label**
        img2=Image.open(r"C:\Users\DELL\OneDrive\Desktop\ninja\g1.jfif")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)
        #**labelframe***
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking Details",font=("arial",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)
         #**labels and enrties**
        # student contact 
        lbl_stud_contact=Label(labelframeleft,text="student Contact",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_stud_contact.grid(row=0,column=0,sticky=W)

        entry_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact,font=("arial",13,"bold"),width=20)
        entry_contact.grid(row=0,column=1,sticky=W)

        #fetch data buttons
        

        btnFetchData=Button(labelframeleft,command=self.fetch_data,text="Fetch Data",font=("arial",9,"bold"),bg="black",fg="gold",width=9)
        btnFetchData.place(x=347,y=4)

        
        
        # Room Type

        label_RoomType=Label(labelframeleft, font=("arial", 12, "bold"), text="Room Type:", padx=2,pady=6) 
        label_RoomType.grid(row=3, column=0, sticky=W)

        combo_RoomType=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype, font=("arial", 12, "bold"),width=27, state="readonly") 
        combo_RoomType["value"]=("Single", "Double")
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3, column=1)

        #Available Room

        lblRoomAvailable=Label(labelframeleft, font=("arial", 12, "bold"), text="Available Room:",padx=2,pady=6)
        lblRoomAvailable.grid(row=4, column=0, sticky=W)

        txtRoomAvailable=ttk.Entry(labelframeleft,textvariable=self.var_roomavailable ,font=("arial", 13, "bold"),width=29)
        txtRoomAvailable.grid(row=4, column=1)
        #Meal

        lblMeal=Label(labelframeleft, font=("arial", 12, "bold"), text="Meal:",padx=2,pady=6)
        lblMeal.grid(row=5, column=0, sticky=W)

        txtMeal=ttk.Entry (labelframeleft,textvariable=self.var_meal, font=("arial",13, "bold"),width=29) 
        txtMeal.grid(row=5, column=1)

        #Total Cost

        lbltotal=Label(labelframeleft, font=("arial",12,"bold"), text="total cost:",padx=2,pady=6)
        lbltotal.grid(row=6, column=0, sticky=W)

        txttotal=ttk.Entry (labelframeleft,textvariable=self.var_total, font=("arial", 13, "bold"),width=29)
        txttotal.grid(row=6, column=1)
        #*****bill buttons****
        btnBill=Button(labelframeleft,text="Bill",font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnBill.grid(row=10,column=0,padx=1,sticky=W)

        #*******btns*********
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnadd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnadd.grid(row=0,column=0,padx=1)

        btnupdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnupdate.grid(row=0,column=1,padx=1)

        btndelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btndelete.grid(row=0,column=2,padx=1)

        btnreset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnreset.grid(row=0,column=3,padx=1)
        #right side image
        img3=Image.open(r"C:\Users\DELL\OneDrive\Desktop\ninja\g2.jfif")
        img3=img3.resize((400,300),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lblimg.place(x=760,y=55,width=400,height=300)

        #**********table frame**************
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="view details and search system",font=("arial",12,"bold"),padx=2)
        table_frame.place(x=435,y=200,width=860,height=260)

        lblsearchby=Label(table_frame,text="search by",font=("arial",12,"bold"),bg="red",fg="white")
        lblsearchby.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var = StringVar()
        combo_search=ttk.Combobox(table_frame,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_search["value"]=("Available Room","Room Type")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        self.txt_search = StringVar()
        textsearch=ttk.Entry(table_frame,textvariable=self.txt_search,width=24,font=("arial",13,"bold"))
        textsearch.grid(row=0,column=2,padx=2)

        btnsearch=Button(table_frame,text="Search",font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnsearch.grid(row=0,column=3,padx=1)

        btnshowall=Button(table_frame,text="Show All",font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnshowall.grid(row=0,column=4,padx=1)

        #******show data table*******
        details_table=Frame(table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=180)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        self.room_table=ttk.Treeview(details_table,column=("contact","roomtype","available","meal","totalcost"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact",text="Contact")
        self.room_table.heading("roomtype",text="Room Type")
        self.room_table.heading("available",text="Room number")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("totalcost",text="Total cost")
        self.room_table["show"]="headings"
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cuersor)
        self.fetch_data()

        self.room_table.column("contact",width = 100)
        self.room_table.column("roomtype",width = 100)
        self.room_table.column("available",width = 100)
        self.room_table.column("meal",width = 100)
        self.room_table.column("totalcost",width = 100)
        self.room_table.pack(fill=BOTH,expand=1)

    # ============All Data Fetch====================

    def Fetch_room(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter available room no", parent=self.root)
        else:
            conn = mysql.connector.connect(host = "localhost",username = "root",password = "Koya2003@",database = "management")
            my_cursor = conn.cursor()
            query=("select * from room where roomavailable=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()


            if row==None:
                messagebox.showerror("Error","This room is not available",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=450,y=55,width=300,height=180)

                lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
                lbl.place(x=0,y=0)

                lbl=label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)

                # ================contact=======================
                conn = mysql.connector.connect(host = "localhost",username = "root",password = "Koya2003@",database = "management")
                my_cursor = conn.cursor()
                query=("select contact from room where roomavailable=%s")
                value=(self.var_roomavaiable.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()


                lblcontact=Label(showDataframe,text="contact:",font=("arial",12,"bold"))
                lbl.place(x=0,y=30)

                lbl2=label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=30)

                # ===============roomtype=====================
                conn = mysql.connector.connect(host = "localhost",username = "root",password = "Koya2003@",database = "management")
                my_cursor = conn.cursor()
                query=("select roomtype from room where roomavailable=%s")
                value=(self.var_roomavaiable.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()


                lblroomtype=Label(showDataframe,text="RoomType:",font=("arial",12,"bold"))
                lbl.place(x=0,y=60)

                lbl2=label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=60)

                # ===========meal===================
                conn = mysql.connector.connect(host = "localhost",username = "root",password = "Koya2003@",database = "management")
                my_cursor = conn.cursor()
                query=("select meal from room where roomavailable=%s")
                value=(self.var_roomavaiable.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()


                lblmeal=Label(showDataframe,text="Meal:",font=("arial",12,"bold"))
                lbl.place(x=0,y=90)

                lbl2=label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=90)

                # ===============totalcost===============
                conn = mysql.connector.connect(host = "localhost",username = "root",password = "Koya2003@",database = "management")
                my_cursor = conn.cursor()
                query=("select total from room where roomavailable=%s")
                value=(self.var_roomavaiable.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()


                lbltotal=Label(showDataframe,text="TotalCost:",font=("arial",12,"bold"))
                lbl.place(x=0,y=120)

                lbl2=label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=120)
    

    #add data
    def add_data(self):
            if self.var_contact.get() == "" or self.var_roomavailable.get() == "":
                messagebox.showerror("Error","All fields are required")
            else:
                try:
                    conn = mysql.connector.connect(host = "localhost",username = "root",password = "Koya2003@",database = "management")
                    my_cursor = conn.cursor()
                    my_cursor.execute("insert into room values(%s,%s,%s,%s,%s)",(
                    self.var_contact.get(),
                    self.var_roomtype.get(),
                    self.var_roomavailable.get(),
                    self.var_meal.get(),
                    self.var_total.get()
                    ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success","Room booked",parent = self.root)
                except Exception as es:
                    messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent = self.root)

    # fetch data
    def fetch_data(self):
                conn = mysql.connector.connect(host = "localhost",username = "root",password = "Koya2003@",database = "management")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from room")
                rows = my_cursor.fetchall()
                if len(rows)!=0:
                    self.room_table.delete(*self.room_table.get_children())
                    for i in rows:
                        self.room_table.insert("",END,values = i)
                    conn.commit()
                conn.close()

    # getcursor
    def get_cuersor(self,event = ""):
            cusrsor_row = self.room_table.focus()
            content = self.room_table.item(cusrsor_row)
            row = content["values"]

            
            self.var_contact.set(row[0]),
            self.var_roomtype.set(row[1]),
            self.var_roomavailable.set(row[2]),
            self.var_meal.set(row[3]),
            self.var_total.set(row[4])

     # update function
    def update(self):
         if self.var_roomavailable.get()=="":
            messagebox.showerror("Error","Please enter available room",parent = self.root)
         else:
            conn = mysql.connector.connect(host = "localhost", username = "root", password = "Koya2003@",database = "management")
            my_cursor = conn.cursor()
            my_cursor.execute("update room set contact = %s,roomtype = %s,meal = %s,totalcost = %s where available = %s",(
             self.var_contact.get(),
             self.var_roomtype.get(),
             self.var_meal.get(),
             self.var_total.get(),
             self.var_roomavailable.get()
             ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room details have been updated successfully")

    # delete function
    def mDelete(self):
         mDelete = messagebox.askyesno("Hostel Management System","Do you want to delete this booking",parent = self.root)
         if mDelete>0:
              conn = mysql.connector.connect(host = "localhost", username = "root", password = "Koya2003@",database = "management")
              my_cursor = conn.cursor()
              my_cursor.execute("delete from room where roomavailable = %s",(self.var_roomavaiable.get(),))
         else:
              if not mDelete:
                   return
         conn.commit()
         self.fetch_data()
         conn.close()

    # reset
    def reset(self):
        self.var_contact.set("")
        
        self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_meal.set("")
        
        self.var_total.set("")

    # All data fetch
    def Fetch_roomtype(self):
        if self.var_roomavaiable.get()=="":
            messagebox.showerror("Error","Please enter available room", parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Koya2003@",database="management")
            my_cursor=conn.cursor()
            query=("select roomtype from room where roomavailable=%s")
            value=(self.var_roomtype.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                message.showerror("Error","This room is not available", parent=self.root)
            else:
                conn.commit()
                conn.close()

        # address k baad last me ayega ye func

        # search system
        def search(self):
            conn = mysql.connector.connect(host = "localhost",username = "root",password = "Koya2003@",database = "management")
            my_cursor = conn.cursor()
            my_cursor.execute("Select * from room where"+str(self.search_var.get())+"LIKE'%"+str(self.txt_search.get())+"%'")
            rows = my_cursor.fetchall()
            if len(rows)!=0:
                self.room_table.delete(*self.room_table.get_children())
                for i in rows:
                    self.room_table.insert("",END,values = 1)
                conn.commit()
            conn.close()

        





























if __name__ =="__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()