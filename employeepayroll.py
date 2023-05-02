from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
import random
import time
import os
import tempfile
import datetime
from tkcalendar import *
from tkinter import messagebox

import pymysql

class Payroll:
    def __init__(self,root):
        self.root=root
        self.root.title("Employee Payroll Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

##################################### Frame 1 Variable
        self.employeecode=StringVar()
        self.designation = StringVar()
        self.name = StringVar()
        self.age = StringVar()
        self.gender = StringVar()
        self.email= StringVar()
        self.hiredlocation = StringVar()
        self.txt_address = StringVar()

        ##################################### Frame 2 Variable
        self.doj = StringVar()
        self.dob = StringVar()
        self.experience = StringVar()
        self.proofid = StringVar()
        self.contactno = StringVar()
        self.status= StringVar()

        ##################################### Frame 3 Variable
        self.month = StringVar()
        self.year = StringVar()
        self.basicsalary = StringVar()
        self.totaldays = StringVar()
        self.absents = StringVar()
        self.medical= StringVar()
        self.convence = StringVar()
        self.profedence = StringVar()
        self.netsalary = StringVar()
        self.operator=StringVar()



        title1 = Label(self.root, text="EMPLOYEE PAYROLL MANAGEMENT SYSTEM",font=("times new roman", 20), bd=20, bg="green", fg="white",relief=GROOVE,anchor=W).pack(side=TOP,fill=X)
        btn_logout=Button(title1,text="LOGOUT",bg="red",fg="white",bd=1,height=1,width=10,command=self.logout).place(x=1250,y=25)
        btn_allemployee = Button(title1, text="All Employee's", font=("times new roman",12, "bold"),bg="green", command=self.employee_frame,fg="white", bd=1, height=1, width=15).place(x=1100, y=23)

#######################################################################################################

        frame1=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        frame1.place(x=5,y=70,width=790,height=575)
        title2=Label(frame1,text="Employee Details",font=("times new roman",20),bd=1,bg="lightgray",relief=GROOVE).pack(side=TOP,fill=X)
####ROW1 Label
        lbl_code = Label(frame1, text="Employee code:", font=("times new roman",15),bg="white").place(x=10,y=50)
        lbl_designation = Label(frame1, text="Designation:", font=("times new roman", 15), bg="white").place(x=10, y=100)
        lbl_name = Label(frame1, text="Name:", font=("times new roman", 15), bg="white").place(x=10,y=150)
        lbl_age = Label(frame1, text="Age:", font=("times new roman", 15), bg="white").place(x=10, y=200)
        lbl_gender = Label(frame1, text="Gender:", font=("times new roman", 15), bg="white").place(x=10,y=250)
        lbl_email = Label(frame1, text="Email:", font=("times new roman", 15), bg="white").place(x=10,y=300)
        lbl_hiredlocation = Label(frame1, text="Hired Location:", font=("times new roman", 15), bg="white").place(x=10, y=350)
        lbl_address = Label(frame1, text="Address:", font=("times new roman", 15), bg="white").place(x=10,y=400)

        ####ROW1 Entry Text
        self.txt_code=Entry(frame1,fg="black",bg="lightyellow",font=("times new roman",12),textvariable=self.employeecode,width=50)
        self.txt_code.place(x=150,y=50)
        btn_search=Button(frame1,text="Search",bg="white",fg="black",height=1,width=8,command=self.search).place(x=560,y=50)

        txt_designation=Entry(frame1,fg="black",bg="lightyellow",font=("times new roman",12),textvariable=self.designation,width=30).place(x=150,y=100)
        txt_name = Entry(frame1, fg="black", bg="lightyellow", font=("times new roman", 12),textvariable=self.name, width=30).place(x=150, y=150)
        txt_age = Entry(frame1, fg="black", bg="lightyellow", font=("times new roman", 12),textvariable=self.age, width=30).place( x=150, y=200)
        txt_gender = Entry(frame1, fg="black", bg="lightyellow", font=("times new roman", 12),textvariable=self.gender, width=30).place(x=150, y=250)
        txt_email = Entry(frame1, fg="black", bg="lightyellow", font=("times new roman", 12),textvariable=self.email, width=30).place(x=150, y=300)
        txt_hiredlocation = Entry(frame1, fg="black", bg="lightyellow", font=("times new roman", 12),textvariable=self.hiredlocation, width=30).place(x=150,y=350)
        self.txt_address = Text(frame1, fg="black", bg="lightyellow", font=("times new roman", 12), width=70,height=8)
        self.txt_address.place( x=150, y=400)
#######################################################################################################
####ROW2 Label

        lbl_doj = Label(frame1, text="D.O.J:", font=("times new roman", 15), bg="white").place(x=410, y=100)
        lbl_dob= Label(frame1, text="D.O.B:", font=("times new roman", 15), bg="white").place(x=410,y=150)
        lbl_experience = Label(frame1, text="Experience:", font=("times new roman", 15), bg="white").place(x=410, y=200)
        lbl_proofid = Label(frame1, text="Proof ID:", font=("times new roman", 15), bg="white").place(x=410,y=250)
        lbl_contactno = Label(frame1, text="Contact No:", font=("times new roman", 15), bg="white").place(x=410,y=300)
        lbl_status= Label(frame1, text="Status:", font=("times new roman", 15), bg="white").place(x=410, y=350)


        ####ROW2 Entry Text
        txt_doj = Entry(frame1, fg="black", bg="lightyellow", font=("times new roman", 12),textvariable=self.doj, width=30).place( x=530, y=100)
        txt_dob = Entry(frame1, fg="black", bg="lightyellow", font=("times new roman", 12),textvariable=self.dob, width=30).place(x=530, y=150)
        txt_experience = Entry(frame1, fg="black", bg="lightyellow", font=("times new roman", 12),textvariable=self.experience, width=30).place(x=530, y=200)
        txt_proofid= Entry(frame1, fg="black", bg="lightyellow", font=("times new roman", 12),textvariable=self.proofid, width=30).place(x=530, y=250)
        txt_contactno = Entry(frame1, fg="black", bg="lightyellow", font=("times new roman", 12),textvariable=self.contactno, width=30).place(x=530, y=300)
        txt_status = Entry(frame1, fg="black", bg="lightyellow", font=("times new roman", 12),textvariable=self.status, width=30).place(x=530,y=350)

        frame2=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        frame2.place(x=800,y=70,width=545,height=305)
        title3=Label(frame2,text="Employee Salary Details",font=("times new roman",20),bd=1,bg="lightgray",relief=GROOVE).pack(side=TOP,fill=X)

        lbl_month = Label(frame2, text="Month:", font=("times new roman", 15), bg="white").place(x=10, y=50)
        lbl_year = Label(frame2, text="Year:", font=("times new roman", 15), bg="white").place(x=155, y=50)
        lbl_basicsalary = Label(frame2, text="Basic Salary:", font=("times new roman", 15), bg="white").place(x=315, y=50)

        txt_month = Entry(frame2, fg="black", bg="lightyellow", font=("times new roman", 12),textvariable=self.month, width=10).place(x=70, y=50)
        txt_year = Entry(frame2, fg="black", bg="lightyellow", font=("times new roman", 12),textvariable=self.year, width=13).place(x=205,y=50)
        txt_basicsalary = Entry(frame2, fg="black", bg="lightyellow", font=("times new roman", 12),textvariable=self.basicsalary, width=13).place( x=425, y=50)

        lbl_tataldays = Label(frame2, text="Total Days:", font=("times new roman", 15), bg="white").place(x=10, y=100)
        lbl_absents = Label(frame2, text="Absents:", font=("times new roman", 15), bg="white").place(x=200, y=100)

        lbl_medical = Label(frame2, text="Medical:", font=("times new roman", 15), bg="white").place(x=10, y=150)
        lbl_convence= Label(frame2, text="Convence:", font=("times new roman", 15), bg="white").place(x=10, y=200)

        lbl_profidentfund= Label(frame2, text="Profident Fund:", font=("times new roman", 15), bg="white").place(x=270, y=150)
        lbl_netsalary = Label(frame2, text="Net Salary:", font=("times new roman", 15), bg="white").place(x=270, y=200)

        txt_tataldays = Entry(frame2, fg="black", bg="lightyellow", font=("times new roman", 12),textvariable=self.totaldays, width=8).place(x=110, y=100)
        txt_absents = Entry(frame2, fg="black", bg="lightyellow", font=("times new roman", 12),textvariable=self.absents, width=25).place(x=280, y=100)

        txt_medical = Entry(frame2, fg="black", bg="lightyellow", font=("times new roman", 12),textvariable=self.medical, width=20).place( x=90, y=150)
        txt_convence = Entry(frame2, fg="black", bg="lightyellow", font=("times new roman", 12),textvariable=self.convence, width=15).place(x=100, y=200)

        txt_profidentfund = Entry(frame2, fg="black", bg="lightyellow", font=("times new roman", 12),textvariable=self.profedence, width=13).place(x=400, y=150)
        txt_netsalary = Entry(frame2, fg="black", bg="lightyellow", font=("times new roman", 12),textvariable=self.netsalary, width=13,state=DISABLED).place(x=365, y=200)

        btn_calculate=Button(frame2,text="Calculate",bg="yellow",fg="black",height=1,width=8,command=self.calculate).place(x=50,y=250)

        self.btn_save = Button(frame2, text="Save", bg="lightgreen", fg="black", height=1, width=8,command=self.add)
        self.btn_save.place(x=150, y=250)

        self.btn_clear = Button(frame2, text="Clear", bg="lightgray", fg="black", height=1, width=8,command=self.clear)
        self.btn_clear.place(x=250, y=250)

        self.btn_update = Button(frame2, text="update", bg="lightblue", fg="black", height=1, width=8,command=self.update)
        self.btn_update.place(x=350, y=250)

        self.btn_delete = Button(frame2, text="Delete", bg="red", fg="black", height=1, width=8,command=self.delete)
        self.btn_delete.place(x=450, y=250)

############################################################################################################################################
        frame3=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        frame3.place(x=800,y=380,width=550,height=265)
########################################################################################################Calculator
        frame4 = Frame(frame3, bd=3, relief=RIDGE, bg="white")
        frame4.place(x=0, y=0, width=250, height=257)

        ##############Calculate Frame CALCULATOR
        self.txt_result=StringVar()
        self.operator=''
        def btn_click(num):
            self.operator=self.operator+str(num)
            self.txt_result.set(self.operator)

        def result():
            res = str(eval(self.operator))
            self.txt_result.set(res)
            self.operator=''

        def clear_cal():
            self.txt_result.set('')
            self.operator =''

        txt_result = Entry(frame4, fg="black", bg="lightgray", font=("times new roman", 20), justify=RIGHT,state='readonly', width=17, textvariable=self.txt_result).place(x=2, y=5)

        btn_7= Button(frame4, text="7",font=("times new roman", 13, "bold"), bg="lightgray", fg="black", height=2, width=5,command=lambda:btn_click(7)).place(x=2, y=42)
        btn_8 = Button(frame4, text="8",font=("times new roman", 13, "bold"), bg="lightgray", fg="black", height=2, width=5,command=lambda:btn_click(8)).place(x=62, y=42)
        btn_9 = Button(frame4, text="9",font=("times new roman", 13, "bold"), bg="lightgray", fg="black", height=2, width=5,command=lambda:btn_click(9)).place(x=122, y=42)
        btn_division = Button(frame4, text="/",font=("times new roman", 13, "bold"), bg="lightgray", fg="black", height=2, width=5,command=lambda:btn_click('/')).place(x=182, y=42)

        btn_4 = Button(frame4, text="4", font=("times new roman", 13, "bold"), bg="lightgray", fg="black", height=2,width=5,command=lambda:btn_click(4)).place(x=2, y=94)
        btn_5 = Button(frame4, text="5", font=("times new roman", 13, "bold"), bg="lightgray", fg="black", height=2,width=5,command=lambda:btn_click(5)).place(x=62, y=94)
        btn_6 = Button(frame4, text="6", font=("times new roman", 13, "bold"), bg="lightgray", fg="black", height=2,width=5,command=lambda:btn_click(6)).place(x=122, y=94)
        btn_multiplication = Button(frame4, text="*", font=("times new roman", 13, "bold"), bg="lightgray", fg="black", height=2, width=5,command=lambda:btn_click('*')).place(x=182, y=94)

        btn_1 = Button(frame4, text="1", font=("times new roman", 13, "bold"), bg="lightgray", fg="black", height=2,width=5,command=lambda:btn_click(1)).place(x=2, y=146)
        btn_2 = Button(frame4, text="2", font=("times new roman", 13, "bold"), bg="lightgray", fg="black", height=2,width=5,command=lambda:btn_click(2)).place(x=62, y=146)
        btn_3 = Button(frame4, text="3", font=("times new roman", 13, "bold"), bg="lightgray", fg="black", height=2,width=5,command=lambda:btn_click(3)).place(x=122, y=146)
        btn_mimus = Button(frame4, text="-", font=("times new roman", 13, "bold"), bg="lightgray", fg="black", height=2, width=5,command=lambda:btn_click('-')).place(x=182, y=146)

        btn_zero = Button(frame4, text="0", font=("times new roman", 13, "bold"), bg="lightgray", fg="black", height=2,width=5,command=lambda:btn_click('0')).place(x=2, y=198)
        btn_dot = Button(frame4, text="C", font=("times new roman", 13, "bold"), bg="lightgray", fg="black", height=2,width=5,command=clear_cal).place(x=62, y=198)
        btn_plus = Button(frame4, text="+", font=("times new roman", 13, "bold"), bg="lightgray", fg="black", height=2,width=5,command=lambda:btn_click('+')).place(x=122, y=198)
        btn_equalto = Button(frame4, text="=", font=("times new roman", 13, "bold"), bg="lightgray", fg="black",height=2,width=5,command=result).place(x=182, y=198)

        ########################################################################################################SALARY FRAME
        frame5 = Frame(frame3, bd=2, relief=RIDGE, bg="white",)
        frame5.place(x=250, y=0, width=290, height=257)

        lbl_Salaryreceipt = Label(frame5, text="Salary Receipt", font=("times new roman", 15),bd=1, bg="lightgray", relief=GROOVE).pack(side=TOP, fill=X)


        
        ############### Table #######################
        ############### Scrollbar #####################
        frame6 = Frame(frame5, bd=2, relief=RIDGE, bg="white", )
        frame6.place(x=0, y=30,relwidth=1, height=180)

        self.sample = f'''\tCompany Name, XYZ\n\tAddress: Xyz, Floor4
-------------------------------------------
Employeee ID\t\t: DD
Salary Of\t\t: DD
Generated On\t\t: DD-MM-YYYY
-------------------------------------------
Total Days\t\t: DD
Total Present\t\t: DD
Total Absent\t\t: DD
Convence\t\t: #----
Medical\t\t: #----
PF\t\t: #----
Gross Payment\t\t: #----
Net Salary\t\t: #----
------------------------------------------
This is a computer generated slip, not required any signature
'''

        scroll_y = Scrollbar(frame6, orient=VERTICAL)
        scroll_y.pack(fill=Y, side=RIGHT)

        self.txt_salaryreceipt = Text(frame6, font=("times new roman", 12), bg="lightyellow", yscrollcommand=scroll_y.set)
        self.txt_salaryreceipt.pack(fill=BOTH, expand=1)
        scroll_y.config(command=self.txt_salaryreceipt.yview)

        self.txt_salaryreceipt.insert(END,self.sample)


        self.btn_print = Button(frame5, text="Print", bg="blue", fg="white", height=1, width=8,command=self.print)
        self.btn_print.place(x=200, y=220)
        self.check_connection()

        ########################################################################################################BOTTOM FRAME
        Bottom1 = Frame(self.root, bd=3, relief=RIDGE, bg="green")
        Bottom1.place(x=0, y=645, width=1350, height=50)
        lbl_projectby = Label(Bottom1, text="Project design by: Alagboofe Jumoke Rukayat", font=("times new roman", 13,"bold"),  bg="green",fg="white").place(x=0, y=10)
        lbl_emailby = Label(Bottom1, text="Email: jrukayat09@gmail.com", font=("times new roman", 13,"bold"),bg="green",fg="yellow").place(x=1100, y=10)
 ######################################################################################################
    def calculate(self):
        if self.month.get()=="" or self.year.get()=="" or self.basicsalary.get()=="" or self.month.get()=="":
            messagebox.showerror("Error", "All Fields are Required")
        else:
            # self.netsalary.set("RESULT")
            # 35000/31==1752
            # 31-10-21*1752
            per_day=int(self.basicsalary.get())/int(self.totaldays.get())
            work_day=int(self.totaldays.get()) - int(self.absents.get())
            salary=per_day*work_day
            deduct=int(self.medical.get())+int(self.absents.get())
            addition=int(self.convence.get())
            net=salary-deduct+addition
            self.netsalary.set(str(round(net,2)))


################Salary Frame################Update the receipt

        new_sample = f'''\tCompany Name, XYZ\n\tAddress: Xyz, Floor4
-------------------------------------------
Employeee ID\t\t: {self.employeecode.get()}
Salary Of\t\t: {self.month.get()}-{self.year.get()}
Generated On\t\t: {str(time.strftime("%D-%M-%Y"))}
-------------------------------------------
Total Days\t\t:{self.totaldays.get()}
Total Present\t\t: {str(int(self.totaldays.get())-int(self.absents.get()))}
Total Absent\t\t: {self.absents.get()}
Convence\t\t: # {self.convence.get()}
Medical\t\t: # {self.medical.get()}
PF\t\t: # {self.profedence.get()}
Gross Payment\t\t: #{self.basicsalary.get()}
Net Salary\t\t: #{self.netsalary.get()}
------------------------------------------
This is a computer generated slip, not required any signature
'''
        self.txt_salaryreceipt.delete('1.0',END)
        self.txt_salaryreceipt.insert(END, new_sample)

    ######################################################################################################
    def check_connection(self):
        try:
            con= pymysql.connect(host='localhost', user='root', password='', db='employee_management_system')
            cur=con.cursor()
            cur.execute("select * from employee_details  ")
            rows=cur.fetchall()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}")
######################################################################################################
    def add(self):
        try:
            if self.month.get() == "" or self.year.get() == "" or self.basicsalary.get() == "" or self.netsalary.get() == "":
                messagebox.showerror("Error", "All Fields are Required")
            else:
                con = pymysql.connect(host='localhost', user='root', password='', db='employee_management_system')
                cur = con.cursor()
                cur.execute("insert into employee_details values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                            self.designation.get(),
                            self.name.get(),
                            self.age.get(),
                            self.gender.get(),
                            self.email.get(),
                            self.hiredlocation.get(),
                            self.txt_address.get('1.0',END),
                            self.doj.get(),
                            self.dob.get(),
                            self.experience.get(),
                            self.proofid.get(),
                            self.contactno.get(),
                            self.status.get(),

                            ############################################
                            self.month.get(),
                            self.year.get(),
                            self.basicsalary.get(),
                            self.totaldays.get(),
                            self.absents.get(),
                            self.medical.get(),
                            self.convence.get(),
                            self.profedence.get(),
                            self.netsalary.get(),
                            self.employeecode.get()+".txt"
                            #101
                       ))
                con.commit()
                con.close()
                file = open("Salary_receipt/" + str(self.employeecode.get())+".txt",'w')
                file.write(self.txt_salaryreceipt.get('1.0',END))
                file.close()

                messagebox.showinfo("Success", "Record has been Successfully Inserted")
                self.clear()
                self.btn_print.config(state=NORMAL)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to:{str(ex)}")


######################################################################################################

    def show(self):
        try:
            con = pymysql.connect(host='localhost', user='root', password='', db='employee_management_system')
            cur = con.cursor()
            cur.execute("Select * from employee_details")
            row = cur.fetchall()
            # print(row)
            self.Employee_tree.delete(*self.Employee_tree.get_children())
            for row in row:
                self.Employee_tree.insert('', END, values=row)
            con.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to:{str(ex)}")

######################################################################################################

    def search(self):
        try:
            con = pymysql.connect(host='localhost', user='root', password='', db='employee_management_system')
            cur = con.cursor()
            cur.execute("Select * from employee_details where employee_ID=%s",(self.employeecode.get()))
            row = cur.fetchone()
            # print(row)
            if row == None:
                messagebox.showerror("Error", "Invalid employeeID, Please try with another Employee ID")
            else:
                #print(row)
                self.employeecode.set(row[0])
                self.designation.set(row[1])
                self.name.set(row[2])
                self.age.set(row[3])
                self.gender.set(row[4])
                self.email.set(row[5])
                self.hiredlocation.set(row[6])
                self.txt_address.delete('1.0',END)
                self.txt_address.insert(END,row[7])
                self.doj.set(row[8])
                self.dob.set(row[9])
                self.experience.set(row[10])
                self.proofid.set(row[11])
                self.contactno.set(row[12])
                self.status.set(row[13])

                ############################################
                self.month.set(row[14])
                self.year.set(row[15])
                self.basicsalary.set(row[16])
                self.totaldays.set(row[17])
                self.absents.set(row[18])
                self.medical.set(row[19])
                self.convence.set(row[20])
                self.profedence.set(row[21])
                self.netsalary.set(row[22])
                file=open('Salary_receipt/'+str(row[23]),'r')
                self.txt_salaryreceipt.delete('1.0',END)
                for i in file:
                    self.txt_salaryreceipt.insert(END,i)
                file.close()

                self.btn_save.config(state=DISABLED)
                self.btn_update.config(state=NORMAL)
                self.btn_delete.config(state=NORMAL)
                self.txt_code.config(state='readonly')


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")

#UPDATE####################################################################################################
    def update(self):
        try:
            con = pymysql.connect(host='localhost', user='root', password='', db='employee_management_system')
            cur = con.cursor()
            cur.execute("Select * from employee_details where employee_ID=%s", (self.employeecode.get()))
            row = cur.fetchone()
            # print(row)
            if row == None:
                messagebox.showerror("Error", "Invalid employeeID, Please try with another Employee ID",parent=self.root)
            else:
                cur.execute('Update employee_details SET designation=%s, name=%s, age=%s, gender=%s, email=%s, hiredlocation=%s, address=%s, doj=%s, dob=%s, experience=%s, proofid=%s,contactno=%s, status=%s, month=%s, year=%s,Basicsalary=%s, totaldays=%s,absents=%s, medical=%s, profidentfund=%s, convence=%s, netsalary=%s, salary_receipt=%s WHERE employee_ID=%s',
                            (self.designation.get(),
                             self.name.get(),
                             self.age.get(),
                             self.gender.get(),
                             self.email.get(),
                             self.hiredlocation.get(),
                             self.txt_address.get('1.0', END),
                             self.doj.get(),
                             self.dob.get(),
                             self.experience.get(),
                             self.proofid.get(),
                             self.contactno.get(),
                             self.status.get(),

                            ############################################
                             self.month.get(),
                             self.year.get(),
                             self.basicsalary.get(),
                             self.totaldays.get(),
                             self.absents.get(),
                             self.medical.get(),
                             self.convence.get(),
                             self.profedence.get(),
                             self.netsalary.get(),
                             self.employeecode.get()+".txt",
                             self.employeecode.get()


                             ))
                con.commit()
                con.close()
                file = open("salary_receipt/"+str(self.employeecode.get())+".txt",'w')
                file.write(self.txt_salaryreceipt.get('1.0',END))
                file.close()

                messagebox.showinfo("Update", "Record has been Successfully Uppdated")
                self.clear()
                self.btn_print.config(state=NORMAL)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to:{str(ex)}")



######################################################################################################
    def clear(self):
        self.btn_save.config(state=NORMAL)
        self.btn_update.config(state=DISABLED)
        self.btn_delete.config(state=DISABLED)
        self.btn_print.config(state=DISABLED)
        self.txt_code.config(state=NORMAL)

        self.employeecode.set("")
        self.designation.set("")
        self.name.set("")
        self.age.set("")
        self.gender.set("")
        self.email.set("")
        self.hiredlocation.set("")
        self.txt_address.delete('1.0',END)
        self.doj.set("")
        self.dob.set("")
        self.experience.set("")
        self.proofid.set("")
        self.contactno.set("")
        self.status.set("")

        ############################################
        self.month.set("")
        self.year.set("")
        self.basicsalary.set("")
        self.totaldays.set("")
        self.absents.set("")
        self.medical.set("")
        self.convence.set("")
        self.profedence.set("")
        self.netsalary.set("")
        self.txt_salaryreceipt.delete('1.0', END)
        self.txt_salaryreceipt.insert(END, self.sample)



######################################################################################################
    def delete(self):
        try:
            con = pymysql.connect(host='localhost', user='root', password='', db='employee_management_system')
            cur = con.cursor()
            cur.execute("Select * from employee_details where employee_ID=%s", (self.employeecode.get()))
            row = cur.fetchall()
            # print(rows)
            if row==None:
                messagebox.showerror("Error","Invalid employeeID, Please try with another employee ID")
            else:
                op=messagebox.askyesno("Confirm","Do you really want to Delete?")
                #print(op)
                if op==True:
                    cur.execute("Delete FROM `employee_details` WHERE employee_ID=%s",(self.employeecode.get()))
                    con.commit()
                    con.close()

                    messagebox.showinfo("Delete", "Employee record Deleted Successfully",parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to:{str(ex)}")

 ###########################################################################################################################

    def logout(self):
        logout= messagebox.askyesno("Employee Payroll Management", "Confirm if you want to exit")
        if logout > 0:
            root.destroy()
            return

 ###################################### EMPLOYEE GRID VIEW OR TREE VIEW ################################################################
    def employee_frame(self):
        self.root2=Toplevel(self.root)
        self.root2.title("Employee Payroll Management System")
        self.root2.geometry("1000x500+120+60")
        self.root2.config(bg="white")
        title=Label(self.root2,text="All Employee Details",font=("times new roman",20,"bold"),fg="white",bg="green",anchor=W).pack(side=TOP,fill=X)
        self.root2.focus_force()
 ######################################################################################################

        scrolly=Scrollbar(self.root2, orient=VERTICAL)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx=Scrollbar(self.root2, orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM, fill=X)

        self.Employee_tree = ttk.Treeview(self.root2,columns=("employee_ID", "designation", "name", "age", "gender",
                                                              "email", "hiredlocation", "address", "doj", "dob",
                                                              "experience", "proofid", "contactus", "status","month",
                                                              "year", "Basicsalary", "totaldays", "absents","medical",
                                                              "profidentfund", "convence", "netsalary","receipt"),yscrollcommand=scrolly.set,
                                                                 xscrollcommand=scrollx.set)


        self.Employee_tree.heading("employee_ID", text="employee_ID")
        self.Employee_tree.heading("designation", text="designation.")
        self.Employee_tree.heading("name", text="name")
        self.Employee_tree.heading("age", text="age")
        self.Employee_tree.heading("gender", text="gender")
        self.Employee_tree.heading("email", text="email")
        self.Employee_tree.heading("hiredlocation", text="hiredlocation")
        self.Employee_tree.heading("address", text="address")
        self.Employee_tree.heading("doj", text="doj")
        self.Employee_tree.heading("dob", text="dob")
        self.Employee_tree.heading("experience", text="experience")
        self.Employee_tree.heading("proofid", text="proofid")
        self.Employee_tree.heading("contactus", text="contactus")
        self.Employee_tree.heading("status", text="status")
        self.Employee_tree.heading("month", text="month")
        self.Employee_tree.heading("year", text="year")
        self.Employee_tree.heading("Basicsalary", text="Basicsalary")
        self.Employee_tree.heading("totaldays", text="totaldays")
        self.Employee_tree.heading("absents", text="absents")
        self.Employee_tree.heading("medical", text="medical")
        self.Employee_tree.heading("profidentfund", text="profidentfund")
        self.Employee_tree.heading("convence", text="convence")
        self.Employee_tree.heading("netsalary", text="netsalary")
        self.Employee_tree.heading("receipt", text="receipt")


        self.Employee_tree["show"] = "headings"

        self.Employee_tree.column("employee_ID", width=100)
        self.Employee_tree.column("designation", width=100)
        self.Employee_tree.column("name", width=100)
        self.Employee_tree.column("age", width=100)
        self.Employee_tree.column("gender", width=100)
        self.Employee_tree.column("email",width=100)
        self.Employee_tree.column("hiredlocation",width=100)
        self.Employee_tree.column("address", width=100)
        self.Employee_tree.column("doj", width=100)
        self.Employee_tree.column("dob", width=100)
        self.Employee_tree.column("experience", width=100)
        self.Employee_tree.column("proofid",width=100)
        self.Employee_tree.column("contactus",width=100)
        self.Employee_tree.column("status", width=100)
        self.Employee_tree.column("month",width=100)
        self.Employee_tree.column("year", width=100)
        self.Employee_tree.column("Basicsalary",width=100)
        self.Employee_tree.column("totaldays",width=100)
        self.Employee_tree.column("absents", width=100)
        self.Employee_tree.column("medical",width=100)
        self.Employee_tree.column("profidentfund", width=100)
        self.Employee_tree.column("convence",width=100)
        self.Employee_tree.column("netsalary",width=100)
        self.Employee_tree.column("receipt", width=100)

        scrollx.config(command=self.Employee_tree.xview)
        scrolly.config(command=self.Employee_tree.yview)
        self.Employee_tree.pack(fill=BOTH, expand=1)
        self.show()

 ###########################################################
    def print(self):
        file = tempfile.mktemp(".txt")
        open(file, "w").write(self.txt_salaryreceipt.get('1.0', END))
        os.startfile(file, 'print')

        self.root2.mainloop()

######################################################################################################

root = Tk()
ob = Payroll(root)
root.mainloop()
