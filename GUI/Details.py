from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk       #pip install pillow
import mysql.connector

class det_win:
    def __init__(self,root):
        self.root=root
        self.root.title("Details")
        self.root.geometry("1079x422+190+225")
        self.root.configure(bg="black")
        
        #==============VARIABLES==================
        self.var_floor=StringVar()
        self.var_room_no=StringVar()
        self.var_room_type=StringVar()
        
        #=================TITLE=====================
        lblheadline=Label(self.root,text="ROOM DETAILS",font=("times new roman",15,"bold"),fg="red",bg="black",bd=4,relief=RIDGE)      #FAF9F6
        lblheadline.place(x=0,y=0,width=1079,height=30)
        
        #===================LABEL FRAME====================
        LabelFrameleft=LabelFrame(self.root,bd=4,relief=RIDGE,text="Room Details",font=("times new roman",20,"bold"),padx=2)
        LabelFrameleft.place(x=0,y=30,width=425,height=392)
        
        #FLOOR
        room_floor=Label(LabelFrameleft,text="     ",font=("times new roman",12,"bold"),padx=2,pady=6,fg="black")
        room_floor.grid(row=0,column=0,sticky=W)
        
        room_floor=Label(LabelFrameleft,text="Floor No     ",font=("times new roman",15,"bold"),padx=2,pady=6,fg="black")
        room_floor.grid(row=1,column=0,sticky=W)
        
        #self.txt_room_floor=ttk.Entry(LabelFrameleft,textvariable=self.var_floor,font=("arial",15),width=20)
        #self.txt_room_floor.grid(row=1,column=1)
        self.room_type=ttk.Combobox(LabelFrameleft,textvariable=self.var_floor,font=("times new roman",15),state="readonly",width=20)
        self.room_type["values"]=("Select","Ground","1st","2nd","3rd","4th")
        self.room_type.grid(row=1,column=1)
        self.room_type.current(0)
        
        #ROOM NO
        room_no=Label(LabelFrameleft,text="Room No     ",font=("times new roman",15,"bold"),padx=2,pady=6,fg="black")
        room_no.grid(row=2,column=0,sticky=W)
        
        self.txt_room_no=ttk.Entry(LabelFrameleft,textvariable=self.var_room_no,font=("arial",15),width=20)
        self.txt_room_no.grid(row=2,column=1)
        
        #ROOM TYPE
        room_type=Label(LabelFrameleft,text="Room Type      ",font=("times new roman",15,"bold"),padx=2,pady=6,fg="black")
        room_type.grid(row=3,column=0,sticky=W)
        
        #self.txt_room_type=ttk.Entry(LabelFrameleft,textvariable=self.var_room_type,font=("arial",15),width=20)
        #self.txt_room_type.grid(row=3,column=1)
        self.room_type=ttk.Combobox(LabelFrameleft,textvariable=self.var_room_type,font=("times new roman",15),state="readonly",width=20)
        self.room_type["values"]=("Select","Single","Double","Luxury")
        self.room_type.grid(row=3,column=1)
        self.room_type.current(0)
        
        #=====================================Buttons=================================================
        #btn_frame=Frame(LabelFrameleft,bd=0,relief=RIDGE)
        #btn_frame.place(x=100,y=120,width=105,height=305)
        
        btn_add=Button(LabelFrameleft,text="INSERT",command=self.add_data,font=("arial",11,"bold"),bg="black",bd=4,fg="gold",width=9,cursor="hand2")
        #btn_add.grid(row=0,column=0,padx=1,sticky=W)
        btn_add.place(x=70,y=200,height=40,width=100)
        
        btn_del=Button(LabelFrameleft,text="DELETE",command=self.delt,font=("arial",11,"bold"),bg="black",bd=4,fg="gold",width=9,cursor="hand2")
        #btn_del.grid(row=1,column=0,padx=1,sticky=W)
        btn_del.place(x=240,y=200,height=40,width=100)
        
        btn_upd=Button(LabelFrameleft,text="UPDATE",command=self.updat,font=("arial",11,"bold"),bg="black",bd=4,fg="gold",width=9,cursor="hand2")
        #btn_upd.grid(row=2,column=0,padx=1,sticky=W)
        btn_upd.place(x=70,y=270,height=40,width=100)
        
        btn_res=Button(LabelFrameleft,text="RESET",command=self.resset,font=("arial",11,"bold"),bg="black",bd=4,fg="gold",width=9,cursor="hand2")
        #btn_res.grid(row=3,column=0,padx=1,sticky=W)
        btn_res.place(x=240,y=270,height=40,width=100)
        
        #================================Table Frame=============================
        botmleft=Image.open(r"E:\DBPy\Login\top1.png")
        botmleft=botmleft.resize((810,232),Image.LANCZOS)
        self.botmleft=ImageTk.PhotoImage(botmleft)
        lbl_botmleft=Label(self.root,image=self.botmleft,bd=1,relief=RIDGE)
        lbl_botmleft.place(x=425,y=29,width=652,height=142)
        
        LabelFrameright=LabelFrame(self.root,bd=4,relief=RIDGE,text="View Room Details",font=("times new roman",20,"bold"),padx=2)
        LabelFrameright.place(x=425,y=172,width=652,height=250)
        
        #================================Data Table================================
        details_frame=Frame(LabelFrameright,bd=4,relief=RIDGE)
        details_frame.place(x=0,y=30,width=640,height=180)
        
        scroll_x=ttk.Scrollbar(details_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_frame,orient=VERTICAL)
        
        self.room_details_table=ttk.Treeview(details_frame,column=("Floor No","Room No","Room Type"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.room_details_table.xview)
        scroll_y.config(command=self.room_details_table.yview)
        
        self.room_details_table.heading("Floor No",text="Floor No")
        self.room_details_table.heading("Room No",text="Room No")
        self.room_details_table.heading("Room Type",text="Room Typer")
        
        self.room_details_table["show"]="headings"
        
        self.room_details_table.column("Floor No",width=100)
        self.room_details_table.column("Room No",width=100)
        self.room_details_table.column("Room Type",width=100)
        
        self.room_details_table.pack(fill=BOTH,expand=1)
        self.room_details_table.bind("<ButtonRelease-1>",self.get_currsor)
        self.fetch_data()
        
    #=============================ADD DATA=================================    
    def add_data(self):
        if self.var_floor.get()=="" or self.var_room_no.get()=="":
            messagebox.showerror("ERROR","Floor and Room No is mandatory",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", password="Uit54321", user="root",database="hotel_and_motel")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",(
                    self.var_floor.get(),
                    self.var_room_no.get(),
                    self.var_room_type.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("SUCCESS","Record Successfully Added in Room Details",parent=self.root)
            except Exception as es:
                messagebox.showwarning("WARNING",f"Something Went Wrong:{str(es)}",parent=self.root)
        
    #=========================DELETE DATA=============================            
    def delt(self):
        delt=messagebox.askyesno("DELETE","Do you want to delete this Room Details",parent=self.root)
        if delt>0:
            conn=mysql.connector.connect(host="localhost", password="Uit54321", user="root",database="hotel_and_motel")
            my_cursor=conn.cursor()
            query="delete from details where room_no=%s"
            value=(self.var_room_no.get(),)
            my_cursor.execute(query,value)
        else:
            if not delt:
                return
        conn.commit()
        self.fetch_data()
        conn.close() 
        
    #======================UPDATE DATA======================
    def updat(self):
        if self.var_room_no.get()=="":
            messagebox.showerror("Error","Please Enter Room No Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost", password="Uit54321", user="root",database="hotel_and_motel")
            my_cursor=conn.cursor()
            my_cursor.execute("update details set floor=%s, room_type=%s where room_no=%s",(
                
                self.var_floor.get(),
                self.var_room_type.get(),
                self.var_room_no.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room Details Updated Successfully",parent=self.root) 
    
    #========================RESET FIELDS==================================    
    def resset(self):
        
        self.var_floor.set("Select"),
        self.var_room_no.set(""),
        self.var_room_type.set("Select")
    
    #=====================Fetch Data========================            
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost", password="Uit54321", user="root",database="hotel_and_motel")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
        rows=my_cursor.fetchall()
        
        if len(rows)!=0:
            self.room_details_table.delete(*self.room_details_table.get_children())
            for i in rows:
                self.room_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    #===================Cursor=====================    
    def get_currsor(self,event=""):
        cursor_row=self.room_details_table.focus()
        content=self.room_details_table.item(cursor_row)
        row=content["values"]
        
        self.var_floor.set(row[0]),
        self.var_room_no.set(row[1]),
        self.var_room_type.set(row[2])
        


if __name__ == "__main__":
    root=Tk()
    app=det_win(root)
    root.mainloop()