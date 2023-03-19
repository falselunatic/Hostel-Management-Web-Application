from tkinter import*
from PIL import Image,ImageTk
from student import stud_win
from details import DetailsRoom




class hostelmanagementsystem:
    def __init__(self,root):
        self.root=root
        self.root.title("hostel management system")
        self.root.geometry("1550x800+0+0")

#************************ist img*************************
        img1=Image.open(r"C:\Users\DELL\OneDrive\Desktop\ninja\g3.jfif")
        # img1=img1.resize((1550,240),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)
#***************logo**************
        img2=Image.open(r"C:\Users\DELL\OneDrive\Desktop\ninja\g1.jfif")
        img2=img2.resize((230,140),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)
#**************************title***********************************
        lbl_title=Label(self.root,text="HOSTEL MANAGEMENT SYSTEM",font=("Lato",40,"bold"),bg="purple",fg="yellow",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=100,width=1550,height=100)

        #***main frame***
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

        #***menu***
        lbl_menu=Label(main_frame,text="Menu",font=("Lato",20,"bold"),bg="purple",fg="yellow",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=250,height=40)

        #***btn frame***
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=470)

        stud_btn=Button(btn_frame,text="Student",command=self.stud_details,height=3,width=22,font=("Lato",14,"bold"),bg="purple",fg="yellow",bd=0,cursor="hand1")
        stud_btn.grid(row=0,column=0,pady=2)

        room_btn=Button(btn_frame,text="Room",width=22,height=3,font=("Lato",14,"bold"),bg="purple",fg="yellow",bd=2,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=2)

        details_btn=Button(btn_frame,text="Details",width=22,height=3,font=("Lato",14,"bold"),bg="purple",fg="yellow",bd=2,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=2)

        report_btn=Button(btn_frame,text="Report",width=22,height=3,font=("Lato",14,"bold"),bg="purple",fg="yellow",bd=2,cursor="hand1")
        report_btn.grid(row=3,column=0,pady=2)

        logout_btn=Button(btn_frame,text="Logout",width=22,height=3,font=("Lato",14,"bold"),bg="purple",fg="yellow",bd=2,cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=2)

        #*************right side images*************
        img3=Image.open(r"C:\Users\DELL\OneDrive\Desktop\ninja\g2.jfif")
        img3=img3.resize((1310,590),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=225,y=0,width=1310,height=590)


        # img4=Image.open(r"C:\Users\Lenovo\Downloads\h2.jpg")
        # img4=img4.resize((230,210),Image.ANTIALIAS)
        # self.photoimg4=ImageTk.PhotoImage(img4)

        # lblimg2=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        # lblimg2.place(x=0,y=225,width=230,height=210)


        # img5=Image.open(r"C:\Users\Lenovo\Downloads\h3.jpg")
        # img5=img5.resize((230,190),Image.ANTIALIAS)
        # self.photoimg5=ImageTk.PhotoImage(img5)

        # lblimg3=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        # lblimg3.place(x=0,y=420,width=230,height=220)

    def stud_details(self):
        self.new_window=Toplevel(self.root)
        self.app=stud_win(self.new_window)
    def details(self):
        self.new_window=Toplevel(self.root)
        self.app=stud_win(self.new_window)







if __name__ == "__main__":
    root=Tk()
    obj=hostelmanagementsystem(root)
    root.mainloop()
