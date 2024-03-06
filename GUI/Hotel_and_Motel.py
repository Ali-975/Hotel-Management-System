from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk       #pip install pillow
import mysql.connector
from Customers import cust_win
from Rooms import rooms_win
from Details import det_win
from Packages import pack_win

class MMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Motel Management System")
        self.root.geometry("1600x900+0+0")
        self.root.configure(bg="black")
        
        #========================VARIABLES===============================
        self.var_lblmenu=StringVar()
        self.var_menu_btn=StringVar()
        self.var_cust_btn=StringVar()
        self.var_rooms_btn=StringVar()
        self.var_details_btn=StringVar()
        self.var_packages_btn=StringVar()
        
        #=========================TOP LEFT CORNER===============================
        topleft=Image.open(r"E:\DBPy\Login\out.png")
        topleft=topleft.resize((190,130),Image.LANCZOS)
        self.topleft=ImageTk.PhotoImage(topleft)
        lbl_topleft=Label(self.root,image=self.topleft,bd=4,relief=RIDGE)
        lbl_topleft.place(x=0,y=0,width=195,height=130)
        
        topleft1=Image.open(r"E:\DBPy\Login\in.png")
        topleft1=topleft1.resize((100,60),Image.LANCZOS)
        self.topleft1=ImageTk.PhotoImage(topleft1)
        lbl_topleft1=Label(self.root,image=self.topleft1)
        lbl_topleft1.place(x=50,y=15,width=100,height=60)
        
        #==================================HEADLINE=====================================
        head=Image.open(r"E:\DBPy\Login\headline1.png")
        head=head.resize((1085,120),Image.LANCZOS)
        self.head=ImageTk.PhotoImage(head)
        lbl_head=Label(self.root,image=self.head,bd=4,relief=RIDGE)
        lbl_head.place(x=195,y=0,width=1085,height=130)
        
        lblheadline=Label(self.root,text="MOTEL MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),fg="red",bg="black",bd=4,relief=RIDGE)      #FAF9F6
        lblheadline.place(x=0,y=130,width=1280,height=50)
        
        #================================Main Frame==========================================
        mainframe=Frame(self.root,bd=4,relief=RIDGE)
        mainframe.place(x=0,y=180,width=1280,height=475)
        
        #======================================MENU===========================================
        widd=Image.open(r"E:\DBPy\Login\main_menu.png")
        widd=widd.resize((35,35),Image.LANCZOS)
        self.widd=ImageTk.PhotoImage(widd)
        lbl_widd=Label(mainframe,image=self.widd,bg="black",bd=0,relief=RIDGE)
        lbl_widd.place(x=0,y=0,width=40,height=40)
        
        menubar=Menu(root)
        root.config(menu=menubar)

        fileMenu=Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Customer",menu=fileMenu)
        menubar.add_cascade(label="Rooms",menu=fileMenu)
        menubar.add_cascade(label="Details",menu=fileMenu)
        menubar.add_cascade(label="Packages",menu=fileMenu)
        
        
        #opt=["MENU","Customer","Rooms","Details","Packages"]
        #text1=StringVar()
        #text1.set(opt[0])
        #menu_btn= OptionMenu(mainframe,text1,*opt)
        #menu_btn.config(bg="black", fg="red")
        #menu_btn["menu"].config(font=("times new roman",15,"bold"),fg="red",bg="black",bd=4,relief=RIDGE,cursor="hand2")
        #menu_btn.place(x=40,y=0,width=155,height=40)
        
        #menu_btn=Button(mainframe,text="MENU",font=("times new roman",15,"bold"),fg="red",bg="black",bd=4,relief=RIDGE,cursor="hand2")      #FAF9F6
        #menu_btn.place(x=0,y=0,width=195)
               
        #self.menu_btn=ttk.Combobox(mainframe,textvariable=self.var_menu_btn,font=("times new roman",15,"bold"),foreground="red",background="black",state="readonly",cursor="hand2")
        #self.menu_btn["values"]=("MENU","Customer","Rooms","Details","Packages")
        #self.menu_btn.place(x=0,y=0,width=195)
        #self.menu_btn.current(0)
        
        #==================================BUTTON FRAME=========================================
        btn_frame=Frame(mainframe,bd=0,relief=RIDGE)
        btn_frame.place(x=0,y=40,width=195,height=425)
        
        lblmenu=Label(mainframe,text="MENU",font=("times new roman",15,"bold"),fg="red",bg="black",bd=0,relief=RIDGE)      #FAF9F6
        lblmenu.place(x=40,y=0,width=155,height=40)
        
        cust_btn=Button(btn_frame,text="Customer",width=18,font=("times new roman",13,"bold"),command=self.win_customer,fg="red",bg="black",bd=4,cursor="hand2")
        cust_btn.grid(row=0,column=0,pady=1)
        
        rooms_btn=Button(btn_frame,text="Rooms",width=18,font=("times new roman",13,"bold"),command=self.win_room,fg="red",bg="black",bd=4,cursor="hand2")
        rooms_btn.grid(row=1,column=0,pady=1)
        
        details_btn=Button(btn_frame,text="Details",width=18,font=("times new roman",13,"bold"),command=self.win_detail,fg="red",bg="black",bd=4,cursor="hand2")
        details_btn.grid(row=2,column=0,pady=1)
        
        packages_btn=Button(btn_frame,text="Packages",width=18,font=("times new roman",13,"bold"),command=self.win_package,fg="red",bg="black",bd=4,cursor="hand2")
        packages_btn.grid(row=3,column=0,pady=1)
        
        botmleft=Image.open(r"E:\DBPy\Login\botmleft.png")
        botmleft=botmleft.resize((195,255),Image.LANCZOS)
        self.botmleft=ImageTk.PhotoImage(botmleft)
        lbl_botmleft=Label(self.root,image=self.botmleft,bd=1,relief=RIDGE)
        lbl_botmleft.place(x=5,y=380,width=195,height=255)
        
        #=================================MAIN WINDOW==================================================
        win_frame=Frame(self.root,bd=4,relief=RIDGE)
        win_frame.place(x=195,y=180,width=1085,height=475)
        
        mwin=Image.open(r"E:\DBPy\Login\mainwin.png")
        mwin=mwin.resize((1078,490),Image.LANCZOS)
        self.mwin=ImageTk.PhotoImage(mwin)
        lbl_mwin=Label(win_frame,image=self.mwin,bd=1,relief=RIDGE)
        lbl_mwin.place(x=0,y=0,width=1078,height=490)
    #===========FUNCTIONS============
    def win_customer(self):        
        self.new_win1=Toplevel(self.root)
        self.app=cust_win(self.new_win1)
        
    def win_room(self):
        self.new_win1.destroy()
        
        self.new_win2=Toplevel(self.root)
        self.app=rooms_win(self.new_win2)
        
    def win_detail(self):
        self.new_win1.destroy()
        self.new_win2.destroy()
        
        self.new_win3=Toplevel(self.root)
        self.app=det_win(self.new_win3)
        
    def win_package(self):
        self.new_win1.destroy()
        self.new_win3.destroy()
        self.new_win2.destroy()
        
        self.new_win4=Toplevel(self.root)
        self.app=pack_win(self.new_win4)
        



if __name__ == "__main__":
    root=Tk()
    app=MMS(root)
    root.mainloop()