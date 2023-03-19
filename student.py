from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class stud_win:
    def __init__(self,root):
        self.root=root
        self.root.title("hostel management system")
        self.root.geometry("1295x580+230+190")
#********************variables***********************
        self.var_enr = StringVar()
        self.var_stud_name = StringVar()
        self.var_gname = StringVar()
        self.var_gender = StringVar()
        self.var_postcode = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_idproof = StringVar()
        self.var_idnumber = StringVar()
        self.var_address = StringVar()
#********************title****************************

        lbl_title=Label(self.root,text="ADD STUDENT DETAILS",font=("arial",18,"bold"),bg="purple",fg="yellow",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)
#*****************label********************
        img2=Image.open(r"C:\Users\DELL\OneDrive\Desktop\ninja\h2.jfif")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

#**********************labelframe*************************
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="student details",font=("arial",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #****************labels and enrties**********************
        # stude_roll num
        lbl_stud_roll=Label(labelframeleft,text="enrollment no.",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_stud_roll.grid(row=0,column=0,sticky=W)

        entry_roll=ttk.Entry(labelframeleft,textvariable=self.var_enr,width=29,font=("arial",13,"bold"))
        entry_roll.grid(row=0,column=1)

        #stud name
        sname=Label(labelframeleft,text="student name",font=("arial",12,"bold"),padx=2,pady=6)
        sname.grid(row=1,column=0,sticky=W)

        textsname=ttk.Entry(labelframeleft,textvariable=self.var_stud_name,width=29,font=("arial",13,"bold"))
        textsname.grid(row=1,column=1)

        # guardian name

        lblgname=Label(labelframeleft,text="guardian's name",font=("arial",12,"bold"),padx=2,pady=6)
        lblgname.grid(row=2,column=0,sticky=W)

        textgname=ttk.Entry(labelframeleft,textvariable=self.var_gname,width=29,font=("arial",13,"bold"))
        textgname.grid(row=2,column=1)

        # gender combobox

        lblgender=Label(labelframeleft,text="gender",font=("arial",12,"bold"),padx=2,pady=6)
        lblgender.grid(row=3,column=0,sticky=W)
        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial",12,"bold"),width=27,state="readonly")
        combo_gender["value"]=("Male","Female","Others")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)
        

        # postcode

        lblpostcode=Label(labelframeleft,text="postcode",font=("arial",12,"bold"),padx=2,pady=6)
        lblpostcode.grid(row=4,column=0,sticky=W)

        textpostcode=ttk.Entry(labelframeleft,textvariable=self.var_postcode,width=29,font=("arial",13,"bold"))
        textpostcode.grid(row=4,column=1)

        #mobile number

        lblmobile=Label(labelframeleft,text="mobile number",font=("arial",12,"bold"),padx=2,pady=6)
        lblmobile.grid(row=5,column=0,sticky=W)

        textmobile=ttk.Entry(labelframeleft,textvariable=self.var_mobile,width=29,font=("arial",13,"bold"))
        textmobile.grid(row=5,column=1)

        #email

        lblemail=Label(labelframeleft,text="email",font=("arial",12,"bold"),padx=2,pady=6)
        lblemail.grid(row=6,column=0,sticky=W)

        textemail=ttk.Entry(labelframeleft,textvariable=self.var_email,width=29,font=("arial",13,"bold"))
        textemail.grid(row=6,column=1)

        #nationality

        lblnationality=Label(labelframeleft,text="nationality",font=("arial",12,"bold"),padx=2,pady=6)
        lblnationality.grid(row=7,column=0,sticky=W)

        combo_nationality=ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=("arial",12,"bold"),width=27,state="readonly")
        combo_nationality["value"]=("indian","american","Others")
        combo_nationality.current(0)
        combo_nationality.grid(row=7,column=1)
        

        #idproof type combobox

        lblidproof=Label(labelframeleft,text="id proof type",font=("arial",12,"bold"),padx=2,pady=6)
        lblidproof.grid(row=8,column=0,sticky=W)
        combo_idproof=ttk.Combobox(labelframeleft,textvariable=self.var_idproof,font=("arial",12,"bold"),width=27,state="readonly")
        combo_idproof["value"]=("adhaar","PAN","Others")
        combo_idproof.current(0)
        combo_idproof.grid(row=8,column=1)
        

        #id number

        lblidnumber=Label(labelframeleft,text="id number",font=("arial",12,"bold"),padx=2,pady=6)
        lblidnumber.grid(row=9,column=0,sticky=W)

        textidnumber=ttk.Entry(labelframeleft,textvariable=self.var_idnumber,width=29,font=("arial",13,"bold"))
        textidnumber.grid(row=9,column=1)

        #address
        lbladdress=Label(labelframeleft,text="address",font=("arial",12,"bold"),padx=2,pady=6)
        lbladdress.grid(row=10,column=0,sticky=W)

        textaddress=ttk.Entry(labelframeleft,textvariable=self.var_address,width=29,font=("arial",13,"bold"))
        textaddress.grid(row=10,column=1)
#******************btns**************************
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnadd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="purple",fg="yellow",width=10)
        btnadd.grid(row=0,column=0,padx=1)

        btnupdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="purple",fg="yellow",width=10)
        btnupdate.grid(row=0,column=1,padx=1)

        btndelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",12,"bold"),bg="purple",fg="yellow",width=10)
        btndelete.grid(row=0,column=2,padx=1)

        btnreset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="purple",fg="yellow",width=10)
        btnreset.grid(row=0,column=3,padx=1)

#***************************table frame*****************************************
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="view details and search system",font=("arial",12,"bold"),padx=2)
        table_frame.place(x=435,y=50,width=860,height=490)

        lblsearchby=Label(table_frame,text="search by",font=("arial",12,"bold"),bg="red",fg="white")
        lblsearchby.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var = StringVar()
        combo_search=ttk.Combobox(table_frame,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_search["value"]=("mobile no.","enrollment no.")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        self.txt_search = StringVar()
        textsearch=ttk.Entry(table_frame,textvariable=self.txt_search,width=24,font=("arial",13,"bold"))
        textsearch.grid(row=0,column=2,padx=2)

        btnsearch=Button(table_frame,text="Search",command=self.search,font=("arial",12,"bold"),bg="purple",fg="yellow",width=10)
        btnsearch.grid(row=0,column=3,padx=1)

        btnshowall=Button(table_frame,text="Show All",command=self.fetch_data,font=("arial",12,"bold"),bg="purple",fg="yellow",width=10)
        btnshowall.grid(row=0,column=4,padx=1)

#*******************show data table**********************
        details_table=Frame(table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=350)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        self.stud_details_table=ttk.Treeview(details_table,column=("enr","name","gname","gender","postcode","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.stud_details_table.xview)
        scroll_y.config(command=self.stud_details_table.yview)

        self.stud_details_table.heading("enr",text="enrollment number")
        self.stud_details_table.heading("name",text="Student's name")
        self.stud_details_table.heading("gname",text="guardian's name")
        self.stud_details_table.heading("gender",text="gender")
        self.stud_details_table.heading("postcode",text="postcode")
        self.stud_details_table.heading("mobile",text="Mobile number")
        self.stud_details_table.heading("email",text="email")
        self.stud_details_table.heading("nationality",text="nationality")
        self.stud_details_table.heading("idproof",text="ID proof")
        self.stud_details_table.heading("idnumber",text="ID number")
        self.stud_details_table.heading("address",text="Address")
        self.stud_details_table["show"]="headings"
        self.stud_details_table.pack(fill=BOTH,expand=1)
        self.stud_details_table.bind("<ButtonRelease-1>",self.get_cuersor)
        self.fetch_data()
        






    def add_data(self):
        if self.var_mobile.get() == "" or self.var_email.get() == "":
              messagebox.showerror("Error","All fields are required")
        else:
             try:
                conn = mysql.connector.connect(host = "localhost",username = "root",password = "Koya2003@",database = "management")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.var_enr.get(),
                self.var_stud_name.get(),
                self.var_gname.get(),
                self.var_gender.get(),
                self.var_postcode.get(),
                self.var_mobile.get(),
                self.var_email.get(),
                self.var_nationality.get(),
                self.var_idproof.get(),
                self.var_idnumber.get(),
                self.var_address.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","details has been added",parent = self.root)
             except Exception as es:
                 messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent = self.root)


    def fetch_data(self):
            conn = mysql.connector.connect(host = "localhost",username = "root",password = "Koya2003@",database = "management")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from student")
            rows = my_cursor.fetchall()
            if len(rows)!=0:
                self.stud_details_table.delete(*self.stud_details_table.get_children())
                for i in rows:
                    self.stud_details_table.insert("",END,values = i)
                conn.commit()
            conn.close()
    def get_cuersor(self,event = ""):
         cusrsor_row = self.stud_details_table.focus()
         content = self.stud_details_table.item(cusrsor_row)
         row = content["values"]

         self.var_enr.set(row[0])
         self.var_stud_name.set(row[1])
         self.var_gname.set(row[2])
         self.var_gender.set(row[3])
         self.var_postcode.set(row[4])
         self.var_mobile.set(row[5])
         self.var_email.set(row[6])
         self.var_nationality.set(row[7])
         self.var_idproof.set(row[8])
         self.var_idnumber.set(row[9])
         self.var_address.set(row[10])

    def update(self):
         if self.var_mobile.get()=="":
              messagebox.showerror("Error","Please enter mobile number",parent = self.root)
         else:
                conn = mysql.connector.connect(host = "localhost", username = "root", password = "Koya2003@",database = "management")
                my_cursor = conn.cursor()
                my_cursor.execute("update student set name = %s,gname = %s,gender = %s,postcode = %s,mobile = %s,email = %s,nationality = %s,idproof = %s,idnumber = %s,address = %s where enr = %s",(
                 self.var_stud_name.get(),
                 self.var_gname.get(),
                 self.var_gender.get(),
                 self.var_postcode.get(),
                 self.var_mobile.get(),
                 self.var_email.get(),
                 self.var_nationality.get(),
                 self.var_idproof.get(),
                 self.var_idnumber.get(),
                 self.var_address.get(),
                 self.var_enr.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Update","Student details has been updated successfully")

    def mDelete(self):
         mDelete = messagebox.askyesno("Hostel Management System","Do you want to delete this Student details",parent = self.root)
         if mDelete>0:
              conn = mysql.connector.connect(host = "localhost", username = "root", password = "Koya2003@",database = "management")
              my_cursor = conn.cursor()
              my_cursor.execute("delete from student where enr = %s",(self.var_enr.get(),))
         else:
              if not mDelete:
                   return
         conn.commit()
         self.fetch_data()
         conn.close()
    def reset(self):
         self.var_enr.set("")
         self.var_stud_name.set("")
         self.var_gname.set("")
         #self.var_gender.set("")
         self.var_postcode.set("")
         self.var_mobile.set("")
         self.var_email.set("")
         #self.var_nationality.set("")
         #self.var_idproof.set("")
         self.var_idnumber.set("")
         self.var_address.set("")
    def search(self):
         conn = mysql.connector.connect(host = "localhost",username = "root",password = "Koya2003@",database = "management")
         my_cursor = conn.cursor()
         my_cursor.execute("Select * from student where"+str(self.search_var.get())+"LIKE'%"+str(self.txt_search.get())+"%'")
         rows = my_cursor.fetchall()
         if len(rows)!=0:
              self.stud_details_table.delete(*self.stud_details_table.get_children())
              for i in rows:
                   self.stud_details_table.insert("",END,values = 1)
              conn.commit()
         conn.close()
         
                                
              




if __name__ =="__main__":
    root=Tk()
    obj=stud_win(root)
    root.mainloop()
