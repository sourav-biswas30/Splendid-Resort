from tkinter import*
from PIL import Image, ImageTk
from customer import Cust_Win
from room import Roombooking


class ResortManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title('Resort Management System')
        self.root.geometry('1550x800+0+0')

        #IMage adding======================================
        img1 = Image.open(r"F:\Bohubrihi app\RMS\images\resort2.jpeg")
        img1 = img1.resize((1950, 150), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        # Create and place a label to display the image
        lbling = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lbling.place(x=0, y=0, width=1950, height=150)



            
        lbl_title=Label(self.root, text="Splendid Resort",font=("arial", 40, "bold"), bg="black", fg="#77c53a",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=150,width=1950, height=50)
        #ESSESSEE
        #######main Framessess
        main_frame=Frame(self.root,bd=4, relief=RIDGE)
        main_frame.place(x=0,y=200,width=1920, height=800)


        menu=Label(main_frame, text="Menu",font=("arial", 20, "bold"), bg="black", fg="#77c53a",bd=3,relief=RIDGE)
        menu.place(x=0,y=0,width=230)

        #Button frame
        button_frame=Frame(main_frame,bd=4, relief=RIDGE)
        button_frame.place(x=0,y=35,width=228, height=190)

        cust_btn=Button(button_frame, text="Guest",command=self.cust_details,width=20,font=("arial", 14, "bold"), bg="black", fg="#77c53a",bd=0,cursor='hand2')
        cust_btn.grid(row=0, column=0,pady=1)

        room_btn=Button(button_frame,command=self.roombooking, text="Rooms/Cottages",width=20,font=("arial", 14, "bold"), bg="black", fg="#77c53a",bd=0,cursor='hand2')
        room_btn.grid(row=1, column=0,pady=1)

        details_btn=Button(button_frame, text="Details",width=20,font=("arial", 14, "bold"), bg="black", fg="#77c53a",bd=0,cursor='hand2')
        details_btn.grid(row=2, column=0,pady=1)

        report_btn=Button(button_frame, text="Report",width=20,font=("arial", 14, "bold"), bg="black", fg="#77c53a",bd=0,cursor='hand2')
        report_btn.grid(row=3, column=0,pady=1)

        logout_btn=Button(button_frame, text="Logout",width=20,font=("arial", 14, "bold"), bg="black", fg="#77c53a",bd=0,cursor='hand2')
        logout_btn.grid(row=4, column=0,pady=1)


        #Main Image adding=====================================================
        img2 = Image.open(r"F:\Bohubrihi app\RMS\images\image2.jpg")
        img2 = img2.resize((1680, 790), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lbling2 = Label(main_frame, image=self.photoimg2, bd=4, relief=RIDGE)
        lbling2.place(x=225, y=0, width=1680, height=790)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window)
        
    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)
       
        
        



if __name__ == "__main__":
    root = Tk()
    obj = ResortManagementSystem(root)
    root.mainloop()
