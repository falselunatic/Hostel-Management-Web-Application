from tkinter import *
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox
class DetailsRoom:

    def __init__(self,root):
        self.root=root
        self.root.title("HOSTEL MANAGEMENT SYSTEM")
        self.root.geometry("1295x550+230+220")

        #room logo and label frame ,label entry,btns
        #********************title****************************

        lbl_title=Label(self.root,text="ADD STUDENT DETAILS",font=("arial",18,"bold"),bg="purple",fg="yellow",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)
        #*****************label********************
        img2=Image.open(r"C:\Users\DELL\OneDrive\Desktop\ninja\g1.jfif")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

        #**********************labelframe*************************
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",font=("arial",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=540,height=350)
        #****************labels and enrties**********************
        # floor
        lbl_floor=Label(labelframeleft,text="Floor",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W,padx=20)

        self.var_floor=StringVar()
        entry_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor,font=("arial",13,"bold"),width=20)
        entry_floor.grid(row=0,column=1,sticky=W)
        # room no
        lbl_RoomNo=Label(labelframeleft,text="Room No.",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_RoomNo.grid(row=1,column=0,sticky=W,padx=20)

        self.var_RoomNo=StringVar()
        entry_RoomNo=ttk.Entry(labelframeleft,textvariable=self.var_RoomNo,font=("arial",13,"bold"),width=20)
        entry_RoomNo.grid(row=1,column=1,sticky=W)
        # Room Type
        lbl_RoomType=Label(labelframeleft,text="Room Type",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_RoomType.grid(row=2,column=0,sticky=W)

        self.var_RoomType=StringVar()
        entry_RoomType=ttk.Entry(labelframeleft,textvariable=self.var_RoomType,font=("arial",13,"bold"),width=20)
        entry_RoomType.grid(row=2,column=1,sticky=W)

        #******************btns**************************
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=412,height=40)

        btnadd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="purple",fg="gold",width=8)
        btnadd.grid(row=0,column=0,padx=1)

        btnupdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="purple",fg="gold",width=8)
        btnupdate.grid(row=0,column=1,padx=1)

        btndelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",12,"bold"),bg="purple",fg="gold",width=8)
        btndelete.grid(row=0,column=2,padx=1)

        btnreset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="purple",fg="gold",width=8)
        btnreset.grid(row=0,column=3,padx=1)
        #tabel frame search style
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="show room details",font=("arial",12,"bold"),padx=2)
        table_frame.place(x=600,y=55,width=600,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.room_details=ttk.Treeview(table_frame,column=("floor","RoomNo","RoomType"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.room_details.xview)
        scroll_y.config(command=self.room_details.yview)
        
        self.room_details.heading("floor",text="floor")
        self.room_details.heading("RoomNo",text="RoomNo")
        self.room_details.heading("RoomType",text="RoomType")
        
        self.room_details["show"]="headings"

        self.room_details.column("floor",width=100)
        self.room_details.column("RoomNo",width=100)
        self.room_details.column("RoomType",width=100)
        


        self.room_details.pack(fill=BOTH,expand=1)
        self.room_details.bind("<ButtonRelease-1>",self.get_cuersor)
        self.fetch_data()

    def add_data(self):
        if self.var_floor.get() == "" or self.var_RoomType.get() == "":
            messagebox.showerror("Error","All fields are required")
        else:
             try:
                conn = mysql.connector.connect(host = "localhost",username = "root",password = "Koya2003@",database = "management")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into room_details values(%s,%s,%s)",(
                self.var_floor.get(),
                self.var_RoomNo.get(),
                self.var_RoomType.get(),
                
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room has been added",parent = self.root)
             except Exception as es:
                 messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent = self.root)
    
    def fetch_data(self):
            conn = mysql.connector.connect(host = "localhost",username = "root",password = "Koya2003@",database = "management")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from room_details")
            rows = my_cursor.fetchall()
            if len(rows)!=0:
                self.room_details.delete(*self.room_details.get_children())
                for i in rows:
                    self.room_details.insert("",END,values = i)
                conn.commit()
            conn.close()
    
    def get_cuersor(self,event = ""):
        cusrsor_row = self.room_details.focus()
        content = self.room_details.item(cusrsor_row)
        row = content["values"]

        self.var_floor.set(row[0])
        self.var_RoomNo.set(row[1])
        self.var_RoomType.set(row[2])
    
    def update(self):
        if self.var_floor.get()=="":
              messagebox.showerror("Error","Please enter the floor",parent = self.root)
        else:
                conn = mysql.connector.connect(host = "localhost", username = "root", password = "Koya2003@",database = "management")
                my_cursor = conn.cursor()
                my_cursor.execute("update room_details set floor = %s,RoomType = %s where RoomNo=%s",(
                 self.var_floor.get(),
                 self.var_RoomType.get(),
                 self.var_RoomNo.get(),
                 
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Update","Room details has been updated successfully")
    
    def mDelete(self):
        mDelete = messagebox.askyesno("Hostel Management System","Do you want to delete this room details",parent = self.root)
        if mDelete>0:
            conn = mysql.connector.connect(host = "localhost", username = "root", password = "Koya2003@",database = "management")
            my_cursor = conn.cursor()
            my_cursor.execute("delete from room_details where RoomNo = %s",(self.var_RoomNo.get(),))
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
    def reset(self):
        self.var_floor.set("")
        self.var_RoomNo.set("")
        self.var_RoomType.set("")
        


        


if __name__ =="__main__":
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop()
    