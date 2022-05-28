# ------------------------------Add Student definition----------------------# 
def addstudent():
    def submitadd():

        # Getting the values into variables
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        mentor = mentorval.get()
        addeddate = date.today().strftime("%d/%m/%Y")
        addedtime = datetime.now().strftime("%I:%M:%S")

        try:
            # strr is the query  that is executed by execute method 
            strr = 'insert into studentdata values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            # The parameters found in strr are bound to the variables in the query
            mycursor.execute(strr,(id,name,mobile,email,address,gender,dob,addeddate,addedtime))
            con.commit()
            res = messagebox.askyesnocancel('Notification',' Student Id: {} Name: {} details added successfully... and want to clean the form'.format(id,name),parent=addroot)
            if(res==True):
                idval.set('')
                nameval.set('')
                mobileval.set('')
                emailval.set('')
                addressval.set('')
                genderval.set('')
                dobval.set('')
                mentorval.set('')    

        except:  # If same id exists
            messagebox.showerror('Notification','Student with Id: {} Already exist!!!'.format(id),parent=addroot)
        
        strr = 'select id,name,mobile_no,email,address,gender,dob,sslc,puc,pucboard,college,Mentorid,Mname,Mph_no,date,time from studentdata left join Academicdetails on studentdata.id = Academicdetails.accid left join mentorstable on studentdata.id = mentorstable.studid'
        mycursor.execute(strr) 
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15]]
            studenttable.insert('', END, values=vv)

 #----------------------------------Addroot Frame------------------------        
    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('470x510+130+100')
    addroot.title('Add Student details')
    addroot.iconbitmap("book.ico")
    addroot.config(bg='gray34')
    addroot.resizable(False,False)

    #-----------------------Add Root Frame Labels-----------------------#

    idlabel = Label(addroot,text='Enter ID:*',bg='cyan2',font="comicsans 19 bold",relief=GROOVE,borderwidth=3,width=13,anchor='w')
    idlabel.place(x=10,y=10)
    
    namelabel = Label(addroot,text='Enter Name:*',bg='cyan2',font="comicsans 19 bold",relief=GROOVE,borderwidth=3,width=13,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel = Label(addroot,text='Enter Mobile:*',bg='cyan2',font="comicsans 19 bold",relief=GROOVE,borderwidth=3,width=13,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel = Label(addroot,text='Enter Email:',bg='cyan2',font="comicsans 19 bold",relief=GROOVE,borderwidth=3,width=13,anchor='w')
    emaillabel.place(x=10,y=190)
    
    addresslabel = Label(addroot,text='Enter Address:',bg='cyan2',font="comicsans 19 bold",relief=GROOVE,borderwidth=3,width=13,anchor='w')
    addresslabel.place(x=10,y=250)

    genderlabel = Label(addroot,text='Enter Gender:',bg='cyan2',font="comicsans 19 bold",relief=GROOVE,borderwidth=3,width=13,anchor='w')
    genderlabel.place(x=10,y=310)

    doblabel = Label(addroot,text='Enter D.O.B:'+'\n'+'(dd/mm/yyyy)',bg='cyan2',font="comicsans 19 bold",relief=GROOVE,borderwidth=3,width=13,anchor='w')
    doblabel.place(x=10,y=370)

    ##-----------------------Entery boxes for Add root frame Labels-----------------------## 
    
    options = ["Male","Female","Other"] 
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    mentorval = StringVar()
    dobval = StringVar()
    
    identry = Entry(addroot,font="comicsans 19 bold",width=14,borderwidth=5,textvariable=idval)
    identry.place(x=250,y=10)
    
    nameentry = Entry(addroot,font="comicsans 19 bold",width=14,borderwidth=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileentry = Entry(addroot,font="comicsans 19 bold",width=14,borderwidth=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    emailentry = Entry(addroot,font="comicsans 19 bold",width=14,borderwidth=5,textvariable=emailval)
    emailentry.place(x=250,y=190)

    addressentry = Entry(addroot,font="comicsans 19 bold",width=14,borderwidth=5,textvariable=addressval)
    addressentry.place(x=250,y=250)

    # genderentry = Entry(addroot,font="comicsans 19 bold",width=14,borderwidth=5,textvariable=genderval)
    genderdrop = OptionMenu(addroot , genderval , *options)
    genderdrop.config(width=14,font=('comicsans', 15),borderwidth=5)
    genderdrop.place(x=250,y=310)

    dobentry = Entry(addroot,font="comicsans 19 bold",width=14,borderwidth=5,textvariable=dobval)
    dobentry.place(x=250,y=370,height=70)

    ##-----------------------ADD button for the add root Frame-----------------------##

    submitbtn = Button(addroot,text='Submit',font="comicsans 15 bold",width=20,borderwidth=5,activebackground='cyan4',activeforeground='white',bg='cyan2',command=submitadd)
    submitbtn.place(x=105,y=450)


    addroot.mainloop()
#####################################################################################
# ------------------------------Academicdetails definition----------------------# 
def Academicdetails():
    def submit():
        id = idval.get()
        name = nameval.get()
        sslc = sslcval.get()
        puc = pucval.get()
        pucboard = selectval.get()
        college = collegeval.get()

        try:
            strr = 'insert into Academicdetails values(%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(id,name,sslc,puc,pucboard,college))
            con.commit()
            messagebox.showinfo('Notification','The Academic Details of {} with id {} was added successfully...'.format(name,id),parent=accroot)
            accroot.destroy()
        except:
            messagebox.showerror('Error','The Academic Details of {} with id {} is already exist'.format(name,id),parent=accroot)
        
        strr = 'select id,name,mobile_no,email,address,gender,dob,sslc,puc,pucboard,college,Mentorid,Mname,Mph_no,date,time from studentdata left join Academicdetails on studentdata.id = Academicdetails.accid left join mentorstable on studentdata.id = mentorstable.studid'
        mycursor.execute(strr) 
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15]]
            studenttable.insert('', END, values=vv)

    accroot = Toplevel(master=DataEntryFrame)
    accroot.grab_set()
    accroot.geometry('470x450+130+100')
    accroot.title('Academic Details')
    accroot.config(bg='gray34')
    accroot.iconbitmap('book.ico')
    accroot.resizable(False,False)
    
    idlabel = Label(accroot,text='Student ID:',bg='cyan2',font="comicsans 20 bold",relief=GROOVE,borderwidth=3,width=13,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(accroot,text='Student Name:',bg='cyan2',font="comicsans 20 bold",relief=GROOVE,borderwidth=3,width=13,anchor='w')
    namelabel.place(x=10,y=70)
    
    tenthlabel = Label(accroot,text='SSLC %:*',bg='cyan2',font="comicsans 20 bold",relief=GROOVE,borderwidth=3,width=13,anchor='w')
    tenthlabel.place(x=10,y=130)

    twellabel = Label(accroot,text='PUC %:*',bg='cyan2',font="comicsans 20 bold",relief=GROOVE,borderwidth=3,width=13,anchor='w')
    twellabel.place(x=10,y=190)

    boardlabel = Label(accroot,text='PUC Board :*',bg='cyan2',font="comicsans 20 bold",relief=GROOVE,borderwidth=3,width=13,anchor='w')
    boardlabel.place(x=10,y=250)
    
    colllabel = Label(accroot,text='College Name:*',bg='cyan2',font="comicsans 20 bold",relief=GROOVE,borderwidth=3,width=13,anchor='w')
    colllabel.place(x=10,y=310)


    idval = StringVar()
    nameval = StringVar()
    sslcval = StringVar()
    pucval = StringVar()
    pucboardval = StringVar()
    collegeval = StringVar()
    selectval = StringVar()
    options = ["State Board","CBSE Board"]

    identry = Entry(accroot,font="comicsans 15 bold",borderwidth=5,textvariable=idval,width =18,state=DISABLED)
    identry.place(x=250,y=10)

    nameentry = Entry(accroot,font="comicsans 15 bold",borderwidth=5,textvariable=nameval,width =18,state=DISABLED)
    nameentry.place(x=250,y=70)
    
    sslcentry = Entry(accroot,font="comicsans 15 bold",borderwidth=5,textvariable=sslcval,width =18)
    sslcentry.place(x=250,y=130)

    pucentry = Entry(accroot,font="comicsans 15 bold",borderwidth=5,textvariable=pucval,width =18)
    pucentry.place(x=250,y=190)

    # pucboardentry = Entry(accroot,font=('roman',15,'bold'),borderwidth=5,textvariable=pucboardval)
    # pucboardentry.place(x=250,y=250)
    selectdrop = OptionMenu(accroot , selectval , *options)
    selectdrop.config(width=15,font="comicsans 15 bold",borderwidth=5)
    selectdrop.place(x=250,y=250)

    collegeentry = Entry(accroot,font="comicsans 15 bold",borderwidth=5,textvariable=collegeval,width =18)
    collegeentry.place(x=250,y=310)


    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values']
    if(len(pp) != 0):
        idval.set(pp[0])
        nameval.set(pp[1])

    if(cc!=''):
        submitbtn = Button(accroot,text='Submit',font="comicsans 15 bold",width=20,borderwidth=5,activebackground='cyan4',activeforeground='white',bg='cyan2',command=submit)
        submitbtn.place(x=150,y=370)
    else:
        messagebox.showerror('Notification','You have not selected any student,Please select a student!!!')
        accroot.destroy()


    accroot.mainloop()
#####################################################################################
# ------------------------------Mentorsdetails definition----------------------# 
def mentorsdetails():
    def submit():
        studid = studidval.get()
        mid = midval.get()
        mname = mnameval.get()
        mph_no = mph_noval.get() 

        try:
            strr = 'insert into mentorstable values(%s,%s,%s,%s)'
            mycursor.execute(strr,(studid,mid,mname,mph_no))
            con.commit()
            messagebox.showinfo('Notification','The Mentors Details of student id {} is added successfully...'.format(studid),parent=menroot)
            menroot.destroy()
        except:
            messagebox.showerror('Error','The Mentors Details of student id {}   already exist '.format(studid,mname,mid),parent=menroot)
        
        strr = 'select id,name,mobile_no,email,address,gender,dob,sslc,puc,pucboard,college,mentorid,Mname,Mph_no,date,time from studentdata left join Academicdetails on studentdata.id = Academicdetails.accid left join mentorstable on studentdata.id = mentorstable.studid'
        mycursor.execute(strr) 
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15]]
            studenttable.insert('', END, values=vv)

    menroot = Toplevel(master=DataEntryFrame)
    menroot.grab_set()
    menroot.geometry('470x300+130+100')
    menroot.title('Mentors Details')
    menroot.config(bg='gray34')
    menroot.iconbitmap('book.ico')
    menroot.resizable(False,False)
    
    studidlabel = Label(menroot,text='Student ID:',bg='cyan2',font="comicsans 20 bold",relief=GROOVE,borderwidth=3,width=13,anchor='w')
    studidlabel.place(x=10,y=10)

    menidlabel = Label(menroot,text='Mentor ID:*',bg='cyan2',font="comicsans 20 bold",relief=GROOVE,borderwidth=3,width=13,anchor='w')
    menidlabel.place(x=10,y=70)

    namelabel = Label(menroot,text='Mentor Name:*',bg='cyan2',font="comicsans 20 bold",relief=GROOVE,borderwidth=3,width=13,anchor='w')
    namelabel.place(x=10,y=130)
    
    phnolabel = Label(menroot,text='Contact No.:*',bg='cyan2',font="comicsans 20 bold",relief=GROOVE,borderwidth=3,width=13,anchor='w')
    phnolabel.place(x=10,y=190)

    studidval = StringVar()
    midval = StringVar()
    mnameval = StringVar()
    mph_noval = StringVar()
    
    studidentry = Entry(menroot,font="comicsans 15 bold",borderwidth=5,textvariable=studidval,width =18,state=DISABLED)
    studidentry.place(x=250,y=10)

    menidentry = Entry(menroot,font="comicsans 15 bold",borderwidth=5,textvariable=midval,width =18)
    menidentry.place(x=250,y=70)

    nameentry = Entry(menroot,font="comicsans 15 bold",borderwidth=5,textvariable=mnameval,width =18)
    nameentry.place(x=250,y=130)
    
    phnoentry = Entry(menroot,font="comicsans 15 bold",borderwidth=5,textvariable=mph_noval,width =18)
    phnoentry.place(x=250,y=190)


    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values']
    if(len(pp) != 0):
        studidval.set(pp[0])

    if(cc!=''):
        submitbtn = Button(menroot,text='Submit',font="comicsans 15 bold",width=20,borderwidth=5,activebackground='cyan4',activeforeground='white',bg='cyan2',command=submit)
        submitbtn.place(x=150,y=250)
    else:
        messagebox.showerror('Notification','You have not selected any student,Please select a student from the Student Table!!!')
        menroot.destroy()

    menroot.mainloop()
####################################################################################
# ------------------------------Search Student definition----------------------# 
def searchstudent():
    def search():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        date = dateval.get()
        
        if(id != ''):
            strr = 'select id from studentdata where id = %s'
            mycursor.execute(strr,(id,))
            datas = mycursor.fetchall() 
            if(datas):
                strr = 'select id,name,mobile_no,email,address,gender,dob,sslc,puc,pucboard,college,Mentorid,Mname,Mph_no,date,time from studentdata left join academicdetails on studentdata.id = academicdetails.accid left join mentorstable on studentdata.id = mentorstable.studid where studentdata.id = %s'
                #if the database app is mysql place ',' after the value Ex:id,
                mycursor.execute(strr,(id,))
                datas = mycursor.fetchall() # Stores all the data where mycursor is currently pointing in the form of tuple 
                studenttable.delete(*studenttable.get_children())# Deleting in-order to remove the previous entry on show frame
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15]]
                    studenttable.insert('', END, values=vv)# Displays the data
                idval.set('')
            else:
                messagebox.showerror('Notification',"Data you are searched doesn't exist")
        elif(name != ''):
            strr = 'select id from studentdata where name = %s'
            mycursor.execute(strr,(name,))
            datas = mycursor.fetchall() 
            if(datas):
                strr = "select id,name,mobile_no,email,address,gender,dob,sslc,puc,pucboard,college,Mentorid,Mname,Mph_no,date,time from studentdata left join academicdetails on studentdata.id = academicdetails.accid left join mentorstable on studentdata.id = mentorstable.studid where studentdata.name = %s"
                mycursor.execute(strr,(name,)) 
                datas = mycursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15]]
                    studenttable.insert('', END, values=vv)
                nameval.set('')
            else:
                messagebox.showerror('Notification',"Data you are searched doesn't exist")

        elif(mobile != ''):
            strr = 'select id from studentdata where mobile_no = %s'
            mycursor.execute(strr,(mobile,))
            datas = mycursor.fetchall() 
            if(datas):
                strr = "select id,name,mobile_no,email,address,gender,dob,sslc,puc,pucboard,college,Mentorid,Mname,Mph_no,date,time from studentdata left join academicdetails on studentdata.id = academicdetails.accid left join mentorstable on studentdata.id = mentorstable.studid where studentdata.mobile_no= %s"
                mycursor.execute(strr,(mobile,))
                datas = mycursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15]]
                    studenttable.insert('', END, values=vv)
                mobileval.set('')
            else:
                messagebox.showerror('Notification',"Data you are searched doesn't exist")

        elif(email != ''):
            strr = 'select id from studentdata where email = %s'
            mycursor.execute(strr,(email,))
            datas = mycursor.fetchall() 
            if(datas):
                strr = "select id,name,mobile_no,email,address,gender,dob,sslc,puc,pucboard,college,Mentorid,Mname,Mph_no,date,time from studentdata left join academicdetails on studentdata.id = academicdetails.accid left join mentorstable on studentdata.id = mentorstable.studid where studentdata.email = %s"
                mycursor.execute(strr,(email,))
                datas = mycursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15]]
                    studenttable.insert('', END, values=vv)
                emailval.set('')
            else:
                messagebox.showerror('Notification',"Data you are searched doesn't exist")
            
        elif(address != ''):
            strr = 'select id from studentdata where address = %s'
            mycursor.execute(strr,(address,))
            datas = mycursor.fetchall() 
            if(datas):
                strr = "select id,name,mobile_no,email,address,gender,dob,sslc,puc,pucboard,college,Mentorid,Mname,Mph_no,date,time from studentdata left join academicdetails on studentdata.id = academicdetails.accid left join mentorstable on studentdata.id = mentorstable.studid where studentdata.address=%s"
                mycursor.execute(strr,(address,))
                datas = mycursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15]]
                    studenttable.insert('', END, values=vv)
                addressval.set('')
            else:
                messagebox.showerror('Notification',"Data you are searched doesn't exist")
                
            
        elif(gender != ''):
            strr = 'select id from studentdata where gender = %s'
            mycursor.execute(strr,(gender,))
            datas = mycursor.fetchall() 
            if(datas):
                strr = "select id,name,mobile_no,email,address,gender,dob,sslc,puc,pucboard,college,Mentorid,Mname,Mph_no,date,time from studentdata left join academicdetails on studentdata.id = academicdetails.accid left join mentorstable on studentdata.id = mentorstable.studid where studentdata.gender=%s"
                mycursor.execute(strr,(gender,))
                datas = mycursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15]]
                    studenttable.insert('', END, values=vv)
                genderval.set('')
            else:
                messagebox.showerror('Notification',"Data you are searched doesn't exist")
                
        elif(dob != ''):
            strr = 'select id from studentdata where dob = %s'
            mycursor.execute(strr,(dob,))
            datas = mycursor.fetchall() 
            if(datas):
                strr = "select id,name,mobile_no,email,address,gender,dob,sslc,puc,pucboard,college,Mentorid,Mname,Mph_no,date,time from studentdata left join academicdetails on studentdata.id = academicdetails.accid left join mentorstable on studentdata.id = mentorstable.studid where studentdata.dob=%s"
                mycursor.execute(strr,(dob,))
                datas = mycursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15]]
                    studenttable.insert('', END, values=vv)
                dobval.set('')
            else:
                messagebox.showerror('Notification',"Data you are searched doesn't exist")
                
        elif(date != ''):
            strr = 'select id from studentdata where date = %s'
            mycursor.execute(strr,(date,))
            datas = mycursor.fetchall() 
            if(datas):
                strr = "select id,name,mobile_no,email,address,gender,dob,sslc,puc,pucboard,college,Mentorid,Mname,Mph_no,date,time from studentdata left join academicdetails on studentdata.id = academicdetails.accid left join mentorstable on studentdata.id = mentorstable.studid where studentdata.date=%s"
                mycursor.execute(strr,(date,))
                datas = mycursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15]]
                    studenttable.insert('', END, values=vv)
                dateval.set('')
            else:
                messagebox.showerror('Notification',"Data you are searched doesn't exist")

        else:
            messagebox.showerror('Notification',"Data you are searched doesn't exist")

    ##-----------------------Search root Frame-----------------------##

    searchroot = Toplevel(master = DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('470x300+10+100')
    searchroot.title('Search')
    searchroot.config(bg='gray34')
    searchroot.iconbitmap('book.ico')
    searchroot.resizable(False,False)

    ##-----------------------Labels for Seacrh root Frame-----------------------##
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    selectval = StringVar()

    options = ["ID","Name","Mobile No","Email","Address","Gender","D.O.B","Added Date"]

    def showentrybox(): 

        iselectval = StringVar()
        selectoption = selectval.get()

        if(selectoption == "ID"):
            for widget in searchroot.winfo_children():
                widget.destroy()
            idlabel = Label(searchroot,text='Search By:',bg='cyan2',font="comicsans 19 bold",relief=GROOVE,borderwidth=3,width=13,anchor='w')
            idlabel.place(x=10,y=10)

            selectdrop = OptionMenu(searchroot , selectval , *options)
            selectdrop.config(width=14,font=('comicsans', 15),borderwidth=5)
            selectdrop.place(x=250,y=10)


            selectbtn = Button(searchroot,text='Select',font="comicsans 15 bold",width=20,borderwidth=5,activebackground='cyan4',activeforeground='white',bg='cyan2',command=showentrybox)
            selectbtn.place(x=110,y=70)

            idlabel = Label(searchroot,text='Enter Id:',bg='cyan2',font="comicsans 19 bold",relief=GROOVE,borderwidth=3,width=13,anchor='w')
            idlabel.place(x=10,y=130)
            identry = Entry(searchroot,font="comicsans 15 bold",width=18,borderwidth=5,textvariable=idval)
            identry.place(x=250,y=130)
            submitbtn = Button(searchroot,text='Search',font="comicsans 15 bold",width=20,borderwidth=5,activebackground='cyan4',activeforeground='white',bg='cyan2',command=search)
            submitbtn.place(x=110,y=190)

        elif(selectoption == "Name"):
            for widget in searchroot.winfo_children():
                widget.destroy()
            idlabel = Label(searchroot,text='Search By:',bg='cyan2',font="comicsans 19 bold",relief=GROOVE,borderwidth=3,width=13,anchor='w')
            idlabel.place(x=10,y=10)

            selectdrop = OptionMenu(searchroot , selectval , *options)
            selectdrop.config(width=14,font=('comicsans', 15),borderwidth=5)
            selectdrop.place(x=250,y=10)

            selectbtn = Button(searchroot,text='Select',font="comicsans 15 bold",width=20,borderwidth=5,activebackground='cyan4',activeforeground='white',bg='cyan2',command=showentrybox)
            selectbtn.place(x=110,y=70)

            namelabel = Label(searchroot,text='Enter Name:',bg='cyan2',font="comicsans 19 bold",relief=GROOVE,borderwidth=3,width=13,anchor='w')
            namelabel.place(x=10,y=130)
            nameentry = Entry(searchroot,font="comicsans 15 bold",width=18,borderwidth=5,textvariable=nameval)
            nameentry.place(x=250,y=130)
            submitbtn = Button(searchroot,text='Search',font="comicsans 15 bold",width=20,borderwidth=5,activebackground='cyan4',activeforeground='white',bg='cyan2',command=search)
            submitbtn.place(x=110,y=190)

        elif(selectoption == "Mobile No"):
            for widget in searchroot.winfo_children():
                widget.destroy()
            idlabel = Label(searchroot,text='Search By:',bg='cyan2',font="comicsans 19 bold",relief=GROOVE,borderwidth=3,width=13,anchor='w')
            idlabel.place(x=10,y=10)

            selectdrop = OptionMenu(searchroot , selectval , *options)
            selectdrop.config(width=14,font=('comicsans', 15),borderwidth=5)
            selectdrop.place(x=250,y=10)

            selectbtn = Button(searchroot,text='Select',font="comicsans 15 bold",width=20,borderwidth=5,activebackground='cyan4',activeforeground='white',bg='cyan2',command=showentrybox)
            selectbtn.place(x=110,y=70)

            mobilelabel = Label(searchroot,text='Enter Mobile:',bg='cyan2',font="comicsans 19 bold",relief=GROOVE,borderwidth=3,width=13,anchor='w')
            mobilelabel.place(x=10,y=130)
            mobileentry = Entry(searchroot,font="comicsans 15 bold",width=18,borderwidth=5,textvariable=mobileval)
            mobileentry.place(x=250,y=130)
            submitbtn = Button(searchroot,text='Search',font="comicsans 15 bold",width=20,borderwidth=5,activebackground='cyan4',activeforeground='white',bg='cyan2',command=search)
            submitbtn.place(x=110,y=190)

        elif(selectoption == "Email"):
            for widget in searchroot.winfo_children():
                widget.destroy()
            idlabel = Label(searchroot,text='Search By:',bg='cyan2',font="comicsans 19 bold",relief=GROOVE,borderwidth=3,width=13,anchor='w')
            idlabel.place(x=10,y=10)

            selectdrop = OptionMenu(searchroot , selectval , *options)
            selectdrop.config(width=14,font=('comicsans', 15),borderwidth=5)
            selectdrop.place(x=250,y=10)

            selectbtn = Button(searchroot,text='Select',font="comicsans 15 bold",width=20,borderwidth=5,activebackground='cyan4',activeforeground='white',bg='cyan2',command=showentrybox)
            selectbtn.place(x=110,y=70)

            emaillabel = Label(searchroot,text='Enter Email:',bg='cyan2',font="comicsans 19 bold",relief=GROOVE,borderwidth=3,width=13,anchor='w')
            emaillabel.place(x=10,y=130)
            emailentry = Entry(searchroot,font="comicsans 15 bold",width=18,borderwidth=5,textvariable=emailval)
            emailentry.place(x=250,y=130)
            submitbtn = Button(searchroot,text='Search',font="comicsans 15 bold",width=20,borderwidth=5,activebackground='cyan4',activeforeground='white',bg='cyan2',command=search)
            submitbtn.place(x=110,y=190)

        elif(selectoption == "Address"):
            for widget in searchroot.winfo_children():
                widget.destroy()
            idlabel = Label(searchroot,text='Search By:',bg='cyan2',font="comicsans 19 bold",relief=GROOVE,borderwidth=3,width=13,anchor='w')
            idlabel.place(x=10,y=10)

            selectdrop = OptionMenu(searchroot , selectval , *options)
            selectdrop.config(width=14,font=('comicsans', 15),borderwidth=5)
            selectdrop.place(x=250,y=10)

            selectbtn = Button(searchroot,text='Select',font="comicsans 15 bold",width=20,borderwidth=5,activebackground='cyan4',activeforeground='white',bg='cyan2',command=showentrybox)
            selectbtn.place(x=110,y=70)

            addresslabel = Label(searchroot,text='Enter Address:',bg='cyan2',font="comicsans 19 bold",relief=GROOVE,borderwidth=3,width=13,anchor='w')
            addresslabel.place(x=10,y=130)
            addressentry = Entry(searchroot,font="comicsans 15 bold",width=18,borderwidth=5,textvariable=addressval)
            addressentry.place(x=250,y=130)
            submitbtn = Button(searchroot,text='Search',font="comicsans 15 bold",width=20,borderwidth=5,activebackground='cyan4',activeforeground='white',bg='cyan2',command=search)
            submitbtn.place(x=110,y=190)

        elif(selectoption == "Gender"):
            for widget in searchroot.winfo_children():
                widget.destroy()
            idlabel = Label(searchroot,text='Search By:',bg='cyan2',font="comicsans 19 bold",relief=GROOVE,borderwidth=3,width=13,anchor='w')
            idlabel.place(x=10,y=10)

            selectdrop = OptionMenu(searchroot , selectval , *options)
            selectdrop.config(width=14,font=('comicsans', 15),borderwidth=5)
            selectdrop.place(x=250,y=10)

            selectbtn = Button(searchroot,text='Select',font="comicsans 15 bold",width=20,borderwidth=5,activebackground='cyan4',activeforeground='white',bg='cyan2',command=showentrybox)
            selectbtn.place(x=110,y=70)

            genderoptions = ["Male","Female","Other"]
            genderlabel = Label(searchroot,text='Enter Gender:',bg='cyan2',font="comicsans 19 bold",relief=GROOVE,borderwidth=3,width=13,anchor='w')
            genderlabel.place(x=10,y=130)
            # igenderentry = Entry(searchroot,font="comicsans 15 bold",width=18,borderwidth=5,textvariable=genderval)
            genderdrop = OptionMenu(searchroot , genderval , *genderoptions)
            genderdrop.config(width=14,font=('comicsans', 15),borderwidth=5)
            genderdrop.place(x=250,y=130)
            submitbtn = Button(searchroot,text='Search',font="comicsans 15 bold",width=20,borderwidth=5,activebackground='cyan4',activeforeground='white',bg='cyan2',command=search)
            submitbtn.place(x=110,y=190)

        elif(selectoption == "D.O.B"):
            for widget in searchroot.winfo_children():
                widget.destroy()
            idlabel = Label(searchroot,text='Search By:',bg='cyan2',font="comicsans 19 bold",relief=GROOVE,borderwidth=3,width=13,anchor='w')
            idlabel.place(x=10,y=10)

            selectdrop = OptionMenu(searchroot , selectval , *options)
            selectdrop.config(width=14,font=('comicsans', 15),borderwidth=5)
            selectdrop.place(x=250,y=10)


            selectbtn = Button(searchroot,text='Select',font="comicsans 15 bold",width=20,borderwidth=5,activebackground='cyan4',activeforeground='white',bg='cyan2',command=showentrybox)
            selectbtn.place(x=110,y=70)

            doblabel = Label(searchroot,text='Enter D.O.B:',bg='cyan2',font="comicsans 19 bold",relief=GROOVE,borderwidth=3,width=13,anchor='w')
            doblabel.place(x=10,y=130)
            dobentry = Entry(searchroot,font="comicsans 15 bold",width=18,borderwidth=5,textvariable=dobval)
            dobentry.place(x=250,y=130)
            submitbtn = Button(searchroot,text='Search',font="comicsans 15 bold",width=20,borderwidth=5,activebackground='cyan4',activeforeground='white',bg='cyan2',command=search)
            submitbtn.place(x=110,y=190)

        elif(selectoption == "Added Date"):
            for widget in searchroot.winfo_children():
                widget.destroy()
            idlabel = Label(searchroot,text='Search By:',bg='cyan2',font="comicsans 19 bold",relief=GROOVE,borderwidth=3,width=13,anchor='w')
            idlabel.place(x=10,y=10)

            selectdrop = OptionMenu(searchroot , selectval , *options)
            selectdrop.config(width=14,font=('comicsans', 15),borderwidth=5)
            selectdrop.place(x=250,y=10)

            selectbtn = Button(searchroot,text='Select',font="comicsans 15 bold",width=20,borderwidth=5,activebackground='cyan4',activeforeground='white',bg='cyan2',command=showentrybox)
            selectbtn.place(x=110,y=70)

            datelabel = Label(searchroot,text='Enter date:',bg='cyan2',font="comicsans 19 bold",relief=GROOVE,borderwidth=3,width=13,anchor='w')
            datelabel.place(x=10,y=130)
            dateentry = Entry(searchroot,font="comicsans 15 bold",width=18,borderwidth=5,textvariable=dateval)
            dateentry.place(x=250,y=130)
            submitbtn = Button(searchroot,text='Search',font="comicsans 15 bold",width=20,borderwidth=5,activebackground='cyan4',activeforeground='white',bg='cyan2',command=search)
            submitbtn.place(x=110,y=190)

        else:
            messagebox.showerror("Error","Please Select Search Option from Dropdown Menu!!!")

    idlabel = Label(searchroot,text='Search By:',bg='cyan2',font="comicsans 19 bold",relief=GROOVE,borderwidth=3,width=13,anchor='w')
    idlabel.place(x=10,y=10)

    selectdrop = OptionMenu(searchroot , selectval , *options)
    selectdrop.config(width=14,font=('comicsans', 15),borderwidth=5)
    selectdrop.place(x=250,y=10)

    selectbtn = Button(searchroot,text='Select',font="comicsans 15 bold",width=20,borderwidth=5,activebackground='cyan4',activeforeground='white',bg='cyan2',command=showentrybox)
    selectbtn.place(x=110,y=70)


    searchroot.mainloop()
#####################################################################################
# ------------------------------Delete Student definition----------------------#  
def deletestudent():
    #copy the data of the selected cursor(on which data we have clicked) on the table to cc
    cc = studenttable.focus()
    #identify where we have clicked and copied to content
    content = studenttable.item(cc)
    #pp is to store the id of the selected cursor
    if(cc!=''):
        pp = content['values'][0]
        res = messagebox.askyesno('Notification','Do you want to delete details of Student with Id: {}'.format(pp))
        if(res == True):
            strr = 'delete from Academicdetails where Accid=%s'
            mycursor.execute(strr,(pp,))
            strr = 'delete from mentorstable where studid=%s'
            mycursor.execute(strr,(pp,))
            strr = 'delete from studentdata where id=%s'
            mycursor.execute(strr,(pp,))
            #con we have created before to link mysql
            con.commit()
            messagebox.showinfo('Notification','Record with Id: {} deleted Sucessfully...'.format(pp))
        
    else:
        messagebox.showerror('Error','You have not Selected Any Data!!!\nPlease select the data you want to Ddelete')
    
    #-----------------------Update the data shown table after deleting the the specific data-----------------------##
    strr = 'select id,name,mobile_no,email,address,gender,dob,sslc,puc,pucboard,college,Mentorid,Mname,Mph_no,date,time from studentdata left join Academicdetails on studentdata.id = Academicdetails.accid left join mentorstable on studentdata.id = mentorstable.studid'
    mycursor.execute(strr) 
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15]]
        studenttable.insert('', END, values=vv)
####################################################################################### ------------------------------Update Student definition----------------------# 
def updatestudent():

    def studentdataupdate():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        date = dateval.get()       
        time = timeval.get()

        strr = 'update studentdata set name=%s,mobile_no=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
        mycursor.execute(strr,(name,mobile,email,address,gender,dob,date,time,id))
        #con object will update to the mysql
        con.commit()
        messagebox.showinfo('Notification','Id: {} Updated Sucessfully....'.format(id),parent=updateroot)
        updateroot.destroy()
        strr = 'select id,name,mobile_no,email,address,gender,dob,sslc,puc,pucboard,college,Mentorid,Mname,Mph_no,date,time from studentdata left join academicdetails on studentdata.id = academicdetails.accid left join mentorstable on studentdata.id = mentorstable.studid'
        mycursor.execute(strr) 
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15]]
            studenttable.insert('', END, values=vv)

    def accdataupdate():
        id = accidval.get()
        name = accnameval.get()
        sslc = sslcval.get()
        puc = pucval.get()
        pucboard = selectboardval.get()
        college = collegeval.get()

        strr = 'update academicdetails set Accname=%s,sslc=%s,puc=%s,pucboard=%s,college=%s where Accid=%s'
        mycursor.execute(strr,(name,sslc,puc,pucboard,college,id))
        #con object will update to the mysql
        con.commit()
        messagebox.showinfo('Notification','Id: {} Updated Sucessfully....'.format(id),parent=updateroot)
        updateroot.destroy()
        strr = 'select id,name,mobile_no,email,address,gender,dob,sslc,puc,pucboard,college,Mentorid,Mname,Mph_no,date,time from studentdata left join academicdetails on studentdata.id = academicdetails.accid left join mentorstable on studentdata.id = mentorstable.studid'
        mycursor.execute(strr) 
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15]]
            studenttable.insert('', END, values=vv)
    def mendataupdate():
        id = menstudidval.get()
        menid = menidval.get()
        name = mennameval.get()
        contactno = mencontactnoval.get()


        strr = 'update mentorstable set Mentorid=%s,Mname=%s,Mph_no=%s where studid=%s'
        mycursor.execute(strr,(menid,name,contactno,id))
        #con object will update to the mysql
        con.commit()
        messagebox.showinfo('Notification','Id: {} Updated Sucessfully....'.format(id),parent=updateroot)
        updateroot.destroy()
        strr = 'select id,name,mobile_no,email,address,gender,dob,sslc,puc,pucboard,college,Mentorid,Mname,Mph_no,date,time from studentdata left join academicdetails on studentdata.id = academicdetails.accid left join mentorstable on studentdata.id = mentorstable.studid'
        mycursor.execute(strr) 
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15]]
            studenttable.insert('', END, values=vv)

    ##-----------------------Update root frame-----------------------##

    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('490x720+140+0')
    updateroot.title('Update')
    updateroot.config(bg='gray34')
    updateroot.iconbitmap('book.ico')
    updateroot.resizable(False,False)

    ##-----------------------Lables of the update root Frame-----------------------##
    idval = StringVar()
    nameval = StringVar()
    accidval = StringVar()
    accnameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    sslcval = StringVar()
    pucval = StringVar()
    pucboardval = StringVar()
    collegeval = StringVar()
    menstudidval = StringVar()
    menidval = StringVar()
    mennameval = StringVar()
    mencontactnoval = StringVar()
    dateval = StringVar()
    timeval = StringVar()
    selectboardval = StringVar()
    selectval = StringVar()

    options = ["Update Studentdata","Update academic details","Update Mentors Details"]
    

    def Updatedetails():
        selectoption = selectval.get()

        if(selectoption == "Update Studentdata"):
            for widget in updateroot.winfo_children():
                widget.destroy()
            idlabel = Label(updateroot,text='Update data:',bg='cyan2',font="comicsans 19 bold",relief=GROOVE,borderwidth=3,width=13,anchor='w')
            idlabel.place(x=10,y=10)

            selectdrop = OptionMenu(updateroot, selectval , *options)
            selectdrop.config(width=21,font=('comicsans', 10),borderwidth=5)
            selectdrop.place(x=250,y=10)

            selectbtn=Button(updateroot,text='Select',font="comicsans 15 bold",width=20,borderwidth=5,activebackground='cyan4',activeforeground='white',bg='cyan2',command=Updatedetails)
            selectbtn.place(x=110,y=70)

            idlabel = Label(updateroot,text='Enter ID:',bg='cyan2',font=('times',20),relief=GROOVE,borderwidth=3,width=13,anchor='w')
            idlabel.place(x=10,y=130)

            namelabel = Label(updateroot,text='Enter Name:',bg='cyan2',font=('times',20),relief=GROOVE,borderwidth=3,width=13,anchor='w')
            namelabel.place(x=10,y=190)

            mobilelabel = Label(updateroot,text='Enter Mobile:',bg='cyan2',font=('times',20),relief=GROOVE,borderwidth=3,width=13,anchor='w')
            mobilelabel.place(x=10,y=250)

            emaillabel = Label(updateroot,text='Enter Email:',bg='cyan2',font=('times',20),relief=GROOVE,borderwidth=3,width=13,anchor='w')
            emaillabel.place(x=10,y=310)

            addresslabel = Label(updateroot,text='Enter Address:',bg='cyan2',font=('times',20),relief=GROOVE,borderwidth=3,width=13,anchor='w')
            addresslabel.place(x=10,y=370)
            
            genderoptions = ["Male","Female","Other"]
            genderlabel = Label(updateroot,text='Enter Gender:',bg='cyan2',font=('times',20),relief=GROOVE,borderwidth=3,width=13,anchor='w')
            genderlabel.place(x=10,y=430)

            doblabel = Label(updateroot,text='Enter D.O.B:',bg='cyan2',font=('times',20),relief=GROOVE,borderwidth=3,width=13,anchor='w')
            doblabel.place(x=10,y=490)

            datelabel = Label(updateroot,text='Enter date:',bg='cyan2',font=('times',20),relief=GROOVE,borderwidth=3,width=13,anchor='w')
            datelabel.place(x=10,y=550)

            timelabel = Label(updateroot,text='Enter Time:',bg='cyan2',font=('times',20),relief=GROOVE,borderwidth=3,width=13,anchor='w')
            timelabel.place(x=10,y=605)

            ##-----------------------Entery boxes for update root frame lables-----------------------## 

            identry = Entry(updateroot,font=('comicsans',15,'bold'),borderwidth=5,textvariable=idval,state=DISABLED)
            identry.place(x=250,y=130)

            nameentry = Entry(updateroot,font=('comicsans',15,'bold'),borderwidth=5,textvariable=nameval)
            nameentry.place(x=250,y=190)

            mobileentry = Entry(updateroot,font=('comicsans',15,'bold'),borderwidth=5,textvariable=mobileval)
            mobileentry.place(x=250,y=250)

            emailentry = Entry(updateroot,font=('comicsans',15,'bold'),borderwidth=5,textvariable=emailval)
            emailentry.place(x=250,y=310)

            addressentry = Entry(updateroot,font=('comicsans',15,'bold'),borderwidth=5,textvariable=addressval)
            addressentry.place(x=250,y=370)

            igenderdrop = OptionMenu(updateroot , genderval , *genderoptions)
            igenderdrop.config(width=16,font=('comicsans', 15),borderwidth=5)
            igenderdrop.place(x=250,y=430)

            dobentry = Entry(updateroot,font=('comicsans',15,'bold'),borderwidth=5,textvariable=dobval)
            dobentry.place(x=250,y=490)

            dateentry = Entry(updateroot,font=('comicsans',15,'bold'),borderwidth=5,textvariable=dateval,state=DISABLED)
            dateentry.place(x=250,y=550)

            timeentry = Entry(updateroot,font=('comicsans',15,'bold'),borderwidth=5,textvariable=timeval,state=DISABLED)
            timeentry.place(x=250,y=605)


            ##-----------------------Automatically fill the details of the data selected by click(mouse click) and clicking on update button-----------------------##

            cc = studenttable.focus()
            content = studenttable.item(cc)
            pp = content['values']
            if(len(pp) != 0):
                idval.set(pp[0])
                nameval.set(pp[1])
                mobileval.set(pp[2])
                emailval.set(pp[3])
                addressval.set(pp[4])
                genderval.set(pp[5])
                dobval.set(pp[6])
                dateval.set(date.today().strftime("%d/%m/%Y"))
                timeval.set(datetime.now().strftime("%I:%M:%S"))

            ##-----------------------ADD button for the updateroot Fram-----------------------##
            submitbtn = Button(updateroot,text='Update',font=('comicsans',15,'bold'),width=20,borderwidth=5,activebackground='cyan4',activeforeground='white',bg='cyan2',command=studentdataupdate)
            submitbtn.place(x=120,y=650)

        elif(selectoption == "Update academic details"):
            for widget in updateroot.winfo_children():
                widget.destroy()
            idlabel = Label(updateroot,text='Update data:',bg='cyan2',font="comicsans 19 bold",relief=GROOVE,borderwidth=3,width=13,anchor='w')
            idlabel.place(x=10,y=10)

            selectdrop = OptionMenu(updateroot, selectval , *options)
            selectdrop.config(width=21,font=('comicsans', 10),borderwidth=5)
            selectdrop.place(x=250,y=10)

            selectbtn=Button(updateroot,text='Select',font="comicsans 15 bold",width=20,borderwidth=5,activebackground='cyan4',activeforeground='white',bg='cyan2',command=Updatedetails)
            selectbtn.place(x=110,y=70)

            accidlabel = Label(updateroot,text='Enter ID:',bg='cyan2',font=('times',20),relief=GROOVE,borderwidth=3,width=13,anchor='w')
            accidlabel.place(x=10,y=130)

            accnamelabel = Label(updateroot,text='Enter Name:',bg='cyan2',font=('times',20),relief=GROOVE,borderwidth=3,width=13,anchor='w')
            accnamelabel.place(x=10,y=190)

            sslclabel = Label(updateroot,text='SSLC Marks:',bg='cyan2',font=('times',20),relief=GROOVE,borderwidth=3,width=13,anchor='w')
            sslclabel.place(x=10,y=250)

            puclabel = Label(updateroot,text='PUC Marks:',bg='cyan2',font=('times',20),relief=GROOVE,borderwidth=3,width=13,anchor='w')
            puclabel.place(x=10,y=310)

            pucboardlabel = Label(updateroot,text='Puc Edu.Board:',bg='cyan2',font=('times',20),relief=GROOVE,borderwidth=3,width=13,anchor='w')
            pucboardlabel.place(x=10,y=370)

            collegelabel = Label(updateroot,text='College Name:',bg='cyan2',font=('times',20),relief=GROOVE,borderwidth=3,width=13,anchor='w')
            collegelabel.place(x=10,y=430)

            ##-----------------------Entery boxes for update root frame lables-----------------------## 
            selectboard = ["State Board","CBSE Board"]

            accidentry = Entry(updateroot,font=('comicsans',15,'bold'),borderwidth=5,textvariable=accidval,state=DISABLED)
            accidentry.place(x=250,y=130)

            accnameentry = Entry(updateroot,font=('comicsans',15,'bold'),borderwidth=5,textvariable=accnameval,state=DISABLED)
            accnameentry.place(x=250,y=190)

            sslceentry = Entry(updateroot,font=('comicsans',15,'bold'),borderwidth=5,textvariable=sslcval)
            sslceentry.place(x=250,y=250)

            pucentry = Entry(updateroot,font=('comicsans',15,'bold'),borderwidth=5,textvariable=pucval)
            pucentry.place(x=250,y=310)

            # pucboardentry = Entry(updateroot,font=('comicsans',15,'bold'),borderwidth=5,textvariable=pucboardval)
            selectdrop = OptionMenu(updateroot , selectboardval , *selectboard)
            selectdrop.config(width=16,font=('comicsans', 15),borderwidth=5)
            selectdrop.place(x=250,y=370)

            collegeentry = Entry(updateroot,font=('comicsans',15,'bold'),borderwidth=5,textvariable=collegeval)
            collegeentry.place(x=250,y=430)

            ##-----------------------Automatically fill the details of the data selected by click(mouse click) and clicking on update button-----------------------##

            cc = studenttable.focus()
            content = studenttable.item(cc)
            pp = content['values']
            if(len(pp) != 0):
                accidval.set(pp[0])
                accnameval.set(pp[1])
                sslcval.set(pp[7])
                pucval.set(pp[8])
                selectboardval.set(pp[9])
                collegeval.set(pp[10])

            ##-----------------------ADD button for the updateroot Fram-----------------------##
            submitbtn = Button(updateroot,text='Update',font=('comicsans',15,'bold'),width=20,borderwidth=5,activebackground='cyan4',activeforeground='white',bg='cyan2',command=accdataupdate)
            submitbtn.place(x=120,y=490)

        elif(selectoption == "Update Mentors Details"):

            for widget in updateroot.winfo_children():
                widget.destroy()
            idlabel = Label(updateroot,text='Update data:',bg='cyan2',font="comicsans 19 bold",relief=GROOVE,borderwidth=3,width=13,anchor='w')
            idlabel.place(x=10,y=10)

            selectdrop = OptionMenu(updateroot, selectval , *options)
            selectdrop.config(width=21,font=('comicsans', 10),borderwidth=5)
            selectdrop.place(x=250,y=10)

            selectbtn=Button(updateroot,text='Select',font="comicsans 15 bold",width=20,borderwidth=5,activebackground='cyan4',activeforeground='white',bg='cyan2',command=Updatedetails)
            selectbtn.place(x=110,y=70)

            menstudidlabel = Label(updateroot,text='Enter StudentId:',bg='cyan2',font=('times',20),relief=GROOVE,borderwidth=3,width=13,anchor='w')
            menstudidlabel.place(x=10,y=130)

            menidlabel = Label(updateroot,text='Enter MentorId:',bg='cyan2',font=('times',20),relief=GROOVE,borderwidth=3,width=13,anchor='w')
            menidlabel.place(x=10,y=190)

            mennamelabel = Label(updateroot,text='Enter Name:',bg='cyan2',font=('times',20),relief=GROOVE,borderwidth=3,width=13,anchor='w')
            mennamelabel.place(x=10,y=250)

            mencontactnolabel = Label(updateroot,text='Enter Contact_no:',bg='cyan2',font=('times',20),relief=GROOVE,borderwidth=3,width=13,anchor='w')
            mencontactnolabel.place(x=10,y=310)

            ##-----------------------Entery boxes for update root frame lables-----------------------## 

            menstudidentry = Entry(updateroot,font=('comicsans',15,'bold'),borderwidth=5,textvariable=menstudidval,state=DISABLED)
            menstudidentry.place(x=250,y=130)

            menidentry = Entry(updateroot,font=('comicsans',15,'bold'),borderwidth=5,textvariable=menidval)
            menidentry.place(x=250,y=190)

            mennameentry = Entry(updateroot,font=('comicsans',15,'bold'),borderwidth=5,textvariable=mennameval)
            mennameentry.place(x=250,y=250)

            mencontactnoentry = Entry(updateroot,font=('comicsans',15,'bold'),borderwidth=5,textvariable=mencontactnoval)
            mencontactnoentry.place(x=250,y=310)

            ##-----------------------Automatically fill the details of the data selected by click(mouse click) and clicking on update button-----------------------##

            cc = studenttable.focus()
            content = studenttable.item(cc)
            pp = content['values']
            if(len(pp) != 0):
                menstudidval.set(pp[0])
                menidval.set(pp[11])
                mennameval.set(pp[12])
                mencontactnoval.set(pp[13])

            ##-----------------------ADD button for the updateroot Fram-----------------------##
            submitbtn = Button(updateroot,text='Update',font=('comicsans',15,'bold'),width=20,borderwidth=5,activebackground='cyan4',activeforeground='white',bg='cyan2',command=mendataupdate)
            submitbtn.place(x=120,y=370)

        else:
            messagebox.showerror("Error","Please Select Update Option from Dropdown Menu!!!")
            

    idlabel = Label(updateroot,text='Update data:',bg='cyan2',font="comicsans 19 bold",relief=GROOVE,borderwidth=3,width=13,anchor='w')
    idlabel.place(x=10,y=10)

    selectdrop = OptionMenu(updateroot, selectval , *options)
    selectdrop.config(width=21,font=('comicsans', 10),borderwidth=5)
    selectdrop.place(x=250,y=10)

    cc = studenttable.focus()
    if(cc!=''):
        selectbtn=Button(updateroot,text='Select',font="comicsans 15 bold",width=20,borderwidth=5,activebackground='cyan4',activeforeground='white',bg='cyan2',command=Updatedetails)
        selectbtn.place(x=110,y=70)
    else:
        messagebox.showerror('Error','You have Not Selected Any Data!!!\nPlease select the data you want to Update')
        updateroot.destroy()

    updateroot.mainloop()
    #####################################################################################
#####################################################################################
#-------------------------Show All definition--------------------------------# 
def showstudent():
    strr = 'select id,name,mobile_no,email,address,gender,dob,sslc,puc,pucboard,college,Mentorid,Mname,Mph_no,date,time from studentdata left join Academicdetails on studentdata.id = Academicdetails.accid left join mentorstable on studentdata.id = mentorstable.studid'
    mycursor.execute(strr) 
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15]]
        studenttable.insert('', END, values=vv)
####################################################################################
# --------------------------Exportdefnition---------------------------------#       
def exportstudent():
    val = messagebox.askyesno("Notification","Want to export the details to .csv files??")
    if val:
        #ff is to copy the path of saved file 
        ff = filedialog.asksaveasfilename()
        gg = studenttable.get_children()
        id,name,mobile,email,address,gender,dob,sslc,puc,pucboard,college,Mentorid,Mname,Mph_no,addeddate,addedtime = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
        for i in gg:
            content = studenttable.item(i)
            pp = content['values']
            id.append(pp[0]),name.append(pp[1]),mobile.append(pp[2]),email.append(pp[3]),address.append(pp[4]),gender.append(pp[5]),dob.append(pp[6]),sslc.append(pp[7]),puc.append(pp[8]),pucboard.append(pp[9]),college.append(pp[10]),Mentorid.append(pp[11]),Mname.append(pp[12]),Mph_no.append(pp[13]),addeddate.append(pp[14]),addedtime.append(pp[15])    
        #to put heading in the exported files
        dd = ['ID','Name','Mobile_No','Email','Address','Gender','D.O.B','SSLC Marks','PUC Marks','PUC Edu.Board Marks','College Name','Mentors ID','Mentors Name','Mentors Contact_no','Added Date','Added Time']
        df = pandas.DataFrame(list(zip(id,name,mobile,email,address,gender,dob,sslc,puc,pucboard,college,Mentorid,Mname,Mph_no,addeddate,addedtime)),columns=dd)
        paths = r'{}.csv'.format(ff)
        df.to_csv(paths,index=False)
        if paths != ".csv":
            messagebox.showinfo('Notification','Student Data is Sucessfully Exported to {}'.format(paths))
# --------------------------Exitdefnition---------------------------------#     
def exitstudent():
    res = messagebox.askquestion('Notification','Do you want to Exit?')
    if(res == "yes"):
        root.destroy()
######################################################### Connection of database
def Connectdb():
    def submitdb():
        #Storing the values in the variables
        host = hostval.get()
        user = userval.get()
        password = passval.get()
        
        global con,mycursor
        try:         # Connection to the database using mysql.connector module
            # Here connect takes four parameters host,user,password and name of the database
            con = mysql.connector.connect(host=host,user=user,password=password)

            # Cursor enables to perform sql queries
            mycursor = con.cursor()
            
        except:       # If wrong deatils are entered message is shown
            messagebox.showerror('Notification','Incorrect data Please try again',parent=dbroot)
            return

        try:
            strr = 'create database studentmanagement'
            mycursor.execute(strr)
            strr = 'use studentmanagement'
            mycursor.execute(strr)
            strr = 'create table studentdata(id int not null,Name varchar(20),Mobile_no bigint,email varchar(30),address varchar(100),gender varchar(50),DOB varchar(50),date varchar(50),time varchar(50),primary key (id))'
            mycursor.execute(strr)
            strr = 'create table Academicdetails(Accid int not null,Accname varchar(20),sslc int,puc int,pucboard varchar(50),college varchar(50),primary key(Accid),foreign key(Accid) references studentdata(id))'
            mycursor.execute(strr)
            strr = 'create table mentorstable(studid int not null,Mentorid int not null,Mname varchar(10),Mph_no bigint,foreign key(studid) references studentdata(id),primary key(studid))'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','Database is Created and Connected  Sucessfully....',parent=dbroot)

            
        except:
            strr = 'use studentmanagement'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','You are Connected to Database Sucessfully....',parent=dbroot) # Parent is which window to place the dialog on top of
            strr = 'select id,name,mobile_no,email,address,gender,dob,sslc,puc,pucboard,college,Mentorid,Mname,Mph_no,date,time from studentdata left join Academicdetails on studentdata.id = Academicdetails.accid left join mentorstable on studentdata.id = mentorstable.studid'
            mycursor.execute(strr) 
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15]]
                
                studenttable.insert('', END, values=vv)
        dbroot.destroy()

    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry("470x250+700+230")
    dbroot.title("Connect to DB")
    dbroot.iconbitmap("book.ico")
    dbroot.resizable(False,False)
    dbroot.config(bg='gray34')
    #-------------------------------------- Connectdb Labesl

    hostlabel = Label(dbroot,text="Enter Host:",bg='cyan2',font="comicsans 19 bold",relief=GROOVE,borderwidth=3,width=13,anchor="w")
    hostlabel.place(x=10,y=10)

    userlabel = Label(dbroot,text="Enter User:",bg='cyan2',font="comicsans 19 bold",relief=GROOVE,borderwidth=3,width=13,anchor="w")
    userlabel.place(x=10,y=70)

    passwordlabel  = Label(dbroot,text="Enter Password:",bg='cyan2',font="comicsans 19 bold",relief=GROOVE,borderwidth=3,width=13,anchor="w")
    passwordlabel.place(x=10,y=130)
    #---------------------------------------------Connectdb entries

    hostval = StringVar()
    userval = StringVar()
    passval = StringVar()
    
    hostentry = Entry(dbroot,font="comicsans 19 bold",width = 15,bd=5,textvariable=hostval)
    hostentry.place(x=240,y=10)
    
    userentry = Entry(dbroot,font="comicsans 19 bold",width = 15,bd=5,textvariable=userval)
    userentry.place(x=240,y=70)

    passwordentry = Entry(dbroot,font="comicsans 19 bold",width = 15,bd=5,textvariable=passval,show='*')
    passwordentry.place(x=240,y=130)

    #-----------------------Submit Button for DBMS connection frame-----------------------##
    submitbutton = Button(dbroot,text="Connect",font="comicsans 15 bold",bg='cyan2',borderwidth=5,width=20,activebackground='cyan4',activeforeground='white',command=submitdb)
    submitbutton.place(x=130,y=180)

    dbroot.mainloop()


####################################################################################

def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%y")
    clock.configure(text="Date :"+date_string+"\n"+"Time :"+time_string)
    clock.after(200,tick)

#####################################################################################
from tkinter import *
from tkinter import Toplevel,messagebox,filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import mysql.connector
import pandas
import time 
from datetime import date
from datetime import datetime



root = Tk()
root.title("Student Record Management System")
root.config(bg='gray30')
root.geometry("1120x710+100+0")
root.iconbitmap("book.ico")
root.resizable(False,False)

########################################################################### Frames
######################################################### DataEntry Frame
DataEntryFrame = Frame(root,bg='cyan2',relief=GROOVE,borderwidth=8)
DataEntryFrame.place(x=10,y=68,width=460,height=620) 

frontlabel = Label(DataEntryFrame,text='--------------------------Welcome------------------------',width=35,font="comicsans 19 bold",bg='cyan')
frontlabel.pack(side=TOP,expand=True)

adddbutton = Button(DataEntryFrame,text=" Add Student",width=25,font="comicsans 19 bold",borderwidth=6,bg='gray45',foreground='black',activebackground='gray14',relief=RIDGE,activeforeground='white',command=addstudent)
adddbutton.pack(side=TOP,expand=True)

acadbutton = Button(DataEntryFrame,text="  Add Academic Details",width=25,font="comicsans 19 bold",borderwidth=6,bg='gray45',foreground='black',activebackground='gray14',relief=RIDGE,activeforeground='white',command=Academicdetails)
acadbutton.pack(side=TOP,expand=True)

mentbutton = Button(DataEntryFrame,text="  Add Mentors Details",width=25,font="comicsans 19 bold",borderwidth=6,bg='gray45',foreground='black',activebackground='gray14',relief=RIDGE,activeforeground='white',command=mentorsdetails)
mentbutton.pack(side=TOP,expand=True)

searchbutton = Button(DataEntryFrame,text="  Search Student",width=25,font="comicsans 19 bold",borderwidth=6,bg='gray45',foreground='black',activebackground='gray14',relief=RIDGE,activeforeground='white',command=searchstudent)
searchbutton.pack(side=TOP,expand=True)

deletbutton = Button(DataEntryFrame,text="  Delete Student",width=25,font="comicsans 19 bold",borderwidth=6,bg='gray45',foreground='black',activebackground='gray14',relief=RIDGE,activeforeground='white',command=deletestudent)
deletbutton.pack(side=TOP,expand=True)

updatebutton = Button(DataEntryFrame,text="  Update Student",width=25,font="comicsans 19 bold",borderwidth=6,bg='gray45',foreground='black',activebackground='gray14',relief=RIDGE,activeforeground='white',command=updatestudent)
updatebutton.pack(side=TOP,expand=True)

showallbutton = Button(DataEntryFrame,text="  Show All",width=25,font="comicsans 19 bold",borderwidth=6,bg='gray45',foreground='black',activebackground='gray14',relief=RIDGE,activeforeground='white',command=showstudent)
showallbutton.pack(side=TOP,expand=True)

exportbutton = Button(DataEntryFrame,text="  Export data",width=25,font="comicsans 19 bold",borderwidth=6,bg='gray45',foreground='black',activebackground='gray14',relief=RIDGE,activeforeground='white',command=exportstudent)
exportbutton.pack(side=TOP,expand=True)

exitbutton = Button(DataEntryFrame,text="  Exit",width=25,font="comicsans 19 bold",borderwidth=6,bg='gray45',foreground='black',activebackground='gray14',relief=RIDGE,activeforeground='white',command=exitstudent)
exitbutton.pack(side=TOP,expand=True)
    

###################################################################### ShowDataFrame
## Show data frame with the scroll option
ShowDataFrame = Frame(root,bg='gray25',relief=GROOVE,borderwidth=8)
ShowDataFrame.place(x=500,y=68,width=600,height=620)

# Styling the heading of show show data frame
style = ttk.Style()    
style.configure('Treeview.Heading',font="comicsans 18 bold",foreground='black')

# Styling for the content of the table(DBMS data)
style.configure('Treeview',font="comicsans 15 ",background='cyan',foreground='white')

# Placing scrollbars at the bottom and on right side
scroll_x = Scrollbar(ShowDataFrame,orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame,orient=VERTICAL)
studenttable = Treeview(ShowDataFrame,columns=('Id','Name','Mobile No','Email','Address','Gender','D.O.B','SSLC Marks','PUC Marks','PUC Edu.Board Marks','College Name',"Mentor id","Mentor name","Mentor Contact_no","Added Date",'Added Time'),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)

scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)

# Placing the headings  
studenttable.heading('Id',text='Id',anchor = CENTER) 
studenttable.heading('Name',text='Name',anchor = CENTER)
studenttable.heading('Mobile No',text='Mobile No',anchor = CENTER)
studenttable.heading('Email',text='Email',anchor = CENTER)
studenttable.heading('Address',text='Address',anchor = CENTER)
studenttable.heading('Gender',text='Gender',anchor = CENTER)
studenttable.heading('D.O.B',text='D.O.B',anchor = CENTER)
studenttable.heading('SSLC Marks',text='SSLC Marks',anchor = CENTER)
studenttable.heading('PUC Marks',text='PUC Marks',anchor = CENTER)
studenttable.heading('PUC Edu.Board Marks',text='PUC Edu.Board Marks',anchor = CENTER)
studenttable.heading('College Name',text='College Name',anchor = CENTER)
studenttable.heading('Mentor id',text='Mentor id',anchor = CENTER)
studenttable.heading('Mentor name',text='Mentor name',anchor = CENTER)
studenttable.heading('Mentor Contact_no',text='Mentor Contact_no',anchor = CENTER)
studenttable.heading('Added Date',text='Added Date',anchor = CENTER)
studenttable.heading('Added Time',text='Added Time',anchor = CENTER)
studenttable['show'] = 'headings' # To remove extra column added by Treeview

# Size of the Columns of the table
studenttable.column('Id',width=100,anchor = CENTER)
studenttable.column('Name',width=200,anchor = CENTER)
studenttable.column('Mobile No',width=200,anchor = CENTER)
studenttable.column('Email',width=300,anchor = CENTER)
studenttable.column('Address',width=200,anchor = CENTER)
studenttable.column('Gender',width=150,anchor = CENTER)
studenttable.column('D.O.B',width=150,anchor = CENTER)
studenttable.column('SSLC Marks',width=150,anchor = CENTER)
studenttable.column('PUC Marks',width=150,anchor = CENTER)
studenttable.column('PUC Edu.Board Marks',width=150,anchor = CENTER)
studenttable.column('College Name',width=220,anchor = CENTER)
studenttable.column('Mentor id',width=200,anchor = CENTER)
studenttable.column('Mentor name',width=200,anchor = CENTER)
studenttable.column('Mentor Contact_no',width=250,anchor = CENTER)
studenttable.column('Added Date',width=200,anchor = CENTER)
studenttable.column('Added Time',width=200,anchor = CENTER)

studenttable.pack(fill=BOTH,expand=1)# Packing such that it covers entire frame


###################################################  Display of the title
HeaderLabel = Label(root,text="Student Record Management System",relief=RIDGE,borderwidth=4,font="comicsans 24 bold",bg='cyan',padx=20,pady=6)
HeaderLabel.place(x=230,y=0)
########################################################################## Clock
clock = Label(root,relief=RIDGE,borderwidth=4,font="comicsans 16 bold",bg='cyan2',padx=10)
clock.place(x=0,y=0)
tick()
##########################################################     Connectdatabase button
connectbutton = Button(root,text="Connect to Database",width=16,relief=RIDGE,borderwidth=4,font="comicsans 16 bold",bg='cyan2',activebackground='cyan4',activeforeground='white',command=Connectdb,padx=5,pady=7)
connectbutton.place(x=890,y=0)


root.mainloop()