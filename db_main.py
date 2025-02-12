from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3 as sq
import hashlib as hb
import os


program_path = os.path.dirname(os.path.realpath(__file__))
db_path = os.path.join(program_path, 'Data.db')
conn = sq.connect(db_path)
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS passcode (user TEXT NOT NULL PRIMARY KEY UNIQUE, \
password TEXT , statu TEXT)')
conn.commit()
conn.close()

if cur:
    print("Succesfuly connected")

def Encrypt_String(hash_string):
    sha_signature = hb.sha256(hash_string.encode()).hexdigest()
    return sha_signature
    

def Message(basx,msx):
    msg = messagebox.showinfo(basx,msx)
    
def save_F():
    val1 = nameg.get()
    val2 = passwordg.get()
    try:
        conn = sq.connect(db_path)
        cur = conn.cursor()
        cur.execute("INSERT INTO passcode (user, password, statu) VALUES ('%s','%s','%s')"\
                   %(val1,Encrypt_String(val2),''))
        conn.commit()
        conn.close()
        Message("Inform", 'Succesfully saved!')
    except Exception as x:
        print('Error',x)
        Message("Error", str(x))
        
        
        
        
def Login_F():
    try:
        conn = sq.connect(db_path)
        cur = conn.cursor()
        userx = ("'"+(nameg.get())+"'")
        passwordx = Encrypt_String(passwordg.get())
        sql1 = "SELECT password FROM passcode WHERE user = %s" %userx
        cur.execute(sql1)
        resultL = cur.fetchone()
        passwordTable = resultL[0]
        conn.commit()
        conn.close()

        if passwordTable == passwordx:
            Message('Inform','login succesful!')
            giris.destroy()
            Open_Gui(True)
        else:
            Message('Error','Wrong user name or password')
    except Exception as x:
        print("Login Error", x)
        Message("Error", str(x))
        
    
def on_click(event):
    if nameg['state'] == 'disabled':
        nameg.config(state = 'normal')
        nameg.delete(0, END)
    else:
        pass

def on_click2(event):
    if passwordg['state'] == 'disabled':
        passwordg.config(state = 'normal')
        passwordg.delete(0, END)
    else:
        pass
    
    
#D4E6F1
giris = Tk()
giris.title('User Login')
giris.config(bg = "#D4E6F1")
giris.geometry('600x400+400+150')
giris.resizable(False,False)

icon1_path = os.path.join(program_path, r'Pictures\icon1.png')
icon1 = Image.open(icon1_path)
icon1 = icon1.convert("RGBA")
icon1_tk = ImageTk.PhotoImage(icon1)

label_icon1 = Label(giris, image= icon1_tk, bg = "#D4E6F1")
label_icon1.grid(row=0, column=0, padx = 140, pady= 110)  

font1 = ('New Roman Times',16)
nameg = Entry(giris, width = 20, font = font1)
nameg.insert(0,'User Name')
nameg.config(state = 'disabled')
nameg.place(x = 170, y= 5)

passwordg = Entry(giris,show = '*', width = 20, font = font1)
passwordg.insert(0,'Password')
passwordg.config(state = 'disabled')
passwordg.place(x = 170, y = 40)

Newuser = Button(giris, text = 'New User', command = save_F)
Newuser.place(x = 210, y = 90)

Login = Button(giris, text = 'Sign in', command = Login_F)
Login.place(x= 320, y = 90)


on_click_id = nameg.bind('<Button-1>',on_click)
on_click_id2 = passwordg.bind('<Button-1>',on_click2)



def Open_Gui(x):
    if x == True:
        def save_f():
            try:
                if Entryname.get() == "" or EntryMail.get() == "" or EntryRole.get() == "":
                    raise ValueError("Please do not fill the fields blank")   
                conn = sq.connect(db_path)
                cur = conn.cursor()
                cur.execute("INSERT INTO users (ad, email, role) VALUES ('%s', '%s', '%s') " \
                           %(Entryname.get(), EntryMail.get(), EntryRole.get()))
                conn.commit()
                conn.close()
                Message("Inform","Saved succesfully!")
                List()
            except Exception as e:
                print("Savemede bir Error oluştu", str(e))
                Message("Error", str(e))

        def List_Print():
            try:
                conn = sq.connect(db_path)
                cur = conn.cursor()
                cur.execute("Select * From users")
                result2 = cur.fetchall()
                conn.commit()
                conn.close()
                for data in result2:
                    print(data)
                Message("Inform","Printed Succesfully")
            except Exception as x:
                print('Error',x)
                Message("Error", str(x))
        

        def List():
            try:
                List_tree.delete(*List_tree.get_children())
                conn = sq.connect(db_path)
                cur = conn.cursor()
                cur.execute("Select * From users order by id desc")
                result3 = cur.fetchall()
                conn.commit()
                conn.close()
                for data in result3:
                    List_tree.insert("", 0 , text = data[0], values = (data[1], data[2], data[3]))
            except Exception as x:
                print('Error',x)
                Message("Error", str(x))
        

        def Get_data(event):
            try:
                conn = sq.connect(db_path)
                cur = conn.cursor()
                idno = List_tree.item(List_tree.selection()[0])['text']
                sql = "Select * from users where id = %s" % idno
                cur.execute(sql)
                result4 = cur.fetchone()
                conn.commit()
                conn.close()

                EntryId.delete(0, END)
                EntryId.insert(0, result4[0])

                Entryname.delete(0, END)
                Entryname.insert(0, result4[1])

                EntryMail.delete(0, END)
                EntryMail.insert(0, result4[2])

                EntryRole.delete(0, END)
                EntryRole.insert(0, result4[3])
            except Exception as x:
                print(x)
                if str(x) == "tuple index out of range":
                    pass
                else:
                    print('Error',x)
                    Message("Error", str(x))
            

        def Update_f():
            try:
                conn = sq.connect(db_path)
                cur = conn.cursor()
                cur.execute("UPDATE users SET ad = '%s',email = '%s',role = '%s' WHERE Id = %s " \
                            %(Entryname.get(),EntryMail.get(), EntryRole.get(), EntryId.get()))
                conn.commit()
                conn.close()
                Message("Inform","Updated Succesfully!")
                List()
            except Exception as x:
                print('Error',x)
                Message("Error", str(x))
        

        def Sil_f():
            try:
                conn = sq.connect(db_path)
                cur = conn.cursor()
                cur.execute("DELETE FROM users WHERE Id = %s" %EntryId.get())
                conn.commit()
                conn.close()
                Message("Inform","Deleted Succesfully")
                List()
            except Exception as x:
                print('Error',x)
                Message("Error", str(x))
        

        def Message(data,textp):
            msg = messagebox.showinfo(data,textp)




        conn = sq.connect(db_path)
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS users (Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, ad TEXT,\
        email TEXT, role TEXT)')
        cur.execute('CREATE TABLE IF NOT EXISTS Rolp (Rol_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, Rol_ad \
        TEXT NOT NULL)')
        sqlrol = "select Rol_ad from Rolp"
        cur.execute(sqlrol)
        result = cur.fetchall()
        conn.commit()
        conn.close()
        if cur:
            print('Connected Succesfully')


        form = Tk()
        form.geometry('800x600')
        form.title('ANKA APPLICATION')
        form.config(bg = "#D4E6F1")
        form.resizable(False,False)

        img_path = os.path.join(program_path, r'Pictures\icon.png')
        print(img_path)

        Labelname = Label(form, text = 'Name-Surname',bg = "#D4E6F1").place(x = 5,y = 10)
        Entryname = Entry(form, bd = 2, width = 23)
        Entryname.place(x = 100, y = 10)

        Labelmail = Label(form, text = 'E-mail',bg = "#D4E6F1").place(x = 5, y = 40)
        EntryMail = Entry(form, bd = 2, width = 23)
        EntryMail.place(x = 100, y = 40)

        labelId = Label(form, text = 'Id', bg = "#D4E6F1").place(x = 250,y = 10)
        EntryId = Entry(form, bd = 2, width = 5)
        EntryId.place(x = 270, y = 10)

        LabelRole = Label(form, text = 'User Role', bg = "#D4E6F1").place(x = 5, y = 70)
        EntryRole = ttk.Combobox(form)
        EntryRole["values"] = result
        EntryRole["values"] = ("Admin","Guest","Super_User","Student")
        EntryRole.place(x = 100, y = 70)

        img = Image.open(img_path)
        img = img.convert("RGBA")  
        img_tk = ImageTk.PhotoImage(img)

        LabelIcon = Label(form, image=img_tk, bg='black', bd=4)
        LabelIcon.image = img_tk 
        LabelIcon.place(x=680, y=10)

        saveimg_path = os.path.join(program_path, r'Pictures\save.png')
        saveimg = Image.open(saveimg_path)
        saveimg = saveimg.convert("RGBA")
        saveimg_tk = ImageTk.PhotoImage(saveimg)
        Save = Button(form, text='Save', height=55, width=55, image=saveimg_tk, compound='top', bd=3, bg = "#D4E6F1",  command=save_f)
        Save.place(x=20, y=100)

        # Diğer resimler için aynı şekilde yol belirleyebilirsiniz
        gunimg_path = os.path.join(program_path, r'Pictures\Update.png')
        gunimg = Image.open(gunimg_path)
        gunimg = gunimg.convert("RGBA")
        gunimg_tk = ImageTk.PhotoImage(gunimg)
        Update = Button(form, text='Update', height=55, width=55, image=gunimg_tk, compound='top', bd=3, bg = "#D4E6F1", command=Update_f)
        Update.place(x=105, y=100)

        delete_img_path = os.path.join(program_path, r'Pictures\Delete.png')
        delete_img = Image.open(delete_img_path)
        delete_img = delete_img.convert("RGBA")
        delete_img_tk = ImageTk.PhotoImage(delete_img)
        Delete = Button(form, text='Delete', height=55, width=55, image=delete_img_tk, compound='top', bd=3, bg = "#D4E6F1", command=Sil_f)
        Delete.place(x=190, y=100)

        Listimg_path = os.path.join(program_path, r'Pictures\List.png')
        Listimg = Image.open(Listimg_path)
        Listimg = Listimg.convert("RGBA")
        Listimg_tk = ImageTk.PhotoImage(Listimg)
        Print = Button(form, text='List', height=55, width=55, image=Listimg_tk, compound='top', bd=3, bg = "#D4E6F1",  command=List_Print)
        Print.place(x=275, y=100)



        List_tree = ttk.Treeview(form, height = 21)
        List_tree["columns"] = ("sut1", "sut2", "sut3") 
        List_tree.place(x = 0, y = 170)
        List_tree.heading('#0', text = "id")
        List_tree.heading('sut1', text = "Name")
        List_tree.heading('sut2', text = "Email")
        List_tree.heading('sut3', text = "Role")
        List_tree.bind("<ButtonRelease-1>", Get_data)

        List()
        
        form.mainloop()
        
    else:
        print('Not working')
    
giris.mainloop()