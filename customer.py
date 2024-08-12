from tkinter import*
from tkinter import ttk
import random 
import mysql.connector 
from tkinter import messagebox


class Cust_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("Resort Management System")
        self.root.geometry("1655x740+230+240")
        
        
        
        
        self.var_ref=StringVar()
        x=random. randint (1000,9999)
        
        self.var_ref.set(str(x))
        self.var_cust_name=StringVar()
        self.var_gender=StringVar()
        self.var_phone=StringVar()
        self.var_email=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()
        self.var_adderss=StringVar()


        #guest page title==============================
        lbl1_title=Label(self.root, text="Add Guest Details",font=("arial",15 , "bold"), bg="black", fg="#77c53a",bd=4,relief=RIDGE)
        lbl1_title.place(x=0,y=0,width=1655, height=40)

        #Left frame============================================
        labelframeleft=Frame(self.root,bd=4, relief=RIDGE)
        labelframeleft.place(x=0,y=35,width=425, height=490)

        #Frame details: Name,ID etc==============================================

        lb1_cust_ref=Label(labelframeleft, text="Customer Ref", font=("arial", 12, "bold"), padx=2, pady=6)
        lb1_cust_ref.grid(row=0, column=0, sticky=W)
        enty_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref, font=("arial",13, "bold"),width=29,state="readonly")
        enty_ref.grid(row=0, column=1)
        
        name=Label(labelframeleft, text="Name", font=("arial", 12, "bold"), padx=2, pady=6)
        name.grid(row=1, column=0, sticky=W)
        nametxt=ttk.Entry(labelframeleft,textvariable=self.var_cust_name, font=("arial",13, "bold"),width=29)
        nametxt.grid(row=1, column=1)
        
        label_gender=Label(labelframeleft, font=("arial",12, "bold"), text="Sex", padx=2, pady=6)
        label_gender.grid(row=2, column=0, sticky=W)
        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender, font=("arial", 12, "bold") ,width=27, state="readonly" )
        combo_gender ["value" ]= ("Male", "Female")
        combo_gender. current (0)
        combo_gender. grid (row=2, column=1)
        
        
        address=Label(labelframeleft, text="Address", font=("arial", 12, "bold"), padx=2, pady=6)
        address.grid(row=3, column=0, sticky=W)
        addresstxt=ttk.Entry(labelframeleft,textvariable=self.var_adderss, font=("arial",13, "bold"),width=29)
        addresstxt.grid(row=3, column=1)
        
        
        phn=Label(labelframeleft, text="Phone Number", font=("arial", 12, "bold"), padx=2, pady=6)
        phn.grid(row=4, column=0, sticky=W)
        phntxt=ttk.Entry(labelframeleft,textvariable=self.var_phone, font=("arial",13),width=29)
        phntxt.grid(row=4, column=1)
        
        #Email===========
        phn2=Label(labelframeleft, text="Email", font=("arial", 12, "bold"), padx=2, pady=6)
        phn2.grid(row=5, column=0, sticky=W)
        phntxt2=ttk.Entry(labelframeleft,textvariable=self.var_email, font=("arial",13),width=29)
        phntxt2.grid(row=5, column=1)

        #Id type=======
        lblIdProof=Label(labelframeleft, font=("arial", 12, "bold"), text="Id Proof Type:", padx=2, pady=6)
        lblIdProof.grid(row=6, column=0, sticky=W)
        combo_id=ttk.Combobox(labelframeleft,textvariable=self.var_id_proof,font=("arial",12,"bold"),width=27, state="readonly")
        combo_id["value"]=("NID", "Driving Licence", "Passport")
        combo_id. current(0)
        combo_id. grid(row=6, column= 1)
        
        #Id number=======
        name=Label(labelframeleft, text="ID number", font=("arial", 12, "bold"), padx=2, pady=6)
        name.grid(row=7, column=0, sticky=W)
        nametxt=ttk.Entry(labelframeleft,textvariable=self.var_id_number, font=("arial",13, "bold"),width=29)
        nametxt.grid(row=7, column=1)
        
        
        
        #Button Frame=============================
        btn_frame=Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412, height=40)
        
        btnAdd=Button(btn_frame, text="Add",command=self.add_data, font=("arial", 11, "bold"), bg="black", fg="#77c53a", width=10)
        btnAdd .grid(row=0,column=0,padx=1)
        btnUpdate=Button(btn_frame, text="Update",command=self.update,font=("arial", 11, "bold"), bg="black", fg="#77c53a", width=10)
        btnUpdate.grid(row=0,column=1, padx=1)
        btnDelete=Button(btn_frame, text="Delete",command=self.mDelete , font=("arial", 11, "bold"), bg="black", fg="#77c53a", width=10)
        btnDelete.grid(row=0, column=2, padx=1)
        btnReset=Button(btn_frame, text="Reset",command=self.reset, font=("arial", 11, "bold"), bg="black", fg="#77c53a", width=10)
        btnReset. grid(row=0, column=3,padx=1)

        
        
        #VIEW DETAILS FRAME ON RIGHT ======Search System
        Table_Frame=LabelFrame(self.root, bd=2, relief=RIDGE, text="View Deatils And Search", font= ("arial", 12,'bold'),padx=2)
        Table_Frame.place(x=435,y=50, width=1220,height=490)
        
        lblSearchBy=Label (Table_Frame, font=("arial", 12,"bold"), text="Search By:", bg="red", fg="white" )
        lblSearchBy.grid(row=0, column=0, sticky=W,padx=2)
        
        self.search_var=StringVar()
        combo_Serach=ttk.Combobox(Table_Frame,textvariable=self.search_var, font=("arial", 12, "bold") ,width=24, state="readonly" )
        combo_Serach["value"]= ("Phone", "Ref" )
        combo_Serach. current(0)
        combo_Serach.grid(row=0, column=1, padx=2)
        
        self.txt_search=StringVar()
        txtSearch=ttk. Entry(Table_Frame,textvariable=self.txt_search, font=("arial",13, "bold" ),width=24)
        txtSearch.grid(row=0, column=2, padx=2)
        
        
        btnSearch=Button(Table_Frame,command=self.search, text="Search",font=("arial",11, "bold"), bg="black", fg="#77c53a", width=10)
        btnSearch.grid(row=0, column=3,padx=1)
        btnShowAll=Button(Table_Frame,command=self.fetch_data, text="Show All", font=("arial", 11, "bold"), bg="black", fg="#77c53a", width=10)
        btnShowAll.grid(row=0, column=4, padx=1)
        
        
        #Data table showwwww=========================================
        details_table=Frame(Table_Frame, bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=1220, height=420)
        
        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        
        self.Cust_Details_Table=ttk. Treeview(details_table,column=("ref","name","gender","phone","email","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x. pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x. config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)
        
        
        self.Cust_Details_Table.heading("ref", text="Refer No")
        self.Cust_Details_Table.heading("name", text="Name")
        self.Cust_Details_Table.heading ("gender", text="Gender")
        self.Cust_Details_Table.heading("phone", text="phone")
        self.Cust_Details_Table.heading("email" ,text="Email")
        self.Cust_Details_Table.heading("idproof", text="Id Proof")
        self.Cust_Details_Table.heading ("idnumber", text="Id Number")
        self.Cust_Details_Table.heading ("address", text="Address")
       
        self.Cust_Details_Table["show" ]="headings"
        self.Cust_Details_Table.pack(fill=BOTH, expand=1)
        
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cuersor)
        
        
        self.fetch_data()
        
        
        
    def add_data(self) :
        if self.var_phone.get()=="" or self.var_cust_name.get()=="" or self.var_gender.get()=="" or self.var_email.get()=="" or self.var_id_number.get()=="" :
            messagebox. showerror("Error","All fields are required")
            
        else:
            try:
                conn=mysql. connector. connect(host="localhost", username="sourav",password="WowSql/69#@", database="resort_management")
                my_cursor=conn. cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s)",
                                (self.var_ref.get(),
                                self.var_cust_name.get(),
                                self.var_gender.get(),
                                self.var_phone.get(),
                                self.var_email.get(),
                                self.var_id_proof.get(),
                                self.var_id_number.get(),
                                self.var_adderss.get()    
                                
                                ))
                                                                       
                
                conn.commit()
                self.fetch_data()
                conn.close()                   
                messagebox.showinfo("Success", "customer has been added", parent=self.root)
            except Exception as es:
                messagebox. showwarning ("Warning", f"Some thing went wrong: {str(es)}",parent=self.root)                                           
    
    
    def fetch_data(self):
        conn=mysql. connector. connect(host="localhost", username="sourav",password="WowSql/69#@", database="resort_management")
        my_cursor=conn. cursor()
        my_cursor.execute("select * from customer")
        
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("", END,values=i)
            conn.commit()
        conn.close()
        
        
    def get_cuersor(self, event=""):
        cursor_row=self.Cust_Details_Table. focus()
        content=self.Cust_Details_Table.item(cursor_row)
        row=content ["values"]
        self.var_ref.set (row[0]),
        self.var_cust_name.set (row[1]),
        self.var_gender.set (row[2]),
        self.var_phone.set(row[3]),
        self.var_email.set(row[4]),
        self.var_id_proof.set(row[5]),
        self.var_id_number.set (row[6]),
        self.var_adderss.set(row[7])
        
    
    def update (self) :
        if self.var_phone.get()=="":
            messagebox. showerror ("Error", "Please enter mobile number",parent=self.root)
        else:
            conn=mysql. connector. connect(host="localhost", username="sourav",password="WowSql/69#@", database="resort_management")
            my_cursor=conn.cursor()
            my_cursor. execute("UPDATE customer SET name=%s, gender=%s, phone=%s, email=%s, idproof=%s, idnumber=%s, address=%s WHERE ref=%s",(
                                
                                self.var_cust_name.get(),
                                self.var_gender.get(),
                                self.var_phone.get(),
                                self.var_email.get(),
                                self.var_id_proof.get(),
                                self.var_id_number.get(),
                                self.var_adderss.get(),
                                self.var_ref.get()
                
                
                
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Information updated successfully!",parent=self.root)
    
    
    
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System", "Do you want delete this customer", parent=self.root)
        if mDelete>0:
            conn=mysql. connector. connect(host="localhost", username="sourav",password="WowSql/69#@", database="resort_management")
            my_cursor=conn.cursor()
            query="delete from customer WHERE ref=%s"
            value=(self.var_ref.get(),)
            my_cursor. execute(query, value)
        else:
            if not mDelete:
                return
        conn. commit ()
        self.fetch_data()
        conn. close()
        


    def reset(self):
        self.var_cust_name.set(""),
        self.var_phone.set(""),
        self.var_email.set(""),
        self.var_id_number.set(""),
        self.var_adderss.set("")
       
        x=random. randint (1000,9999)
        self.var_ref.set(str(x))
                                
    
    
    def search(self):
        conn=mysql. connector. connect(host="localhost", username="sourav",password="WowSql/69#@", database="resort_management")
        my_cursor=conn. cursor()
        my_cursor.execute("SELECT * from customer WHERE "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self .Cust_Details_Table.insert ("",END,values=i)
            conn.commit()
        conn. close()                          




if __name__ == "__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()