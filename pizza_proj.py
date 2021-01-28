from sqlite3 import *
from tkinter import *
from tkinter import messagebox

class Login:

    pizzalist=[("Margherita",100,150,200),("Double Cheese",150,200,250),("Paneer Fest",175,225,275),("Italian Supreme",250,300,350),("Country Feast",300,350,400),("Exotic Supreme",500,550,600),
 ("Spicy Chicken",350,400,450),("Chickeroni",400,450,500),("Chicken Tikka",450,500,550),("Chicken Supremo",500,550,600),("Chicken Italian",600,650,700),("Chicken Exotica",700,750,800),
 ("Garlic Dip",20,40,50),("CheeZee Sticks",75,100,125),("Wings O' Hotness",140,180,200),("Brazilian Veg Pasta",150,180,210),("Chicken Pasta",200,230,250),("Chicken Paneer",250,270,300),
 ("Coca-Cola",40,60,80),("Thumbs Up",40,60,80),("Pepsi",40,60,80),("Mirinda",40,60,80),("7-UP",40,60,80),("Fanta",40,60,80)]
    bill=[]

    
    
    def __init__(sf):
        sf.c=connect("mydata.db")
        sf.cur=sf.c.cursor()
        try:
            sf.cur.execute("create table staff(user varchar(50),passw varchar(50))")
        except:
            pass
        sf.scr=Tk(className="Pizza Management System")
        sf.scr.geometry('900x440')
       
        #Frame of login buttons
        sf.f=Frame(sf.scr,bg="blue")
        sf.f.pack_propagate(0)
        sf.f.pack(fill=BOTH,expand=1,side=RIGHT)
        imgs=PhotoImage(file='images/Untitled-5.png')
        sf.l2=Label(sf.f,image=imgs,height=300)
        sf.l2.place(x=0, y=0, relwidth=1, relheight=1)

        sf.f1=Frame(sf.f,bg='black')
        sf.f1.pack(side=LEFT)
        sf.l=Label(sf.f1,bg='black',fg='red',font=('times',20,'bold'),text='User Name')
        sf.l.grid(row=1,column=3)
        sf.user=Entry(sf.f1,bg='black',bd=5,fg='white',selectborderwidth=10,font=('times',20,'bold'))
        sf.user.grid(row=1,column=4)
        sf.l1=Label(sf.f1,bg='black',fg='red',font=('times',20,'bold'),text='Password')
        sf.l1.grid(row=2,column=3)
        sf.passw=Entry(sf.f1,bg='black',bd=5,fg='white',font=('times',20,'bold'),show='*')
        sf.passw.grid(row=2,column=4)
        sf.b=Button(sf.f1,text="Submit",bg='black',fg='red',font=('times',20,'bold'),relief=FLAT,command=lambda :sf.result("login"))
        sf.b.grid(row=5,column=3)
        sf.b1=Button(sf.f1,text="Register",bg='black',fg='red',font=('times',20,'bold'),relief=FLAT,command=sf.register)
        sf.b1.grid(row=5,column=4)

        
        sf.scr.mainloop()

#User register screen        
    def register(sf):
        try:
            sf.scr.destroy()
        except:
            try:
                sf.scr1.destroy()
            except:
                pass
        sf.scr1=Tk(className="Pizza Management System Register")
        sf.scr1.geometry('800x340')

        sf.f=Frame(sf.scr1,bg="blue")
        sf.f.pack_propagate(0)
        sf.f.pack(fill=BOTH,expand=1,side=RIGHT)
        img3=PhotoImage(file='images/3557a5e1c942b53.png')
        sf.l2=Label(sf.f,image=img3,height=300)
        sf.l2.place(x=0, y=0, relwidth=1, relheight=1)
        
        sf.l=Label(sf.f,bg='black',fg='white',font=('times',20,'bold'),text='User Name')
        sf.l.grid(row=1,column=0)
        sf.user=Entry(sf.f,bg='black',bd=5,fg='white',font=('times',20,'bold'))
        sf.user.grid(row=1,column=1)
        sf.l1=Label(sf.f,bg='black',fg='white',font=('times',20,'bold'),text='Password')
        sf.l1.grid(row=2,column=0)
        sf.passw=Entry(sf.f,bg='black',bd=5,fg='white',font=('times',20,'bold'),show='*')
        sf.passw.grid(row=2,column=1)
        sf.l2=Label(sf.f,bg='black',fg='white',font=('times',20,'bold'),text='Retype Password')
        sf.l2.grid(row=3,column=0)
        sf.passw1=Entry(sf.f,bg='black',bd=5,fg='white',font=('times',20,'bold'),show='*')
        sf.passw1.grid(row=3,column=1)
        sf.b=Button(sf.f,text="Submit",bg='black',fg='white',font=('times',20,'bold'),command=lambda :sf.result("register"))
        sf.b.grid(row=4,column=0)
        sf.b1=Button(sf.f,text="Clear",bg='black',fg='white',font=('times',20,'bold'))
        sf.b1.grid(row=4,column=1)
        sf.scr1.mainloop()

#Final Bill
    def finalbill(sf):
        sf.scr3.destroy()
        sf.scr5=Tk(className="bill")
        sf.scr5.geometry("1350x700+0+0")
        sf.i=PhotoImage(file='images/piizza0.png')
        sf.lbg=Label(sf.scr5,image=sf.i)
        sf.lbg.place(x=0,y=0,relheight=1,relwidth=1)

        sf.t=Frame(sf.scr5, width=1350, height=100 ,bd=14,relief="raise")
        sf.t.pack(side=TOP)

        sf.f2=Frame(sf.scr5, width=1350, height=650 ,bd=8,relief="raise")
        sf.f2.pack(side=BOTTOM)
        sf.i2=PhotoImage(file='images/piizza2.png')
        sf.lbg2=Label(sf.f2,image=sf.i2)
        sf.lbg2.place(x=0,y=0,relheight=1,relwidth=1)

        sf.ft2=Frame(sf.f2, width=1350, height=450 ,bd=12,relief="raise")
        sf.ft2.pack(side=TOP)

        sf.fb2=Frame(sf.f2, width=1350, height=250 ,bd=16,relief="raise")
        sf.fb2.pack(side=BOTTOM)

        sf.l=Label(sf.t,font=('arial',70,'bold'),text="\tYour Bill                " ,bd=10)
        sf.l.grid(row=0,column=0)

        sf.l1=Label(sf.ft2,font=('arial',12,'bold'),text="Receipt",bd=2)
        sf.l1.grid(row=0,column=0,sticky=W)
        sf.tx1=Text(sf.ft2,width=99,height=22,bg="white",bd=8,font=('arial',11,'bold'))
        sf.tx1.grid(row=1,column=0)
#------------------------
        
        def pay():
            messagebox.showinfo("","Thank You for your Purchase")
            sf.scr5.destroy()


        sf.cost=0
        sf.tax=0
        sf.tot=0
#----------------------------------
        sf.lsub=Label(sf.fb2,font=('arial',16,'bold'),text="Sub Total",bd=8)
        sf.lsub.grid(row=0,column=0)
        sf.txsub=Entry(sf.fb2,font=('arial',16,'bold'),bd=8,insertwidth=2,justify='left')
        sf.txsub.grid(row=0,column=1)

        sf.ltax=Label(sf.fb2,font=('arial',16,'bold'),text="Tax",bd=8)
        sf.ltax.grid(row=0,column=2)
        sf.txtax=Entry(sf.fb2,font=('arial',16,'bold'),bd=8,insertwidth=2,justify='left')
        sf.txtax.grid(row=0,column=3)

        sf.ltotal=Label(sf.fb2,font=('arial',16,'bold'),text="Total",bd=8)
        sf.ltotal.grid(row=0,column=4)
        sf.txtotal=Entry(sf.fb2,font=('arial',16,'bold'),bd=8,insertwidth=2,justify='left')
        sf.txtotal.grid(row=0,column=5)

        sf.bpay=Button(sf.fb2,padx=16,pady=1 ,bd=4,fg="black",font=('arial',16,'bold'),width=5,text="Pay",command=pay)
        sf.bpay.grid(row=0,column=6)

        sf.tx1.insert(END,'Items\t\t\t\t\t'+'Price\t\t\t'+'QTY\t\t'+'T.Price\n')
        for i,j in enumerate(sf.bill):
            sf.tx1.insert(END,sf.bill[i][0]+'\t\t\t\t\t'+str(sf.bill[i][1])+'\t\t\t'+str(sf.bill[i][2])+'\t\t'+str(sf.bill[i][3])+'\n')
            sf.cost+=sf.bill[i][3]

        sf.txsub.insert(END,str(sf.cost))
        sf.tax=(sf.cost*15)/100
        sf.txtax.insert(END,str(sf.tax))
        sf.tot=sf.cost+sf.tax
        sf.txtotal.insert(END,str(sf.tot))

        sf.txsub.config(state=DISABLED)
        sf.txtotal.config(state=DISABLED)
        sf.txtax.config(state=DISABLED)
        

        sf.scr5.mainloop()

        
#Bill Update
    def billup(sf,tupn,sqty,mqty,lqty):
        sf.scr4.destroy()
        sf.el=sf.pizzalist[tupn]
    
        for i in range(1,4):
            if(i==1):
                sf.size='(s)'
                sf.mul=sqty
    
            elif(i==2):
                sf.size='(m)'
                sf.mul=mqty
            
            elif(i==3):
                sf.size='(l)'
                sf.mul=lqty
            
            if(sf.mul==0):
                    pass
            else:    
                sf.ape=(sf.el[0]+sf.size,sf.el[i],sf.mul,(sf.el[i]*sf.mul))
                #global sf.bill
                sf.bill.append(sf.ape)
        print(sf.bill)
        sf.mainpage()


    
#For reopening the mainpage after order selection
    def remenu(sf):
        sf.scr4.destroy()
        sf.mainpage()

        
#This screen is used for taking orders        
    def ordermenu(sf,linx):
        sf.scr3.destroy()
        sf.scr4=Tk(className='Select Quantity')

        sf.u=IntVar()
        sf.v=IntVar()
        sf.w=IntVar()

        sf.var1=IntVar()
        sf.var1.set(0)
        sf.var2=IntVar()
        sf.var2.set(0)
        sf.var3=IntVar()
        sf.var3.set(0)


        sf.fo=Frame(sf.scr4)
        sf.fo.pack(fill=BOTH,expand=1,side=RIGHT)
        imgg=PhotoImage(file='images/3b73ef769b13e2846506698b150127dc.png')
        sf.l=Label(sf.fo,image=imgg,height=300)
        sf.l.place(x=0, y=0, relwidth=1, relheight=1)

        def butfun1():
            if sf.u.get()==2:
                sf.b11.config(state=ACTIVE)
                sf.b12.config(state=ACTIVE)
            else:
                sf.b11.config(state=DISABLED)
                sf.b12.config(state=DISABLED)
                sf.var1.set(0)
        
        def butfun2():        
            if sf.v.get()==4:
                sf.b21.config(state=ACTIVE)
                sf.b22.config(state=ACTIVE)
            else:
                sf.b21.config(state=DISABLED)
                sf.b22.config(state=DISABLED)
                sf.var2.set(0)
        
        def butfun3():        
            if sf.w.get()==6:
                sf.b31.config(state=ACTIVE)
                sf.b32.config(state=ACTIVE)
            else:
                sf.b31.config(state=DISABLED)
                sf.b32.config(state=DISABLED)    
                sf.var3.set(0)

        if(linx==0):
            sf.img1=PhotoImage(file='images/1.png')
            sf.pim=sf.img1
        elif linx==1:
            sf.img2=PhotoImage(file='images/2.png')
            sf.pim=sf.img2
        elif linx==2:
            sf.img3=PhotoImage(file='images/3.png')
            sf.pim=sf.img3
        elif linx==3:
            sf.img4=PhotoImage(file='images/4.png')
            sf.pim=sf.img4
        elif linx==4:
            sf.img5=PhotoImage(file='images/5.png')
            sf.pim=sf.img5
        elif linx==5:
            sf.img6=PhotoImage(file='images/6.png')
            sf.pim=sf.img6
        elif linx==6:
            sf.img7=PhotoImage(file='images/7.png')
            sf.pim=sf.img7
        elif linx==7:
            sf.img8=PhotoImage(file='images/8.png')
            sf.pim=sf.img8
        elif linx==8:
            sf.img9=PhotoImage(file='images/9.png')
            sf.pim=sf.img9
        elif linx==9:
            sf.img10=PhotoImage(file='images/10.png')
            sf.pim=sf.img10
        elif linx==10:
            sf.img11=PhotoImage(file='images/11.png')
            sf.pim=sf.img11
        elif linx==11:
            sf.img12=PhotoImage(file='images/12.png')
            sf.pim=sf.img12
        elif linx==12:
            sf.img13=PhotoImage(file='images/13.png')
            sf.pim=sf.img13
        elif linx==13:
            sf.img14=PhotoImage(file='images/14.png')
            sf.pim=sf.img14
        elif linx==14:
            sf.img15=PhotoImage(file='images/15.png')
            sf.pim=sf.img15
        elif linx==15:
            sf.img16=PhotoImage(file='images/16.png')
            sf.pim=sf.img16
        elif linx==16:
            img17=PhotoImage(file='images/17.png')
            sf.pim=sf.img17
        elif linx==17:
            sf.img18=PhotoImage(file='images/18.png')
            sf.pim=sf.img18
        elif linx==18:
            sf.img19=PhotoImage(file='images/19.png')
            sf.pim=sf.img19
        elif linx==19:
            sf.img20=PhotoImage(file='images/20.png')
            sf.pim=sf.img20
        elif linx==20:
            sf.img21=PhotoImage(file='images/21.png')
            sf.pim=sf.img21
        elif linx==21:
            sf.img22=PhotoImage(file='images/22.png')
            sf.pim=sf.img22
        elif linx==22:
            sf.img23=PhotoImage(file='images/23.png')
            sf.pim=sf.img23
        elif linx==23:
            sf.img24=PhotoImage(file='images/24.png')
            sf.pim=sf.img24
        
        sf.labe=Label(sf.fo,relief='sunken',image=sf.pim,bd=10)
        sf.labe.grid(column=4,rowspan=3,padx=5,pady=10)
        

        sf.c1=Checkbutton(sf.fo,onvalue=2,offvalue=5,variable=sf.u,text='small',command=butfun1)
        sf.c1.grid(row=0,column=0,padx=20,pady=10)
        sf.c2=Checkbutton(sf.fo,onvalue=4,offvalue=6,variable=sf.v,text='medium',command=butfun2)
        sf.c2.grid(row=1,column=0,padx=20,pady=10)
        sf.c3=Checkbutton(sf.fo,onvalue=6,offvalue=7,variable=sf.w,text='large',command=butfun3)
        sf.c3.grid(row=2,column=0,padx=20,pady=10)

        


        sf.b11=Button(sf.fo,text='-',overrelief='sunken',command=lambda:sf.var1.set(sf.var1.get()-1) if sf.var1.get()>0 else sf.var1.set(0),state=DISABLED)
        sf.b11.grid(row=0,column=1,padx=20,pady=10)
        sf.b21=Button(sf.fo,text='-',overrelief='sunken',command=lambda:sf.var2.set(sf.var2.get()-1) if sf.var2.get()>0 else sf.var2.set(0),state=DISABLED)
        sf.b21.grid(row=1,column=1,padx=20,pady=10)
        sf.b31=Button(sf.fo,text='-',overrelief='sunken',command=lambda:sf.var3.set(sf.var3.get()-1) if sf.var3.get()>0 else sf.var3.set(0),state=DISABLED)
        sf.b31.grid(row=2,column=1,padx=20,pady=10)


        sf.l1 =Label( sf.fo, textvariable=sf.var1, relief=RAISED )
        sf.l1.grid(row=0,column=2,padx=20,pady=10)

        sf.l2 =Label( sf.fo, textvariable=sf.var2, relief=RAISED )
        sf.l2.grid(row=1,column=2,padx=20,pady=10)

        sf.l3 =Label( sf.fo, textvariable=sf.var3, relief=RAISED )
        sf.l3.grid(row=2,column=2,padx=20,pady=10)

        sf.b12=Button(sf.fo,text='+',overrelief='sunken',command=lambda:sf.var1.set(sf.var1.get()+1),state=DISABLED)
        sf.b12.grid(row=0,column=3,padx=20,pady=10)
        sf.b22=Button(sf.fo,text='+',overrelief='sunken',command=lambda:sf.var2.set(sf.var2.get()+1),state=DISABLED)
        sf.b22.grid(row=1,column=3,padx=20,pady=10)
        sf.b32=Button(sf.fo,text='+',overrelief='sunken',command=lambda:sf.var3.set(sf.var3.get()+1),state=DISABLED)
        sf.b32.grid(row=2,column=3,padx=20,pady=10)

        sf.subbut=Button(sf.fo,text='Submit',bg='black',fg='red',overrelief='sunken',font=('times',20),command=lambda:sf.billup(linx,sf.var1.get(),sf.var2.get(),sf.var3.get()))
        sf.subbut.grid(row=3 ,column= 0,padx=20,pady=10)
        sf.canbut=Button(sf.fo,text='Cancel',bg='black',fg='red',overrelief='sunken',font=('times',20),command=sf.remenu)
        sf.canbut.grid(row=3 ,column= 1,columnspan=2,padx=20,pady=10)

        
        
        sf.scr4.mainloop()


#mainpage of the interface        
    def mainpage(sf):
        
        sf.scr3=Tk()
        sf.scr3.geometry('1700x1800+0+0')


        #veg
        def fun1():
            sf.b1.config(bg='black',fg='red')
            sf.b2.config(bg='white',fg='black')
            sf.b3.config(bg='white',fg='black')
            sf.b4.config(bg='white',fg='black')
    
            sf.ll2.destroy()
            sf.ll3.destroy()
            sf.ll4.destroy()

            sf.img1=PhotoImage(file='images/1.png')
            sf.img2=PhotoImage(file='images/2.png')
            sf.img3=PhotoImage(file='images/3.png')
            sf.img4=PhotoImage(file='images/4.png')
            sf.img5=PhotoImage(file='images/5.png')
            sf.img6=PhotoImage(file='images/6.png')

            
            sf.ll1=Listbox(sf.f,bg='black')
            sf.ll1.grid(row=2,column=0,columnspan=4,padx=10,pady=20)
            

            sf.c1=Button(sf.ll1,image=sf.img1,overrelief='sunken',command=lambda:sf.ordermenu(0))
            sf.c1.grid(row=0,column=0,padx=20,pady=10)
            sf.c1.image=sf.img1
            sf.c2=Button(sf.ll1,image=sf.img2,overrelief='sunken',command=lambda:sf.ordermenu(1))
            sf.c2.grid(row=1,column=0,padx=20,pady=10)
            sf.c2.image=sf.img2
            sf.c3=Button(sf.ll1,image=sf.img3,overrelief='sunken',command=lambda:sf.ordermenu(2))
            sf.c3.grid(row=0,column=1,padx=20,pady=10)
            sf.c3.image=sf.img3
            sf.c4=Button(sf.ll1,image=sf.img4,overrelief='sunken',command=lambda:sf.ordermenu(3))
            sf.c4.grid(row=1,column=1,padx=20,pady=10)
            sf.c4.image=sf.img4
            sf.c5=Button(sf.ll1,image=sf.img5,overrelief='sunken',command=lambda:sf.ordermenu(4))
            sf.c5.grid(row=0,column=2,padx=20,pady=10)
            sf.c5.image=sf.img5
            sf.c6=Button(sf.ll1,image=sf.img6,overrelief='sunken',command=lambda:sf.ordermenu(5))
            sf.c6.grid(row=1,column=2,padx=20,pady=10)
            sf.c6.image=sf.img6

    
        #nonveg
        def fun2():
            sf.b1.config(bg='white',fg='black')
            sf.b2.config(bg='black',fg='red')
            sf.b3.config(bg='white',fg='black')
            sf.b4.config(bg='white',fg='black')
    
            sf.ll1.destroy()
            sf.ll3.destroy()
            sf.ll4.destroy()
        
            sf.img7=PhotoImage(file='images/7.png')
            sf.img8=PhotoImage(file='images/8.png')
            sf.img9=PhotoImage(file='images/9.png')
            sf.img10=PhotoImage(file='images/10.png')
            sf.img11=PhotoImage(file='images/11.png')
            sf.img12=PhotoImage(file='images/12.png')
            
            sf.ll2=Listbox(sf.f,bg='black')
            sf.ll2.grid(row=2,column=0,columnspan=4,padx=10,pady=20)

            sf.c7=Button(sf.ll2,image=sf.img7,overrelief='sunken',command=lambda:sf.ordermenu(6))
            sf.c7.grid(row=0,column=0,padx=20,pady=10)
            sf.c7.image=sf.img7
            sf.c8=Button(sf.ll2,image=sf.img8,overrelief='sunken',command=lambda:sf.ordermenu(7))
            sf.c8.grid(row=1,column=0,padx=20,pady=10)
            sf.c8.image=sf.img8
            sf.c9=Button(sf.ll2,image=sf.img9,overrelief='sunken',command=lambda:sf.ordermenu(8))
            sf.c9.grid(row=0,column=1,padx=20,pady=10)
            sf.c9.image=sf.img9
            sf.c10=Button(sf.ll2,image=sf.img10,overrelief='sunken',command=lambda:sf.ordermenu(9))
            sf.c10.grid(row=1,column=1,padx=20,pady=10)
            sf.c10.image=sf.img10
            sf.c11=Button(sf.ll2,image=sf.img11,overrelief='sunken',command=lambda:sf.ordermenu(10))
            sf.c11.grid(row=0,column=2,padx=20,pady=10)
            sf.c11.image=sf.img11
            sf.c12=Button(sf.ll2,image=sf.img12,overrelief='sunken',command=lambda:sf.ordermenu(11))
            sf.c12.grid(row=1,column=2,padx=20,pady=10)
            sf.c12.image=sf.img12


        #breads
        def fun3():
            sf.b1.config(bg='white',fg='black')
            sf.b2.config(bg='white',fg='black')
            sf.b3.config(bg='black',fg='red')
            sf.b4.config(bg='white',fg='black')
    
            sf.ll2.destroy()
            sf.ll1.destroy()
            sf.ll4.destroy()
        
            sf.img13=PhotoImage(file='images/13.png')
            sf.img14=PhotoImage(file='images/14.png')
            sf.img15=PhotoImage(file='images/15.png')
            sf.img16=PhotoImage(file='images/16.png')
            sf.img17=PhotoImage(file='images/17.png')
            sf.img18=PhotoImage(file='images/18.png')
            
            sf.ll3=Listbox(sf.f,bg='black')
            sf.ll3.grid(row=2,column=0,columnspan=4,padx=10,pady=20)

            sf.c13=Button(sf.ll3,image=sf.img13,overrelief='sunken',command=lambda:sf.ordermenu(12))
            sf.c13.grid(row=0,column=0,padx=20,pady=10)
            sf.c13.image=sf.img13
            sf.c14=Button(sf.ll3,image=sf.img14,overrelief='sunken',command=lambda:sf.ordermenu(13))
            sf.c14.grid(row=1,column=0,padx=20,pady=10)
            sf.c14.image=sf.img14
            sf.c15=Button(sf.ll3,image=sf.img15,overrelief='sunken',command=lambda:sf.ordermenu(14))
            sf.c15.grid(row=0,column=1,padx=20,pady=10)
            sf.c15.image=sf.img15
            sf.c16=Button(sf.ll3,image=sf.img16,overrelief='sunken',command=lambda:sf.ordermenu(15))
            sf.c16.grid(row=1,column=1,padx=20,pady=10)
            sf.c16.image=sf.img16
            sf.c17=Button(sf.ll3,image=sf.img17,overrelief='sunken',command=lambda:sf.ordermenu(16))
            sf.c17.grid(row=0,column=2,padx=20,pady=10)
            sf.c17.image=sf.img17
            sf.c18=Button(sf.ll3,image=sf.img18,overrelief='sunken',command=lambda:sf.ordermenu(17))
            sf.c18.grid(row=1,column=2,padx=20,pady=10)
            sf.c18.image=sf.img18


        #drinks
        def fun4():
            sf.b1.config(bg='white',fg='black')
            sf.b2.config(bg='white',fg='black')
            sf.b3.config(bg='white',fg='black')
            sf.b4.config(bg='black',fg='red')
            sf.ll2.destroy()
            sf.ll3.destroy()
            sf.ll1.destroy()
        
            sf.ll4=Listbox(sf.f,bg='black')
            sf.ll4.grid(row=2,column=0,columnspan=4,padx=10,pady=20)

            sf.img19=PhotoImage(file='images/19.png')
            sf.img20=PhotoImage(file='images/20.png')
            sf.img21=PhotoImage(file='images/21.png')
            sf.img22=PhotoImage(file='images/22.png')
            sf.img23=PhotoImage(file='images/23.png')
            sf.img24=PhotoImage(file='images/24.png')
    
            sf.c19=Button(sf.ll4,image=sf.img19,overrelief='sunken',command=lambda:sf.ordermenu(18))
            sf.c19.grid(row=0,column=0,padx=20,pady=10)
            sf.c19.image=sf.img19
            sf.c20=Button(sf.ll4,image=sf.img20,overrelief='sunken',command=lambda:sf.ordermenu(19))
            sf.c20.grid(row=1,column=0,padx=20,pady=10)
            sf.c20.image=sf.img20
            sf.c21=Button(sf.ll4,image=sf.img21,overrelief='sunken',command=lambda:sf.ordermenu(20))
            sf.c21.grid(row=0,column=1,padx=20,pady=10)
            sf.c21.image=sf.img21
            sf.c22=Button(sf.ll4,image=sf.img22,overrelief='sunken',command=lambda:sf.ordermenu(21))
            sf.c22.grid(row=1,column=1,padx=20,pady=10)
            sf.c22.image=sf.img22
            sf.c23=Button(sf.ll4,image=sf.img23,overrelief='sunken',command=lambda:sf.ordermenu(22))
            sf.c23.grid(row=0,column=2,padx=20,pady=10)
            sf.c23.image=sf.img23
            sf.c24=Button(sf.ll4,image=sf.img24,overrelief='sunken',command=lambda:sf.ordermenu(23))
            sf.c24.grid(row=1,column=2,padx=20,pady=10)
            sf.c24.image=sf.img24


       
        #Frame of login buttons
        sf.f=Frame(sf.scr3,bg="blue")
        sf.f.pack_propagate(0)
        sf.f.pack(fill=BOTH,expand=1,side=RIGHT)
        imgs=PhotoImage(file='images/3b73ef769b13e2846506698b150127dc.png')
        sf.la2=Label(sf.f,image=imgs,height=300)
        sf.la2.place(x=0, y=0, relwidth=1, relheight=1)

        img=PhotoImage(file='images/Webp.net-gifmaker.gif')
        i=PhotoImage(file='images/Pizza-forever-slider-logo.png')
        sf.b=Button(sf.f,text='p1',image=i,height=60,width=800)
        sf.b.grid(row=0,columnspan=4,column=0,pady=20)

        sf.b1=Button(sf.f,text='Veg Pizza',height=2,width=40,command=fun1,bd=2,bg='black',fg='red',overrelief='sunken')
        sf.b1.grid(row=1,column=0)
        sf.b2=Button(sf.f,text='Non Veg',height=2,width=40,command=fun2,bd=2,bg='white',fg='black',overrelief='sunken')
        sf.b2.grid(row=1,column=1)
        sf.b3=Button(sf.f,text='Sides',height=2,width=40,command=fun3,bd=2,bg='white',fg='black',overrelief='sunken')
        sf.b3.grid(row=1,column=2)
        sf.b4=Button(sf.f,text='Drinks',height=2,width=40,command=fun4,bd=2,bg='white',fg='black',overrelief='sunken')
        sf.b4.grid(row=1,column=3)

        
        sf.ll1=Listbox(sf.f,bg='black')
        sf.ll1.grid(row=2,column=0,columnspan=4,padx=10,pady=20)
        img1=PhotoImage(file='images/1.png')
        img2=PhotoImage(file='images/2.png')
        img3=PhotoImage(file='images/3.png')
        img4=PhotoImage(file='images/4.png')
        img5=PhotoImage(file='images/5.png')
        img6=PhotoImage(file='images/6.png')

        sf.c1=Button(sf.ll1,image=img1,overrelief='sunken',command=lambda:sf.ordermenu(0))
        sf.c1.grid(row=0,column=0,padx=20,pady=10)
        sf.c1.image=img1
        sf.c2=Button(sf.ll1,image=img2,overrelief='sunken',command=lambda:sf.ordermenu(1))
        sf.c2.grid(row=1,column=0,padx=20,pady=10)
        sf.c2.image=img2
        sf.c3=Button(sf.ll1,image=img3,overrelief='sunken',command=lambda:sf.ordermenu(2))
        sf.c3.grid(row=0,column=1,padx=20,pady=10)
        sf.c3.image=img3
        sf.c4=Button(sf.ll1,image=img4,overrelief='sunken',command=lambda:sf.ordermenu(3))
        sf.c4.grid(row=1,column=1,padx=20,pady=10)
        sf.c4.image=img4
        sf.c5=Button(sf.ll1,image=img5,overrelief='sunken',command=lambda:sf.ordermenu(4))
        sf.c5.grid(row=0,column=2,padx=20,pady=10)
        sf.c5.image=img5
        sf.c6=Button(sf.ll1,image=img6,overrelief='sunken',command=lambda:sf.ordermenu(5))
        sf.c6.grid(row=1,column=2,padx=20,pady=10)
        sf.c6.image=img6

            
        sf.ll2=Listbox(sf.f,bg='black')
        sf.ll3=Listbox(sf.f,bg='black')
        sf.ll4=Listbox(sf.f,bg='black')

        sf.donbut=Button(sf.f,text='Bill Up',overrelief='sunken',relief='raised',font=('times',20,'bold'),bg='red',fg='white',command=sf.finalbill)
        sf.donbut.grid(row=2,column=5)
        sf.scr3.mainloop()

        
        
    def result(sf,val):
        if val=="login":
            try:
                sf.username=sf.user.get()
                sf.passd=sf.passw.get()
                sf.scr.destroy()
                x=sf.cur.execute("select count(*) from staff where user=%r and passw=%r"%(sf.username,sf.passd))
                if list(x)[0][0]==0:
                    sf.__init__()
                else:
                    sf.mainpage()
            except:
                pass
        elif val=='register':
            if sf.passw.get()==sf.passw1.get():
                x=sf.cur.execute("select count(*) from staff where user=%r"%(sf.user.get()))
                if list(x)[0][0]!=0 or len(sf.user.get())==0:
                    messagebox.showinfo("pizza","username allready exists or field is empty")
                    sf.register()
                else:
                    sf.cur.execute("insert into staff values(%r,%r)"%(sf.user.get(),sf.passw.get()))
                    sf.c.commit()
                try:
                    sf.scr1.destroy()
                except:
                    pass
                sf.__init__()
            else:
                try:
                    sf.scr1.destroy()
                except:
                    pass
                sf.register()

s=Login()
