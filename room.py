from tkinter import*
from tkinter import ttk
import random 
import mysql.connector 
from tkinter import messagebox
from time import strftime
from datetime import datetime


class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Resort Management System")
        self.root.geometry("1655x740+230+240")
        
        #==================variables========================
        self.var_conatct=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()
        
        
        
        
        #guest page title==============================
        lbl1_title=Label(self.root, text="Room/Cottage Booking",font=("arial",15 , "bold"), bg="black", fg="#77c53a",bd=4,relief=RIDGE)
        lbl1_title.place(x=0,y=0,width=1655, height=40)

        #Left frame============================================
        labelframeleft=Frame(self.root,bd=4, relief=RIDGE)
        labelframeleft.place(x=0,y=35,width=425, height=490)
        
        #Contact
        lb1_cust_contact=Label(labelframeleft, text="Customer Contact", font=("arial", 12, "bold"), padx=2, pady=6)
        lb1_cust_contact.grid(row=0, column=0, sticky=W)
        enty_contact=ttk.Entry(labelframeleft,textvariable=self.var_conatct, font=("arial",13, "bold"),width=20,state="normal")
        enty_contact.grid(row=0, column=1,sticky=W)
        #Fetch Data button
        btnFetch=Button(labelframeleft,command=self.Fetch_contact, text="Fetch Data", font=("arial", 8, "bold"), bg="black", fg="#77c53a", width=8)
        btnFetch .place(x=350, y=4)
        
        #Checkin
        check_in_date=Label(labelframeleft, text="Check-in Date", font=("arial", 12, "bold"), padx=2, pady=6)
        check_in_date.grid(row=1, column=0, sticky=W)
        enty_checkin=ttk.Entry(labelframeleft,textvariable=self.var_checkin,font=("arial",13, "bold"),width=29,state="normal")
        enty_checkin.grid(row=1, column=1)
        
        #Checkout
        check_out_date=Label(labelframeleft, text="Check-out Date", font=("arial", 12, "bold"), padx=2, pady=6)
        check_out_date.grid(row=2, column=0, sticky=W)
        enty_checkout=ttk.Entry(labelframeleft,textvariable=self.var_checkout,font=("arial",13, "bold"),width=29,state="normal")
        enty_checkout.grid(row=2, column=1)
        
        #Room Type
        room_type=Label(labelframeleft, text="Room Type", font=("arial", 12, "bold"), padx=2, pady=6)
        room_type.grid(row=3, column=0, sticky=W)
       # enty_room_type=ttk.Entry(labelframeleft, font=("arial",13, "bold"),width=29,state="readonly")
        #enty_room_type.grid(row=3, column=1)
        combo_RoomType=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype, font=("arial",12, "bold"), width=27, state="readonly")
        combo_RoomType ["value" ]=("Single", "Double", "luxary")
        combo_RoomType. current (0)
        combo_RoomType.grid(row=3, column=1)
        
        
        #Available Room
        available_room=Label(labelframeleft, text="Available Room", font=("arial", 12, "bold"), padx=2, pady=6)
        available_room.grid(row=4, column=0, sticky=W)
        enty_available=ttk.Entry(labelframeleft,textvariable=self.var_roomavailable, font=("arial",13, "bold"),width=29,state="normal")
        enty_available.grid(row=4, column=1)
        
        #Meal
        meal=Label(labelframeleft, text="Meal", font=("arial", 12, "bold"), padx=2, pady=6)
        meal.grid(row=5, column=0, sticky=W)
        enty_meal=ttk.Entry(labelframeleft,textvariable=self.var_meal, font=("arial",13, "bold"),width=29,state="normal")
        enty_meal.grid(row=5, column=1)
        
        #No of days
        days=Label(labelframeleft, text="No of days", font=("arial", 12, "bold"), padx=2, pady=6)
        days.grid(row=6, column=0, sticky=W)
        enty_days=ttk.Entry(labelframeleft,textvariable=self.var_noofdays, font=("arial",13, "bold"),width=29,state="normal")
        enty_days.grid(row=6, column=1)
        
        #PAid Tax
        tax=Label(labelframeleft, text="Paid Tax", font=("arial", 12, "bold"), padx=2, pady=6)
        tax.grid(row=7, column=0, sticky=W)
        enty_tax=ttk.Entry(labelframeleft,textvariable=self.var_paidtax, font=("arial",13, "bold"),width=29,state="normal")
        enty_tax.grid(row=7, column=1)
        
        #Sub Total
        sub_total=Label(labelframeleft, text="Sub Total", font=("arial", 12, "bold"), padx=2, pady=6)
        sub_total.grid(row=8, column=0, sticky=W)
        enty_sub=ttk.Entry(labelframeleft,textvariable=self.var_actualtotal, font=("arial",13, "bold"),width=29,state="normal")
        enty_sub.grid(row=8, column=1)
        
        #Total Cost
        total=Label(labelframeleft, text="Total Cost", font=("arial", 12, "bold"), padx=2, pady=6)
        total.grid(row=9, column=0, sticky=W)
        enty_total=ttk.Entry(labelframeleft,textvariable=self.var_total, font=("arial",13, "bold"),width=29,state="normal")
        enty_total.grid(row=9, column=1)
        
        #Bill Buttttton ===========================
        btnBill=Button(labelframeleft, text="Bill",command=self.total, font=("arial", 11, "bold"), bg="black", fg="#77c53a", width=10)
        btnBill .grid(row=10,column=0,padx=1,sticky=W)
        
        
        #=======================Button Frame=============================
        btn_frame=Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412, height=40)
        
        btnAdd=Button(btn_frame, text="Add",command=self.add_data, font=("arial", 11, "bold"), bg="black", fg="#77c53a", width=10)
        btnAdd .grid(row=0,column=0,padx=1)
        btnUpdate=Button(btn_frame, text="Update", command=self.update,font=("arial", 11, "bold"), bg="black", fg="#77c53a", width=10)
        btnUpdate.grid(row=0,column=1, padx=1)
        btnDelete=Button(btn_frame, text="Delete",command=self.mDelete, font=("arial", 11, "bold"), bg="black", fg="#77c53a", width=10)
        btnDelete.grid(row=0, column=2, padx=1)
        btnReset=Button(btn_frame, text="Reset",command=self.reset, font=("arial", 11, "bold"), bg="black", fg="#77c53a", width=10)
        btnReset. grid(row=0, column=3,padx=1)
        
        
        
         #=====================VIEW DETAILS FRAME ON RIGHT ======Search System
        Table_Frame=LabelFrame(self.root, bd=2, relief=RIDGE, text="View Deatils And Search", font= ("arial", 12,'bold'),padx=2)
        Table_Frame.place(x=435,y=280, width=1220,height=260)
        
        lblSearchBy=Label (Table_Frame, font=("arial", 12,"bold"), text="Search By:", bg="red", fg="white" )
        lblSearchBy.grid(row=0, column=0, sticky=W,padx=2)
        
        self.search_var=StringVar()
        combo_Serach=ttk.Combobox(Table_Frame,textvariable=self.search_var, font=("arial", 12, "bold") ,width=24, state="readonly" )
        combo_Serach["value"]= ("Contact", "roomavailable" )
        combo_Serach. current(0)
        combo_Serach.grid(row=0, column=1, padx=2)
        
        self.txt_search=StringVar()
        txtSearch=ttk. Entry(Table_Frame,textvariable=self.txt_search, font=("arial",13, "bold" ),width=24)
        txtSearch.grid(row=0, column=2, padx=2)
        
        
        btnSearch=Button(Table_Frame, text="Search",command=self.search,font=("arial",11, "bold"), bg="black", fg="#77c53a", width=10)
        btnSearch.grid(row=0, column=3,padx=1)
        btnShowAll=Button(Table_Frame, text="Show All", font=("arial", 11, "bold"), bg="black", fg="#77c53a", width=10)
        btnShowAll.grid(row=0, column=4, padx=1)
        
        
        #Data table showwwww=========================================
        details_table=Frame(Table_Frame, bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=1220, height=180)
        
        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        
        self.Cust_Details_Table=ttk. Treeview(details_table,column=("contact","checkin","checkout","roomtype","roomavailable","meal","noOfdays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x. pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x. config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)
        
        
        self.Cust_Details_Table.heading("contact", text="Phone")
        self.Cust_Details_Table.heading("checkin", text="Check-in")
        self.Cust_Details_Table.heading ("checkout", text="Check-out")
        self.Cust_Details_Table.heading("roomtype", text="Room Type")
        self.Cust_Details_Table.heading("roomavailable" ,text="Room No")
        self.Cust_Details_Table.heading("meal", text="Meal")
        self.Cust_Details_Table.heading ("noOfdays", text="Number Of Days")
        #self.Cust_Details_Table.heading ("address", text="Address")
       
        self.Cust_Details_Table["show" ]="headings"
        self.Cust_Details_Table.pack(fill=BOTH, expand=1)
        
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cuersor)
        self.fetch_data()
        
        
        
    #==============AllDAta Fetchhhhh====================    
    def Fetch_contact(self) :
        if self.var_conatct.get()=='' :
            messagebox. showerror ("Error", "Plaese enter Contact Number",parent=self.root)
        else:
            conn=mysql. connector. connect(host="localhost", username="sourav",password="WowSql/69#@", database="resort_management")
            my_cursor=conn. cursor()
            query=("select name from customer where phone=%s")
            value=(self.var_conatct.get() ,)
            my_cursor. execute(query, value)
            row=my_cursor. fetchone()
            if row==None:
                messagebox. showerror ("Error", "This number Not Found",parent=self.root)
            else:
                conn.commit()
                conn.close()
            
                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=455,y=55,width=300,height=180)
                
                lblName=Label (showDataframe, text="Name:", font=("arial", 12, "bold") )
                lblName. place(x=0, y=0)  
                
                lb1=Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lb1. place(x=90, y=0)
                
                #Email========================
                conn=mysql. connector. connect(host="localhost", username="sourav",password="WowSql/69#@", database="resort_management")
                my_cursor=conn. cursor()
                query=("select email from customer where phone=%s")
                value=(self.var_conatct.get() ,)
                my_cursor. execute(query, value)
                row=my_cursor. fetchone()
                
                lblemail=Label (showDataframe, text="Email:", font=("arial", 12, "bold") )
                lblemail. place(x=0, y=30)  
                
                lb12=Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lb12. place(x=90, y=30)
                
                #idproof===================
                conn=mysql. connector. connect(host="localhost", username="sourav",password="WowSql/69#@", database="resort_management")
                my_cursor=conn. cursor()
                query=("select idproof from customer where phone=%s")
                value=(self.var_conatct.get() ,)
                my_cursor. execute(query, value)
                row=my_cursor. fetchone()
                
                lblidtype=Label (showDataframe, text="ID Type:", font=("arial", 12, "bold") )
                lblidtype. place(x=0, y=60)  
                
                lb13=Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lb13. place(x=90, y=60)
                
                #idnumber===========================================
                conn=mysql. connector. connect(host="localhost", username="sourav",password="WowSql/69#@", database="resort_management")
                my_cursor=conn. cursor()
                query=("select idnumber from customer where phone=%s")
                value=(self.var_conatct.get() ,)
                my_cursor. execute(query, value)
                row=my_cursor. fetchone()
                
                lblidnum=Label (showDataframe, text="ID Num:", font=("arial", 12, "bold") )
                lblidnum. place(x=0, y=90)  
                
                lb14=Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lb14. place(x=90, y=90)
                
                #Address================================
                conn=mysql. connector. connect(host="localhost", username="sourav",password="WowSql/69#@", database="resort_management")
                my_cursor=conn. cursor()
                query=("select address from customer where phone=%s")
                value=(self.var_conatct.get() ,)
                my_cursor. execute(query, value)
                row=my_cursor. fetchone()
                
                lblAddress=Label (showDataframe, text="Address:", font=("arial", 12, "bold") )
                lblAddress. place(x=0, y=120)  
                
                lb15=Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lb15. place(x=90, y=120)
                

    def add_data(self):
        if self.var_conatct.get() == "" or self.var_checkin.get() == "" or self.var_checkout.get() == "" or self.var_roomtype.get() == "" or self.var_roomavailable.get() == "" or self.var_meal.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
            # Connect to the database
                conn = mysql.connector.connect(host="localhost", username="sourav", password="WowSql/69#@", database="resort_management")
                my_cursor = conn.cursor()
                
                # Execute the insert query
                my_cursor.execute("INSERT INTO room (Contact, check_in, check_out, roomtype, roomavailable, meal,noOfdays) VALUES (%s, %s, %s, %s, %s, %s,%s)", (
                    self.var_conatct.get(),
                    self.var_checkin.get(),
                    self.var_checkout.get(),
                    self.var_roomtype.get(),
                    self.var_roomavailable.get(),
                    self.var_meal.get(),
                    self.var_noofdays.get()
                ))
                
                # Commit the transaction
                conn.commit()
                self.fetch_data()
                conn.close()  # Close the connection
                
                # Show success message
                messagebox.showinfo("Success", "Room has been added", parent=self.root)
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Database error: {str(err)}", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}", parent=self.root)

    
    
    def fetch_data(self):
        conn=mysql. connector. connect(host="localhost", username="sourav",password="WowSql/69#@", database="resort_management")
        my_cursor=conn. cursor()
        my_cursor.execute("select * from room")
        
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("", END,values=i)
            conn.commit()
        conn.close()  


    def get_cuersor (self, event=""):
        cuersor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cuersor_row)
        row=content ["values"]
        
        self.var_conatct.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set (row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal. set(row[5])
        self.var_noofdays.set (row[6])


    def update(self):
        if self.var_conatct.get() == "":
            messagebox.showerror("Error", "Please enter mobile number", parent=self.root)
            

        else:
            # Connect to the database
            conn = mysql.connector.connect(host="localhost", username="sourav", password="WowSql/69#@", database="resort_management")
            my_cursor = conn.cursor()
            
            # Execute the update query
            my_cursor.execute("UPDATE room SET check_in=%s, check_out=%s, roomtype=%s, roomavailable=%s, meal=%s, noOfDays=%s WHERE Contact=%s",
                            (
                                self.var_checkin.get(),
                                self.var_checkout.get(),
                                self.var_roomtype.get(),
                                self.var_roomavailable.get(),
                                self.var_meal.get(),
                                self.var_noofdays.get(),
                                self.var_conatct.get()
                            ))
            
            # Commit the transaction
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Room Details have been updated successfully!", parent=self.root)
            
        
            
    def mDelete(self):
        mDelete=messagebox.askyesno("Resort Management System", "Do you want delete this Room?", parent=self.root)
        if mDelete>0:
            conn=mysql. connector. connect(host="localhost", username="sourav",password="WowSql/69#@", database="resort_management")
            my_cursor=conn.cursor()
            query="delete from room WHERE Contact=%s"
            value=(self.var_conatct.get(),)
            my_cursor. execute(query, value)
        else:
            if not mDelete:
                return
        conn. commit ()
        self.fetch_data()
        conn. close()  


    def reset(self):
        self.var_conatct.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_meal.set(""),
        self.var_roomavailable.set("")
        self.var_roomtype.set("")
        self.var_noofdays.set("")
        
        
    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate, "%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate).days)
        
        if (self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="luxary"):
            
       
            ql=float (150) #Breakfast 150 taka
            q2=float(2000) # Luxary room 2k per day
            q3=float(self.var_noofdays. get())
            q4=float (ql+q2) #Per day
            q5=float (q3*q4) #Total cost
            Tax="BDT. "+str ("%.2f"%((q5) *0.09))
            ST="BDT. "+str ("%.2f"%((q5)))
            TT="BDT. "+str ("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax. set (Tax)
            self.var_actualtotal. set(ST)
            self.var_total.set(TT)
            
        if ((self.var_meal.get()=="Lunch" or "Dinner") and self.var_roomtype.get()=="luxary"):
            
       
            ql=float (300) # LUNCH and DInner duitai 300 kore
            q2=float(2000)
            q3=float(self.var_noofdays. get())
            q4=float (ql+q2) #Per day
            q5=float (q3*q4) #Total cost
            Tax="BDT. "+str ("%.2f"%((q5) *0.09))
            ST="BDT. "+str ("%.2f"%((q5)))
            TT="BDT. "+str ("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax. set (Tax)
            self.var_actualtotal. set(ST)
            self.var_total.set(TT)
            
        if (self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Double"):
            
       
            ql=float (150) 
            q2=float(1200)
            q3=float(self.var_noofdays. get())
            q4=float (ql+q2) #Per day
            q5=float (q3*q4) #Total cost
            Tax="BDT. "+str ("%.2f"%((q5) *0.09))
            ST="BDT. "+str ("%.2f"%((q5)))
            TT="BDT. "+str ("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax. set (Tax)
            self.var_actualtotal. set(ST)
            self.var_total.set(TT)
            
        if ((self.var_meal.get()=="Lunch" or "Dinner") and self.var_roomtype.get()=="Double"):
            
       
            ql=float (300) 
            q2=float(1200)
            q3=float(self.var_noofdays. get())
            q4=float (ql+q2) #Per day
            q5=float (q3*q4) #Total cost
            Tax="BDT. "+str ("%.2f"%((q5) *0.09))
            ST="BDT. "+str ("%.2f"%((q5)))
            TT="BDT. "+str ("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax. set (Tax)
            self.var_actualtotal. set(ST)
            self.var_total.set(TT)
            
            
        if (self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Single"):
            
       
            ql=float (150) 
            q2=float(800)
            q3=float(self.var_noofdays. get())
            q4=float (ql+q2) #Per day
            q5=float (q3*q4) #Total cost
            Tax="BDT. "+str ("%.2f"%((q5) *0.09))
            ST="BDT. "+str ("%.2f"%((q5)))
            TT="BDT. "+str ("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax. set (Tax)
            self.var_actualtotal. set(ST)
            self.var_total.set(TT)
            
        if ((self.var_meal.get()=="Lunch" or "Dinner") and self.var_roomtype.get()=="Single"):
            
       
            ql=float (300) 
            q2=float(800)
            q3=float(self.var_noofdays. get())
            q4=float (ql+q2) #Per day
            q5=float (q3*q4) #Total cost
            Tax="BDT. "+str ("%.2f"%((q5) *0.09))
            ST="BDT. "+str ("%.2f"%((q5)))
            TT="BDT. "+str ("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax. set (Tax)
            self.var_actualtotal. set(ST)
            self.var_total.set(TT)
           
       
    def search(self):
        conn=mysql. connector. connect(host="localhost", username="sourav",password="WowSql/69#@", database="resort_management")
        my_cursor=conn. cursor()
        my_cursor.execute("SELECT * from room WHERE "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self .Cust_Details_Table.insert ("",END,values=i)
            conn.commit()
        conn. close()           
    


    

if __name__ == "__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()