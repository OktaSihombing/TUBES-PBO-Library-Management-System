import tkinter as tk
import time
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql
from datetime import datetime, timedelta
from dateutil.relativedelta import *

mypass = ""
mydatabase="library_system"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()
cur.execute("select * from items")
current_balance = 1000

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.shared_data = {'Balance':tk.IntVar()}
        container = tk.Frame(self)
        my_tree = ttk.Treeview(self)

        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, Lending, ReturnBook, BorrowBook, MainLibraryAdmin, MainLibraryStudent,Kelola, SigninStudent, SigninAdmin, MenuStudent, MenuAdmin, LoginAdmin, LoginStudent):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        space_label = tk.Label(self, height=7)
        space_label.pack()

        logopilih = tk.PhotoImage(file="pilih.png")
        logopilih_label = tk.Label(self, image=logopilih)
        logopilih_label.image = logopilih
        logopilih_label.pack()

        space_label = tk.Label(self, height=1)
        space_label.pack()

        admin = tk.PhotoImage(file="subscriber.png")
        admin_label = tk.Label(self, image=admin)
        admin_label.image = admin

        def MenuAdmin():
            controller.show_frame('MenuAdmin')
           
        masuk_button = tk.Button(self,image=admin,command=MenuAdmin,border=0)
        masuk_button.place(x=350, y=450)

        student = tk.PhotoImage(file="admin.png")
        student_label = tk.Label(self, image=student)
        student_label.image = student

        space_label = tk.Label(self, height=4)
        space_label.pack()

        def MenuStudent():
            controller.show_frame('MenuStudent')
           
        daftar_button = tk.Button(self,image=student,command=MenuStudent,border=0)
        daftar_button.place(x=700, y=450)

        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')

        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)
           
        time_label = tk.Label(bottom_frame,font=('roboto',12))
        time_label.pack(side='right')

        tick()
class MenuAdmin(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def back():
            controller.show_frame('StartPage')
        back = tk.Button(self, text="Back",command=back)
        back.configure(font=('roboto',12, "bold"), bg='red', fg='white')
        back.place(x=10, y=10)

        space_label = tk.Label(self, height=7)
        space_label.pack()

        logo = tk.PhotoImage(file="Logo.png")
        logo_label = tk.Label(self, image=logo)
        logo_label.image = logo
        logo_label.pack()

        space_label = tk.Label(self, height=1)
        space_label.pack()

        space_label = tk.Label(self, height=2)
        space_label.pack()

        login = tk.PhotoImage(file="login.png")
        login_label = tk.Label(self, image=login)
        login_label.image = login

        def Login():
            controller.show_frame('LoginAdmin')
           
        masuk_button = tk.Button(self,image=login,command=Login,border=0)
        masuk_button.pack()

        signin = tk.PhotoImage(file="signin.png")
        signin_label = tk.Label(self, image=signin)
        signin_label.image = signin

        space_label = tk.Label(self, height=4)
        space_label.pack()

        def Signin():
            controller.show_frame('SigninAdmin')
           
        daftar_button = tk.Button(self,image=signin,command=Signin,border=0)
        daftar_button.pack()

        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')

        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)
           
        time_label = tk.Label(bottom_frame,font=('roboto',12))
        time_label.pack(side='right')

        tick()

class MenuStudent(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def back():
            controller.show_frame('StartPage')
        back = tk.Button(self, text="Back",command=back)
        back.configure(font=('roboto',12, "bold"), bg='red', fg='white')
        back.place(x=10, y=10)

        space_label = tk.Label(self, height=7)
        space_label.pack()

        logo = tk.PhotoImage(file="Logo.png")
        logo_label = tk.Label(self, image=logo)
        logo_label.image = logo
        logo_label.place(x=0, y=0)
        logo_label.pack()

        space_label = tk.Label(self, height=1)
        space_label.pack()

        space_label = tk.Label(self, height=2)
        space_label.pack()

        login = tk.PhotoImage(file="login.png")
        login_label = tk.Label(self, image=login)
        login_label.image = login

        def Login():
            controller.show_frame('LoginStudent')
           
        masuk_button = tk.Button(self,image=login,command=Login,border=0)
        masuk_button.pack()

        signin = tk.PhotoImage(file="signinn.png")
        signin_label = tk.Label(self, image=signin)
        signin_label.image = signin

        space_label = tk.Label(self, height=4)
        space_label.pack()

        def Signin():
            controller.show_frame('SigninStudent')
           
        daftar_button = tk.Button(self,image=signin,command=Signin,border=0)
        daftar_button.pack()

        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')

        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)
           
        time_label = tk.Label(bottom_frame,font=('roboto',12))
        time_label.pack(side='right')
        tick()

class LoginAdmin(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def back():
            controller.show_frame('MenuAdmin')
        back = tk.Button(self, text="Back",command=back)
        back.configure(font=('roboto',12, "bold"), bg='red', fg='white')
        back.place(x=10, y=10)

        space_label = tk.Label(self, height=7)
        space_label.pack()

        photo = tk.PhotoImage(file="LogoSign.png")
        labels = tk.Label(self, image=photo)
        labels.image = photo
        labels.place(x=0, y=0)
        labels.pack()

        self.controller = controller

        space_label = tk.Label(self, height=4)
        space_label.pack()

        username_entry_box = tk.Entry(self,font=('roboto',12),width=40, bg='grey94')
        username_entry_box.place(width=308, height=30)
        username_entry_box.insert(0, 'Username')
        username_entry_box.pack()

        space_label = tk.Label(self, height=2)
        space_label.pack()

        password_entry_box = tk.Entry(self,font=('roboto',12),width=40, bg='grey94')
        password_entry_box.place(width=308, height=30)
        password_entry_box.insert(0, 'Password')
        password_entry_box.pack()

        def handle_focus_in(_):
            password_entry_box.configure(fg='black',show='*')
           
        password_entry_box.bind('<FocusIn>',handle_focus_in)

        def CekLogin():
            cur.execute("Select * from Admin where username=%s and password=%s", (username_entry_box.get(), password_entry_box.get()))
            row=cur.fetchone()
            if row==None:
                messagebox.showerror("Warning", "USER NOT FOUND")
            else:
                messagebox.showinfo("Success", "Login Success")
                #if
                controller.show_frame('MainLibraryAdmin')

        space_label = tk.Label(self, height=4)
        space_label.pack()
               
        login = tk.PhotoImage(file="login.png")
        loginmenu_label = tk.Label(self, image=login)
        loginmenu_label.image = login    

        loginmenu_button = tk.Button(self,image=login,command=CekLogin,border=0)
        loginmenu_button.place(x=450, y=480)
        loginmenu_button.pack()

        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')

        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)
           
        time_label = tk.Label(bottom_frame,font=('roboto',12))
        time_label.pack(side='right')
        tick()

class LoginStudent(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def back():
            controller.show_frame('MenuStudent')
        back = tk.Button(self, text="Back",command=back)
        back.configure(font=('roboto',12, "bold"), bg='red', fg='white')
        back.place(x=10, y=10)

        space_label = tk.Label(self, height=7)
        space_label.pack()

        photo = tk.PhotoImage(file="LogoSign.png")
        labels = tk.Label(self, image=photo)
        labels.image = photo
        labels.place(x=0, y=0)
        labels.pack()

        self.controller = controller

        space_label = tk.Label(self, height=4)
        space_label.pack()

        username_entry_box = tk.Entry(self,font=('roboto',12),width=40, bg='grey94')
        username_entry_box.place(width=308, height=30)
        username_entry_box.insert(0, 'Username')
        username_entry_box.pack()

        space_label = tk.Label(self, height=2)
        space_label.pack()

        password_entry_box = tk.Entry(self,font=('roboto',12),width=40, bg='grey94')
        password_entry_box.place(width=308, height=30)
        password_entry_box.insert(0, 'Password')
        password_entry_box.pack()

        def handle_focus_in(_):
            password_entry_box.configure(fg='black',show='*')
           
        password_entry_box.bind('<FocusIn>',handle_focus_in)

        def CekLogin():
            cur.execute("Select * from Subscribers where username=%s and password=%s", (username_entry_box.get(), password_entry_box.get()))
            row=cur.fetchone()
            if row==None:
                messagebox.showerror("Warning", "USER NOT FOUND")
            else:
                messagebox.showinfo("Success", "Login Success")
                controller.show_frame('MainLibraryStudent')

        space_label = tk.Label(self, height=4)
        space_label.pack()
               
        login = tk.PhotoImage(file="login.png")
        loginmenu_label = tk.Label(self, image=login)
        loginmenu_label.image = login    

        loginmenu_button = tk.Button(self,image=login,command=CekLogin,border=0)
        loginmenu_button.place(x=450, y=480)
        loginmenu_button.pack()

        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')

        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)
           
        time_label = tk.Label(bottom_frame,font=('roboto',12))
        time_label.pack(side='right')
        tick()

class SigninAdmin(tk.Frame):

    def __init__(self, parent, controller):
        global nama_entry_box, username_entry_box, password_entry_box
        tk.Frame.__init__(self, parent)

        def back():
            controller.show_frame('MenuAdmin')
        back = tk.Button(self, text="Back",command=back)
        back.configure(font=('roboto',12, "bold"), bg='red', fg='white')
        back.place(x=10, y=10)

        space_label = tk.Label(self, height=1)
        space_label.pack()

        photo = tk.PhotoImage(file="LogoSign.png")
        labels = tk.Label(self, image=photo)
        labels.image = photo
        labels.place(x=0, y=0)
        labels.pack()

        space_label = tk.Label(self, height=2)
        space_label.pack()

        self.controller = controller

        email_entry_box = tk.Entry(self,font=('roboto',12),width=40, bg='grey94')
        email_entry_box.place(width=308, height=30)
        email_entry_box.insert(0, 'E-mail')
        email_entry_box.pack()

        space_label = tk.Label(self, height=2)
        space_label.pack()

        adminid_entry_box = tk.Entry(self,font=('roboto',12),width=40, bg='grey94')
        adminid_entry_box.place(width=308, height=30)
        adminid_entry_box.insert(0, 'Admin_ID')
        adminid_entry_box.pack()

        space_label = tk.Label(self, height=2)
        space_label.pack()

        nama_entry_box = tk.Entry(self,font=('roboto',12),width=40, bg='grey94')
        nama_entry_box.place(width=308, height=30)
        nama_entry_box.insert(0, 'Nama Lengkap')
        nama_entry_box.pack()

        space_label = tk.Label(self, height=2)
        space_label.pack()

        username_entry_box = tk.Entry(self,font=('roboto',12),width=40, bg='grey94')
        username_entry_box.place(width=308, height=30)
        username_entry_box.insert(0, 'Username')
        username_entry_box.pack()

        space_label = tk.Label(self, height=2)
        space_label.pack()

        password_entry_box = tk.Entry(self,font=('roboto',12),width=40, bg='grey94')
        password_entry_box.place(width=308, height=30)
        password_entry_box.insert(0, 'Password')
        password_entry_box.pack()

        space_label = tk.Label(self, height=2)
        space_label.pack()

        alamat_entry_box = tk.Entry(self,font=('roboto',12),width=40, bg='grey94')
        alamat_entry_box.place(width=308, height=30)
        alamat_entry_box.insert(0, 'Alamat')
        alamat_entry_box.pack()

        space_label = tk.Label(self, height=2)
        space_label.pack()

        nohp_entry_box = tk.Entry(self,font=('roboto',12),width=40, bg='grey94')
        nohp_entry_box.place(width=308, height=30)
        nohp_entry_box.insert(0, 'No. Handphone')
        nohp_entry_box.pack()

        space_label = tk.Label(self, height=1)
        space_label.pack()

        signinad = tk.PhotoImage(file="signin.png")
        signinmenu_label = tk.Label(self, image=signinad)
        signinmenu_label.image = signinad    

        def CekSigninAdmin():
            adminid = adminid_entry_box.get()
            nama = nama_entry_box.get()
            username = username_entry_box.get()
            password = password_entry_box.get()
            nohp = nohp_entry_box.get()
            email = email_entry_box.get()
            alamat = alamat_entry_box.get()

            sql = "insert into Admin values ('"+adminid+"','"+nama+"','"+username+"','"+password+"','"+alamat+"','"+nohp+"','"+email+"')"
            try:
                cur.execute(sql)
                con.commit()
                messagebox.showinfo("Success", "Sign In Success")
                controller.show_frame('MenuAdmin')
            except:
                messagebox.showerror("Error inserting","Cannot add data to Database")

        signinmenu_button = tk.Button(self,image=signinad,command=CekSigninAdmin,border=0)
        signinmenu_button.place(x=450, y=480)
        signinmenu_button.pack()

        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')

        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)
           
        time_label = tk.Label(bottom_frame,font=('roboto',12))
        time_label.pack(side='right')
        tick()

class SigninStudent(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def back():
            controller.show_frame('MenuStudent')
        back = tk.Button(self, text="Back",command=back)
        back.configure(font=('roboto',12, "bold"), bg='red', fg='white')
        back.place(x=10, y=10)

        space_label = tk.Label(self, height=4)
        space_label.pack()

        photo = tk.PhotoImage(file="LogoSign.png")
        labels = tk.Label(self, image=photo)
        labels.image = photo
        labels.place(x=0, y=0)
        labels.pack()

        space_label = tk.Label(self, height=2)
        space_label.pack()

        self.controller = controller

        email_entry_box = tk.Entry(self,font=('roboto',12),width=40, bg='grey94')
        email_entry_box.place(width=308, height=30)
        email_entry_box.insert(0, 'E-mail')
        email_entry_box.pack()

        space_label = tk.Label(self, height=1)
        space_label.pack()

        subid_entry_box = tk.Entry(self,font=('roboto',12),width=40, bg='grey94')
        subid_entry_box.place(width=308, height=30)
        subid_entry_box.insert(0, 'Subscriber ID')
        subid_entry_box.pack()

        space_label = tk.Label(self, height=1)
        space_label.pack()

        nama_entry_box = tk.Entry(self,font=('roboto',12),width=40, bg='grey94')
        nama_entry_box.place(width=308, height=30)
        nama_entry_box.insert(0, 'Nama Lengkap')
        nama_entry_box.pack()

        space_label = tk.Label(self, height=1)
        space_label.pack()

        username_entry_box = tk.Entry(self,font=('roboto',12),width=40, bg='grey94')
        username_entry_box.place(width=308, height=30)
        username_entry_box.insert(0, 'Username')
        username_entry_box.pack()

        space_label = tk.Label(self, height=1)
        space_label.pack()

        password_entry_box = tk.Entry(self,font=('roboto',12),width=40, bg='grey94')
        password_entry_box.place(width=308, height=30)
        password_entry_box.insert(0, 'Password')
        password_entry_box.pack()

        space_label = tk.Label(self, height=1)
        space_label.pack()

        alamat_entry_box = tk.Entry(self,font=('roboto',12),width=40, bg='grey94')
        alamat_entry_box.place(width=308, height=30)
        alamat_entry_box.insert(0, 'Alamat')
        alamat_entry_box.pack()

        space_label = tk.Label(self, height=1)
        space_label.pack()

        nohp_entry_box = tk.Entry(self,font=('roboto',12),width=40, bg='grey94')
        nohp_entry_box.place(width=308, height=30)
        nohp_entry_box.insert(0, 'No. Handphone')
        nohp_entry_box.pack()

        space_label = tk.Label(self, height=1)
        space_label.pack()

        lists = ["Golden", "Regular"]
        listtype = StringVar(self)
        listtype.set("Type")
        menu = OptionMenu(self, listtype, *lists)
        menu.place(x=620, y=430)
        menu.pack()
       
        space_label = tk.Label(self, height=1)
        space_label.pack()

        signinstu = tk.PhotoImage(file="signin.png")
        signinmenu_label = tk.Label(self, image=signinstu)
        signinmenu_label.image = signinstu    

        def CekSigninStudent():
            email = email_entry_box.get()
            subid = subid_entry_box.get()
            nama = nama_entry_box.get()
            username = username_entry_box.get()
            password = password_entry_box.get()
            alamat = alamat_entry_box.get()
            nohp = nohp_entry_box.get()
            tipe = listtype.get()

            sql = "insert into Subscribers values ('"+subid+"','"+tipe+"','"+nama+"','"+username+"','"+password+"','"+alamat+"','"+nohp+"','"+email+"')"
            try:
                cur.execute(sql)
                con.commit()
                messagebox.showinfo("Success", "Sign In Success")
                controller.show_frame('MenuStudent')
            except:
                messagebox.showerror("Error inserting","Cannot add data to Database")

        signinmenu_button = tk.Button(self,image=signinstu,command=CekSigninStudent,border=0)
        signinmenu_button.place(x=450, y=480)
        signinmenu_button.pack()

        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')

        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)
           
        time_label = tk.Label(bottom_frame,font=('roboto',12))
        time_label.pack(side='right')
        tick()

class MainLibraryAdmin(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
   
        space_label = tk.Label(self, height=7)
        space_label.pack()

        frame1 = tk.PhotoImage(file="dashboard.png")
        frame1_label = tk.Label(self, image=frame1)
        frame1_label.pack()
        frame1_label.image = frame1

        mainlibrary = tk.PhotoImage(file="manage.png")
        mainlibrary_label = tk.Label(self, image=mainlibrary)
        mainlibrary_label.image = mainlibrary

        def mainlibraryadmin():
            controller.show_frame('Kelola')
           
        daftar_button = tk.Button(self,image=mainlibrary,command=mainlibraryadmin,border=0)
        daftar_button.place(x=400, y=290)

        cslibrary = tk.PhotoImage(file="lending.png")
        cslibrary_label = tk.Label(self, image=cslibrary)
        cslibrary_label.image = cslibrary

        def cslibraryadmin():
            controller.show_frame('Lending')
           
        daftar_button = tk.Button(self,image=cslibrary,command=cslibraryadmin,border=0)
        daftar_button.place(x=410, y=370)

        eliblary = tk.PhotoImage(file="logout.png")
        eliblary_label = tk.Label(self, image=eliblary)
        eliblary_label.image = eliblary

        def eliblaryadmin():
            controller.show_frame('StartPage')
           
        daftar_button = tk.Button(self,image=eliblary,command=eliblaryadmin,border=0)
        daftar_button.place(x=405, y=470)

        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')

        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)
           
        time_label = tk.Label(bottom_frame,font=('roboto',12))
        time_label.pack(side='right')
        tick()

class Kelola(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        def back():
            controller.show_frame('MainLibraryAdmin')
        back = tk.Button(self, text="Back",command=back)

        back.configure(font=('roboto',12, "bold"), bg='red', fg='white')
        back.place(x=10, y=10)
        self.controller = controller
        cur.execute("select * from items order by Item_ID;")
        my_tree = ttk.Treeview(self)
        my_tree['show']='headings'

        s=ttk.Style(self)
        s.theme_use("clam")

        s.configure(".", font=('roboto',12))
        s.configure("Treeview.Heading", foreground='blue', font=('roboto',12, "bold"))

        my_tree["columns"]=("Item_ID", "Library_ID", "Category", "Title", "Author", "Publisher", "Production_Year", "Copies")
        my_tree.column("Item_ID", width=100, minwidth=50, anchor=CENTER)
        my_tree.column("Library_ID", width=100, minwidth=50, anchor=CENTER)
        my_tree.column("Category", width=100, minwidth=100, anchor=CENTER)
        my_tree.column("Title", width=200, minwidth=150, anchor=CENTER)
        my_tree.column("Author", width=150, minwidth=100, anchor=CENTER)
        my_tree.column("Publisher", width=150, minwidth=150, anchor=CENTER)
        my_tree.column("Production_Year", width=150, minwidth=50, anchor=CENTER)
        my_tree.column("Copies", width=50, minwidth=100, anchor=CENTER)

        my_tree.heading("Item_ID", text="Item_ID", anchor=CENTER)
        my_tree.heading("Library_ID", text="Library_ID", anchor=CENTER)
        my_tree.heading("Category", text="Category", anchor=CENTER)
        my_tree.heading("Title", text="Title", anchor=CENTER)
        my_tree.heading("Author", text="Author", anchor=CENTER)
        my_tree.heading("Publisher", text="Publisher", anchor=CENTER)
        my_tree.heading("Production_Year", text="Production_Year", anchor=CENTER)
        my_tree.heading("Copies", text="Copies", anchor=CENTER)
        
        t1=StringVar()
        t2=StringVar()
        t3=StringVar()
        t4=StringVar()
        t5=StringVar()
        t6=StringVar()
        t7=StringVar()
        t8=StringVar()

        i=0
        for ro in cur:
            my_tree.insert('', i, text="", values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5], ro[6], ro[7]))
            i=i+1

        hsb=ttk.Scrollbar(self, orient="horizontal", command=my_tree.xview)
        my_tree.configure(xscrollcommand=hsb.set)
        hsb.pack(fill=X,side=BOTTOM)

        vsb=ttk.Scrollbar(self, orient="vertical", command=my_tree.yview)
        my_tree.configure(yscrollcommand=vsb.set)
        vsb.pack(fill=Y,side=RIGHT)

        my_tree.pack()

        f=Frame(self, width=450, height=450, background="#cb945c")
        f.place(x=475,y=250)

        l1=tk.Label(f, text="Item_ID", width=8, font=('roboto',12, "bold"), background="#cb945c")
        l1.place(x=70,y=30)
        e1=tk.Entry(f,width=25,textvariable=t1,)
        e1.place(x=230,y=30)

        l2=tk.Label(f, text="library_ID", width=8, font=('roboto',12, "bold"), background="#cb945c")
        l2.place(x=70,y=70)
        e2=tk.Entry(f,width=25,textvariable=t2)
        e2.place(x=230,y=70)

        l3=tk.Label(f, text="Category", width=8, font=('roboto',12, "bold"), background="#cb945c")
        l3.place(x=70,y=110)
        e3=tk.Entry(f,width=25,textvariable=t3)
        e3.place(x=230,y=110)

        l4=tk.Label(f, text="Title", width=8, font=('roboto',12, "bold"), background="#cb945c")
        l4.place(x=70,y=150)
        e4=tk.Entry(f,width=25,textvariable=t4)
        e4.place(x=230,y=150)

        l5=tk.Label(f, text="Author", width=8, font=('roboto',12, "bold"), background="#cb945c")
        l5.place(x=70,y=190)
        e5=tk.Entry(f,width=25,textvariable=t5)
        e5.place(x=230,y=190)

        l6=tk.Label(f, text="Publisher", width=8, font=('roboto',12, "bold"), background="#cb945c")
        l6.place(x=70,y=230)
        e6=tk.Entry(f,width=25,textvariable=t6)
        e6.place(x=230,y=230)

        l7=tk.Label(f, text="Production_Year", width=15, font=('roboto',12, "bold"), background="#cb945c")
        l7.place(x=40,y=270)
        e7=tk.Entry(f,width=25,textvariable=t7)
        e7.place(x=230,y=270)

        l8=tk.Label(f, text="Copies", width=8, font=('roboto',12, "bold"), background="#cb945c")
        l8.place(x=70,y=310)
        e8=tk.Entry(f,width=25,textvariable=t8)
        e8.place(x=230,y=310)

        def getrow(event):
            rowid=my_tree.identify_row(event.y)
            item=my_tree.item(my_tree.focus())
            t1.set(item['values'][0])
            t2.set(item['values'][1])
            t3.set(item['values'][2])
            t4.set(item['values'][3])
            t5.set(item['values'][4])
            t6.set(item['values'][5])
            t7.set(item['values'][6])
            t8.set(item['values'][7])

        my_tree.bind('<Double 1>', getrow)

        def InsertBook():
            iid=t1.get()
            lid=t2.get()
            category=t3.get()
            title=t4.get()
            author=t5.get()
            publisher=t6.get()
            pyear=t7.get()
            copi=t8.get()

            sql = "insert into items values ('"+iid+"','"+lid+"','"+category+"','"+title+"','"+author+"','"+publisher+"','"+pyear+"','"+copi+"')"
            try:
                cur.execute(sql)
                con.commit()
                my_tree.insert('', 'end', text="", values=(iid, lid, category, title, author, publisher, pyear, copi))
                messagebox.showinfo("Success", "Insert Book Success")
            except:
                messagebox.showerror("Error inserting","Cannot add data to Database")

        def DeleteBook():
            selected_item=my_tree.selection()[0]
            print(my_tree.item(selected_item)['values'])
            uid=my_tree.item(selected_item)['values'][0]
            sql = "Delete from items where Item_ID=%s"
            try:
                sel_data=(uid,)
                cur.execute(sql,sel_data)
                con.commit()
                my_tree.delete(selected_item)
                messagebox.showinfo("Success", "Delete Book Success")
            except:
                messagebox.showerror("Error inserting","Cannot add data to Database")

        def UpdateBook():
            iid=t1.get()
            lid=t2.get()
            category=t3.get()
            title=t4.get()
            author=t5.get()
            publisher=t6.get()
            pyear=t7.get()
            copi=t8.get()

            sql="update items set Library_ID=%s, Category=%s, Title=%s, Author=%s, Publisher=%s, Production_Year=%s, Copies=%s where Item_ID=%s"
            try:
                selected=my_tree.focus()
                val=(lid,category,title,author,publisher,pyear,copi,iid)
                cur.execute(sql,val)
                con.commit()
                my_tree.item(selected, text="", values=(iid, lid, category, title, author, publisher, pyear, copi))
                messagebox.showinfo("Success", "Insert Book Success")
            except:
                messagebox.showerror("Error inserting","Cannot add data to Database")
    
        insertbutton = tk.Button(self, text="Insert",command=InsertBook)
        insertbutton.configure(font=('roboto',12, "bold"), bg='green', fg='white')
        insertbutton.place(x=570, y=650)

        deletebutton = tk.Button(self, text="Delete",command=DeleteBook)
        deletebutton.configure(font=('roboto',12, "bold"), bg='red', fg='white')
        deletebutton.place(x=670, y=650)

        updatebutton = tk.Button(self, text="Update",command=UpdateBook)
        updatebutton.configure(font=('roboto',12, "bold"), bg='yellow', fg='white')
        updatebutton.place(x=770, y=650)

class Lending(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        def back():
            controller.show_frame('MainLibraryAdmin')
        back = tk.Button(self, text="Back",command=back)
        back.configure(font=('roboto',12, "bold"), bg='red', fg='white')
        back.place(x=10, y=10)

        self.controller = controller
        cur.execute("select * from borrowing;")
        my_tree = ttk.Treeview(self)
        my_tree['show']='headings'

        s=ttk.Style(self)
        s.theme_use("clam")

        s.configure(".", font=('roboto',12))
        s.configure("Treeview.Heading", foreground='blue', font=('roboto',12, "bold"))

        my_tree["columns"]=("Subscriber_ID", "Borrow_Date", "Item_ID", "Return_Date", "Fee")
        my_tree.column("Subscriber_ID", width=100, minwidth=50, anchor=CENTER)
        my_tree.column("Borrow_Date", width=200, minwidth=50, anchor=CENTER)
        my_tree.column("Item_ID", width=100, minwidth=100, anchor=CENTER)
        my_tree.column("Return_Date", width=200, minwidth=150, anchor=CENTER)
        my_tree.column("Fee", width=150, minwidth=100, anchor=CENTER)

        my_tree.heading("Subscriber_ID", text="Subscriber_ID", anchor=CENTER)
        my_tree.heading("Borrow_Date", text="Borrow_Date", anchor=CENTER)
        my_tree.heading("Item_ID", text="Item_ID", anchor=CENTER)
        my_tree.heading("Return_Date", text="Return_Date", anchor=CENTER)
        my_tree.heading("Fee", text="Fee", anchor=CENTER)

        i=0
        for ro in cur:
            my_tree.insert('', i, text="", values=(ro[0], ro[1], ro[2], ro[3], ro[4]))
            i=i+1

        hsb=ttk.Scrollbar(self, orient="horizontal", command=my_tree.xview)
        my_tree.configure(xscrollcommand=hsb.set)
        hsb.pack(fill=X,side=BOTTOM)

        vsb=ttk.Scrollbar(self, orient="vertical", command=my_tree.yview)
        my_tree.configure(yscrollcommand=vsb.set)
        vsb.pack(fill=Y,side=RIGHT)

        my_tree.pack()
class MainLibraryStudent(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
   
        space_label = tk.Label(self, height=7)
        space_label.pack()

        frame1 = tk.PhotoImage(file="dashboard.png")
        frame1_label = tk.Label(self, image=frame1)
        frame1_label.pack()
        frame1_label.image = frame1

        mainlibrary = tk.PhotoImage(file="borrow.png")
        mainlibrary_label = tk.Label(self, image=mainlibrary)
        mainlibrary_label.image = mainlibrary

        def borrow():
            controller.show_frame('BorrowBook')
           
        daftar_button = tk.Button(self,image=mainlibrary,command=borrow,border=0)
        daftar_button.place(x=405, y=290)

        cslibrary = tk.PhotoImage(file="return.png")
        cslibrary_label = tk.Label(self, image=cslibrary)
        cslibrary_label.image = cslibrary

        def cslibraryadmin():
            controller.show_frame('ReturnBook')
           
        daftar_button = tk.Button(self,image=cslibrary,command=cslibraryadmin,border=0)
        daftar_button.place(x=410, y=370)

        eliblary = tk.PhotoImage(file="logoutt.png")
        eliblary_label = tk.Label(self, image=eliblary)
        eliblary_label.image = eliblary

        def eliblaryadmin():
            controller.show_frame('StartPage')
           
        daftar_button = tk.Button(self,image=eliblary,command=eliblaryadmin,border=0)
        daftar_button.place(x=405, y=470)

        bottom_frame = tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')

        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)
           
        time_label = tk.Label(bottom_frame,font=('roboto',12))
        time_label.pack(side='right')
        tick()

class BorrowBook(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        def back():
            controller.show_frame('MainLibraryStudent')
        back = tk.Button(self, text="Back",command=back)
        back.configure(font=('roboto',12, "bold"), bg='red', fg='white')
        back.place(x=10, y=10)

        self.controller = controller
        cur.execute("select Item_ID, category, title, author, publisher from items")
        my_tree = ttk.Treeview(self)
        my_tree['show']='headings'

        s=ttk.Style(self)
        s.theme_use("clam")

        s.configure(".", font=('roboto',12))
        s.configure("Treeview.Heading", foreground='blue', font=('roboto',12, "bold"))

        my_tree["columns"]=("Item_ID","Category", "Title", "Author", "Publisher")
        my_tree.column("Item_ID", width=100, minwidth=100, anchor=CENTER)
        my_tree.column("Category", width=100, minwidth=100, anchor=CENTER)
        my_tree.column("Title", width=200, minwidth=150, anchor=CENTER)
        my_tree.column("Author", width=150, minwidth=100, anchor=CENTER)
        my_tree.column("Publisher", width=150, minwidth=150, anchor=CENTER)

        my_tree.heading("Item_ID", text="Item ID", anchor=CENTER)
        my_tree.heading("Category", text="Category", anchor=CENTER)
        my_tree.heading("Title", text="Title", anchor=CENTER)
        my_tree.heading("Author", text="Author", anchor=CENTER)
        my_tree.heading("Publisher", text="Publisher", anchor=CENTER)

        t1=StringVar()
        t2=StringVar()
        t3=StringVar()
        t4=StringVar()
        t5=StringVar()
        t6=StringVar()

        i=0
        for ro in cur:
            my_tree.insert('', i, text="", values=(ro[0], ro[1], ro[2], ro[3], ro[4]))
            i=i+1

        hsb=ttk.Scrollbar(self, orient="horizontal", command=my_tree.xview)
        my_tree.configure(xscrollcommand=hsb.set)
        hsb.pack(fill=X,side=BOTTOM)

        vsb=ttk.Scrollbar(self, orient="vertical", command=my_tree.yview)
        my_tree.configure(yscrollcommand=vsb.set)
        vsb.pack(fill=Y,side=RIGHT)

        my_tree.pack()
        f=Frame(self, width=450, height=450, background="#cb945c")
        f.place(x=475,y=250)

        l1=tk.Label(f, text="Subscriber ID", width=10, font=('roboto',12, "bold"), background="#cb945c")
        l1.place(x=60,y=70)
        e1=tk.Entry(f,width=25,textvariable=t1,)
        e1.place(x=230,y=70)

        l2=tk.Label(f, text="Item ID", width=8, font=('roboto',12, "bold"), background="#cb945c")
        l2.place(x=70,y=110)
        e2=tk.Entry(f,width=25,textvariable=t2)
        e2.place(x=230,y=110)

        l3=tk.Label(f, text="Category", width=8, font=('roboto',12, "bold"), background="#cb945c")
        l3.place(x=70,y=150)
        e3=tk.Entry(f,width=25,textvariable=t3)
        e3.place(x=230,y=150)

        l4=tk.Label(f, text="Title", width=8, font=('roboto',12, "bold"), background="#cb945c")
        l4.place(x=70,y=190)
        e4=tk.Entry(f,width=25,textvariable=t4)
        e4.place(x=230,y=190)

        l5=tk.Label(f, text="Author", width=8, font=('roboto',12, "bold"), background="#cb945c")
        l5.place(x=70,y=230)
        e5=tk.Entry(f,width=25,textvariable=t5)
        e5.place(x=230,y=230)

        l6=tk.Label(f, text="Publisher", width=15, font=('roboto',12, "bold"), background="#cb945c")
        l6.place(x=40,y=270)
        e6=tk.Entry(f,width=25,textvariable=t6)
        e6.place(x=230,y=270)

        def getrow(event):
            rowid=my_tree.identify_row(event.y)
            item=my_tree.item(my_tree.focus())
            t2.set(item['values'][0])
            t3.set(item['values'][1])
            t4.set(item['values'][2])
            t5.set(item['values'][3])
            t6.set(item['values'][4])


        my_tree.bind('<Double 1>', getrow)

        subid=t1.get()
        iid=t2.get()
        category=t3.get()
        title=t4.get()
        author=t5.get()
        publisher=t6.get()

        def Borrow():
            subid=t1.get()
            iid=t2.get()
            category=t3.get()
            title=t4.get()
            author=t5.get()
            publisher=t6.get()
            oldtime=datetime.now()
            newtime=oldtime+relativedelta(weeks=+3)
            
            sqla = "insert into borrowing (subscriber_id, Borrow_Date, Item_ID, Return_Date, Fee) values (%s, %s, %s, %s,NULL)"
            sqlb = "insert into borrowingsubscribers (Title_Book, Borrow_Date, Item_ID, Return_Date) values (%s, %s, %s, %s)"
            try:
                val=(subid,oldtime,iid,newtime)
                cur.execute(sqla, val)
                con.commit()
                al=(title,oldtime,iid,newtime)
                cur.execute(sqlb, al)
                con.commit()
                messagebox.showinfo("Success", "Borrow Book Success")
            except:
                messagebox.showerror("Error inserting","Cannot add data to Database")
    
        insertbutton = tk.Button(self, text="Borrow",command=Borrow)
        insertbutton.configure(font=('roboto',12, "bold"), bg='green', fg='white')
        insertbutton.place(x=670, y=650)

class ReturnBook(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def back():
            controller.show_frame('MainLibraryStudent')
        back = tk.Button(self, text="Back",command=back)
        back.configure(font=('roboto',12, "bold"), bg='red', fg='white')
        back.place(x=10, y=10)
        self.controller = controller
        cur.execute("select * from BorrowingSubscribers ;")
        my_tree = ttk.Treeview(self)
        my_tree['show']='headings'

        s=ttk.Style(self)
        s.theme_use("clam")

        s.configure(".", font=('roboto',12))
        s.configure("Treeview.Heading", foreground='blue', font=('roboto',12, "bold"))

        my_tree["columns"]=("Title_Book","Borrow_Date", "Item_ID", "Return_Date")
        my_tree.column("Title_Book", width=200, minwidth=100, anchor=CENTER)
        my_tree.column("Borrow_Date", width=100, minwidth=150, anchor=CENTER)
        my_tree.column("Item_ID", width=200, minwidth=100, anchor=CENTER)
        my_tree.column("Return_Date", width=150, minwidth=150, anchor=CENTER)

        my_tree.heading("Title_Book", text="Title Book", anchor=CENTER)
        my_tree.heading("Borrow_Date", text="Borrow Date", anchor=CENTER)
        my_tree.heading("Item_ID", text="Item ID", anchor=CENTER)
        my_tree.heading("Return_Date", text="Return Date", anchor=CENTER)
        t1=StringVar()
        t2=StringVar()
        t3=StringVar()
        t4=StringVar()

        i=0
        for ro in cur:
            my_tree.insert('', i, text="", values=(ro[0], ro[1], ro[2], ro[3]))
            i=i+1

        hsb=ttk.Scrollbar(self, orient="horizontal", command=my_tree.xview)
        my_tree.configure(xscrollcommand=hsb.set)
        hsb.pack(fill=X,side=BOTTOM)

        vsb=ttk.Scrollbar(self, orient="vertical", command=my_tree.yview)
        my_tree.configure(yscrollcommand=vsb.set)
        vsb.pack(fill=Y,side=RIGHT)

        my_tree.pack()

        f=Frame(self, width=450, height=450, background="#cb945c")
        f.place(x=475,y=250)

        l1=tk.Label(f, text="Title_Book", width=10, font=('roboto',12, "bold"), background="#cb945c")
        l1.place(x=70,y=70)
        e1=tk.Entry(f,width=25,textvariable=t1)
        e1.place(x=230,y=70)

        l2=tk.Label(f, text="Borrow_Date", width=10, font=('roboto',12, "bold"), background="#cb945c")
        l2.place(x=70,y=110)
        e2=tk.Entry(f,width=25,textvariable=t2)
        e2.place(x=230,y=110)

        l3=tk.Label(f, text="Item_ID", width=10, font=('roboto',12, "bold"), background="#cb945c")
        l3.place(x=70,y=150)
        e3=tk.Entry(f,width=25,textvariable=t3)
        e3.place(x=230,y=150)

        l4=tk.Label(f, text="Return_Date", width=8, font=('roboto',12, "bold"), background="#cb945c")
        l4.place(x=70,y=190)
        e4=tk.Entry(f,width=25,textvariable=t4)
        e4.place(x=230,y=190)

        def getrow(event):
            rowid=my_tree.identify_row(event.y)
            item=my_tree.item(my_tree.focus())
            t1.set(item['values'][0])
            t2.set(item['values'][1])
            t3.set(item['values'][2])
            t4.set(item['values'][3])

        my_tree.bind('<Double 1>', getrow)

        def returnb():
            title=t1.get()
            bd=t2.get()
            iid=t3.get()
            rd=t4.get()
            ss=datetime.now()
            t=datetime.strptime(rd, '%Y-%m-%d')
            denda=(ss-t)
            p=denda.days
            if p <= 0:
                denda=0
            else:
                denda=p*1000
            selected_item=my_tree.selection()[0]
            print(my_tree.item(selected_item)['values'])
            uid=my_tree.item(selected_item)['values'][2]
            sql1 = "update borrowing set fee = %s where item_id=%s;"
            val=(denda,iid)
            cur.execute(sql1, val)
            con.commit()
            if denda <= 0:
                messagebox.showinfo("Denda", "Anda Tidak Kena denda")
                q=tk.Label(f, text="Denda ", width=10, font=('roboto',12, "bold"), background="#cb945c")
                q.place(x=62,y=230)
                a=tk.Label(f, text=denda, width=10, font=('roboto',12, "bold"), background="white")
                a.place(x=230,y=230)
            else:
                messagebox.showinfo("Denda", "Anda Kena denda")
                q=tk.Label(f, text="Denda ", width=10, font=('roboto',12, "bold"), background="#cb945c")
                q.place(x=62,y=230)
                a=tk.Label(f, text=denda, width=10, font=('roboto',12, "bold"), background="white")
                a.place(x=230,y=230)
            sql2 = "Delete from BorrowingSubscribers where Item_ID=%s"
            try:
                sel_data=(uid,)
                cur.execute(sql2,sel_data)
                con.commit()
                my_tree.delete(selected_item)
                messagebox.showinfo("Success", "Return Book Success")
            except:
                messagebox.showerror("Error inserting","Cannot add data to Database")
        deletebutton = tk.Button(self, text="return",command=returnb)
        deletebutton.configure(font=('roboto',12, "bold"), bg='red', fg='white')
        deletebutton.place(x=670, y=650)

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()