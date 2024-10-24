from tkinter import *
from tkinter import messagebox
import webbrowser
import subprocess
import math
import os 
import random


pro = Tk()
pro.geometry('800x450+280+50')
pro.resizable(False, False)
pro.title('creativity market')
pro.iconbitmap('D:\\programming project\\python\\desktopApp\\supermarket project\\super.ico')

titlel1 = Label(pro, text=' نظام ادارة سوبر ماركت', fg='gold', bg='black', font=('tajawal', '16', 'bold'))
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

def log():
    user = en1.get()
    passw = en2.get()
    if user == 'ahmed' and passw == '123456':
        messagebox.showinfo('ترحيب', 'اهلا بك عزيزي العميل احسنت عملا بأدخالك البيانات الصحيحة ')
        class super1():
            def __init__(self,root) :
                self.root =root
                self.root.geometry("1300x700+30+10")
                self.root.title('supermarket سوبر ماركت')
                self.root.resizable(False,False)
                self.root.iconbitmap('D:\\programming project\\python\\desktopApp\\supermarket project\\super.ico')
                title=Label(self.root,text='ادارة السوبر ماركت',fg='white',bg='#0B4C5F',font=('tajawal',15,'bold'))
                title.pack(fill=X)
                
                
                #======================intvar=======================
                self.q1=IntVar()
                self.q2=IntVar()
                self.q3=IntVar()
                self.q4=IntVar()
                self.q5=IntVar()
                self.q6=IntVar()
                self.q7=IntVar()
                self.q8=IntVar()
                self.q9=IntVar()
                self.q10=IntVar()
                self.q11=IntVar()
                self.q12=IntVar()
                self.q13=IntVar()
                self.q14=IntVar()
                self.q15=IntVar()
                self.q16=IntVar()
                self.q17=IntVar()
                self.q18=IntVar()
                self.qq1=IntVar()
                self.qq2=IntVar()
                self.qq3=IntVar()
                self.qq4=IntVar()
                self.qq5=IntVar()
                self.qq6=IntVar()
                self.qq7=IntVar()
                self.qq8=IntVar()
                self.qq9=IntVar()
                self.qq10=IntVar()
                self.qq11=IntVar()
                self.qq12=IntVar()
                self.qq13=IntVar()
                self.qq14=IntVar()
                self.qq15=IntVar()
                self.qq16=IntVar()
                self.qq17=IntVar()
                self.qq18=IntVar()
                self.qqq1=IntVar()
                self.qqq2=IntVar()
                self.qqq3=IntVar()
                self.qqq4=IntVar()
                self.qqq5=IntVar()
                self.qqq6=IntVar()
                self.qqq7=IntVar()
                self.qqq8=IntVar()
                self.qqq9=IntVar()
                self.qqq10=IntVar()
                self.qqq11=IntVar()
                self.qqq12=IntVar()
                self.qqq13=IntVar()
                self.qqq14=IntVar()
                self.qqq15=IntVar()
                
                #======================varibals======================
                self.bacoliat=StringVar()
                self.lohom=StringVar()
                self.drinks=StringVar()
                self.nemo=StringVar()
                self.phono=StringVar()
                self.fatora=StringVar()
                x=random.randint(1000,9999)
                self.fatora.set(str(x))
                
                
                #=============================COUSTOMER DATA ======================
                f1=Frame(root,bd=2,width=338,height=170,bg='#0B4C5F')
                f1.place(x=961,y=31)
                tit=Label(f1,text='بيانات المشتري',fg='tomato',bg='#0B4C5F',font=('tajawal',15,'bold'))
                tit.place(x=140,y=0)
                his_name=Label(f1,text='اسم المشتري',fg='white',bg='#0B4C5F',font=('tajawal',13,'bold'))
                his_name.place(x=230,y=40)
                his_phone=Label(f1,text='هاتف المشتري',fg='white',bg='#0B4C5F',font=('tajawal',13,'bold'))
                his_phone.place(x=223,y=70)
                bill_num=Label(f1,text='رقم المشتري',fg='white',bg='#0B4C5F',font=('tajawal',13,'bold'))
                bill_num.place(x=232,y=100)
                ent_name=Entry(f1,justify='center',textvariable=self.nemo)
                ent_name.place(x=90,y=43)
                ent_phone=Entry(f1,justify='center',textvariable=self.phono)
                ent_phone.place(x=90,y=73)
                ent_bill=Entry(f1,justify='center',textvariable=self.fatora)
                ent_bill.place(x=90,y=103)
                btn_customer=Button(f1,text='بحث',width=6,height=4,bg='white',font=('tajawal',13,'bold'),command=self.find)
                btn_customer.place(x=10,y=40)
                #======================bill==============================
                titdd=Label(f1,text='[الفواتير]',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='gold')
                titdd.place(x=125,y=135)
                f3=Frame(root,bd=2,width=338,height=399,bg='white')
                f3.place(x=961,y=205)
                scroll_y=Scrollbar(f3,orient=VERTICAL)
                self.textarea=Text(f3,yscrollcommand=scroll_y.set)
                scroll_y.pack(side=LEFT,fill=Y)
                scroll_y.config(command=self.textarea.yview)
                self.textarea.pack(fill=BOTH,expand=1)
                
                #=========================price=================================
                f4=Frame(root,bd=2,width=667,height=112,bg='#0B4C5F')
                f4.place(x=641,y=587)
                hesab=Button(f4,text='الحساب',width=13,height=1,font=('tajawal',13,'bold'),fg='#0B4C5F',bg='gold',command=self.total)
                hesab.place(x=507,y=10)
                fatora1=Button(f4,text='تصدير الفاتورة',width=13,height=1,font=('tajawal',13,'bold'),fg='#0B4C5F',bg='gold',command=self.billing)
                fatora1.place(x=507,y=55)
                clear=Button(f4,text='افراغ الحقول ',width=13,height=1,font=('tajawal',13,'bold'),fg='#0B4C5F',bg='gold',command=self.clear)
                clear.place(x=365,y=10)
                exite=Button(f4,text='الخروج من البرنامج',width=13,height=1,font=('tajawal',13,'bold'),fg='#0B4C5F',bg='gold',command=self.exet)
                exite.place(x=365,y=55)

                lblo1=Label(f4,text='الحساب الكلي للبوقوليات',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='gold')
                lblo1.place(x=210,y=10)
                lblo2=Label(f4,text='الحساب الكلي للحوم',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='gold')
                lblo2.place(x=240,y=40)
                lblo3=Label(f4,text='الحساب الكلي للمشروبات الغازية والعصائر',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='gold')
                lblo3.place(x=115,y=70)
                ento1=Entry(f4,width=16,textvariable=self.bacoliat)
                ento1.place(x=10,y=12)
                ento2=Entry(f4,width=16,textvariable=self.lohom)
                ento2.place(x=10,y=42)
                ento3=Entry(f4,width=16,textvariable=self.drinks)
                ento3.place(x=10,y=72)
                #===========================items1=================================
                ff1=Frame(root,bd=2,width=318,height=664,bg='#0B4C5F')
                ff1.place(x=1,y=31)
                t=Label(ff1,text='البقوليات',font=('tajawal',15,'bold'),bg='#0B4C5F',fg='gold')
                t.place(x=122,y=0)
                bq1=Label(ff1,text='مكرونة',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='white')
                bq1.place(x=250,y=50)
                bq2=Label(ff1,text='عدس',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='white')
                bq2.place(x=260,y=80)
                bq3=Label(ff1,text='فول',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='white')
                bq3.place(x=265,y=110)
                bq4=Label(ff1,text='بطاطس',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='white')
                bq4.place(x=245,y=140)
                bq5=Label(ff1,text='طماطم',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='white')
                bq5.place(x=250,y=170)
                bq6=Label(ff1,text='لوبيا',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='white')
                bq6.place(x=260,y=200)
                bq7=Label(ff1,text='فاصوليا',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='white')
                bq7.place(x=242,y=230)
                bq8=Label(ff1,text='بصل',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='white')
                bq8.place(x=258,y=270)
                bq9=Label(ff1,text='رز',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='white')
                bq9.place(x=266,y=300)
                bq10=Label(ff1,text='جزر',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='white')
                bq10.place(x=258,y=330)
                bq11=Label(ff1,text='خيار',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='white')
                bq11.place(x=255,y=370)
                bq12=Label(ff1,text='شعرية',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='white')
                bq12.place(x=247,y=400)
                bq13=Label(ff1,text='لسان عصفور',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='white')
                bq13.place(x=207,y=430)
                bq14=Label(ff1,text='صلصة',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='white')
                bq14.place(x=247,y=470)
                bq15=Label(ff1,text='فلفل شطة',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='white')
                bq15.place(x=226,y=500)
                bq16=Label(ff1,text='فلفل رومي',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='white')
                bq16.place(x=221,y=530)
                bq17=Label(ff1,text='كوسة',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='white')
                bq17.place(x=249,y=570)
                bq18=Label(ff1,text='باذنجان',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='white')
                bq18.place(x=243,y=600)
                bqent1=Entry(ff1,width=12,textvariable=self.q1)
                bqent1.place(x=70,y=50)
                bqent2=Entry(ff1,width=12,textvariable=self.q2)
                bqent2.place(x=70,y=80)
                bqent3=Entry(ff1,width=12,textvariable=self.q3)
                bqent3.place(x=70,y=110)
                bqent4=Entry(ff1,width=12,textvariable=self.q4)
                bqent4.place(x=70,y=140)
                bqent5=Entry(ff1,width=12,textvariable=self.q5)
                bqent5.place(x=70,y=170)
                bqent6=Entry(ff1,width=12,textvariable=self.q6)
                bqent6.place(x=70,y=200)
                bqent7=Entry(ff1,width=12,textvariable=self.q7)
                bqent7.place(x=70,y=230)
                bqent8=Entry(ff1,width=12,textvariable=self.q8)
                bqent8.place(x=70,y=270)
                bqent9=Entry(ff1,width=12,textvariable=self.q9)
                bqent9.place(x=70,y=300)
                bqent10=Entry(ff1,width=12,textvariable=self.q10)
                bqent10.place(x=70,y=330)
                bqent11=Entry(ff1,width=12,textvariable=self.q11)
                bqent11.place(x=70,y=370)
                bqent12=Entry(ff1,width=12,textvariable=self.q12)
                bqent12.place(x=70,y=400)
                bqent13=Entry(ff1,width=12,textvariable=self.q13)
                bqent13.place(x=70,y=430)
                bqent14=Entry(ff1,width=12,textvariable=self.q14)
                bqent14.place(x=70,y=470)
                bqent15=Entry(ff1,width=12,textvariable=self.q15)
                bqent15.place(x=70,y=500)
                bqent16=Entry(ff1,width=12,textvariable=self.q16)
                bqent16.place(x=70,y=530)
                bqent17=Entry(ff1,width=12,textvariable=self.q17)
                bqent17.place(x=70,y=570)
                bqent18=Entry(ff1,width=12,textvariable=self.q18)
                bqent18.place(x=70,y=600)
                #=========================items2======================================
                ff2=Frame(root,bd=2,width=318,height=664,bg='#0B4C5F')
                ff2.place(x=321,y=31)
                t1=Label(ff2,text='اللحوم',font=('tajawal',15,'bold'),bg='#0B4C5F',fg='gold')
                t1.place(x=122,y=0)
                lo1=Label(ff2,text='لحمة بقري',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='white')
                lo1.place(x=240,y=50)
                lo2=Label(ff2,text='لحمة بتلو',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='white')
                lo2.place(x=247,y=80)
                lo3=Label(ff2,text='لحمة جاموسي',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='white')
                lo3.place(x=220,y=110)
                lo4=Label(ff2,text='لحمة ماعز',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='white')
                lo4.place(x=242,y=140)
                lo5=Label(ff2,text='لحمة ضاني ',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='white')
                lo5.place(x=237,y=170)
                lo6=Label(ff2,text='لحمة جملي',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='white')
                lo6.place(x=239,y=200)
                lo7=Label(ff2,text='فراخ بلدي ',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='white')
                lo7.place(x=242,y=230)
                lo8=Label(ff2,text='فراخ بيضة',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='white')
                lo8.place(x=240,y=270)
                lo9=Label(ff2,text='حمام',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='white')
                lo9.place(x=272,y=300)
                lo10=Label(ff2,text='سمان',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='white')
                lo10.place(x=270,y=330)
                lo11=Label(ff2,text='سمك طوبار',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='white')
                lo11.place(x=237,y=370)
                lo12=Label(ff2,text='سمك شبار',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='white')
                lo12.place(x=245,y=400)
                lo13=Label(ff2,text=' سمك بوري',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='white')
                lo13.place(x=235,y=430)
                lo14=Label(ff2,text='سمك تونة',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='white')
                lo14.place(x=245,y=470)
                lo15=Label(ff2,text='سمك باغا ',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='white')
                lo15.place(x=247,y=500)
                lo16=Label(ff2,text=' تونة',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='white')
                lo16.place(x=268,y=530)
                lo17=Label(ff2,text='جمبري',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='white')
                lo17.place(x=258,y=570)
                lo18=Label(ff2,text='كابوريا',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='white')
                lo18.place(x=256,y=600)

                loent1=Entry(ff2,width=12,textvariable=self.qq1)
                loent1.place(x=70,y=50)
                loent2=Entry(ff2,width=12,textvariable=self.qq2)
                loent2.place(x=70,y=80)
                loent3=Entry(ff2,width=12,textvariable=self.qq3)
                loent3.place(x=70,y=110)
                loent4=Entry(ff2,width=12,textvariable=self.qq4)
                loent4.place(x=70,y=140)
                loent5=Entry(ff2,width=12,textvariable=self.qq5)
                loent5.place(x=70,y=170)
                loent6=Entry(ff2,width=12,textvariable=self.qq6)
                loent6.place(x=70,y=200)
                loent7=Entry(ff2,width=12,textvariable=self.qq7)
                loent7.place(x=70,y=230)
                loent8=Entry(ff2,width=12,textvariable=self.qq8)
                loent8.place(x=70,y=270)
                loent9=Entry(ff2,width=12,textvariable=self.qq9)
                loent9.place(x=70,y=300)
                loent10=Entry(ff2,width=12,textvariable=self.qq10)
                loent10.place(x=70,y=330)
                loent11=Entry(ff2,width=12,textvariable=self.qq11)
                loent11.place(x=70,y=370)
                loent12=Entry(ff2,width=12,textvariable=self.qq12)
                loent12.place(x=70,y=400)
                loent13=Entry(ff2,width=12,textvariable=self.qq13)
                loent13.place(x=70,y=430)
                loent14=Entry(ff2,width=12,textvariable=self.qq14)
                loent14.place(x=70,y=470)
                loent15=Entry(ff2,width=12,textvariable=self.qq15)
                loent15.place(x=70,y=500)
                loent16=Entry(ff2,width=12,textvariable=self.qq16)
                loent16.place(x=70,y=530)
                loent17=Entry(ff2,width=12,textvariable=self.qq17)
                loent17.place(x=70,y=570)
                loent18=Entry(ff2,width=12,textvariable=self.qq18)
                loent18.place(x=70,y=600)

                #=============================items3=============================
                ff3=Frame(root,bd=2,width=318,height=553,bg='#0B4C5F')
                ff3.place(x=641,y=31)

                t2=Label(ff3,text='المشروبات',font=('tajawal',15,'bold'),bg='#0B4C5F',fg='gold')
                t2.place(x=122,y=0)

                ma1=Label(ff3,text=' بيبسي',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='white')
                ma1.place(x=257,y=50)
                ma2=Label(ff3,text=' كوكاكولا',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='white')
                ma2.place(x=247,y=80)
                ma3=Label(ff3,text='ستنج ',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='white')
                ma3.place(x=266,y=110)
                ma4=Label(ff3,text=' تويست',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='white')
                ma4.place(x=253,y=140)
                ma5=Label(ff3,text='ريدبول  ',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='white')
                ma5.place(x=256,y=170)
                ma6=Label(ff3,text='فانتا تفاح ',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='white')
                ma6.place(x=241,y=200)
                ma7=Label(ff3,text='فانتا برتفال  ',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='white')
                ma7.place(x=232,y=230)
                ma8=Label(ff3,text='فيروز ',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='white')
                ma8.place(x=261,y=270)
                ma9=Label(ff3,text='شويبس',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='white')
                ma9.place(x=250,y=300)
                ma10=Label(ff3,text='عصير بيتي',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='white')
                ma10.place(x=230,y=330)
                ma11=Label(ff3,text='عصير جهينة ',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='white')
                ma11.place(x=222,y=370)
                ma12=Label(ff3,text=' عصير المراعي',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='white')
                ma12.place(x=206,y=400)
                ma13=Label(ff3,text=' عصير كل يوم',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='white')
                ma13.place(x=214,y=430)
                ma14=Label(ff3,text='مياه معدنية ص ',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='white')
                ma14.place(x=206,y=470)
                ma15=Label(ff3,text=' مياه معدنية ك ',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='white')
                ma15.place(x=209,y=500)

                maent1=Entry(ff3,width=12,textvariable=self.qqq1)
                maent1.place(x=70,y=50)
                maent2=Entry(ff3,width=12,textvariable=self.qqq2)
                maent2.place(x=70,y=80)
                maent3=Entry(ff3,width=12,textvariable=self.qqq3)
                maent3.place(x=70,y=110)
                maent4=Entry(ff3,width=12,textvariable=self.qqq4)
                maent4.place(x=70,y=140)
                maent5=Entry(ff3,width=12,textvariable=self.qqq5)
                maent5.place(x=70,y=170)
                maent6=Entry(ff3,width=12,textvariable=self.qqq6)
                maent6.place(x=70,y=200)
                maent7=Entry(ff3,width=12,textvariable=self.qqq7)
                maent7.place(x=70,y=230)
                maent8=Entry(ff3,width=12,textvariable=self.qqq8)
                maent8.place(x=70,y=270)
                maent9=Entry(ff3,width=12,textvariable=self.qqq9)
                maent9.place(x=70,y=300)
                maent10=Entry(ff3,width=12,textvariable=self.qqq10)
                maent10.place(x=70,y=330)
                maent11=Entry(ff3,width=12,textvariable=self.qqq11)
                maent11.place(x=70,y=370)
                maent12=Entry(ff3,width=12,textvariable=self.qqq12)
                maent12.place(x=70,y=400)
                maent13=Entry(ff3,width=12,textvariable=self.qqq13)
                maent13.place(x=70,y=430)
                maent14=Entry(ff3,width=12,textvariable=self.qqq14)
                maent14.place(x=70,y=470)
                maent15=Entry(ff3,width=12,textvariable=self.qqq15)
                maent15.place(x=70,y=500)
                self.fatorabill()
            def fatorabill(self):
                self.textarea.delete('1.0',END)
                self.textarea.insert(END,"\tسوبر ماركت creativity يرحب بكم")
                self.textarea.insert(END,"\n  ====================================")
                self.textarea.insert(END,f"\n\t B.NUM  : {self.fatora.get()}")
                self.textarea.insert(END,f"\n\t Name   : {self.nemo.get()}")
                self.textarea.insert(END,f"\n\t Phone  : {self.phono.get()}")
                self.textarea.insert(END,"\n======================================")
                self.textarea.insert(END,f"\nالسعر\t      العدد\t       المشتريات ")
                self.textarea.insert(END,"\n======================================")

            def total (self):
                self.makrona=self.q1.get()*10
                self.ads=self.q2.get()*8
                self.fol=self.q3.get()*7
                self.batates=self.q4.get()*12
                self.tomato=self.q5.get()*10
                self.lobya=self.q6.get()*14
                self.fasolia=self.q7.get()*14
                self.basl=self.q8.get()*20
                self.roz=self.q9.get()*15
                self.gazr=self.q10.get()*12
                self.khear=self.q11.get()*10
                self.sherea=self.q12.get()*10
                self.lesanasfor=self.q13.get()*10
                self.salsa=self.q14.get()*6
                self.felflshata=self.q15.get()*16
                self.felfelromy=self.q16.get()*18
                self.kosa=self.q17.get()*20
                self.bazengan=self.q18.get()*10

                self.totalito=float(self.makrona +
                                    self.ads +
                                    self.fol +
                                    self.batates+
                                    self.tomato +
                                    self.lobya +
                                    self.fasolia +
                                    self.basl +
                                    self.roz +
                                    self.gazr +
                                    self.khear +
                                    self.sherea +
                                    self.lesanasfor+
                                    self.salsa +
                                    self.felflshata+
                                    self.felfelromy +
                                    self.kosa +
                                    self.bazengan
                                    )
                self.bacoliat.set(str(self.totalito)+"$")

                self.bakary=self.qq1.get()*400
                self.betli=self.qq2.get()*380
                self.gamosy=self.qq3.get()*400
                self.maez=self.qq4.get()*400
                self.dany=self.qq5.get()*400
                self.gamaly=self.qq6.get()*450
                self.balady=self.qq7.get()*90
                self.beda=self.qq8.get()*80
                self.hmam=self.qq9.get()*70
                self.seman=self.qq10.get()*45
                self.tobar=self.qq11.get()*90
                self.shabar=self.qq12.get()*70
                self.bory=self.qq13.get()*110
                self.samaktona=self.qq14.get()*80
                self.bagha=self.qq15.get()*130
                self.tona=self.qq16.get()*50
                self.gambary=self.qq17.get()*250
                self.kaborya=self.qq18.get()*100
                
                self.lohom1=float(self.bakary +
                                    self.betli +
                                    self.gamosy +
                                    self.maez+
                                    self.dany +
                                    self.gamaly +
                                    self.balady +
                                    self.beda +
                                    self.hmam +
                                    self.seman +
                                    self.tobar +
                                    self.shabar+
                                    self.bory +
                                    self.samaktona+
                                    self.bagha +
                                    self.tona +
                                    self.gambary +
                                    self.kaborya
                                    )
                self.lohom.set(str(self.lohom1)+"$")

                self.bebsi=self.qqq1.get()*13
                self.cocacola=self.qqq2.get()*13
                self.sting=self.qqq3.get()*10
                self.toest=self.qqq4.get()*15
                self.redbol=self.qqq5.get()*35
                self.fanta_t=self.qqq6.get()*13
                self.fanta_b=self.qqq7.get()*13
                self.fayroz=self.qqq8.get()*15
                self.sheobs=self.qqq9.get()*13
                self.bety=self.qqq10.get()*10
                self.gohina=self.qqq11.get()*10
                self.marii=self.qqq12.get()*10
                self.kolyom=self.qqq13.get()*8
                self.maia_s=self.qqq14.get()*5
                self.maia_k=self.qqq15.get()*10
                
                self.mashrobat=float(self.bebsi +
                                    self.cocacola +
                                    self.sting +
                                    self.toest+
                                    self.redbol +
                                    self.fanta_t +
                                    self.fanta_b +
                                    self.fayroz +
                                    self.sheobs +
                                    self.bety +
                                    self.gohina +
                                    self.marii+
                                    self.kolyom +
                                    self.maia_s+
                                    self.maia_k 
                                
                                    )
                self.drinks.set(str(self.mashrobat)+"$")

                self.all=float(self.totalito+self.lohom1+self.mashrobat)


            def clear (self):
                self.q1.set(0)
                self.q2.set(0)
                self.q3.set(0)
                self.q4.set(0)
                self.q5.set(0)
                self.q6.set(0)
                self.q7.set(0)
                self.q8.set(0)
                self.q9.set(0)
                self.q10.set(0)
                self.q11.set(0)
                self.q12.set(0)
                self.q13.set(0)
                self.q14.set(0)
                self.q15.set(0)
                self.q16.set(0)
                self.q17.set(0)
                self.q18.set(0)
                self.qq1.set(0)
                self.qq2.set(0)
                self.qq3.set(0)
                self.qq4.set(0)
                self.qq5.set(0)
                self.qq6.set(0)
                self.qq7.set(0)
                self.qq8.set(0)
                self.qq9.set(0)
                self.qq10.set(0)
                self.qq11.set(0)
                self.qq12.set(0)
                self.qq13.set(0)
                self.qq14.set(0)
                self.qq15.set(0)
                self.qq16.set(0)
                self.qq17.set(0)
                self.qq18.set(0)
                self.qqq1.set(0)
                self.qqq2.set(0)
                self.qqq3.set(0)
                self.qqq4.set(0)
                self.qqq5.set(0)
                self.qqq6.set(0)
                self.qqq7.set(0)
                self.qqq8.set(0)
                self.qqq9.set(0)
                self.qqq10.set(0)
                self.qqq11.set(0)
                self.qqq12.set(0)
                self.qqq13.set(0)
                self.qqq14.set(0)
                self.qqq15.set(0)

                self.bacoliat.set(0)
                self.lohom.set(0)
                self.drinks.set(0)

                self.nemo.set("")
                self.phono.set("")
                self.fatora.set("")

            def exet(self):
                self.root.destroy()

            def billing(self):
                if self.nemo.get()=="" or self.phono.get()=="":
                    messagebox.showerror("حدث خطأ","لا يجوز ترك حقل الاسم ورقم الهاتف فارغا")
                elif self.bacoliat.get()=="0.0 $" and self.lohom.get()=="0.0 $" and self.drinks.get()=="0.0 $":
                    messagebox.showerror("حدث خطأ"," ليس هناك منتجات محددة ولم يتم اختيار احداها يجب اختيار عدد المنتجات")
                else:
                    self.fatorabill()
                    if self.q1.get()!=0:
                        self.textarea.insert(END,f"\n {self.makrona}\t\t{self.q1.get()}\t\t مكرونة ")
                    if self.q2.get()!=0:
                        self.textarea.insert(END,f"\n {self.ads}\t\t{self.q2.get()}\t\t عدس")
                    if self.q3.get()!=0:
                        self.textarea.insert(END,f"\n {self.fol}\t\t{self.q3.get()}\t\tفول ")
                    if self.q4.get()!=0:
                        self.textarea.insert(END,f"\n {self.batates}\t\t{self.q4.get()}\t\t بطاطس")
                    if self.q5.get()!=0:
                        self.textarea.insert(END,f"\n {self.tomato}\t\t{self.q5.get()}\t\tطماطم")
                    if self.q6.get()!=0:
                        self.textarea.insert(END,f"\n {self.lobya}\t\t{self.q6.get()}\t\tلوبيا")
                    if self.q7.get()!=0:
                        self.textarea.insert(END,f"\n {self.fasolia}\t\t{self.q7.get()}\t\tفاصوليا")
                    if self.q8.get()!=0:
                        self.textarea.insert(END,f"\n {self.basl}\t\t{self.q8.get()}\t\tبصل")
                    if self.q9.get()!=0:
                        self.textarea.insert(END,f"\n {self.roz}\t\t{self.q9.get()}\t\tارز ")
                    if self.q10.get()!=0:
                        self.textarea.insert(END,f"\n {self.gazr}\t\t{self.q10.get()}\t\tجزر")
                    if self.q11.get()!=0:
                        self.textarea.insert(END,f"\n {self.khear}\t\t{self.q11.get()}\t\t  خيار ")
                    if self.q12.get()!=0:
                        self.textarea.insert(END,f"\n {self.sherea}\t\t{self.q12.get()}\t\t  شعرية")
                    if self.q13.get()!=0:
                        self.textarea.insert(END,f"\n {self.lesanasfor}\t\t{self.q13.get()}\t\tلسان عصفور")
                    if self.q14.get()!=0:
                        self.textarea.insert(END,f"\n {self.salsa}\t\t{self.q14.get()}\t\t صلصة")
                    if self.q15.get()!=0:
                        self.textarea.insert(END,f"\n {self.felflshata}\t\t{self.q15.get()}\t\tفلفل شطة ")
                    if self.q16.get()!=0:
                        self.textarea.insert(END,f"\n {self.felfelromy}\t\t{self.q16.get()}\t\tفلفل رومي")
                    if self.q17.get()!=0:
                        self.textarea.insert(END,f"\n {self.kosa}\t\t{self.q17.get()}\t\tكوسة")
                    if self.q18.get()!=0:
                        self.textarea.insert(END,f"\n {self.bazengan}\t\t{self.q18.get()}\t\tباذنجان")


                    if self.qq1.get()!=0:
                        self.textarea.insert(END,f"\n {self.bakary}\t\t{self.qq1.get()}\t\t لحمة بقري")
                    if self.qq2.get()!=0:
                        self.textarea.insert(END,f"\n {self.betli}\t\t{self.qq2.get()}\t\t لحمة بتلو")
                    if self.qq3.get()!=0:
                        self.textarea.insert(END,f"\n {self.gamosy}\t\t{self.qq3.get()}\t\tلحمة جاموسي")
                    if self.qq4.get()!=0:
                        self.textarea.insert(END,f"\n {self.maez}\t\t{self.qq4.get()}\t\t لحمة ماعز")
                    if self.qq5.get()!=0:
                        self.textarea.insert(END,f"\n {self.dany}\t\t{self.qq5.get()}\t\t لحمة ضاني")
                    if self.qq6.get()!=0:
                        self.textarea.insert(END,f"\n {self.gamaly}\t\t{self.qq6.get()}\t\t لحمة جملي")
                    if self.qq7.get()!=0:
                        self.textarea.insert(END,f"\n {self.balady}\t\t{self.qq7.get()}\t\t فراخ بلدي")
                    if self.qq8.get()!=0:
                        self.textarea.insert(END,f"\n {self.beda}\t\t{self.qq8.get()}\t\t فراخ بيضة")
                    if self.qq9.get()!=0:
                        self.textarea.insert(END,f"\n {self.hmam}\t\t{self.qq9.get()}\t\t حمام ")
                    if self.qq10.get()!=0:
                        self.textarea.insert(END,f"\n {self.seman}\t\t{self.qq10.get()}\t\t سمان")
                    if self.qq11.get()!=0:
                        self.textarea.insert(END,f"\n {self.tobar}\t\t{self.qq11.get()}\t\t  سمك طوبار ")
                    if self.qq12.get()!=0:
                        self.textarea.insert(END,f"\n {self.shabar}\t\t{self.qq12.get()}\t\t  سمك شبار")
                    if self.qq13.get()!=0:
                        self.textarea.insert(END,f"\n {self.bory}\t\t{self.qq13.get()}\t\t سمك بوري ")
                    if self.qq14.get()!=0:
                        self.textarea.insert(END,f"\n {self.samaktona}\t\t{self.qq14.get()}\t\t سمك تونة")
                    if self.qq15.get()!=0:
                        self.textarea.insert(END,f"\n {self.bagha}\t\t{self.qq15.get()}\t\t سمك باغا  ")
                    if self.qq16.get()!=0:
                        self.textarea.insert(END,f"\n {self.tona}\t\t{self.qq16.get()}\t\t تونة")
                    if self.qq17.get()!=0:
                        self.textarea.insert(END,f"\n {self.gambary}\t\t{self.qq17.get()}\t\t جمبري")
                    if self.qq18.get()!=0:
                        self.textarea.insert(END,f"\n {self.kaborya}\t\t{self.qq18.get()}\t\t كابوريا")


                    if self.qqq1.get()!=0:
                        self.textarea.insert(END,f"\n {self.bebsi}\t\t{self.qqq1.get()}\t\t  بيبسي")
                    if self.qqq2.get()!=0:
                        self.textarea.insert(END,f"\n {self.cocacola}\t\t{self.qqq2.get()}\t\t  كوكاكولا")
                    if self.qqq3.get()!=0:
                        self.textarea.insert(END,f"\n {self.sting}\t\t{self.qqq3.get()}\t\t ستنج")
                    if self.qqq4.get()!=0:
                        self.textarea.insert(END,f"\n {self.toest}\t\t{self.qqq4.get()}\t\t  تويست")
                    if self.qqq5.get()!=0:
                        self.textarea.insert(END,f"\n {self.redbol}\t\t{self.qqq5.get()}\t\t  ريدبول")
                    if self.qqq6.get()!=0:
                        self.textarea.insert(END,f"\n {self.fanta_t}\t\t{self.qqq6.get()}\t\t  فانتا تفاح")
                    if self.qqq7.get()!=0:
                        self.textarea.insert(END,f"\n {self.fanta_b}\t\t{self.qqq7.get()}\t\t  فانتا برتقال")
                    if self.qqq8.get()!=0:
                        self.textarea.insert(END,f"\n {self.fayroz}\t\t{self.qqq8.get()}\t\t  فيروز")
                    if self.qqq9.get()!=0:
                        self.textarea.insert(END,f"\n {self.sheobs}\t\t{self.qqq9.get()}\t\t شويبس ")
                    if self.qqq10.get()!=0:
                        self.textarea.insert(END,f"\n {self.bety}\t\t{self.qqq10.get()}\t\t عصير بيتي")
                    if self.qqq11.get()!=0:
                        self.textarea.insert(END,f"\n {self.gohina}\t\t{self.qqq11.get()}\t\t عصير جهينة ")
                    if self.qqq12.get()!=0:
                        self.textarea.insert(END,f"\n {self.marii}\t\t{self.qqq12.get()}\t\t   عصير المراعي")
                    if self.qqq13.get()!=0:
                        self.textarea.insert(END,f"\n {self.kolyom}\t\t{self.qqq13.get()}\t\t  عصير كل يوم ")
                    if self.qqq14.get()!=0:
                        self.textarea.insert(END,f"\n {self.maia_s}\t\t{self.qqq14.get()}\t\t  مياه صغيرة")
                    if self.qqq15.get()!=0:
                        self.textarea.insert(END,f"\n {self.maia_k}\t\t{self.qqq15.get()}\t\t  مياه كبيرة  ")

                    self.textarea.insert(END,"\n......................................")
                    self.textarea.insert(END,f"\n\t{self.all} $\t     المجموع الكلي")
                    self.textarea.insert(END,"\n......................................")
                    self.savee()

            def savee(self):
                op = messagebox.askyesno("هل تريد حفظ الفاتورة ؟","حفظ")
                if op > 0 :
                    self.bb = self.textarea.get('1.0',END)
                    f1 = open('D:\\programming project\\python\\desktopApp\\supermarket project\\buy\\ '+str(self.fatora.get())+".txt","w",encoding="utf-8")
                    f1.write(self.bb)
                    f1.close()
                else:
                    return
                
            
            def find(self):
                present="no"
                for i in os.listdir("D:\\programming project\\python\\desktopApp\\supermarket project\\buy\\"):
                    if i.split('.')[0] == self.fatora.get():
                        f1=open(f"D:\\programming project\\python\\desktopApp\\supermarket project\\buy\\{i}","r",encoding="utf-8")
                        self.textarea.delete('1.0',END)
                        for d in f1:
                            self.textarea.insert(END,d)
                        self.textarea.insert(END,'')
                        f1.close()
                        present="yes"
                if present == "no":
                        messagebox.showerror('خطأ',' لا توجد اي فاتورة تحمل الرقم الذي كتبته  ')
                



                    

                
                
                










                







        root=Tk()
        ob=super1(root)

        root.mainloop()
    else:
        messagebox.showerror('تحذير', 'ادخلت بيانات خطأ')


    

    

f1111 = Frame(pro, width=230, height=420, bg='#008080')
f1111.place(x=570, y=30)
titlel2 = Label(f1111, text='ادارة السوبر ماركت ', fg='gold', bg='#008080', font=('tajawal', '12', 'bold'))
titlel2.place(x=55, y=10)
titlel3 = Label(f1111, text='المطور احمد ابراهيم', fg='gold', bg='#008080', font=('tajawal', '12', 'bold'))
titlel3.place(x=54, y=50)
titlel4 = Label(f1111, text='وسائل التواصل معنا ', fg='gold', bg='#008080', font=('tajawal', '12', 'bold'))
titlel4.place(x=55, y=90)
B1 = Button(f1111, text='حسابنا علي فيسبوك', width=23, fg='black', bg='gold', font=('tajawal', '11', 'bold'), command=facebook)
B1.place(x=6, y=130)
B2 = Button(f1111, text='حسابنا علي واتساب', width=23, fg='black', bg='gold', font=('tajawal', '11', 'bold'), command=whatsabb)
B2.place(x=6, y=177)
B3 = Button(f1111, text='حسابنا علي انستجرام', width=23, fg='black', bg='gold', font=('tajawal', '11', 'bold'), command=instgram)
B3.place(x=6, y=225)
B4 = Button(f1111, text=' لمحة عن المطور ', width=23, fg='black', bg='gold', font=('tajawal', '11', 'bold'), command=about1)
B4.place(x=6, y=272)
B5 = Button(f1111, text=' لمحة عن البرنامج ', width=23, fg='black', bg='gold', font=('tajawal', '11', 'bold'), command=about2)
B5.place(x=6, y=318)
B6 = Button(f1111, text=' اغلاق البرنامج ', width=23, fg='black', bg='gold', font=('tajawal', '11', 'bold'), command=pro.quit)
B6.place(x=6, y=365)
photo = PhotoImage(file='D:\\programming project\\python\\desktopApp\\supermarket project\\super3.png')
imo = Label(pro, image=photo)
imo.place(x=0, y=32, width=570, height=300)
f2222 = Frame(pro, width=570, height=120, bg='#008080')
f2222.place(x=0, y=330)
photo1 = PhotoImage(file='D:\\programming project\\python\\desktopApp\\supermarket project\\login.png')
imo1 = Label(pro, image=photo1)
imo1.place(x=450, y=335, width=110, height=110)
l1 = Label(f2222, text='اسم المستخدم ', fg='gold', bg='#008080', font=('tajawal', '12', 'bold'))
l1.place(x=370, y=25)
l2 = Label(f2222, text=' كلمة المرور ', fg='gold', bg='#008080', font=('tajawal', '12', 'bold'))
l2.place(x=370, y=70)
en1 = Entry(f2222, font=('tajawal', '12', 'bold'), justify='center')
en1.place(x=130, y=26)
en2 = Entry(f2222, font=('tajawal', '12', 'bold'), justify='center', show='*')
en2.place(x=130, y=70)
B = Button(f2222, text='تسجيل الدخول', bg='gold', fg='#008080', font=('tajawal', '12', 'bold'), command=log)
B.place(x=10, y=30, height=55)

pro.mainloop()
