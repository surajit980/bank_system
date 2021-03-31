from dbhelper import DBHelper #import database
from tkinter import *  #import tkinter for gui
from tkinter import messagebox
from PIL import ImageTk,Image

class bnk_sys:

    def __init__(self):
        # connect to database
        self.db = DBHelper()
        #gui window function call
        self.load_gui_window(self.load_first_gui)
        self.user_data=None
        self.current_balance=None
        self.user2_data=None
     #gui window here describe gui size title background etc
    def load_gui_window(self,gui_type):
        self.root=Tk()

        self.root.title("GUI Banking System")
        self.root.configure(background="#F8F8F8")

        #gui size declare
        self.root.maxsize(400,600)
        self.root.minsize(400,600)

        gui_type()

        self.root.mainloop()


    #delete old gui and new gui 
    def load_new_gui(self,new_gui):
        self.root.destroy()
        self.load_gui_window(new_gui)


     #first gui function .here show log in and register option
    def load_first_gui(self):
        #image
        #add bank image and resize
        self.photo=Image.open("bank_logo.png")
        self.resize_photo=self.photo.resize((90,90),Image.ANTIALIAS)
        self.resized_photo = ImageTk.PhotoImage(self.resize_photo) 
        #add image in label
        self.label2=Label(self.root,image=self.resized_photo,bg="#F8F8F8")
        self.label2.pack(pady=(130,10))


        self.label3=Label(self.root,text="GUI Banking System",bg="#F8F8F8",fg="#8BA1B7")
        self.label3.pack()
        self.label3.configure(font=("arial rounded MT bold",20))

        #frame for positioning button
        self.f1=Frame(self.root,bg="#F8F8F8")
        self.f1.pack(side=LEFT,padx=(50,0))
        self.f2=Frame(self.root,bg="#F8F8F8")
        self.f2.pack(side=RIGHT,padx=(0,50))
        #button
        self.login_btn=Button(self.f1,text="Log In",bg="#003366",fg="#FFFFFF",command=lambda:self.load_new_gui(self.load_login_input))
        self.login_btn.pack(ipadx=30,ipady=5,pady=(0,130))
        self.login_btn.configure(font=("arial",14))

        self.login_btn=Button(self.f2,text="Register",bg="#003366",fg="#FFFFFF",command=lambda:self.load_new_gui(self.load_register_input))
        self.login_btn.pack(ipadx=20,ipady=5,pady=(0,130))
        self.login_btn.configure(font=("arial",14))


    def load_login_input(self):
        self.label4=Label(self.root,text="LogIn to proceed",bg="#F8F8F8",fg="#8BA1B7")
        self.label4.pack(pady=(50,50))
        self.label4.configure(font=("arial rounded MT bold",20,"bold"))

        self.label5=Label(self.root,text="5-Digits Account Number *",bg="#F8F8F8",fg="#555555")
        self.label5.pack(pady=(10,5))
        self.label5.configure(font=("arial",12,"bold"))

        self.accountnumber1_input=Entry(self.root)
        self.accountnumber1_input.pack(pady=(2,10),ipadx=50,ipady=2)
        self.accountnumber1_input.configure(font=("arial",12))

        self.label6=Label(self.root,text="4-Digits pin *",bg="#F8F8F8",fg="#555555")
        self.label6.pack(pady=(20,5))
        self.label6.configure(font=("arial",12,"bold"))

        self.password1_input=Entry(self.root,show="*")
        self.password1_input.pack(pady=(2,10),ipadx=50,ipady=2)
        self.password1_input.configure(font=("arial",12))

        self.login_btn=Button(text="Log In",bg="#486D90",fg="#FFF6E2",command=lambda:self.login_execute())
        self.login_btn.pack(pady=(70,10),ipadx=80,ipady=5)
        self.login_btn.configure(font=("arial",12))
        
        self.reg_btn=Button(text="New User? /Register here",borderwidth=0,bg="#F8F8F8",fg="#63B5EA",command=lambda:self.load_new_gui(self.load_register_input))
        self.reg_btn.pack()
        self.reg_btn.configure(font=("arial",10))

    def load_register_input(self):
        self.label7=Label(self.root,text="User Driven Registration-New User",bg="#F8F8F8",fg="#8BA1B7")
        self.label7.pack(pady=(50,30))
        self.label7.configure(font=("arial rounded MT bold",12,"bold"))

        self.label8=Label(self.root,text="Full Name *",bg="#F8F8F8",fg="#555555")
        self.label8.pack(pady=(10,5))
        self.label8.configure(font=("arial",12,"bold"))

        self.fullname_input=Entry(self.root)
        self.fullname_input.pack(pady=(2,10),ipadx=50,ipady=2)
        self.fullname_input.configure(font=("arial",12))

        self.label9=Label(self.root,text="Mobile Number *",bg="#F8F8F8",fg="#555555")
        self.label9.pack(pady=(10,5))
        self.label9.configure(font=("arial",12,"bold"))
        
        self.mobilenumber_input=Entry(self.root)
        self.mobilenumber_input.pack(pady=(2,10),ipadx=50,ipady=2)
        self.mobilenumber_input.configure(font=("arial",12))

        self.label5=Label(self.root,text="5-Digits Account Number *",bg="#F8F8F8",fg="#555555")
        self.label5.pack(pady=(10,5))
        self.label5.configure(font=("arial",12,"bold"))

        self.accountnumber2_input=Entry(self.root)
        self.accountnumber2_input.pack(pady=(2,10),ipadx=50,ipady=2)
        self.accountnumber2_input.configure(font=("arial",12))

        self.label10=Label(self.root,text="4-Digits pin *",bg="#F8F8F8",fg="#555555")
        self.label10.pack(pady=(10,5))
        self.label10.configure(font=("arial",12,"bold"))

        self.password2_input=Entry(self.root,show="*")
        self.password2_input.pack(pady=(2,10),ipadx=50,ipady=2)
        self.password2_input.configure(font=("arial",12))

        self.register_btn=Button(text="Register",bg="#486D90",fg="#FFF6E2",command=lambda:self.register_data())
        self.register_btn.pack(pady=(50,10),ipadx=80,ipady=5)
        self.register_btn.configure(font=("arial",12))
        
        self.log_btn=Button(text="already have account? /Log In here",borderwidth=0,bg="#F8F8F8",fg="#63B5EA",command=lambda:self.load_new_gui(self.load_login_input))
        self.log_btn.pack()
        self.log_btn.configure(font=("arial",10))


    #main gui page
    def load_main_gui(self):
        #header menu that is use for menu bar
        menu = Menu(self.root)
        self.root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="Home", menu=filemenu)
        filemenu.add_command(label="My Profile",command=lambda:self.load_new_gui(self.myprofile))
        filemenu.add_command(label="LogOut",command=lambda:self.logOut())
        
        self.label11=Label(self.root,text="     Welcome to, GUI Banking System",bg="#F8F8F8",fg="#8BA1B7")
        self.label11.grid(pady=(50,20),row=0,column=0,columnspan=2)
        self.label11.configure(font=("arial rounded MT bold",14,"bold"))

        #image
        #add bank image and resize
        self.im1=Image.open("main1_logo.png")
        self.img1=self.im1.resize((90,90),Image.ANTIALIAS)
        self.image1 = ImageTk.PhotoImage(self.img1) 
        #add image in button
        self.addmoney_btn=Button(image=self.image1,bg="#CBEFFB",command=lambda:self.load_new_gui(self.add_gui))
        self.addmoney_btn.grid(pady=(20,10),row=1,column=0,ipadx=10,ipady=10,padx=(30,0))

         #image
        #add bank image and resize
        self.im2=Image.open("main2_logo.png")
        self.img2=self.im2.resize((90,90),Image.ANTIALIAS)
        self.image2 = ImageTk.PhotoImage(self.img2) 
        #add image in button
        self.checkbalance_btn=Button(image=self.image2,bg="#CBEFFB",command=lambda:self.load_new_gui(self.checkbal_gui))
        self.checkbalance_btn.grid(pady=(20,10),row=1,column=1,ipadx=10,ipady=10)

         #image
        #add bank image and resize
        self.im3=Image.open("withdrawmoney.png")
        self.img3=self.im3.resize((90,90),Image.ANTIALIAS)
        self.image3 = ImageTk.PhotoImage(self.img3) 
        #add image in button
        self.withdraw_btn=Button(image=self.image3,bg="#CBEFFB",command=lambda:self.load_new_gui(self.withdraw_gui))
        self.withdraw_btn.grid(pady=(20,10),row=2,column=0,ipadx=10,ipady=10,padx=(30,0))

         #image
        #add bank image and resize
        self.im4=Image.open("main4_logo.png")
        self.img4=self.im4.resize((90,90),Image.ANTIALIAS)
        self.imsge4 = ImageTk.PhotoImage(self.img4) 
        #add image in button
        self.sendmoney_btn=Button(image=self.imsge4,bg="#CBEFFB",command=lambda:self.load_new_gui(self.sendmoney_gui))
        self.sendmoney_btn.grid(pady=(20,10),row=2,column=1,ipadx=10,ipady=10)


    #log out function
    def logOut(self):
        self.load_new_gui(self.load_first_gui)
        self.user_data=None
        self.current_balance=None
        self.user2_data=None
    #login execute function
    def login_execute(self):
        acc=self.accountnumber1_input.get()
        password=self.password1_input.get()
        data=self.db.login(acc,password)
        
        self.accountnumber1_input.delete(0,"end")
        self.password1_input.delete(0,"end")
        
        if len(data)==1:
            self.user_data=data[0]
            messagebox.showinfo("login message","you have logged in successfully")
            self.load_new_gui(self.load_main_gui)
        else:           
            messagebox.showerror("login message","incorrect email/password please enter a valid one")

    #register data function
    def register_data(self):
        full_name=self.fullname_input.get()
        mobile_number=self.mobilenumber_input.get()
        account_number=self.accountnumber2_input.get()
        password=self.password2_input.get()
        balance=None
        data=self.db.signin_search(account_number)
        if len(account_number)==5 and len(password)==4:
            if len(data)==1:
                self.accountnumber2_input.delete(0,"end")
                messagebox.showerror("register message","this account number is already taken please enter a new one")
            else: 
                self.db.signin(full_name,mobile_number,account_number,password,balance)
                data=self.db.login(account_number,password)
                self.user_data=data[0]
                messagebox.showinfo("login message","you have logged in successfully")
                self.load_new_gui(self.load_main_gui)
                
        else:
            self.accountnumber2_input.delete(0,"end")
            self.password2_input.delete(0,"end")
            messagebox.showerror("register message","account number must be 5 digits and pin must be 4 digit")


    def myprofile(self):
        #header menu that is use for menu bar
        menu = Menu(self.root)
        self.root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="Home", menu=filemenu)
        filemenu.add_command(label="Main Menu",command=lambda:self.load_new_gui(self.load_main_gui))
        filemenu.add_command(label="LogOut",command=lambda:self.logOut())

        #image
        #add bank image and resize
        self.photo=Image.open("bank_logo.png")
        self.resize_photo=self.photo.resize((60,60),Image.ANTIALIAS)
        self.resized_photo = ImageTk.PhotoImage(self.resize_photo) 
        #add image in label
        self.label2=Label(self.root,image=self.resized_photo,bg="#F8F8F8")
        self.label2.grid(row=0,column=0,columnspan=2,padx=(170,80),pady=(30,10))
        
        self.first_name=self.user_data[0].split()
        self.label1=Label(self.root,text="Hii,"+self.first_name[0],bg="#F8F8F8",fg="#8BA1B7")
        self.label1.grid(row=1,column=0,columnspan=2,padx=(90,0))
        self.label1.configure(font=("arial rounded MT bold",14,"bold"))
        
        self.label9=Label(self.root,text="Full Name : "+self.user_data[0],bg="#F8F8F8",fg="#555555")
        self.label9.grid(pady=(50,10),padx=(90,0),row=2,column=0,columnspan=2)
        self.label9.configure(font=("arial",12,"bold"))

        self.label9=Label(self.root,text="Mobile Number : "+str(self.user_data[1]),bg="#F8F8F8",fg="#555555")
        self.label9.grid(pady=(10,10),row=3,column=0,columnspan=2,padx=(90,0))
        self.label9.configure(font=("arial",12,"bold"))

        self.label9=Label(self.root,text="Account Number : "+str(self.user_data[2]),bg="#F8F8F8",fg="#555555")
        self.label9.grid(pady=(10,10),row=4,column=0,columnspan=2,padx=(90,0))
        self.label9.configure(font=("arial",12,"bold"))

        self.label9=Label(self.root,text="Password : "+str(self.user_data[3]),bg="#F8F8F8",fg="#555555")
        self.label9.grid(pady=(10,10),row=5,column=0,columnspan=2,padx=(90,0))
        self.label9.configure(font=("arial",12,"bold"))


    def add_gui(self):
         #header menu that is use for menu bar
        menu = Menu(self.root)
        self.root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="Home", menu=filemenu)
        filemenu.add_command(label="Main Menu",command=lambda:self.load_new_gui(self.load_main_gui))
        filemenu.add_command(label="LogOut",command=lambda:self.logOut())

        self.label7=Label(self.root,text="Add Money Using Your Pin Number...",bg="#F8F8F8",fg="#8BA1B7")
        self.label7.pack(pady=(50,30))
        self.label7.configure(font=("arial rounded MT bold",12,"bold"))

        self.label8=Label(self.root,text="Enter Amount",bg="#F8F8F8",fg="#555555")
        self.label8.pack(pady=(10,5))
        self.label8.configure(font=("arial",12,"bold"))

        self.amount_input=Entry(self.root)
        self.amount_input.pack(pady=(2,10),ipadx=50,ipady=2)
        self.amount_input.configure(font=("arial",12))

        self.label8=Label(self.root,text="Enter Your Pin Number *",bg="#F8F8F8",fg="#555555")
        self.label8.pack(pady=(10,5))
        self.label8.configure(font=("arial",12,"bold"))

        self.add_pin_input=Entry(self.root,show="*")
        self.add_pin_input.pack(pady=(2,10),ipadx=50,ipady=2)
        self.add_pin_input.configure(font=("arial",12))

        self.add_money_btn=Button(text="Add Money",bg="#486D90",fg="#FFF6E2",command=lambda:self.add_amount())
        self.add_money_btn.pack(pady=(50,10),ipadx=80,ipady=5)
        self.add_money_btn.configure(font=("arial",12))

    def checkbal_gui(self):
        #header menu that is use for menu bar
        menu = Menu(self.root)
        self.root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="Home", menu=filemenu)
        filemenu.add_command(label="Main Menu",command=lambda:self.load_new_gui(self.load_main_gui))
        filemenu.add_command(label="LogOut",command=lambda:self.logOut())

        self.current_balance=self.db.signin_search(self.user_data[2])[0][4]

        self.label7=Label(self.root,text="Check Your Current Balance...",bg="#F8F8F8",fg="#8BA1B7")
        self.label7.pack(pady=(50,30))
        self.label7.configure(font=("arial rounded MT bold",12,"bold"))

        self.label8=Label(self.root,text="Savings account",bg="#F8F8F8",fg="#555555")
        self.label8.pack(pady=(10,5))
        self.label8.configure(font=("arial",14,"bold"))

        self.label8=Label(self.root,text="GUI Banking System",bg="#F8F8F8",fg="#555555")
        self.label8.pack(pady=(10,5))
        self.label8.configure(font=("arial",12))

        self.label8=Label(self.root,text="Account balance",bg="#F8F8F8",fg="#555555")
        self.label8.pack(pady=(10,5))
        self.label8.configure(font=("arial",14,"bold"))

        self.label8=Label(self.root,text="₹ "+str(self.current_balance),bg="#F8F8F8",fg="#555555")
        self.label8.pack(pady=(10,5))
        self.label8.configure(font=("arial",12))


    def withdraw_gui(self):
         #header menu that is use for menu bar
        menu = Menu(self.root)
        self.root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="Home", menu=filemenu)
        filemenu.add_command(label="Main Menu",command=lambda:self.load_new_gui(self.load_main_gui))
        filemenu.add_command(label="LogOut",command=lambda:self.logOut())

        self.label7=Label(self.root,text="Withdraw Money Using Your Pin Number...",bg="#F8F8F8",fg="#8BA1B7")
        self.label7.pack(pady=(50,30))
        self.label7.configure(font=("arial rounded MT bold",12,"bold"))

        self.label8=Label(self.root,text="Enter Amount",bg="#F8F8F8",fg="#555555")
        self.label8.pack(pady=(10,5))
        self.label8.configure(font=("arial",12,"bold"))

        self.wdw_amount_input=Entry(self.root)
        self.wdw_amount_input.pack(pady=(2,10),ipadx=50,ipady=2)
        self.wdw_amount_input.configure(font=("arial",12))

        self.label8=Label(self.root,text="Enter Your Pin Number *",bg="#F8F8F8",fg="#555555")
        self.label8.pack(pady=(10,5))
        self.label8.configure(font=("arial",12,"bold"))

        self.wdw_pin_input=Entry(self.root,show="*")
        self.wdw_pin_input.pack(pady=(2,10),ipadx=50,ipady=2)
        self.wdw_pin_input.configure(font=("arial",12))

        self.wdw_money_btn=Button(text="Withdraw",bg="#486D90",fg="#FFF6E2",command=lambda:self.withdraw_amount())
        self.wdw_money_btn.pack(pady=(50,10),ipadx=80,ipady=5)
        self.wdw_money_btn.configure(font=("arial",12))
        

    def sendmoney_gui(self):
         #header menu that is use for menu bar
        menu = Menu(self.root)
        self.root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="Home", menu=filemenu)
        filemenu.add_command(label="Main Menu",command=lambda:self.load_new_gui(self.load_main_gui))
        filemenu.add_command(label="LogOut",command=lambda:self.logOut())

        self.label7=Label(self.root,text="Send Money To Another Account Number...",bg="#F8F8F8",fg="#8BA1B7")
        self.label7.pack(pady=(50,30))
        self.label7.configure(font=("arial rounded MT bold",12,"bold"))

        self.label8=Label(self.root,text="Enter Receiver Account Number *",bg="#F8F8F8",fg="#555555")
        self.label8.pack(pady=(10,5))
        self.label8.configure(font=("arial",12,"bold"))

        self.send_account_input=Entry(self.root)
        self.send_account_input.pack(pady=(2,10),ipadx=50,ipady=2)
        self.send_account_input.configure(font=("arial",12))

        self.label8=Label(self.root,text="Enter Amount *",bg="#F8F8F8",fg="#555555")
        self.label8.pack(pady=(10,5))
        self.label8.configure(font=("arial",12,"bold"))

        self.send_amount_input=Entry(self.root)
        self.send_amount_input.pack(pady=(2,10),ipadx=50,ipady=2)
        self.send_amount_input.configure(font=("arial",12))

        self.label8=Label(self.root,text="Enter Your Pin Number *",bg="#F8F8F8",fg="#555555")
        self.label8.pack(pady=(10,5))
        self.label8.configure(font=("arial",12,"bold"))

        self.send_pin_input=Entry(self.root,show="*")
        self.send_pin_input.pack(pady=(2,10),ipadx=50,ipady=2)
        self.send_pin_input.configure(font=("arial",12))

        self.send_money_btn=Button(text="Send Money",bg="#486D90",fg="#FFF6E2",command=lambda:self.send_amount())
        self.send_money_btn.pack(pady=(50,10),ipadx=80,ipady=5)
        self.send_money_btn.configure(font=("arial",12))

    def add_amount(self):
        add_pin=self.add_pin_input.get()
        account_number=int(self.user_data[2])
        data=self.db.signin_search(self.user_data[2])
        self.current_balance=data[0][4]
        if int(add_pin)==int(self.user_data[3]):
            balance=int(self.amount_input.get())+int(self.current_balance)
            self.db.add_amount(account_number,balance)
            messagebox.showinfo("add money","your money added sucessfully")
            self.current_balance=int(self.db.signin_search(self.user_data[2])[0][4])
            self.add_pin_input.delete(0,"end")
            self.amount_input.delete(0,"end")
            self.load_new_gui(self.load_main_gui)
        else:
            messagebox.showerror("add money","you entered a wrong pin please enter correctly")
            self.add_pin_input.delete(0,"end")
        
    
    def withdraw_amount(self):
        if int(self.wdw_pin_input.get())==int(self.user_data[3]):
            data=self.db.signin_search(self.user_data[2])
            self.current_balance=int(data[0][4])
            if self.current_balance>int(self.wdw_amount_input.get()):
                balance=int(self.current_balance)-int(self.wdw_amount_input.get())
                self.db.add_amount(self.user_data[2],balance)
                messagebox.showinfo("withdraw money","your money withdraw sucessfully")
                self.load_new_gui(self.load_main_gui)
            else:
                messagebox.showerror("withdraw money","sorry we cannot proceed your transaction bacause your money is lessthan {}".format(self.wdw_amount_input.get()))
                self.wdw_amount_input.delete(0,"end")
                self.wdw_pin_input.delete(0,"end")
        else:
            messagebox.showerror("withdraw money","you entered a wrong pin please enter correctly")
            self.wdw_pin_input.delete(0,"end")

    def send_amount(self):
        data1=self.db.signin_search(self.send_account_input.get())
        if len(data1)==1:
            if int(self.send_pin_input.get())==int(self.user_data[3]):
                data=self.db.signin_search(self.user_data[2])
                self.current_balance=int(data[0][4])
                if self.current_balance>int(self.send_amount_input.get()):
                    balance=int(self.current_balance)-int(self.send_amount_input.get())
                    self.db.add_amount(self.user_data[2],balance)
                    messagebox.showinfo("send money","your money send sucessfully")
                    data1=self.db.signin_search(self.send_account_input.get())
                    self.user2_data=int(data1[0][4])+int(self.send_amount_input.get())
                    self.db.add_amount(data1[0][2],self.user2_data)
                    self.load_new_gui(self.load_main_gui)
                else:
                    messagebox.showerror("send money","sorry we cannot proceed your transaction bacause your money is less than {}".format(self.send_amount_input.get()))
                    self.send_pin_input.delete(0,"end")
                    self.send_amount_input.delete(0,"end")
            else:
                messagebox.showerror("send money","you entered a wrong pin please enter correctly")
                self.send_pin_input.delete(0,"end")
        else:
            messagebox.showerror("send money","you entered a wrong account number please enter correctly")
            self.send_account_input.delete(0,"end")
surajit = bnk_sys()

