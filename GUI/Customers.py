from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk       #pip install pillow
import random
import mysql.connector

class cust_win:
    def __init__(self,root):
        self.root=root
        self.root.title("Customer")
        self.root.geometry("1079x422+190+225")
        self.root.configure(bg="black")
        
        #====================VARIABLES======================
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))
        
        self.var_cust_name=StringVar()
        self.var_cust_fname=StringVar()
        self.var_cust_gender=StringVar()
        self.var_cust_idtype=StringVar()
        self.var_cust_id=StringVar()
        self.var_cust_mob_no=StringVar()
        self.var_cust_city=StringVar()
        self.var_cust_nat=StringVar()
        self.var_cust_add=StringVar()
        
        #=================TITLE=====================
        lblheadline=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",15,"bold"),fg="red",bg="black",bd=4,relief=RIDGE)      #FAF9F6
        lblheadline.place(x=0,y=0,width=1079,height=30)
        
        #===================LABEL FRAME====================
        LabelFrameleft=LabelFrame(self.root,bd=4,relief=RIDGE,text="Customer Details",font=("times new roman",20,"bold"),padx=2)
        LabelFrameleft.place(x=0,y=30,width=425,height=392)
        
        #==================LABELS AND ENTRY===================
        #Customer ref
        cust_ref=Label(LabelFrameleft,text="Customer Ref",font=("arial",10,"bold"),padx=2,pady=6,fg="black")
        cust_ref.grid(row=0,column=0,sticky=W)
        
        self.txt_cust_ref=ttk.Entry(LabelFrameleft,textvariable=self.var_ref,font=("arial",10),width=40,state="readonly")
        self.txt_cust_ref.grid(row=0,column=1)
        
        #Name
        cust_name=Label(LabelFrameleft,text="Customer Name",font=("arial",10,"bold"),padx=2,pady=6,fg="black")
        cust_name.grid(row=1,column=0,sticky=W)
        
        self.txt_cust_name=ttk.Entry(LabelFrameleft,textvariable=self.var_cust_name,font=("arial",10),width=40)
        self.txt_cust_name.grid(row=1,column=1)
        
        #Father Name
        cust_fname=Label(LabelFrameleft,text="Father Name",font=("arial",10,"bold"),padx=2,pady=6,fg="black")
        cust_fname.grid(row=2,column=0,sticky=W)
        
        self.txt_cust_fname=ttk.Entry(LabelFrameleft,textvariable=self.var_cust_fname,font=("arial",10),width=40)
        self.txt_cust_fname.grid(row=2,column=1)
        
        #Gender
        cust_gender=Label(LabelFrameleft,text="Gender",font=("arial",10,"bold"),padx=2,pady=6,fg="black")
        cust_gender.grid(row=3,column=0,sticky=W)
        
        self.cust_gender=ttk.Combobox(LabelFrameleft,textvariable=self.var_cust_gender,font=("times new roman",11),state="readonly",width=38)
        self.cust_gender["values"]=("Select","Male","Female","LGBTQ")
        self.cust_gender.grid(row=3,column=1)
        self.cust_gender.current(0)
        
        #Id Type
        cust_idtype=Label(LabelFrameleft,text="Id Type",font=("arial",10,"bold"),padx=2,pady=6,fg="black")
        cust_idtype.grid(row=4,column=0,sticky=W)
        
        self.combo_cust_idtype=ttk.Combobox(LabelFrameleft,textvariable=self.var_cust_idtype,font=("times new roman",11),state="readonly",width=38)
        self.combo_cust_idtype["values"]=("Select","CNIC","Passport No","License No")
        self.combo_cust_idtype.grid(row=4,column=1)
        self.combo_cust_idtype.current(0)
        
        #Id
        cust_id=Label(LabelFrameleft,text="Id Number #",font=("arial",10,"bold"),padx=2,pady=6,fg="black")
        cust_id.grid(row=5,column=0,sticky=W)
        
        self.txt_cust_id=ttk.Entry(LabelFrameleft,textvariable=self.var_cust_id,font=("arial",10),width=40)
        self.txt_cust_id.grid(row=5,column=1)
        
        #Mobile No
        cust_mob_no=Label(LabelFrameleft,text="Cell Phone #",font=("arial",10,"bold"),padx=2,pady=6,fg="black")
        cust_mob_no.grid(row=6,column=0,sticky=W)
        
        self.txt_cust_mob_no=ttk.Entry(LabelFrameleft,textvariable=self.var_cust_mob_no,font=("arial",10),width=40)
        self.txt_cust_mob_no.grid(row=6,column=1)
        
        #City
        cust_city=Label(LabelFrameleft,text="City",font=("arial",10,"bold"),padx=2,pady=6,fg="black")
        cust_city.grid(row=7,column=0,sticky=W)
        
        self.txt_cust_city=ttk.Entry(LabelFrameleft,textvariable=self.var_cust_city,font=("arial",10),width=40)
        self.txt_cust_city.grid(row=7,column=1)
        
        #Nationality
        cust_nat=Label(LabelFrameleft,text="Nationality",font=("arial",10,"bold"),padx=2,pady=6,fg="black")
        cust_nat.grid(row=8,column=0,sticky=W)
        
        self.combo_cust_nat=ttk.Combobox(LabelFrameleft,textvariable=self.var_cust_nat,font=("times new roman",11),state="readonly",width=38)
        self.combo_cust_nat["values"]=("Select","Local","Foriegner")
        self.combo_cust_nat.grid(row=8,column=1)
        self.combo_cust_nat.current(0)
        
        #Address
        cust_add=Label(LabelFrameleft,text="Address",font=("arial",10,"bold"),padx=2,pady=6,fg="black")
        cust_add.grid(row=9,column=0,sticky=W)
        
        self.txt_cust_add=ttk.Entry(LabelFrameleft,textvariable=self.var_cust_add,font=("arial",10),width=40)
        self.txt_cust_add.grid(row=9,column=1)
        
        #=============================================================================================
        #=============================================================================================
        #=====================================Buttons=================================================
        btn_frame=Frame(LabelFrameleft,bd=0,relief=RIDGE)
        btn_frame.place(x=10,y=320,width=405,height=35)
        
        btn_add=Button(btn_frame,text="INSERT",command=self.add_data,font=("arial",11,"bold"),bg="black",bd=4,fg="gold",width=9,cursor="hand2")
        btn_add.grid(row=0,column=0,padx=1,sticky=W)
        
        btn_del=Button(btn_frame,text="DELETE",command=self.delt,font=("arial",11,"bold"),bg="black",bd=4,fg="gold",width=9,cursor="hand2")
        btn_del.grid(row=0,column=1,padx=1,sticky=W)
        
        btn_upd=Button(btn_frame,text="UPDATE",command=self.updat,font=("arial",11,"bold"),bg="black",bd=4,fg="gold",width=9,cursor="hand2")
        btn_upd.grid(row=0,column=2,padx=1,sticky=W)
        
        btn_res=Button(btn_frame,text="RESET",command=self.resset,font=("arial",11,"bold"),bg="black",bd=4,fg="gold",width=9,cursor="hand2")
        btn_res.grid(row=0,column=3,padx=1,sticky=W)
        
        #================================Table Frame=============================
        LabelFrameright=LabelFrame(self.root,bd=4,relief=RIDGE,text="View Details & Search System",font=("times new roman",20,"bold"),padx=2)
        LabelFrameright.place(x=425,y=30,width=652,height=392)
        #============================Search Option=============================
        lbl_searchby=Label(LabelFrameright,text="Search By",font=("arial",10,"bold"),padx=2,pady=6,fg="black")
        lbl_searchby.grid(row=0,column=0,sticky=W,padx=2)
        
        self.var_search=StringVar()
        self.lbl_searchby=ttk.Combobox(LabelFrameright,textvariable=self.var_search,font=("times new roman",11),state="readonly",width=15)
        self.lbl_searchby["values"]=("Select","id_no","Reference","cell_no")
        self.lbl_searchby.grid(row=0,column=1,padx=2)
        self.lbl_searchby.current(0)
        
        self.var_searchby=StringVar()
        self.txt_searchby=ttk.Entry(LabelFrameright,textvariable=self.var_searchby,font=("times new roman",11),width=30)
        self.txt_searchby.grid(row=0,column=2,padx=2)
        
        btn_search=Button(LabelFrameright,text="Search",command=self.search,font=("times new roman",10),bg="black",fg="gold",width=8,cursor="hand2")
        btn_search.grid(row=0,column=3,padx=2)
        
        btn_showA=Button(LabelFrameright,text="Show All",command=self.fetch_data,font=("times new roman",10),bg="black",fg="gold",width=8,cursor="hand2")
        btn_showA.grid(row=0,column=4,padx=2)
        
        #================================Show Data Table================================
        details_frame=Frame(LabelFrameright,bd=4,relief=RIDGE)
        details_frame.place(x=0,y=30,width=640,height=290)
        
        scroll_x=ttk.Scrollbar(details_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_frame,orient=VERTICAL)
        
        self.cust_details_table=ttk.Treeview(details_frame,column=("Reference","Customer Name","Father Name","Gender","Id Type","Id No","Cell Phone No","City","Nationality","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.cust_details_table.xview)
        scroll_y.config(command=self.cust_details_table.yview)
        
        self.cust_details_table.heading("Reference",text="Reference No")
        self.cust_details_table.heading("Customer Name",text="Customer Name")
        self.cust_details_table.heading("Father Name",text="Father Name")
        self.cust_details_table.heading("Gender",text="Gender")
        self.cust_details_table.heading("Id Type",text="Id Type")
        self.cust_details_table.heading("Id No",text="Id No")
        self.cust_details_table.heading("Cell Phone No",text="Cell Phone No")
        self.cust_details_table.heading("City",text="City")
        self.cust_details_table.heading("Nationality",text="Nationalty")
        self.cust_details_table.heading("Address",text="Address")
        
        self.cust_details_table["show"]="headings"
        
        self.cust_details_table.column("Reference",width=100)
        self.cust_details_table.column("Customer Name",width=100)
        self.cust_details_table.column("Father Name",width=100)
        self.cust_details_table.column("Gender",width=100)
        self.cust_details_table.column("Id Type",width=100)
        self.cust_details_table.column("Id No",width=100)
        self.cust_details_table.column("Cell Phone No",width=100)
        self.cust_details_table.column("City",width=100)
        self.cust_details_table.column("Nationality",width=100)
        self.cust_details_table.column("Address",width=100)
        
        self.cust_details_table.pack(fill=BOTH,expand=1)
        self.cust_details_table.bind("<ButtonRelease-1>",self.get_currsor)
        self.fetch_data()
        
    def add_data(self):
        if self.var_cust_id.get()=="" or self.txt_cust_mob_no.get()=="":
            messagebox.showerror("ERROR","Cell Phone # or Id # is mandatory")
        else:
            try:
                conn=mysql.connector.connect(host="localhost", password="Uit54321", user="root",database="hotel_and_motel")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_ref.get(),
                    self.var_cust_name.get(),
                    self.var_cust_fname.get(),
                    self.var_cust_gender.get(),
                    self.var_cust_idtype.get(),
                    self.var_cust_id.get(),
                    self.var_cust_mob_no.get(),
                    self.var_cust_city.get(),
                    self.var_cust_nat.get(),
                    self.var_cust_add.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("SUCCESS","Record Successfully Added in Customer",parent=self.root)
            except Exception as es:
                messagebox.showwarning("WARNING",f"Something Went Wrong:{str(es)}",parent=self.root)
                
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost", password="Uit54321", user="root",database="hotel_and_motel")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        
        if len(rows)!=0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    def get_currsor(self,event=""):
        cursor_row=self.cust_details_table.focus()
        content=self.cust_details_table.item(cursor_row)
        row=content["values"]
        
        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_cust_fname.set(row[2]),
        self.var_cust_gender.set(row[3]),
        self.var_cust_idtype.set(row[4]),
        self.var_cust_id.set(row[5]),
        self.var_cust_mob_no.set(row[6]),
        self.var_cust_city.set(row[7]),
        self.var_cust_nat.set(row[8]),
        self.var_cust_add.set(row[9])
        
    def updat(self):
        if self.var_cust_mob_no.get()=="":
            messagebox.showerror("Error","Please Enter Cell Phone Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost", password="Uit54321", user="root",database="hotel_and_motel")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set name=%s, father_name=%s, gender=%s, id_type=%s, id_no=%s, cell_no=%s, city=%s, nationality=%s, address=%s where reference=%s",(
                self.var_cust_name.get(),
                self.var_cust_fname.get(),
                self.var_cust_gender.get(),
                self.var_cust_idtype.get(),
                self.var_cust_id.get(),
                self.var_cust_mob_no.get(),
                self.var_cust_city.get(),
                self.var_cust_nat.get(),
                self.var_cust_add.get(),
                self.var_ref.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer Details Updated Successfully",parent=self.root)
            
    def delt(self):
        delt=messagebox.askyesno("DELETE","Do you want to delete this Customer",parent=self.root)
        if delt>0:
            conn=mysql.connector.connect(host="localhost", password="Uit54321", user="root",database="hotel_and_motel")
            my_cursor=conn.cursor()
            query="delete from customer where reference=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not delt:
                return
        conn.commit()
        self.fetch_data()
        conn.close()            
        
    def resset(self):
        #self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_cust_fname.set(""),
        self.var_cust_gender.set("Select"),
        self.var_cust_idtype.set("Select"),
        self.var_cust_id.set(""),
        self.var_cust_mob_no.set(""),
        self.var_cust_city.set(""),
        self.var_cust_nat.set("Select"),
        self.var_cust_add.set("")
        
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))
        
    def search(self):
        conn=mysql.connector.connect(host="localhost", password="Uit54321", user="root",database="hotel_and_motel")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer where "+str(self.var_search.get())+" LIKE '%"+str(self.var_searchby.get())+"%'")
        row=my_cursor.fetchall()
        if len (row)!=0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in row:
                self.cust_details_table.insert("",END,values=i)
                conn.commit()
            conn.close()
        else:
            messagebox.showerror("ERROR 404","Not Found",parent=self.root)
            
    


if __name__ == "__main__":
    root=Tk()
    app=cust_win(root)
    root.mainloop()