from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk       #pip install pillow


class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("925x500+170+50")
        self.root.configure(bg="grey")
        
        #bgg=Image.open(r"E:\DBPy\Login\hot_10_pro.png")
        #bgg=bgg.resize((925, 500),Image.ANTIALIAS)
        #self.bg=ImageTk.PhotoImage(bgg)
        #lbl_bg=Label(self.root,image=self.bg)
        #lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        frame=Frame(self.root,bg="black")
        frame.place(x=480,y=50,width=300,height=400)
        
        #======================Admin Panel=====================================
        frame1=Frame(self.root,bg="grey")
        frame1.place(x=30,y=395,width=350,height=70)
        
        pnl=Label(frame1,text="Admin Panel",font=("times new roman",35,"bold"),fg="black",bg="grey")
        pnl.place(x=60,y=10)
        #======================================================================
    
        img1=Image.open(r"E:\DBPy\Login\pngegg.png")
        img1=img1.resize((350, 350),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lbl_img1=Label(image=self.photoimage1,bg='grey')
        lbl_img1.place(x=30,y=65,width=350,height=350)
        
        get_str=Label(frame,text="Get Started",font=("times new roman",35,"bold"),fg="white",bg="black")
        get_str.place(x=25,y=85)
        
        #=====================LABELS============================
        
        #-----------USERNAME-------------
        username=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="yellow",bg="black")
        username.place(x=40,y=145)
        
        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=170)
        
        #-----------PASSWORD-------------
        #password=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="yellow",bg="black")
        #password.place(x=40,y=215)
        
        #self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"),show='*')
        #self.txtpass.place(x=40,y=240)
        
        #def show_password():
        #    if self.txtpass.cget("show")=="*":
        #        self.txtpass.config(show="")
        #    else:
        #        self.txtpass.config(show="*")
        
        #chk_butun=Checkbutton(frame,text="Show Password",font=("times new roman",10,"bold"),fg="black",bg="white",command=show_password)
        #chk_butun.place(x=25,y=275)
        
        #=======================================================================
        show_img=Image.open(r"E:\DBPy\Login\show.png")
        show_img=show_img.resize((20,20),Image.LANCZOS)
        self.photoimage_show=ImageTk.PhotoImage(show_img)
        
        show_img=self.photoimage_show
        
        hide_img=Image.open(r"E:\DBPy\Login\hide.png")
        hide_img=hide_img.resize((20,20),Image.LANCZOS)
        self.photoimage_hide=ImageTk.PhotoImage(hide_img)
        
        hide_img=self.photoimage_hide
        
        def show():
            hide_butun=Button(frame,image=hide_img,command=hide,relief=FLAT,activebackground="white",bg="black")
            hide_butun.place(x=250,y=240)
            self.txtpass.config(show="")
        
        def hide():
            show_butun=Button(frame,image=show_img,command=show,activebackground="white",bg="black",relief=FLAT)
            show_butun.place(x=250,y=240)
            self.txtpass.config(show="*")
            
        password=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="yellow",bg="black")
        password.place(x=40,y=215)
        
        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"),show='*')
        self.txtpass.place(x=40,y=240)
        
        show_butun=Button(frame,image=show_img,command=show,activebackground="white",bg="black",relief=FLAT)
        show_butun.place(x=250,y=240)
        
        #=====================ICONS=================================
        #-------------TOP---------------
        imgtop=Image.open(r"E:\DBPy\Login\top.png")
        imgtop=imgtop.resize((75, 75),Image.LANCZOS)
        self.photoimagetop=ImageTk.PhotoImage(imgtop)
        lbl_imgtop=Label(image=self.photoimagetop)
        lbl_imgtop.place(x=595,y=60,width=75,height=75)
        
        #-----------USERNAME-------------
        img2=Image.open(r"E:\DBPy\Login\username1.png")
        img2=img2.resize((25, 25),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lbl_img2=Label(image=self.photoimage2)
        lbl_img2.place(x=495,y=221,width=25,height=25)
        
        #-----------PASSWORD-------------
        img3=Image.open(r"E:\DBPy\Login\password1.png")
        img3=img3.resize((25, 25),Image.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lbl_img3=Label(image=self.photoimage3)
        lbl_img3.place(x=495,y=291,width=25,height=25)
        
        #===================BUTTONS=========================
        #-----------FORGOT PASSWORD BUTTON-----------------
        forgetbtn=Button(frame,text="Forgot my password",font=("times new roman",10,"bold"),bd=0,relief=RIDGE,fg="white",bg="black")
        forgetbtn.place(x=45,y=275,width=115,height=25)
        
        #-----------------LOGIN BUTTON-----------------------
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="black",bg="yellow",activeforeground="black",activebackground="yellow")
        loginbtn.place(x=18,y=320,width=125,height=35)
        
        #----------------REGISTER BUTTON----------------------
        signupbtn=Button(frame,text="Sign up",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="black",bg="yellow",activeforeground="black",activebackground="yellow")
        signupbtn.place(x=157,y=320,width=125,height=35)
        
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All field required")
        elif self.txtuser.get()=="admin" and self.txtpass.get()=="admin":
            messagebox.showinfo("Success","Welcome")
        else:
            messagebox.showerror("Invalid","Username or Password is incorrect")
        




if __name__ == "__main__":
    root=Tk()
    app=login_window(root)
    root.mainloop()