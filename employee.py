from tkinter import*
from tkinter import messagebox,ttk
import pymysql
import time
from pathlib import Path,PureWindowsPath
import os
import tempfile

class EmployeeSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Employee Payroll Management")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        title=Label(root,text="Employee Payroll Management",font=("times new roman",30,"bold"),bg="#262626",fg="white").place(x=0,y=0,relwidth=1.0)
        btn_show_employees=Button(self.root,text="All Employees",command=self.employee_show,font=("times new roman",13),bg="black",fg="white",borderwidth=2).place(x=1150,y=10,height=30,width=120)
        self.emp_code=StringVar()
        self.emp_designation=StringVar()
        self.emp_name=StringVar()
        self.emp_age=StringVar()
        self.emp_dob=StringVar()
        self.emp_doj=StringVar()
        self.emp_experience=StringVar()
        self.emp_gender=StringVar()
        self.emp_proof_id=StringVar()
        self.emp_email=StringVar()
        self.emp_contact_no=StringVar()
        self.emp_hired_location=StringVar()
        self.emp_status=StringVar()
        self.emp_address=StringVar()
        self.answer=bool()

        Frame1=Frame(root,bd=3,relief=RIDGE,bg="white")
        Frame1.place(x=10,y=70,width=750,height=620)

        title2=Label(Frame1,text="Employee Details",font=("times new roman",20),bg="lightgray",fg="black").place(x=0,y=0,relwidth=1.0)
        lbl_code=Label(Frame1,text="Employee Code:",font=("times new roman",20),bg="white",fg="black").place(x=10,y=70)
        self.txt_code=Entry(Frame1,font=("times new roman",15),textvariable=self.emp_code,bg="lightyellow",fg="black")
        self.txt_code.place(x=220,y=75,width=200)
        btn_search=Button(Frame1,text="Search",command=self.search,font=("times new roman",20),bg="white",fg="black").place(x=450,y=73,height=30,width=120)
        self.btn_delete=Button(Frame1,text="Delete",command=self.delete,font=("times new roman",20),bg="white",fg="black")
        self.btn_delete.place(x=580,y=73,height=30,width=120)


        lbl_Designation=Label(Frame1,text="Designation:",font=("times new roman",20),bg="white",fg="black").place(x=10,y=140)
        txt_Designation=Entry(Frame1,font=("times new roman",15),textvariable=self.emp_designation,bg="lightyellow",fg="black").place(x=170,y=145,width=200)
        lbl_Dob=Label(Frame1,text="D.O.B:",font=("times new roman",20),bg="white",fg="black").place(x=390,y=140)
        txt_Dob=Entry(Frame1,font=("times new roman",15),textvariable=self.emp_dob,bg="lightyellow",fg="black").place(x=520,y=145)

        lbl_Name=Label(Frame1,text="Name:",font=("times new roman",20),bg="white",fg="black").place(x=10,y=190)
        txt_Name=Entry(Frame1,font=("times new roman",15),textvariable=self.emp_name,bg="lightyellow",fg="black").place(x=170,y=195,width=200)
        lbl_Doj=Label(Frame1,text="D.O.J:",font=("times new roman",20),bg="white",fg="black").place(x=390,y=190)
        txt_Doj=Entry(Frame1,font=("times new roman",15),textvariable=self.emp_doj,bg="lightyellow",fg="black").place(x=520,y=195)

        lbl_Age=Label(Frame1,text="Age:",font=("times new roman",20),bg="white",fg="black").place(x=10,y=240)
        txt_Age=Entry(Frame1,font=("times new roman",15),textvariable=self.emp_age,bg="lightyellow",fg="black").place(x=170,y=245,width=200)
        lbl_Experience=Label(Frame1,text="Experience:",font=("times new roman",18),bg="white",fg="black").place(x=390,y=240)
        txt_Experience=Entry(Frame1,font=("times new roman",15),textvariable=self.emp_experience,bg="lightyellow",fg="black").place(x=520,y=245)

        lbl_gender=Label(Frame1,text="Gender:",font=("times new roman",20),bg="white",fg="black").place(x=10,y=290)
        txt_gender=Entry(Frame1,font=("times new roman",15),textvariable=self.emp_gender,bg="lightyellow",fg="black").place(x=170,y=295,width=200)
        lbl_proof=Label(Frame1,text="Proof ID:",font=("times new roman",20),bg="white",fg="black").place(x=390,y=290)
        txt_proof=Entry(Frame1,font=("times new roman",15),textvariable=self.emp_proof_id,bg="lightyellow",fg="black").place(x=520,y=295)

        lbl_email=Label(Frame1,text="Email:",font=("times new roman",20),bg="white",fg="black").place(x=10,y=340)
        txt_email=Entry(Frame1,font=("times new roman",15),textvariable=self.emp_email,bg="lightyellow",fg="black").place(x=170,y=345,width=200)
        lbl_contact=Label(Frame1,text="Contact No:",font=("times new roman",18),bg="white",fg="black").place(x=390,y=340)
        txt_contact=Entry(Frame1,font=("times new roman",15),textvariable=self.emp_contact_no,bg="lightyellow",fg="black").place(x=520,y=345)

        lbl_hired=Label(Frame1,text="Hired Location:",font=("times new roman",18),bg="white",fg="black").place(x=10,y=392)
        txt_hired=Entry(Frame1,font=("times new roman",15),textvariable=self.emp_hired_location,bg="lightyellow",fg="black").place(x=170,y=395,width=200)
        lbl_status=Label(Frame1,text="Status",font=("times new roman",20),bg="white",fg="black").place(x=390,y=390)
        txt_status=Entry(Frame1,font=("times new roman",15),textvariable=self.emp_status,bg="lightyellow",fg="black").place(x=520,y=395)

        lbl_address=Label(Frame1,text="Address:",font=("times new roman",18),bg="white",fg="black").place(x=10,y=442)
        self.txt_address=Text(Frame1,font=("times new roman",15),bg="lightyellow",fg="black")
        self.txt_address.place(x=170,y=445,width=555,height=150)

        self.emp_month=StringVar()
        self.emp_year=StringVar()
        self.emp_salary=StringVar()
        self.emp_days=StringVar()
        self.emp_absents=StringVar()
        self.emp_pf=StringVar()
        self.emp_convence=StringVar()
        self.emp_medical=StringVar()
        self.emp_net_salary=StringVar()

        Frame2=Frame(root,bd=3,relief=RIDGE,bg="white")
        Frame2.place(x=770,y=70,width=580,height=300)

        title2=Label(Frame2,text="Employee Salary Details",font=("times new roman",20),bg="lightgray",fg="black").place(x=0,y=0,relwidth=1.0)
        lbl_month=Label(Frame2,text="Month:",font=("times new roman",18),bg="white",fg="black").place(x=10,y=60)
        txt_month=Entry(Frame2,font=("times new roman",15),textvariable=self.emp_month,bg="lightyellow",fg="black").place(x=90,y=65,width=100)
        lbl_year=Label(Frame2,text="Year:",font=("times new roman",18),bg="white",fg="black").place(x=210,y=60)
        txt_year=Entry(Frame2,font=("times new roman",15),textvariable=self.emp_year,bg="lightyellow",fg="black").place(x=270,y=65,width=100)
        lbl_salary=Label(Frame2,text="Salary:",font=("times new roman",18),bg="white",fg="black").place(x=380,y=60)
        txt_salary=Entry(Frame2,font=("times new roman",15),textvariable=self.emp_salary,bg="lightyellow",fg="black").place(x=460,y=65,width=100)

        lbl_Days=Label(Frame2,text="Total Days:",font=("times new roman",18),bg="white",fg="black").place(x=10,y=100)
        txt_Days=Entry(Frame2,font=("times new roman",15),textvariable=self.emp_days,bg="lightyellow",fg="black").place(x=170,y=105,width=120)
        lbl_absent=Label(Frame2,text="Absents:",font=("times new roman",18),bg="white",fg="black").place(x=300,y=100)
        txt_absent=Entry(Frame2,font=("times new roman",15),textvariable=self.emp_absents,bg="lightyellow",fg="black").place(x=420,y=105,width=140)

        lbl_medical=Label(Frame2,text="Medical: ",font=("times new roman",18),bg="white",fg="black").place(x=10,y=150)
        txt_medical=Entry(Frame2,font=("times new roman",15),textvariable=self.emp_medical,bg="lightyellow",fg="black").place(x=170,y=155,width=120)
        lbl_pf=Label(Frame2,text="PF: ",font=("times new roman",18),bg="white",fg="black").place(x=300,y=150)
        txt_pf=Entry(Frame2,font=("times new roman",15),textvariable=self.emp_pf,bg="lightyellow",fg="black").place(x=420,y=155,width=140)

        lbl_convence=Label(Frame2,text="Convence: ",font=("times new roman",18),bg="white",fg="black").place(x=10,y=200)
        txt_convence=Entry(Frame2,font=("times new roman",15),textvariable=self.emp_convence,bg="lightyellow",fg="black").place(x=170,y=205,width=120)
        lbl_netsalary=Label(Frame2,text="Net Salary: ",font=("times new roman",18),bg="white",fg="black").place(x=300,y=200)
        txt_netsalary=Entry(Frame2,state="readonly",font=("times new roman",15),textvariable=self.emp_net_salary,bg="lightyellow",fg="black").place(x=420,y=205,width=140)

        btn_calculate=Button(Frame2,text="Calculate",command=self.calculate,font=("times new roman",20),bg="white",fg="black").place(x=150,y=250,height=30,width=120)
        self.btn_save=Button(Frame2,text="Save",command=self.add,font=("times new roman",20),bg="white",fg="black")
        self.btn_save.place(x=280,y=250,height=30,width=120)
        btn_clear=Button(Frame2,text="Clear",command=self.clear,font=("times new roman",20),bg="white",fg="black").place(x=410,y=250,height=30,width=120)
        self.btn_update=Button(Frame2,text="Update",command=self.update,font=("times new roman",20),bg="white",fg="black")
        self.btn_update.place(x=20,y=250,height=30,width=120)


        Frame3=Frame(root,bd=3,relief=RIDGE,bg="white")
        Frame3.place(x=770,y=380,width=580,height=310)

        self.var_text=StringVar()
        self.var_operator=''
        def btn_click(num):
            self.var_operator=self.var_operator+str(num)
            self.var_text.set(self.var_operator)

        def result():
            res=str(eval(self.var_operator))
            self.var_text.set(res)
            self.var_operator=''

        def clear_cal():
            self.var_text.set('')
            self.var_operator=''
            
        Cal_Frame=Frame(Frame3,bg="white",bd=2,relief=RIDGE)
        Cal_Frame.place(x=2,y=2,width=246,height=300)

        txt_result=Entry(Cal_Frame,bg="white",state="readonly",textvariable=self.var_text,font=("times new roman",25,"bold"),justify=RIGHT).place(x=0,y=0,relwidth=1.0,height=57)

        btn_7=Button(Cal_Frame,text="7",command=lambda:btn_click(7),font=("times new roman",15,"bold")).place(x=0,y=57,w=60,h=60)
        btn_8=Button(Cal_Frame,text="8",command=lambda:btn_click(8),font=("times new roman",15,"bold")).place(x=61,y=57,w=60,h=60)
        btn_9=Button(Cal_Frame,text="9",command=lambda:btn_click(9),font=("times new roman",15,"bold")).place(x=122,y=57,w=60,h=60)
        btn_d=Button(Cal_Frame,text="/",command=lambda:btn_click('/'),font=("times new roman",15,"bold")).place(x=183,y=57,w=60,h=60)

        btn_4=Button(Cal_Frame,text="4",command=lambda:btn_click(4),font=("times new roman",15,"bold")).place(x=0,y=117,w=60,h=60)
        btn_5=Button(Cal_Frame,text="5",command=lambda:btn_click(5),font=("times new roman",15,"bold")).place(x=61,y=117,w=60,h=60)
        btn_6=Button(Cal_Frame,text="6",command=lambda:btn_click(6),font=("times new roman",15,"bold")).place(x=122,y=117,w=60,h=60)
        btn_m=Button(Cal_Frame,text="*",command=lambda:btn_click('*'),font=("times new roman",15,"bold")).place(x=183,y=117,w=60,h=60)

        btn_1=Button(Cal_Frame,text="1",command=lambda:btn_click(1),font=("times new roman",15,"bold")).place(x=0,y=177,w=60,h=60)
        btn_2=Button(Cal_Frame,text="2",command=lambda:btn_click(2),font=("times new roman",15,"bold")).place(x=61,y=177,w=60,h=60)
        btn_3=Button(Cal_Frame,text="3",command=lambda:btn_click(3),font=("times new roman",15,"bold")).place(x=122,y=177,w=60,h=60)
        btn_s=Button(Cal_Frame,text="-",command=lambda:btn_click('-'),font=("times new roman",15,"bold")).place(x=183,y=177,w=60,h=60)

        btn_f=Button(Cal_Frame,text="C",command=clear_cal,font=("times new roman",15,"bold")).place(x=0,y=237,w=60,h=60)
        btn_0=Button(Cal_Frame,text="0",command=lambda:btn_click(0),font=("times new roman",15,"bold")).place(x=61,y=237,w=60,h=60)
        btn_a=Button(Cal_Frame,text="+",command=lambda:btn_click('+'),font=("times new roman",15,"bold")).place(x=122,y=237,w=60,h=60)
        btn_e=Button(Cal_Frame,text="=",command=result,font=("times new roman",15,"bold")).place(x=183,y=237,w=60,h=60)

        sal_Frame=Frame(Frame3,bg="white",bd=2,relief=RIDGE)
        sal_Frame.place(x=250,y=2,width=320,height=300)

        title_sal=Label(sal_Frame,text="Salary Receipt",font=("times new roman",20),bg="lightgray",fg="black").place(x=0,y=0,relwidth=1.0)

        self.sample=f'''\tCompany Name, XYZ\n\tAddress: Xyz, Floor4
------------------------------------------------
Employee ID\t\t:  1024
Salary Of\t\t:  Mon-YYYY
Generated On\t\t:  DD-MM-YYYY
------------------------------------------------
Total Days\t\t:  DD
Total Present\t\t:  DD
Total Absent\t\t:  DD
Convence\t\t:  Rs.----
Medical\t\t:  Rs.----
PF\t\t:  Rs.----
Gross Payment\t\t:  Rs.------
Net Salary\t\t:  Rs.------
------------------------------------------------
This is computer generated slip, not
required any signature
'''

        sal_Frame2=Frame(sal_Frame,bg="white",bd=2,relief=RIDGE)
        sal_Frame2.place(x=0,y=30,relwidth=1,height=230)

        scroll_y=Scrollbar(sal_Frame2,orient=VERTICAL)
        scroll_y.pack(fill=Y,side=RIGHT)

        self.txt_salary_receipt=Text(sal_Frame2,font=("times new roman",13),bg="lightyellow",yscrollcommand=scroll_y.set)
        self.txt_salary_receipt.pack(fill=BOTH,expand=1)
        scroll_y.config(command=self.txt_salary_receipt.yview)
        self.txt_salary_receipt.insert(END,self.sample)

        btn_print=Button(sal_Frame,text="Print",command=self.print,font=("times new roman",20),bg="white",fg="black").place(x=175,y=263,height=30,width=120)

        self.check_connection()

    def clear(self):
        self.emp_code.set('')
        self.emp_designation.set('')
        self.emp_name.set('')
        self.emp_age.set('')
        self.emp_gender.set('')
        self.emp_email.set('')
        self.emp_hired_location.set('')
        self.emp_doj.set('')
        self.emp_dob.set('')
        self.emp_experience.set('')
        self.emp_proof_id.set('')
        self.emp_contact_no.set('')
        self.emp_status.set('')
        self.txt_address.delete('1.0', END)
        self.emp_month.set('')
        self.emp_year.set('')
        self.emp_salary.set('')
        self.emp_days.set('')
        self.emp_absents.set('')
        self.emp_medical.set('')
        self.emp_pf.set('')
        self.emp_convence.set('')
        self.emp_net_salary.set('')
        self.txt_salary_receipt.delete('1.0', END)
        self.txt_salary_receipt.insert(END,self.sample)

    def delete(self):
        if self.emp_code.get()=='':
            messagebox.showerror('Error','Employee ID must be required')
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',db='ems')
                cur=con.cursor()
                cur.execute('select * from emp_salary where e_code=%s',(self.emp_code.get()))
                rows=cur.fetchone()
                if rows==None:
                    messagebox.showerror("Error","Invalid Employee ID, please try with another ID")
                else:
                    self.answer=messagebox.askyesno("Confirmation","Do you really want to delete?")
                    if self.answer:
                        cur.execute('delete from emp_salary where e_code=%s',(self.emp_code.get()))
                        con.commit()
                        con.close()
                        messagebox.showinfo('Successful','Employee details has been deleted')
                        self.clear()
            except Exception as ex:
                    messagebox.showerror("Error",f"Error due to {str(ex)}")

    def search(self):
        try:
            con=pymysql.connect(host='localhost',user='root',password='',db='ems')
            cur=con.cursor()
            cur.execute('select * from emp_salary where e_code=%s',(self.emp_code.get()))
            rows=cur.fetchone()
            if rows==None:
                messagebox.showerror("Error","Invalid Employee ID, please try with another ID")
            else:
                self.emp_code.set(rows[0])
                self.emp_designation.set(rows[1])
                self.emp_name.set(rows[2])
                self.emp_age.set(rows[3])
                self.emp_gender.set(rows[4])
                self.emp_email.set(rows[5])
                self.emp_hired_location.set(rows[6])
                self.emp_doj.set(rows[7])
                self.emp_dob.set(rows[8])
                self.emp_experience.set(rows[9])
                self.emp_proof_id.set(rows[10])
                self.emp_contact_no.set(rows[11])
                self.emp_status.set(rows[12])
                self.txt_address.delete('1.0', END)
                self.txt_address.insert(END,rows[13])
                self.emp_month.set(rows[14])
                self.emp_year.set(rows[15])
                str(self.emp_salary.set(rows[16]))
                str(self.emp_days.set(rows[17]))
                str(self.emp_absents.set(rows[18]))
                str(self.emp_medical.set(rows[19]))
                str(self.emp_pf.set(rows[20]))
                str(self.emp_convence.set(rows[21]))
                str(self.emp_net_salary.set(rows[22]))
                self.file_path=os.path.join('Salary_receipt',str(rows[23]))
                file_=open(self.file_path,'r')
                (self.txt_salary_receipt.delete('1.0',END))
                for i in file_:
                    self.txt_salary_receipt.insert(END,i)
                file_.close()
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to {str(ex)}")

    def add(self):
        if self.emp_code.get()=='' or self.emp_designation.get()=='' or self.emp_name.get()=='' or self.emp_age.get()=='' or self.emp_dob.get()=='' or self.emp_doj.get()=='' or self.emp_experience.get()=='' or self.emp_gender.get()=='' or self.emp_proof_id.get()=='' or self.emp_email.get()=='' or self.emp_contact_no.get()=='' or self.emp_hired_location.get()=='' or self.emp_status.get()=='' or self.txt_address.get('1.0',END)=='' or self.emp_month.get()=='' or self.emp_year.get()=='' or self.emp_salary.get()=='' or self.emp_days.get()=='' or self.emp_absents.get()=='' or self.emp_pf.get()=='' or self.emp_convence.get()=='' or self.emp_medical.get()=='':
            messagebox.showerror('Error','All Fields Required')
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',db='ems')
                cur=con.cursor()
                cur.execute('select * from emp_salary where e_code=%s',(self.emp_code.get()))
                rows=cur.fetchone()
                if rows!=None:
                    messagebox.showerror("Error","This ID is already present")
                else:
                    cur.execute("""
    INSERT INTO emp_salary (
        e_code, designation, name, age, gender, email,
        hr_location, doj, dob, experience, proof_id,
        contact_no, status, address, month, year, basic_salary,
        total_days, absent_days, medical, pf, convence, net_salary, salary_receipt
    ) VALUES (
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
    )
""", (
    self.emp_code.get(),
    self.emp_designation.get(),
    self.emp_name.get(),
    self.emp_age.get(),
    self.emp_gender.get(),
    self.emp_email.get(),
    self.emp_hired_location.get(),
    self.emp_doj.get(),
    self.emp_dob.get(),
    self.emp_experience.get(),
    self.emp_proof_id.get(),
    self.emp_contact_no.get(),
    self.emp_status.get(),
    self.txt_address.get('1.0', END),
    self.emp_month.get(),
    self.emp_year.get(),
    int(self.emp_salary.get()),
    self.emp_days.get(),
    self.emp_absents.get(),
    self.emp_medical.get(),
    self.emp_pf.get(),
    self.emp_convence.get(),
    self.emp_net_salary.get(),
    self.emp_code.get()+".txt",
))
                    
                    con.commit()
                    con.close()
                    file_=open('Salary_receipt\\'+str(self.emp_code.get())+".txt",'w')
                    file_.write(self.txt_salary_receipt.get('1.0',END))
                    file_.close()
                    messagebox.showinfo("Success","Record Added Successfully!")
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to {str(ex)}")
    
    def update(self):
        if self.emp_code.get()=='' or self.emp_designation.get()=='' or self.emp_name.get()=='' or self.emp_age.get()=='' or self.emp_dob.get()=='' or self.emp_doj.get()=='' or self.emp_experience.get()=='' or self.emp_gender.get()=='' or self.emp_proof_id.get()=='' or self.emp_email.get()=='' or self.emp_contact_no.get()=='' or self.emp_hired_location.get()=='' or self.emp_status.get()=='' or self.txt_address.get('1.0',END)=='' or self.emp_month.get()=='' or self.emp_year.get()=='' or self.emp_salary.get()=='' or self.emp_days.get()=='' or self.emp_absents.get()=='' or self.emp_pf.get()=='' or self.emp_convence.get()=='' or self.emp_medical.get()=='':
            messagebox.showerror('Error','All Fields Required')
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',db='ems')
                cur=con.cursor()
                cur.execute('select * from emp_salary where e_code=%s',(self.emp_code.get()))
                rows=cur.fetchone()
                if rows==None:
                    messagebox.showerror("Error","This ID is Invalid")
                else:
                    cur.execute("""UPDATE emp_salary 
               SET designation=%s, name=%s, age=%s, gender=%s, email=%s, hr_location=%s, doj=%s, dob=%s, experience=%s, proof_id=%s, contact_no=%s, status=%s, address=%s, month=%s, year=%s, basic_salary=%s, total_days=%s, absent_days=%s, medical=%s, pf=%s, convence=%s, net_salary=%s, salary_receipt=%s 
               WHERE e_code=%s""",
              (self.emp_designation.get(),
               self.emp_name.get(),
               self.emp_age.get(),
               self.emp_gender.get(),
               self.emp_email.get(),
               self.emp_hired_location.get(),
               self.emp_doj.get(),
               self.emp_dob.get(),
               self.emp_experience.get(),
               self.emp_proof_id.get(),
               self.emp_contact_no.get(),
               self.emp_status.get(),
               self.txt_address.get('1.0', END),
               self.emp_month.get(),
               self.emp_year.get(),
               int(self.emp_salary.get()),
               self.emp_days.get(),
               self.emp_absents.get(),
               self.emp_medical.get(),
               self.emp_pf.get(),
               self.emp_convence.get(),
               self.emp_net_salary.get(),
               self.emp_code.get() + ".txt",
               self.emp_code.get()))

                    
                    con.commit()
                    con.close()
                    self.file_path=os.path.join('Salary_receipt',str(self.emp_code.get())+".txt")
                    file_=open(self.file_path,'w')
                    file_.write(self.txt_salary_receipt.get('1.0',END))
                    file_.close()
                    messagebox.showinfo("Success","Record Updated Successfully!")
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to {str(ex)}")

    def calculate(self):
        if self.emp_month.get()=="" or self.emp_year.get()=="" or self.emp_salary.get()=="" or self.emp_days.get=="" or self.emp_absents.get()=="" or self.emp_pf.get()=="" or self.emp_convence.get()=="" or self.emp_medical.get()=="":
            messagebox.showerror('Error','All Fields Required')
        else:
            per_day=int(self.emp_salary.get())/int(self.emp_days.get())
            work_day=int(self.emp_days.get())-int(self.emp_absents.get())
            sal_=per_day*work_day
            deduct=int(self.emp_medical.get())+int(self.emp_pf.get())
            addition=int(self.emp_convence.get())
            net_sal=sal_-deduct+addition
            self.emp_net_salary.set(str(round(net_sal,2)))

            new_sample=f'''\tCompany Name, XYZ\n\tAddress: Xyz, Floor4
------------------------------------------------
Employee ID\t\t:  {self.emp_code.get()}
Salary Of\t\t:  {self.emp_month.get()}-{self.emp_year.get()}
Generated On\t\t:  {str(time.strftime("%d-%m-%Y"))}
------------------------------------------------
Total Days\t\t:  {self.emp_days.get()}
Total Present\t\t:  {str(work_day)}
Total Absent\t\t:  {self.emp_absents.get()}
Convence\t\t:  Rs.{self.emp_convence.get()}
Medical\t\t:  Rs.{self.emp_medical.get()}
PF\t\t:  Rs.{self.emp_pf.get()}
Gross Payment\t\t:  Rs.{self.emp_salary.get()}
Net Salary\t\t:  Rs.{self.emp_net_salary.get()}
------------------------------------------------
This is computer generated slip, not
required any signature
'''
            self.txt_salary_receipt.delete('1.0',END)
            self.txt_salary_receipt.insert(END,new_sample)

    
    def employee_show(self):
        self.root2=Toplevel(self.root)
        self.root2.title("Employee Payroll Management")
        self.root2.geometry("1000x600+120+80")
        self.root2.config(bg="white")
        title=Label(self.root2,text="All Employee Details",font=("times new roman",30,"bold"),bg="#262626",fg="white").place(x=0,y=0,relwidth=1.0)
        self.root2.focus_force()
        scrolly=Scrollbar(self.root2,orient=VERTICAL)
        scrollx=Scrollbar(self.root2,orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        self.employee_tree=ttk.Treeview(self.root2,columns=('e_code', 'designation', 'name', 'age', 'gender', 'email', 'hr_location', 'doj', 'dob', 'experience', 'proof_id', 'contact_no', 'status', 'address', 'month', 'year', 'basic_salary', 'total_days', 'absent_days', 'medical', 'pf', 'convence', 'net_salary', 'salary_receipt'),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        self.employee_tree.heading('e_code',text="E ID")
        self.employee_tree.heading('designation',text="Designation")
        self.employee_tree.heading('name',text='Name')
        self.employee_tree.heading('age',text="Age")
        self.employee_tree.heading('gender',text="Gender")
        self.employee_tree.heading('email',text="Email ID")
        self.employee_tree.heading('hr_location',text="Hired Location")
        self.employee_tree.heading('doj',text="Date of Join")
        self.employee_tree.heading('dob',text="Date of Birth")
        self.employee_tree.heading('experience',text="Experience")
        self.employee_tree.heading('proof_id',text="Proof ID")
        self.employee_tree.heading('contact_no',text="Contact")
        self.employee_tree.heading('status',text="Status")
        self.employee_tree.heading('address',text="Address")
        self.employee_tree.heading('month',text="Month")
        self.employee_tree.heading('year',text="Year")
        self.employee_tree.heading('basic_salary',text="Basic Salary")
        self.employee_tree.heading('total_days',text="Total Days")
        self.employee_tree.heading('absent_days',text="Absent Days")
        self.employee_tree.heading('medical',text="Medical")
        self.employee_tree.heading('pf',text="PF")
        self.employee_tree.heading('convence',text="Convence")
        self.employee_tree.heading('net_salary',text="Net Salary")
        self.employee_tree.heading('salary_receipt',text="Salary Receipt")

        self.employee_tree['show']='headings'

        self.employee_tree.column('e_code',width=50)
        self.employee_tree.column('designation',width=100)
        self.employee_tree.column('name',width=100)
        self.employee_tree.column('age',width=100)
        self.employee_tree.column('gender',width=100)
        self.employee_tree.column('email',width=100)
        self.employee_tree.column('hr_location',width=100)
        self.employee_tree.column('doj',width=100)
        self.employee_tree.column('dob',width=100)
        self.employee_tree.column('experience',width=100)
        self.employee_tree.column('proof_id',width=100)
        self.employee_tree.column('contact_no',width=100)
        self.employee_tree.column('status',width=100)
        self.employee_tree.column('address',width=500)
        self.employee_tree.column('month',width=50)
        self.employee_tree.column('year',width=50)
        self.employee_tree.column('basic_salary',width=100)
        self.employee_tree.column('total_days',width=50)
        self.employee_tree.column('absent_days',width=50)
        self.employee_tree.column('medical',width=100)
        self.employee_tree.column('pf',width=100)
        self.employee_tree.column('convence',width=100)
        self.employee_tree.column('net_salary',width=100)
        self.employee_tree.column('salary_receipt',width=100)
        scrollx.config(command=self.employee_tree.xview)
        scrolly.config(command=self.employee_tree.yview)
        self.employee_tree.pack(fill=BOTH,expand=1)
        self.show()
        self.root2.mainloop()

    def show(self):
        try:
            con=pymysql.connect(host='localhost',user='root',password='',db='ems')
            cur=con.cursor()
            cur.execute('select * from emp_salary')
            rows=cur.fetchall()
            #print(rows)
            self.employee_tree.delete(*self.employee_tree.get_children())
            for row in rows:
                self.employee_tree.insert('',END,values=row)
            con.close()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def print(self):
        file_ =tempfile.mktemp(".txt")
        open(file_,'w').write(self.txt_salary_receipt.get('1.0',END))
        os.startfile(file_,'print')

    def check_connection(self):
        try:
            con=pymysql.connect(host='localhost',user='root',password='',db='ems')
            cur=con.cursor()
            cur.execute('select * from emp_salary')
            rows=cur.fetchall()
            #print(rows)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
        
root=Tk()
obj=EmployeeSystem(root)
root.mainloop()