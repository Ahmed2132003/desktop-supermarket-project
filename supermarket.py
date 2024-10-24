from tkinter import *
from tkinter import messagebox
import webbrowser
import subprocess
import sys
import os

def login():
    user = en1.get()
    passw = en2.get()
    if user == 'ahmed' and passw == '123456':
        messagebox.showinfo('ترحيب', 'اهلا بك عزيزي العميل احسنت عملا بأدخالك البيانات الصحيحة ')
        root.destroy()  # إغلاق نافذة تسجيل الدخول
        
        # تحديد المسار المناسب للملف التنفيذي
        if getattr(sys, 'frozen', False):
            # إذا كانت الحزمة مجمعة
            home_path = os.path.join(sys._MEIPASS, 'super.exe')
        else:
            # أثناء التطوير
            home_path = 'D:\\programming project\\python\\desktopApp\\supermarket project\\dist\\super.exe'
        
        subprocess.run([home_path])
    else:
        messagebox.showerror('تحذير', 'ادخلت بيانات خطأ')

# إعداد نافذة تسجيل الدخول
root = Tk()
root.geometry('800x450+280+50')
root.resizable(False, False)
root.title('creativity market')
root.iconbitmap('D:\\programming project\\python\\desktopApp\\supermarket project\\super.ico')

titlel1 = Label(root, text=' نظام ادارة سوبر ماركت', fg='gold', bg='black', font=('tajawal', '16', 'bold'))
titlel1.pack(fill=X)

ui1 = 'https://www.facebook.com/profile.php?id=61558357762152&mibextid=ZbWKwL'
ui2 = 'https://wa.me/201029102507'
ui3 = 'https://www.instagram.com/creativitycode7878?igsh=MTVmdmRwYTVmdzY5Yw=='

def facebook():
    webbrowser.open_new(ui1)

def whatsabb():
    webbrowser.open_new(ui2)

def instgram():
    webbrowser.open_new(ui3)

def about1():
    messagebox.showinfo('المطور', 'طور هذا البرنامج المهندس احمد ابراهيم الرئيس التنفيذي لشركة كريتيفتي كود ')

def about2():
    messagebox.showinfo('عن البرنامج', 'تمت برمجة هذا البرنامج بلغة البايثون من خلال مكتبة تكنتر وذلك بسبب ان هذه المكتبة تتميز بلعديد من الميزات عن غيرها')

f1 = Frame(root, width=230, height=420, bg='#008080')
f1.place(x=570, y=30)
titlel2 = Label(f1, text='ادارة السوبر ماركت ', fg='gold', bg='#008080', font=('tajawal', '12', 'bold'))
titlel2.place(x=55, y=10)
titlel3 = Label(f1, text='المطور احمد ابراهيم', fg='gold', bg='#008080', font=('tajawal', '12', 'bold'))
titlel3.place(x=54, y=50)
titlel4 = Label(f1, text='وسائل التواصل معنا ', fg='gold', bg='#008080', font=('tajawal', '12', 'bold'))
titlel4.place(x=55, y=90)
B1 = Button(f1, text='حسابنا علي فيسبوك', width=23, fg='black', bg='gold', font=('tajawal', '11', 'bold'), command=facebook)
B1.place(x=6, y=130)
B2 = Button(f1, text='حسابنا علي واتساب', width=23, fg='black', bg='gold', font=('tajawal', '11', 'bold'), command=whatsabb)
B2.place(x=6, y=177)
B3 = Button(f1, text='حسابنا علي انستجرام', width=23, fg='black', bg='gold', font=('tajawal', '11', 'bold'), command=instgram)
B3.place(x=6, y=225)
B4 = Button(f1, text=' لمحة عن المطور ', width=23, fg='black', bg='gold', font=('tajawal', '11', 'bold'), command=about1)
B4.place(x=6, y=272)
B5 = Button(f1, text=' لمحة عن البرنامج ', width=23, fg='black', bg='gold', font=('tajawal', '11', 'bold'), command=about2)
B5.place(x=6, y=318)
B6 = Button(f1, text=' اغلاق البرنامج ', width=23, fg='black', bg='gold', font=('tajawal', '11', 'bold'), command=root.quit)
B6.place(x=6, y=365)

photo = PhotoImage(file='D:\\programming project\\python\\desktopApp\\supermarket project\\super3.png')
imo = Label(root, image=photo)
imo.place(x=0, y=32, width=570, height=300)
f2 = Frame(root, width=570, height=120, bg='#008080')
f2.place(x=0, y=330)
photo1 = PhotoImage(file='D:\\programming project\\python\\desktopApp\\supermarket project\\login.png')
imo1 = Label(root, image=photo1)
imo1.place(x=450, y=335, width=110, height=110)
l1 = Label(f2, text='اسم المستخدم ', fg='gold', bg='#008080', font=('tajawal', '12', 'bold'))
l1.place(x=370, y=25)
l2 = Label(f2, text=' كلمة المرور ', fg='gold', bg='#008080', font=('tajawal', '12', 'bold'))
l2.place(x=370, y=70)
en1 = Entry(f2, font=('tajawal', '12', 'bold'), justify='center')
en1.place(x=130, y=26)
en2 = Entry(f2, font=('tajawal', '12', 'bold'), justify='center', show='*')
en2.place(x=130, y=70)
B = Button(f2, text='تسجيل الدخول', bg='gold', fg='#008080', font=('tajawal', '12', 'bold'), command=login)
B.place(x=10, y=30, height=55)

root.mainloop()
