import random
import time
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import mysql.connector


def main():
       root = Tk()
       app = Login1(root)
       root.mainloop()

class Login1:
    def __init__(self, master):
        self.master = master
        self.master.title("MedicareHub")
        self.master.geometry('1350x750+0+0')

        self.frame = Frame(self.master)
        self.frame.pack()

        self.Username  = StringVar()
        self.Password = StringVar()

        self.LabelTitle = Label(self.frame, text="       MedicareHub System       ", font=("cambria", 40, "bold"),
                                bd=10,bg = "#789e9e", relief="sunken")
        self.LabelTitle.grid(row=0, column=0, columnspan=2, pady=20)

        self.Loginframe1 = Frame(self.frame, width = 1000, height = 300, bd = 10,bg = "#789e9e",  relief="groove")
        self.Loginframe1.grid(row=1, column = 0)

        self.Loginframe2 = Frame(self.frame, width = 1000, height = 100, bd = 10,bg = "#789e9e", relief="groove")
        self.Loginframe2.grid(row=2, column = 0, pady = 15)

        self.Loginframe3 = Frame(self.frame, width = 1000, height = 200, bd = 10,bg = "#789e9e", relief="groove")
        self.Loginframe3.grid(row=6, column = 0, pady = 5)

        self.button_reg = Button(self.Loginframe3, text = "Patients System",state = DISABLED, font = ("cambria", 15, "bold"), bg = "#ff9966",command = self.Registration_window)
        self.button_reg.grid(row=0, column = 0, padx = 10, pady = 10)

        self.button_Hosp = Button(self.Loginframe3, text = "Hospital System ",state = DISABLED, font = ("cambria", 15, "bold"),  bg = "#ff9966",command = self.Hospital_window)
        self.button_Hosp.grid(row=0, column = 1, padx = 10, pady = 10)

        self.button_Dr_appt = Button(self.Loginframe3, text = "Dr Appointment System",state = DISABLED, font = ("cambria", 15, "bold"),  bg = "#ff9966",command = self.Dr_Apoint_window)
        self.button_Dr_appt.grid(row=1, column = 0, padx = 10, pady = 10)
       
        self.button_med_stock = Button(self.Loginframe3, text = "Medicine Stock",state = DISABLED, font = ("cambria", 15, "bold"), bg = "#ff9966", command = self.Medicine_stock)
        self.button_med_stock.grid(row=1, column = 1, padx = 10, pady = 10)


#Now we will create a username and passwordframe
        
        self.LabelUsername = Label(self.Loginframe1, text = "User Name", font = ("cambria", 20, "bold"), bd = 3)
        self.LabelUsername.grid(row=0, column = 0)


        self.textUsername = Entry(self.Loginframe1, font = ("cambria", 20, "bold"), bd = 3, textvariable = self.Username)
        self.textUsername.grid(row=0, column = 1, padx = 40, pady = 15)


        self.LabelPassword = Label(self.Loginframe1, text = "Password", font = ("cambria", 20, "bold"), bd = 3)
        self.LabelPassword.grid(row=1, column = 0)

        
        self.textPassword = Entry(self.Loginframe1, font = ("cambria", 20, "bold"),show = "*", bd = 3, textvariable = self.Password)
        self.textPassword.grid(row=1, column = 1, padx = 40, pady = 15)


        self.button_login = Button(self.Loginframe2, text = "Login", width = 20, font = ("cambria", 18, "bold"), bg = "#ff9966", command = self.login_system)
        self.button_login.grid(row=0, column=0, padx = 10, pady = 10)

        self.button_Reset = Button(self.Loginframe2, text = "Reset", width = 20, font = ("cambria", 18, "bold"),  bg = "#ff9966",command = self.reset_btn)
        self.button_Reset.grid(row=0, column=3, padx = 10, pady = 10)

        self.button_Exit = Button(self.Loginframe2, text = "Exit", width = 20, font = ("cambria", 18, "bold"),  bg = "#ff9966",command = self.Exit_btn)
        self.button_Exit.grid(row=0, column=6, padx = 10, pady = 10)

    def login_system(self):
        user = self.Username.get()
        pswd = self.Password.get()

        if(user == str("medicare") and (pswd == str("Hub"))):
            self.button_reg.config(state = NORMAL)
            self.button_Hosp.config(state = NORMAL)
            self.button_Dr_appt.config(state = NORMAL)
            self.button_med_stock.config(state = NORMAL)
        else:
            tkinter.messagebox.askyesno("MedicareHub", "You have entered an invalid user name or password")
            self.button_reg.config(state = DISABLED)
            self.button_Hosp.config(state = DISABLED)
            self.button_Dr_appt.config(state = DISABLED)
            self.button_med_stock.config(state = DISABLED)


            self.Username.set("")
            self.Password.set("")
            self.textUsername.focus()

    def reset_btn(self):
       self.button_reg.config(state = DISABLED)
       self.button_Hosp.config(state = DISABLED)
       self.button_Dr_appt.config(state = DISABLED)
       self.button_med_stock.config(state = DISABLED)

       self.Username.set("")
       self.Password.set("")
       self.textUsername.focus()

    def Exit_btn(self):
       self.Exit_btn = tkinter.messagebox.askyesno("MedicareHub", "Are you sure you want to exit?")
       if self.Exit_btn > 0:
              self.master.destroy()
              return

       #first we will define all our window
        
    def Registration_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Registration(self.newWindow)


    def Hospital_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Hospital(self.newWindow)


    def Dr_Apoint_window(self):
        self.newWindow = Toplevel(self.master)
        self.app =  Doctor(self.newWindow)


    def Medicine_stock(self):
        self.newWindow = Toplevel(self.master)
        self.app = Medicine(self.newWindow)


class Registration:
    def __init__(self, root):
        self.root = root
        self.root.title("Patient Registration System")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background="black")
        
        # Define variables at the class level
        self.Date_of_Registration = StringVar()
        self.Date_of_Registration.set(time.strftime("%d/%m/%y"))
        self.Ref = StringVar()
        self.Mobile_no = StringVar()
        self.Pincode = StringVar()
        self.Address = StringVar()
        self.Firstname = StringVar()
        self.Lastname = StringVar()
        self.var1 = StringVar()
        self.var2 = StringVar()
        self.var3 = StringVar()
        self.var4 = StringVar()
        self.var5 = IntVar()
        self.Membership = StringVar()
        self.Membership.set("0")
        
        self.connection = mysql.connector.connect(
              host="localhost",
              user="root",
              password="Nilu@07_",
              database="patients")
        
        self.cursor = self.connection.cursor()

        print("Connection established: ", self.connection)

        def insert_data(self):
            registration_date = self.Date_of_Registration.get()
            reference_id = self.Ref.get()
            first_name = self.Firstname.get()
            last_name = self.Lastname.get()
            mobile_no = self.Mobile_no.get()
            address = self.Address.get()
            pincode = self.Pincode.get()
            gender = self.var4.get()  # Use self.var4 instead of member_gendercmb
            membership = self.Membership.get()

            insert_query = "INSERT INTO patients.patientregistration (registration_date, reference_id, first_name, last_name, mobile_no, address, pincode, gender, membership) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            data = (registration_date, reference_id, first_name, last_name, mobile_no, address, pincode, gender, membership)

            self.cursor.execute(insert_query, data)
            self.connection.commit()

            tkinter.messagebox.showinfo("Success", "Data inserted into database successfully!")

        def exitbtn():
            exitbtn = tkinter.messagebox.askyesno("Member Registration Form", "Are you sure you want to exit?")
            if exitbtn > 0:
                root.destroy()
                return

        def resetbtn():
            self.Firstname.set("")
            self.Ref.set("")
            self.Mobile_no.set("")
            self.Pincode.set("")
            self.Address.set("")
            self.Lastname.set("") 
            self.var1.set("")
            self.var3.set("")
            self.var4.set("")
            self.var5.set("")
            self.Membership.set("0")
            member_gendercmb.current(0)
            member_id_proofcmb.current(0)
            member_memtypecmb.current(0)
            member_paymentwithcmb.current(0)
            member_membershiptxt.configure(state=DISABLED)

        def reeesetbtn():
            reeesetbtn = tkinter.messagebox.askokcancel("Member Registration Form ", "You want to add a new Record." )
            if reeesetbtn > 0:
                resetbtn()
            elif reeesetbtn <= 0:
                resetbtn()
                self.detail_text.delete("1.0", END)
                return

        def Reference_number():
            ranumber = random.randint(10000, 999999)
            randomnumber = str(ranumber)
            self.Ref.set(randomnumber)

        def membership_fees():
            if self.var5.get() == 1:
                member_membershiptxt.configure(state=NORMAL)
                item = float(15000)
                self.Membership.set(str(item)+ "Rs")
            elif self.var5.get() == 0:
                member_membershiptxt.configure(state=DISABLED)
                self.Membership.set("0")

        def Receipt():
            Reference_number()
            insert_data(self)
            self.detail_text.insert(END, f"{self.Date_of_Registration.get()}\t{self.Ref.get()}\t{self.Firstname.get()}\t{self.Lastname.get()}\t{self.Mobile_no.get()}\t{self.Address.get()}\t{self.Pincode.get()}\t{member_gendercmb.get()}\t{self.Membership.get()}\n")


        ############################ Title #############################
        title = Label(self.root, text="Member Registration Form", font=("monotype corsiva", 30, "bold"), bd=5,
                      relief=GROOVE, bg="#E6005C", fg="#000000")
        title.pack(side=TOP, fill=X)

        ################# member frame #################

        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#001a66")
        Manage_Frame.place(x=20, y=100, width=470, height=680)

        ############# text, label, ##########################
        Cus_title = Label(Manage_Frame, text="Customer Details", font=("cambria", 20, "bold"), bg="#001a66", fg="white")
        Cus_title.grid(row=0, columnspan=2, pady=5)

        member_datelbl = Label(Manage_Frame, text="Date", font=("cambria", 15, "bold"), bg="#001a66", fg="white")
        member_datelbl.grid(row=1, column=0, pady=5, padx=10, sticky="w")

        member_datetxt = Entry(Manage_Frame, font=("cambria", 15, "bold"), textvariable=self.Date_of_Registration)
        member_datetxt.grid(row=1, column=1, pady=5, padx=10, sticky="w")

        member_reflbl = Label(Manage_Frame, text="Reference ID", font=("cambria", 15, "bold"), bg="#001a66", fg="white")
        member_reflbl.grid(row=2, column=0, pady=5, padx=10, sticky="w")

        member_reftxt = Entry(Manage_Frame, font=("cambria", 15, "bold"), state=DISABLED, text=self.Ref)
        member_reftxt.grid(row=2, column=1, pady=5, padx=10, sticky="w")

        member_fnamelbl = Label(Manage_Frame, text="First Name", font=("cambria", 15, "bold"), bg="#001a66", fg="white")
        member_fnamelbl.grid(row=3, column=0, pady=5, padx=10, sticky="w")

        member_fnametxt = Entry(Manage_Frame, font=("cambria", 15, "bold"), textvariable=self.Firstname)
        member_fnametxt.grid(row=3, column=1, pady=5, padx=10, sticky="w")

        member_lnamelbl = Label(Manage_Frame, text="Last Name", font=("cambria", 15, "bold"), bg="#001a66", fg="white")
        member_lnamelbl.grid(row=4, column=0, pady=5, padx=10, sticky="w")

        member_lnametxt = Entry(Manage_Frame, font=("cambria", 15, "bold"), textvariable=self.Lastname)
        member_lnametxt.grid(row=4, column=1, pady=5, padx=10, sticky="w")

        member_mobilelbl = Label(Manage_Frame, text="Mobile No", font=("cambria", 15, "bold"), bg="#001a66", fg="white")
        member_mobilelbl.grid(row=5, column=0, pady=5, padx=10, sticky="w")

        member_mobiletxt = Entry(Manage_Frame, font=("cambria", 15, "bold"), textvariable=self.Mobile_no)
        member_mobiletxt.grid(row=5, column=1, pady=5, padx=10, sticky="w")

        member_addresslbl = Label(Manage_Frame, text="Address", font=("cambria", 15, "bold"), bg="#001a66", fg="white")
        member_addresslbl.grid(row=6, column=0, pady=5, padx=10, sticky="w")

        member_addresstxt = Entry(Manage_Frame, font=("cambria", 15, "bold"), textvariable=self.Address)
        member_addresstxt.grid(row=6, column=1, pady=5, padx=10, sticky="w")

        member_pincodelbl = Label(Manage_Frame, text="Pincode", font=("cambria", 15, "bold"), bg="#001a66", fg="white")
        member_pincodelbl.grid(row=7, column=0, pady=5, padx=10, sticky="w")

        member_pincodetxt = Entry(Manage_Frame, font=("cambria", 15, "bold"), textvariable=self.Pincode)
        member_pincodetxt.grid(row=7, column=1, pady=5, padx=10, sticky="w")

        member_genderlbl = Label(Manage_Frame, text="Gender", font=("cambria", 15, "bold"), bg="#001a66", fg="white")
        member_genderlbl.grid(row=8, column=0, pady=5, padx=10, sticky="w")

        member_gendercmb = ttk.Combobox(Manage_Frame, text=self.var4, state="readonly", font=("cambria", 15, "bold"), width=19)
        member_gendercmb['values'] = ("", "Male", "Female", "Other")
        member_gendercmb.current(0)
        member_gendercmb.grid(row=8, column=1, pady=5, padx=10, sticky="w")

        member_id_prooflbl = Label(Manage_Frame, text="ID Proof", font=("cambria", 15, "bold"), bg="#001a66", fg="white")
        member_id_prooflbl.grid(row=9, column=0, pady=5, padx=10, sticky="w")

        member_id_proofcmb = ttk.Combobox(Manage_Frame, text=self.var3, state="readonly", font=("cambria", 15, "bold"), width=19)
        member_id_proofcmb['values'] = ("", "Adhaar Card", "Passport", "Driving License", "Pan card", "Student ID")
        member_id_proofcmb.current(0)
        member_id_proofcmb.grid(row=9, column=1, pady=5, padx=10, sticky="w")

        member_memtypelbl = Label(Manage_Frame, text="Member Type", font=("cambria", 15, "bold"), bg="#001a66", fg="white")
        member_memtypelbl.grid(row=10, column=0, pady=5, padx=10, sticky="w")

        member_memtypecmb = ttk.Combobox(Manage_Frame, text=self.var2, state="readonly", font=("cambria", 15, "bold"), width=19)
        member_memtypecmb['values'] = ("", "Ayushman Card", "Insurance", "Pay Immediately", "Pay at a leaving")
        member_memtypecmb.current(0)
        member_memtypecmb.grid(row=10, column=1, pady=5, padx=10, sticky="w")

        member_paymentwithlbl = Label(Manage_Frame, text="Payment", font=("cambria", 15, "bold"), bg="#001a66", fg="white")
        member_paymentwithlbl.grid(row=11, column=0, pady=5, padx=10, sticky="w")

        member_paymentwithcmb = ttk.Combobox(Manage_Frame, text=self.var1, state="readonly", font=("cambria", 15, "bold"), width=19)
        member_paymentwithcmb['values'] = ("", "Cash", "Debit Card - Rupay", "Debit Card - Visa", "Card - Mastercard", "Credit Card", "Phonepe", "GooglePay", "Paytm", "Net-Banking")
        member_paymentwithcmb.current(0)
        member_paymentwithcmb.grid(row=11, column=1, pady=5, padx=10, sticky="w")

        member_membership = Checkbutton(Manage_Frame, text="Membership Fees", variable=self.var5, onvalue=1, offvalue=0, font=("cambria", 15, "bold"), bg="#001a66", fg="white", command=membership_fees) 
        member_membership.grid(row=12, column=0, sticky="w")

        member_membershiptxt = Entry(Manage_Frame, font=("cambria", 15, "bold"), state=DISABLED, justify=RIGHT, textvariable=self.Membership)
        member_membershiptxt.grid(row=12, column=1, pady=5, padx=10, sticky="w")

        ############### Detail Frame #####################
        self.detail_frame = Frame(self.root, relief=RIDGE, bg="#001a66")
        self.detail_frame.place(x=500, y=100, width=900, height=680)

        self.detail_label = Label(self.detail_frame, font=("cambria", 11, "bold"), pady=10, padx=2, width=95,
                                  text="Date\tRef Id\tFirstname\tLastname\tMobile No\tAddress\tPincode\tGender\tMembership")
        self.detail_label.grid(row=0, column=0, columnspan=4, sticky="w")

        self.detail_text = Text(self.detail_frame, width=95, height=30, font=("cambria", 12))
        self.detail_text.grid(row=1, column=0, columnspan=4, sticky="nsew")

        self.scrollbar = Scrollbar(self.detail_frame, command=self.detail_text.yview)
        self.scrollbar.grid(row=1, column=4, sticky='nse')

        self.detail_text.configure(yscrollcommand=self.scrollbar.set)

        # Buttons
        self.receipt_btn = Button(self.detail_frame, padx=10, bd=8, font=("cambria", 12, "bold"), bg="#ff9966",
                                  width=20, text="Receipt", command=Receipt)
        self.receipt_btn.grid(row=2, column=0)

        self.reset_btn = Button(self.detail_frame, padx=10, bd=8, font=("cambria", 12, "bold"), bg="#ff9966",
                                width=20, text="Reset", command= resetbtn)
        self.reset_btn.grid(row=2, column=1)

        self.exit_btn = Button(self.detail_frame, padx=10, bd=5, font=("cambria", 12, "bold"), bg="#ff9966",
                               width=20, text="Exit", command=exitbtn)
        self.exit_btn.grid(row=2, column=2)
class Hospital():
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1700x900+0+0")
        self.root.configure(background="black")

        Date_of_Registration = StringVar()
        Date_of_Registration.set(time.strftime("%d/%m/%y"))

        Ref = StringVar()
        cmbTabletNames = StringVar()
        HospitalCode = StringVar()
        Number_of_Tablets = StringVar()
        Lot = StringVar()
        IssuedDate = StringVar()
        ExpiryDate = StringVar()
        DailyDose = StringVar()
        SideEffects = StringVar()
        MoreInformation = StringVar()
        StorageAdvice = StringVar()
        Medication = StringVar()
        PatientId = StringVar()
        PatientNHnumver = StringVar()
        Patientname = StringVar()
        Dateofbirth = StringVar()
        PatientAddress = StringVar()
        Prescription = StringVar()
        NHSnumber = StringVar()

        def Reference_numfunc():
            ranumber = random.randint(10000, 9999999)
            randomnumber = str(ranumber)
            Ref.set(randomnumber)

        def prescriptionfunc(TextPrescription):
            Reference_numfunc()
            TextPrescription.insert(END, "Patient ID: \t\t" + PatientId.get() + "\n")
            TextPrescription.insert(END, "Patient Name: \t\t" + Patientname.get() + "\n")
            TextPrescription.insert(END, "Tablet: \t\t" + cmbTabletNames.get() + "\n")
            TextPrescription.insert(END, "Number of tablet: \t\t" + Number_of_Tablets.get() + "\n")
            TextPrescription.insert(END, "Daily Dose: \t\t" + DailyDose.get() + "\n")
            TextPrescription.insert(END, "Issued Date: \t\t" + IssuedDate.get() + "\n")
            TextPrescription.insert(END, "Expiry Date: \t\t" + ExpiryDate.get() + "\n")
            TextPrescription.insert(END, "Storage: \t\t" + StorageAdvice.get() + "\n")
            TextPrescription.insert(END, "More Information: \t\t" + MoreInformation.get() + "\n")
            return

        def prescriptiondatafunc():
            Reference_numfunc()
            TextPresciptionData.insert(END, Date_of_Registration.get() + "\t" + Ref.get() + "\t\t" +
                                       Patientname.get() + "\t\t" + Dateofbirth.get() + "\t\t" +
                                       NHSnumber.get() + "\t\t" + cmbTabletNames.get() + "\t" +
                                       Number_of_Tablets.get() + "\t\t" + IssuedDate.get() + "\t\t" +
                                       ExpiryDate.get() + "\t\t" + DailyDose.get() + "\t\t" +
                                       StorageAdvice.get() + "\t\t" + PatientId.get() + "\n")
            return

        def exitbtn():
            exitbtn = tkinter.messagebox.askyesno("Hospital Management System", "Are you sure you want to exit?")
            if exitbtn > 0:
                root.destroy()
            return

        def deletefunc():
            Ref.set("")
            cmbTabletNames.set("")
            HospitalCode.set("")
            Number_of_Tablets.set("")
            Lot.set("")
            IssuedDate.set("")
            ExpiryDate.set("")
            DailyDose.set("")
            SideEffects.set("")
            MoreInformation.set("")
            StorageAdvice.set("")
            Medication.set("")
            PatientId.set("")
            PatientNHnumver.set("")
            Patientname.set("")
            Dateofbirth.set("")
            PatientAddress.set("")
            Prescription.set("")
            NHSnumber.set("")
            TextPresciption.delete("1.0", END)
            TextPresciptionData.delete("1.0", END)
            return

        def resetfunc():
            Ref.set("")
            cmbTabletNames.set("")
            HospitalCode.set("")
            Number_of_Tablets.set("")
            Lot.set("")
            IssuedDate.set("")
            ExpiryDate.set("")
            DailyDose.set("")
            SideEffects.set("")
            MoreInformation.set("")
            StorageAdvice.set("")
            Medication.set("")
            PatientId.set("")
            PatientNHnumver.set("")
            Patientname.set("")
            Dateofbirth.set("")
            PatientAddress.set("")
            Prescription.set("")
            NHSnumber.set("")
            TextPresciption.delete("1.0", END)
            return

        title = Label(self.root, text=" + Hospital Management System", font=("cambria", 42, "bold"), bd=5,
                      relief=GROOVE, bg="#2eb8b8", fg="black")
        title.pack(side=TOP, fill=X)

        Manage_Frame = Frame(self.root, width=1510, height=400, bd=5, relief=RIDGE, bg="#0099cc")
        Manage_Frame.place(x=10, y=80)

        Button_Frame = Frame(self.root, width=1510, height=55, bd=4, relief=RIDGE, bg="#328695")
        Button_Frame.place(x=10, y=460)

        Data_Frame = LabelFrame(self.root, width=1510, height=270, bd=4, relief=RIDGE, bg="#266e73")
        Data_Frame.place(x=10, y=510)

        Data_FrameLeft = LabelFrame(Manage_Frame, width=1050, text="General Information",
                                   font=("cambria", 20, "italic bold"), height=390, bd=7, relief=RIDGE, bg="#0099cc")
        Data_FrameLeft.pack(side=LEFT)

        Data_FrameRight = LabelFrame(Manage_Frame, width=1050, text="Prescription",
                                    font=("cambria", 15, "italic bold"), height=390, bd=7, relief=RIDGE, bg="#0099cc")
        Data_FrameRight.pack(side=RIGHT)

        Data_Framedata = LabelFrame(Data_Frame, width=1050, text="Prescription Data",
                            font=("cambria", 12, "italic bold"), height=390, bd=4, relief=RIDGE, bg="#3eb7bb")
        Data_Framedata.grid(row=0, column=0, sticky=W)


        Datelbl = Label(Data_FrameLeft, font=("cambria", 12, "bold"), text="Date", padx=2)
        Datelbl.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        Datetxt = Entry(Data_FrameLeft, font=("cambria", 12, "bold"), width=27, textvariable=Date_of_Registration)
        Datetxt.grid(row=0, column=1, padx=10, pady=5, sticky=E)

        Reflbl = Label(Data_FrameLeft, font=("cambria", 12, "bold"), text="Reference Number", padx=2)
        Reflbl.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        Reftxt = Entry(Data_FrameLeft, font=("cambria", 12, "bold"), width=27, state=DISABLED, textvariable=Ref)
        Reftxt.grid(row=1, column=1, padx=10, pady=5, sticky=E)

        PatientIdlbl = Label(Data_FrameLeft, font=("cambria", 12, "bold"), text="Patient Id", padx=2)
        PatientIdlbl.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        PatientIdtxt = Entry(Data_FrameLeft, font=("cambria", 12, "bold"), width=27, textvariable=PatientId)
        PatientIdtxt.grid(row=2, column=1, padx=10, pady=5, sticky=E)

        PatientNamelbl = Label(Data_FrameLeft, font=("cambria", 12, "bold"), text="Patient Name", padx=2)
        PatientNamelbl.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        PatientNametxt = Entry(Data_FrameLeft, font=("cambria", 12, "bold"), width=27, textvariable=Patientname)
        PatientNametxt.grid(row=3, column=1, padx=10, pady=5, sticky=E)

        Dateofbirthlbl = Label(Data_FrameLeft, font=("cambria", 12, "bold"), text="Date of Birth", padx=2)
        Dateofbirthlbl.grid(row=4, column=0, padx=10, pady=5, sticky=W)
        Dateofbirthtxt = Entry(Data_FrameLeft, font=("cambria", 12, "bold"), width=27, textvariable=Dateofbirth)
        Dateofbirthtxt.grid(row=4, column=1, padx=10, pady=5, sticky=E)

        Addresslbl = Label(Data_FrameLeft, font=("cambria", 12, "bold"), text="Address", padx=2)
        Addresslbl.grid(row=5, column=0, padx=10, pady=5, sticky=W)
        Addresstxt = Entry(Data_FrameLeft, font=("cambria", 12, "bold"), width=27, textvariable=PatientAddress)
        Addresstxt.grid(row=5, column=1, padx=10, pady=5, sticky=E)

        NHSnumberlbl = Label(Data_FrameLeft, font=("cambria", 12, "bold"), text="NHS unique number", padx=2)
        NHSnumberlbl.grid(row=6, column=0, padx=10, pady=5, sticky=W)
        NHSnumbertxt = Entry(Data_FrameLeft, font=("cambria", 12, "bold"), width=27, textvariable=NHSnumber)
        NHSnumbertxt.grid(row=6, column=1, padx=10, pady=5, sticky=E)

        Tabletlbl = Label(Data_FrameLeft, font=("cambria", 12, "bold"), text="Tablet", padx=2)
        Tabletlbl.grid(row=7, column=0, padx=10, pady=5, sticky=W)

        Tabletcmb = ttk.Combobox(Data_FrameLeft, textvariable=cmbTabletNames, width=25, state="readonly",
                                 font=("cambria", 12, "bold"))
        Tabletcmb['values'] = ("", "Paracetamol", "Dan-p", "Dio-l One", "Calpol", "Amlodipine Besylate", "Nexium",
                               "Singulair", "Plavix", "Amoxicillin", "Azithromycin", "Limcin-900")
        Tabletcmb.current(0)
        Tabletcmb.grid(row=7, column=1, padx=10, pady=5)

        No_of_Tabletslbl = Label(Data_FrameLeft, font=("cambria", 12, "bold"), text="Number of Tablets", padx=2)
        No_of_Tabletslbl.grid(row=8, column=0, padx=10, pady=5, sticky=W)
        No_of_Tabletstxt = Entry(Data_FrameLeft, font=("cambria", 12, "bold"), width=27, textvariable=Number_of_Tablets)
        No_of_Tabletstxt.grid(row=8, column=1, padx=10, pady=5, sticky=E)

        Hospitalcodelbl = Label(Data_FrameLeft, font=("cambria", 12, "bold"), text="Hospital code", padx=2)
        Hospitalcodelbl.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        Hospitalcodetxt = Entry(Data_FrameLeft, font=("cambria", 12, "bold"), width=27, textvariable=HospitalCode)
        Hospitalcodetxt.grid(row=0, column=3, padx=10, pady=5, sticky=E)

        StorageaAdvicelbl = Label(Data_FrameLeft, font=("cambria", 12, "bold"), text="Storage Advice", padx=2)
        StorageaAdvicelbl.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        StorageAdvicecmb = ttk.Combobox(Data_FrameLeft, textvariable=StorageAdvice, width=25, state="readonly")
        StorageAdvicecmb['values'] = ("", "Under room temp", "below 5*C", "below 0*C", "Refrigeration")
        StorageAdvicecmb.current(0)
        StorageAdvicecmb.grid(row=1, column=3, padx=10, pady=5, sticky=E)

        Lot_nolbl = Label(Data_FrameLeft, font=("cambria", 12, "bold"), text="Lot number", padx=2)
        Lot_nolbl.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        Lot_notxt = Entry(Data_FrameLeft, font=("cambria", 12, "bold"), width=27, textvariable=Lot)
        Lot_notxt.grid(row=2, column=3, padx=10, pady=5, sticky=E)

        IssuedDatelbl = Label(Data_FrameLeft, font=("cambria", 12, "bold"), text="Date of Issue", padx=2)
        IssuedDatelbl.grid(row=3, column=2, padx=10, pady=5, sticky=W)
        IssuedDatetxt = Entry(Data_FrameLeft, font=("cambria", 12, "bold"), width=27, textvariable=IssuedDate)
        IssuedDatetxt.grid(row=3, column=3, padx=10, pady=5, sticky=E)

        ExpiryDatelbl = Label(Data_FrameLeft, font=("cambria", 12, "bold"), text="Date of Expiry", padx=2)
        ExpiryDatelbl.grid(row=4, column=2, padx=10, pady=5, sticky=W)
        ExpiryDatetxt = Entry(Data_FrameLeft, font=("cambria", 12, "bold"), width=27, textvariable=ExpiryDate)
        ExpiryDatetxt.grid(row=4, column=3, padx=10, pady=5, sticky=E)

        Dailydoselbl = Label(Data_FrameLeft, font=("cambria", 12, "bold"), text="Daily Dose", padx=2)
        Dailydoselbl.grid(row=5, column=2, padx=10, pady=5, sticky=W)
        Dailydosetxt = Entry(Data_FrameLeft, font=("cambria", 12, "bold"), width=27, textvariable=DailyDose)
        Dailydosetxt.grid(row=5, column=3, padx=10, pady=5, sticky=E)

        SideEffectslbl = Label(Data_FrameLeft, font=("cambria", 12, "bold"), text="SideEffects", padx=2)
        SideEffectslbl.grid(row=6, column=2, padx=10, pady=5, sticky=W)
        SideEffectstxt = Entry(Data_FrameLeft, font=("cambria", 12, "bold"), width=27, textvariable=SideEffects)
        SideEffectstxt.grid(row=6, column=3, padx=10, pady=5, sticky=E)

        MoreInformationlbl = Label(Data_FrameLeft, font=("cambria", 12, "bold"), text="More Information", padx=2)
        MoreInformationlbl.grid(row=7, column=2, padx=10, pady=5, sticky=W)
        MoreInformationtxt = Entry(Data_FrameLeft, font=("cambria", 12, "bold"), width=27, textvariable=MoreInformation)
        MoreInformationtxt.grid(row=7, column=3, padx=10, pady=5, sticky=E)

        Medicationlbl = Label(Data_FrameLeft, font=("cambria", 12, "bold"), text="Medication", padx=2)
        Medicationlbl.grid(row=8, column=2, padx=10, pady=5, sticky=W)
        Medicationtxt = Entry(Data_FrameLeft, font=("cambria", 12, "bold"), width=27, textvariable=Medication)
        Medicationtxt.grid(row=8, column=3, padx=10, pady=5, sticky=E)

        TextPresciption = Text(Data_FrameRight, font=("cambria", 12, "bold"), width=55, height=17, padx=3, pady=5)
        TextPresciption.grid(row=0, column=0)

        TextPresciptionData = Text(Data_Framedata, font=("cambria", 12, "bold"), width=203, height=12)
        TextPresciptionData.grid(row=0, column=0)

        Prescriptionbtn = Button(Button_Frame, text="Prescription", bg="#ffaab0", activebackground="#fcceb2",
                                 font=("cambria", 15, "bold"), width=22, command=prescriptionfunc(TextPresciption))
        Prescriptionbtn.grid(row=0, column=0, padx=15)

        Receiptbtn = Button(Button_Frame, text="Receipt", bg="#ffaab0", activebackground="#fcceb2",
                            font=("cambria", 15, "bold"), width=22, command=prescriptiondatafunc)
        Receiptbtn.grid(row=0, column=1, padx=15)

        Resetbtn = Button(Button_Frame, text="Reset", bg="#ffaab0", activebackground="#fcceb2",
                          font=("cambria", 15, "bold"), width=22, command=resetfunc)
        Resetbtn.grid(row=0, column=2, padx=15)

        Deletebtn = Button(Button_Frame, text="Delete", bg="#ffaab0", activebackground="#fcceb2",
                           font=("cambria", 15, "bold"), width=22, command=deletefunc)
        Deletebtn.grid(row=0, column=3, padx=15)

        Exitbtn = Button(Button_Frame, text="Exit", bg="#ffaab0", activebackground="#fcceb2",
                         font=("cambria", 15, "bold"), width=22, command=exitbtn)
        Exitbtn.grid(row=0, column=4, padx=15)

        Prescriptiondatarow = Label(Data_Framedata, bg="white", font=("cambria", 12, "bold"),
                                    text="Date\tReference Id\tPatient Name\tData of Birth\tNHS Number\tTablet\tNo of Tablet\tIssued Date\tExpiry Date \tDaily Dose\tStorage Advice\tPatient Id")
        Prescriptiondatarow.grid(row=1, column=0, sticky=W)


class Doctor():
       def __init__(self,root):
              self.root = root
              self.root.title("Dr. Appoinment System")
              self.root.geometry("1700x900+0+0")
              self.root.configure(background = "Black")

              Date_of_Registration = StringVar()
              Date_of_Registration.set(time.strftime("%d/%m/%y"))
              DrId = StringVar()
              Drname = StringVar()
              DateofBirth = StringVar()
              Spes = StringVar()
              GovtPri = StringVar()
              Surgeries = StringVar()
              Experience = StringVar()
              Nurses = StringVar()
              DrMobile = StringVar()
              PtName = StringVar()
              Apptime = StringVar()
              PtAge = StringVar()
              PatientAddress = StringVar()
              PtMobile = StringVar()
              Disease = StringVar()
              Case = StringVar()
              BenefitCard = StringVar()

              def exitbtn():
                     exitbtn = tkinter.messagebox.askyesno("Dr Appointment System", "Are you sure you want to exit?")
                     if exitbtn > 0:
                            root.destroy()
                            return
              
              def resetfunc():
                     DrId.set("")
                     Drname.set("")
                     DateofBirth.set("")
                     Spes.set("")
                     GovtPri.set("")
                     Surgeries.set("")
                     Experience.set("")
                     Nurses.set("")
                     DrMobile.set("")
                     PtName.set("")
                     Apptime.set("")
                     PtAge.set("")
                     PatientAddress.set("")
                     PtMobile.set("")
                     Disease.set("")
                     Case.set("")
                     BenefitCard.set("")
                     TextPrescription.delete("1.0",END)
                     return
              
              def deletefunc():
                     DrId.set("")
                     Drname.set("")
                     DateofBirth.set("")
                     Spes.set("")
                     GovtPri.set("")
                     Surgeries.set("")
                     Experience.set("")
                     Nurses.set("")
                     DrMobile.set("")
                     PtName.set("")
                     Apptime.set("")
                     PtAge.set("")
                     PatientAddress.set("")
                     PtMobile.set("")
                     Disease.set("")
                     Case.set("")
                     BenefitCard.set("")
                     TextPrescription.delete("1.0",END)
                     TextPrescriptionData.delete("1.0",END)
                     return
              
              def Patient_idFunction():
                     ranumber = random.randint(10000,999999)
                     randomnumber = str(ranumber)
                     DrId.set(randomnumber)
              
              def prescriptiondatafunc():
                     Patient_idFunction()
                     TextPrescriptionData.insert(END, Date_of_Registration.get()+"\t"+DrId.get()+"\t\t"
                     +Drname.get()+"\t\t"+DateofBirth.get()+"\t\t"+Spes.get()+"\t\t"+GovtPri.get()+"\t\t"+
                     Surgeries.get()+"\t\t"+Experience.get()+"\t\t"+Nurses.get()+"\t"+DrMobile.get()+"\t\t"+
                     PtName.get()+"\t\t"+Case.get()+Case.get()+"\t" + PtAge.get()+"\n")
                     return

              def prescriptionfunc():
                     Patient_idFunction()
                     TextPrescription.insert(END, "Date: \t\t"+Date_of_Registration.get()+"\n")
                     TextPrescription.insert(END, "Patient Name: \t\t"+PtName.get()+"\n")
                     TextPrescription.insert(END, "Appointment Time: \t\t"+Apptime.get()+"\n")
                     TextPrescription.insert(END, "Age: \t\t"+PtAge.get()+"\n")
                     TextPrescription.insert(END, "Address: \t\t"+PatientAddress.get()+"\n")
                     TextPrescription.insert(END, "Disease: \t\t"+Disease.get()+"\n")
                     TextPrescription.insert(END, "Case: \t\t"+Case.get()+"\n")
                     TextPrescription.insert(END, "Benefit Card: \t\t"+BenefitCard.get()+"\n")
                     TextPrescription.insert(END, "To meet Dr.: \t\t"+Drname.get()+"\n")
                     TextPrescription.insert(END, "Dr. Mobile No: \t\t"+DrMobile.get()+"\n")
                     return



              ############################ Title Labels #########################################################
              Title = Label(self.root , text = "Doctor Appointment System", font = ("cambria",42,"bold"), bd = 5,
                            relief = GROOVE, bg = "#b7d8d6", fg = "black")
              Title.pack(side = TOP, fill = X)

              ############################### Frame #################################
              Manage_Frame = Frame(self.root, width = 1510, height = 400, bd = 5, relief = RIDGE, bg = "#789e9e")
              Manage_Frame.place(x=10,y=80)

              Button_Frame = Frame(self.root, width = 1510, height = 55, bd = 4, relief = RIDGE, bg = "#eef3db")
              Button_Frame.place(x=10,y=460)

              Data_Frame = Frame(self.root, width = 1510, height = 270, bd = 4, relief = RIDGE, bg = "#eef3db")
              Data_Frame.place(x=10,y=510)

              Data_FrameLeft = LabelFrame(Manage_Frame, width = 1050, text = "General Information", font = ("cambria",20,"italic bold"),
                                           height = 390, bd = 7, pady = 1, relief = RIDGE, bg = "#789e9e")
              Data_FrameLeft.pack(side = LEFT)

              Data_Framedata = LabelFrame(Data_Frame, width = 1050, text = "Doctor's Details", font = ("cambria",12,"italic bold"),
                                           height = 390, bd = 7, relief = RIDGE, bg = "#b7d8d6")
              Data_Framedata.pack(side = LEFT)

              Data_FrameRight = LabelFrame(Manage_Frame, width = 1050, text = "Patient's Information", font = ("cambria",12,"italic bold"),
                                           height = 390, bd = 7, relief = RIDGE, bg = "#789e9e")
              Data_FrameRight.pack(side = RIGHT)

              ###################### Doctor's ID #####################

              DrIdlbl = Label(Data_FrameLeft, font = ("cambria",12,"bold"), width = 20, text = "Doctor ID", bg = "#789e9e")
              DrIdlbl.grid(row = 0, column = 0, padx = 10, pady = 5, sticky = "w")
              DrIdtxt = Entry(Data_FrameLeft, font = ("cambria",12,"bold"), width = 27, state = DISABLED, textvariable = DrId)
              DrIdtxt.grid(row = 0, column = 1, padx = 10, pady = 5, sticky=E)


              DrNamelbl = Label(Data_FrameLeft, font = ("cambria",12,"bold"), width = 20, text = "Doctor Name", bg = "#789e9e")
              DrNamelbl.grid(row = 1, column = 0, padx = 10, pady = 5, sticky = "w")
              DrNametxt = Entry(Data_FrameLeft, font = ("cambria",12,"bold"), width = 27, textvariable = Drname)
              DrNametxt.grid(row = 1, column = 1, padx = 10, pady = 5, sticky=E)


              Dateofbirthlbl = Label(Data_FrameLeft, font = ("cambria",12,"bold"), width = 20, text = "Date of Birthday", bg = "#789e9e")
              Dateofbirthlbl.grid(row = 2, column = 0, padx = 10, pady = 5, sticky = "w")
              Dateofbirthtxt = Entry(Data_FrameLeft, font = ("cambria",12,"bold"), width = 27, textvariable = DateofBirth)
              Dateofbirthtxt.grid(row = 2, column = 1, padx = 10, pady = 5, sticky=E)


              Speslbl = Label(Data_FrameLeft, font = ("cambria",12,"bold"), width = 20, text = "Specialisation", bg = "#789e9e")
              Speslbl.grid(row = 3, column = 0, padx = 10, pady = 5, sticky = "w")
              Spestxt = Entry(Data_FrameLeft, font = ("cambria",12,"bold"), width = 27, textvariable = Spes)
              Spestxt.grid(row = 3, column = 1, padx = 10, pady = 5, sticky=E)


              GovtPrilbl = Label(Data_FrameLeft, font = ("cambria",12,"bold"), width = 20, text = "Govt/Private", bg = "#789e9e")
              GovtPrilbl.grid(row = 4, column = 0, padx = 10, pady = 5, sticky = "w")
              GovtPricmb = ttk.Combobox(Data_FrameLeft, textvariable=GovtPri, width =25, state = "readonly", font = ("cambria",12,"bold"))
              GovtPricmb['values'] = ("", "Goverment", "Private")
              GovtPricmb.current(0)
              GovtPricmb.grid(row = 4, column = 1, padx = 10, pady = 5, sticky=E)


              Surgerieslbl = Label(Data_FrameLeft, font = ("cambria",12,"bold"), width = 20, text = "Surgeries", bg = "#789e9e")
              Surgerieslbl.grid(row = 5, column = 0, padx = 10, pady = 5, sticky = "w")
              Surgeriestxt = Entry(Data_FrameLeft, font = ("cambria",12,"bold"), width = 27, textvariable = Surgeries)
              Surgeriestxt.grid(row = 5, column = 1, padx = 10, pady = 5, sticky=E)

              Experiencelbl = Label(Data_FrameLeft, font = ("cambria",12,"bold"), width = 20, text = "Experience", bg = "#789e9e")
              Experiencelbl.grid(row = 6, column = 0, padx = 10, pady = 5, sticky = "w")
              Experiencetxt = Entry(Data_FrameLeft, font = ("cambria",12,"bold"), width = 27, textvariable = Experience)
              Experiencetxt.grid(row = 6, column = 1, padx = 10, pady = 5, sticky=E)


              Nurseslbl = Label(Data_FrameLeft, font = ("cambria",12,"bold"), width = 20, text = "Nurses under Dr", bg = "#789e9e")
              Nurseslbl.grid(row = 7, column = 0, padx = 10, pady = 5, sticky = "w")
              Nursestxt = Entry(Data_FrameLeft, font = ("cambria",12,"bold"), width = 27, textvariable = Nurses)
              Nursestxt.grid(row = 7, column = 1, padx = 10, pady = 5, sticky=E)


              Drmobilelbl = Label(Data_FrameLeft, font = ("cambria",12,"bold"), width = 20, text = "Dr Mobile No", bg = "#789e9e")
              Drmobilelbl.grid(row = 8, column = 0, padx = 10, pady = 5, sticky = "w")
              Drmobiletxt = Entry(Data_FrameLeft, font = ("cambria",12,"bold"), width = 27, textvariable = DrMobile)
              Drmobiletxt.grid(row = 8, column = 1, padx = 10, pady = 5, sticky=E)


              Datelbl = Label(Data_FrameLeft, font = ("cambria",12,"bold"), width = 20, text = "Date", padx = 2, bg = "#789e9e")
              Datelbl.grid(row = 0, column = 2, padx = 10, pady = 5, sticky = W)
              Datetxt = Entry(Data_FrameLeft, font = ("cambria",12,"bold"), width = 27, textvariable = Date_of_Registration)
              Datetxt.grid(row = 0, column = 3, padx = 10, pady = 5, sticky=E)


              PtNamelbl = Label(Data_FrameLeft, font = ("cambria",12,"bold"), width = 20, text = "Patient Name", padx = 2, bg = "#789e9e")
              PtNamelbl.grid(row = 1, column = 2, padx = 10, pady = 5, sticky = W)
              PtNametxt = Entry(Data_FrameLeft, font = ("cambria",12,"bold"), width = 27, textvariable = PtName)
              PtNametxt.grid(row = 1, column = 3, padx = 10, pady = 5, sticky=E)


              Apptimelbl = Label(Data_FrameLeft, font = ("cambria",12,"bold"),width = 20, text = "Patient Name", padx = 2, bg = "#789e9e")
              Apptimelbl.grid(row = 2, column = 2, padx = 10, pady = 5, sticky = W)
              Apptimetxt = Entry(Data_FrameLeft, font = ("cambria",12,"bold"), width = 27, textvariable = Apptime)
              Apptimetxt.grid(row = 2, column = 3, padx = 10, pady = 5, sticky=E)

              PtAgelbl = Label(Data_FrameLeft, font = ("cambria",12,"bold"),width = 20, text = "Patient Age", padx = 2, bg = "#789e9e")
              PtAgelbl.grid(row = 3, column = 2, padx = 10, pady = 5, sticky = W)
              PtAgetxt = Entry(Data_FrameLeft, font = ("cambria",12,"bold"), width = 27, textvariable = PtAge)
              PtAgetxt.grid(row = 3, column = 3, padx = 10, pady = 5, sticky=E)


              PtAddresslbl = Label(Data_FrameLeft, font = ("cambria",12,"bold"),width = 20, text = "Patient Address", padx = 2, bg = "#789e9e")
              PtAddresslbl.grid(row = 4, column = 2, padx = 10, pady = 5, sticky = W)
              PtAddresstxt = Entry(Data_FrameLeft, font = ("cambria",12,"bold"), width = 27, textvariable = PatientAddress)
              PtAddresstxt.grid(row = 4, column = 3, padx = 10, pady = 5, sticky=E)

              PtMobilelbl = Label(Data_FrameLeft, font = ("cambria",12,"bold"),width = 20, text = "Patient Mobile No", padx = 2, bg = "#789e9e")
              PtMobilelbl.grid(row = 5, column = 2, padx = 10, pady = 5, sticky = W)
              PtMobiletxt = Entry(Data_FrameLeft, font = ("cambria",12,"bold"), width = 27, textvariable = PtMobilelbl)
              PtMobiletxt.grid(row = 5, column = 3, padx = 10, pady = 5, sticky=E)

              Diseaselbl = Label(Data_FrameLeft, font = ("cambria",12,"bold"),width = 20, text = "Disease", padx = 2, bg = "#789e9e")
              Diseaselbl.grid(row = 6, column = 2, padx = 10, pady = 5, sticky = W)
              Diseasetxt = Entry(Data_FrameLeft, font = ("cambria",12,"bold"), width = 27, textvariable = Disease)
              Diseasetxt.grid(row = 6, column = 3, padx = 10, pady = 5, sticky=E)

              Caselbl = Label(Data_FrameLeft, font = ("cambria",12,"bold"),width = 20, text = "Case", padx = 2, bg = "#789e9e")
              Caselbl.grid(row = 7, column = 2, padx = 10, pady = 5, sticky = W)
              Casecmb = ttk.Combobox(Data_FrameLeft, textvariable=Case, width = 25, state = "readonly", font = ("cambria", 12, "bold"))
              Casecmb['values'] = ("", "New Case", "Old Case")
              Casecmb.current(0)
              Casecmb.grid(row = 7, column = 3, padx = 10, pady = 5, sticky=E)

              BenefitCardlbl = Label(Data_FrameLeft, font = ("cambria",12,"bold"),width = 20, text = "Benefit Card", padx = 2, bg = "#789e9e")
              BenefitCardlbl.grid(row = 8, column = 2, sticky = W)
              BenefitCardcmb = ttk.Combobox(Data_FrameLeft, textvariable=BenefitCard, width = 25, state = "readonly", font = ("cambria", 12, "bold"))
              BenefitCardcmb['values'] = ("", "Ayushman Card", "Health Insurance", "Senior Citizens", "Army Card")
              BenefitCardcmb.current(0)
              BenefitCardcmb.grid(row = 8, column = 3, padx = 10, pady = 5, sticky=E)


              ################## Text Prescription #################

              TextPrescription = Text(Data_FrameRight, font =("cambria",12,"bold"),width = 55, height = 17, padx = 3, pady = 5)
              TextPrescription.grid(row = 0, column = 0)
              TextPrescriptionData = Text(Data_Framedata, font = ("cambria",12,"bold"), width = 203, height = 12)
              TextPrescriptionData.grid(row = 1, column = 0)

              ################ Buttons #################

              Prescriptionbtn = Button(Button_Frame, text = "Patient Information", bg = "#fe615a", activebackground = "#cc6686", 
                                       font = ("cambria",15,"bold"),width = 22, command = prescriptionfunc)
              Prescriptionbtn.grid(row = 0, column = 0, padx = 15)

              DoctorDetailbtn = Button(Button_Frame, text = "Doctor's Details", bg = "#fe615a", activebackground = "#cc6686", 
                                       font = ("cambria",15,"bold"),width = 22, command = prescriptiondatafunc)
              DoctorDetailbtn.grid(row = 0, column = 1, padx = 15)


              Resetbtn = Button(Button_Frame, text = "Reset", bg = "#fe615a", activebackground = "#cc6686", 
                                       font = ("cambria",15,"bold"),width = 22, command =resetfunc)
              Resetbtn.grid(row = 0, column = 2, padx = 15)


              Deletebtn = Button(Button_Frame, text = "Delete", bg = "#fe615a", activebackground = "#cc6686", 
                                       font = ("cambria",15,"bold"),width = 22,command = deletefunc)
              Deletebtn.grid(row = 0, column = 3, padx = 15)

              Exitbtn = Button(Button_Frame, text = "Exit", bg = "#fe615a", activebackground = "#cc6686", 
                                       font = ("cambria",15,"bold"),width = 22,command = exitbtn)
              Exitbtn.grid(row = 0, column = 4, padx = 15)

              prescriptiondatarow = Label(Data_Framedata, bg = "white", font = ("cambria",12,"bold"),
                                          text = "Date\tDoctor Id \tDoctorName\tDate of birth\tSpecialisation\tGovt/Private\tSurgeries\tExperiences\tNurses\tDr Mobile No\tPatient Name\tCase\tPt. Age")
              prescriptiondatarow.grid(row = 0, column = 0, sticky = W)


class Medicine:

    def __init__(self,master):
        self.master=master
        self.master.title("Medicine Stock System")
        self.master.geometry("1350x750+0+0")
        self.master.configure(background="grey")
        self.frame=Frame(self.master)
        self.frame.pack()

        cmbTablets=StringVar()
        RefNo=StringVar()
        Dose=StringVar()
        IssueDate=StringVar()
        ExpDate=StringVar()
        SideEffects=StringVar()
        PatientID=StringVar()
        PatientName=StringVar()
        DateOfBirth=StringVar()
        PatientAddress=StringVar()
        NHSNo=StringVar()
        StorageAdvice=StringVar()
        FurtherInformation=StringVar()
        UsingMachine=StringVar()
        Medication=StringVar()
        NoofTablets=StringVar()
        Lot=StringVar()
        Strength=StringVar()
        Prescription=StringVar()

        #.......................................................................................................................#

        def iExit():
            iExit=tkinter.messagebox.askyesno ("Medicine Stock System", "Confirm if you want to exit")
            if iExit>0:
                self.master.destroy()
                return

        def iReset():
            cmbTablets.set("")
            RefNo.set("")
            Dose.set("")
            IssueDate.set("")
            ExpDate.set("")
            SideEffects.set("")
            PatientID.set("")
            PatientName.set("")
            DateOfBirth.set("")
            PatientAddress.set("")
            NHSNo.set("")
            StorageAdvice.set("")
            FurtherInformation.set("")
            UsingMachine.set("")
            Medication.set("")
            NoofTablets.set("")
            Lot.set("")
            Strength.set("")
            self.txtPrescription.delete("1.0",END)
            

            return

        def iDelete():
            cmbTablets.set("")
            RefNo.set("")
            Dose.set("")
            IssueDate.set("")
            ExpDate.set("")
            SideEffects.set("")
            PatientID.set("")
            PatientName.set("")
            DateOfBirth.set("")
            PatientAddress.set("")
            NHSNo.set("")
            StorageAdvice.set("")
            FurtherInformation.set("")
            UsingMachine.set("")
            Medication.set("")
            NoofTablets.set("")
            Lot.set("")
            Strength.set("")
            self.txtPrescription.delete("1.0",END)
            self.txtFrameDetail.delete("1.0",END)

            return

        def iReceipt():

            self.txtFrameDetail.insert(END, cmbTablets.get()+"\t\t"+ RefNo.get()+"\t"+ Dose.get()+"\t\t"+NoofTablets.get() + "\t"+ Lot.get()+ "\t"+ IssueDate.get()+
                                       "\t\t"+ ExpDate.get() +"\t" + Strength.get() + "\t\t"+ StorageAdvice.get() + "\t"+ NHSNo.get() + "\t\t"+ PatientName.get()
                                       + "\t"+ DateOfBirth.get() +"\t"+ PatientAddress.get()+ "\n")

            return

        def iPrescription():
            self.txtPrescription.insert(END,"Name of Tablet: \t\t\t\t" + cmbTablets.get() + "\n")
            self.txtPrescription.insert(END,"Dose: \t\t\t\t" + Dose.get() + "\n")
            self.txtPrescription.insert(END,"Number of Tablets: \t\t\t\t" + NoofTablets.get() + "\n")
            self.txtPrescription.insert(END,"Lot: \t\t\t\t" + Lot.get() + "\n")
            self.txtPrescription.insert(END,"Issue Date: \t\t\t\t" + IssueDate.get() + "\n")
            self.txtPrescription.insert(END,"Exp. Date: \t\t\t\t" + ExpDate.get() + "\n")
            self.txtPrescription.insert(END,"Strength: \t\t\t\t" + Strength.get() + "\n")
            self.txtPrescription.insert(END,"Possible Side Effects: \t\t\t\t" + SideEffects.get() + "\n")
            self.txtPrescription.insert(END,"Storage Advice: \t\t\t\t" + StorageAdvice.get() + "\n")
            self.txtPrescription.insert(END,"NHS Number: \t\t\t\t" + NHSNo.get() + "\n")
            self.txtPrescription.insert(END,"Extra Information: \t\t\t\t" + FurtherInformation.get() + "\n")

            return


        #.......................................................................................................................#
        

        MainFrame=Frame(self.frame)
        MainFrame.grid()

        TitleFrame=Frame(MainFrame,width=1350,padx=20,bd=20,relief=RIDGE)
        TitleFrame.pack(side=TOP)
        
        self.lblTitle=Label(TitleFrame,font=("cambria",40,"bold"),text="Medicine Stock System",padx=2)
        self.lblTitle.grid()

        FrameDetail=Frame(MainFrame,bd=20,width=1350,height=100,padx=20,relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        ButtonFrame=Frame(MainFrame,bd=20,width=1350,height=50,padx=20,relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame=Frame(MainFrame,bd=20,width=1350,height=400,padx=20,relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT=LabelFrame(DataFrame,bd=10,width=800,height=300,font=("cambria",12,"bold"),text="Patient Detail:",relief=RIDGE,padx=20)
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT=LabelFrame(DataFrame,bd=10,width=450,height=300,font=("cambria",12,"bold"),text="Prescription:",relief=RIDGE,padx=20)
        DataFrameRIGHT.pack(side=RIGHT)

        #..................................................................................................................#

        self.lblTablet=Label(DataFrameLEFT,font=("cambria",12,"bold"),text="Tablet:",padx=2,pady=2)
        self.lblTablet.grid(row=0,column=2,sticky=W)

        self.Tablet=ttk.Combobox(DataFrameLEFT,font=("cambria",12,"bold"),state="readonly",width=23,textvariable=cmbTablets)
        self.Tablet["value"]=('',"Panadol","Disprin") #............ARRAY
        self.Tablet.current(0)
        self.Tablet.grid(row=0,column=3)

        #..................................................................................................................#

        labels = ["Patient Name:" , "DateOfBirth:" , "NHS No:" , "Patient Address:" , "Patient ID:" , "Lot:" ,
                  "No.of Tablets:" , "Strength:" , "Medication:"] #.............LIST
        counter = 0
        for i in range (len(labels)):
            self.cur_label = "label" + str(i)
            self.cur_label=Label(DataFrameLEFT,font=("cambria",12,"bold"),text=labels[i],padx=2,pady=2)
            self.cur_label.grid(row=counter,column=0,sticky=W)

            counter += 1

        entry_box = {"Patient Name:":PatientName , "DateOfBirth:":DateOfBirth , "NHS No:":NHSNo , "Patient Address:":PatientAddress , "Patient ID:":PatientID , "Lot:":Lot
                     , "No.of Tablets:":NoofTablets , "Strength:":Strength , "Medication:":Medication} #.........DICTIONARY

        counter = 0

        for i in entry_box:
            self.cur_entrybox = "entry" + i
            self.cur_entrybox = Entry(DataFrameLEFT,font=("cambria",12,"bold"),width=25,textvariable=entry_box[i])
            self.cur_entrybox.grid(row=counter,column=1)
            counter += 1

        labels = ["Dose:" , "Issue Date:" , "Exp Date:" , "Side Effects:" , "Ref No:" , "Storage Advice:" , "Using Machine:" , "Further Information:"]#..LIST
        
        counter = 1
        
        for i in range (len(labels)):
            self.cur_label = "label" + str(i)
            self.cur_label=Label(DataFrameLEFT,font=("cambria",12,"bold"),text=labels[i],padx=2,pady=2)
            self.cur_label.grid(row=counter,column=2,sticky=W)

            counter += 1

        entry_box = {"Dose:":Dose , "Issue Date:":IssueDate , "Exp Date:":ExpDate , "Side Effects:":SideEffects , "Ref No:":RefNo ,
                     "Storage Advice:":StorageAdvice , "Using Machine:":UsingMachine , "Further Information:":FurtherInformation}#........DICTIONARY

        counter = 1

        for i in entry_box:
            self.cur_entrybox = "entry" + i
            self.cur_entrybox = Entry(DataFrameLEFT,font=("cambria",12,"bold"),width=25,textvariable=entry_box[i])
            self.cur_entrybox.grid(row=counter,column=3)
            counter += 1

        #..........................................................................................................................#

        self.txtPrescription=Text(DataFrameRIGHT,font=("cambria",12,"bold"),width=43,height=12,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)

        #..........................................................................................................................#

        self.btnPrescription=Button(ButtonFrame,text="Prescription",font=("cambria",12,"bold"),width=24,bd=4,bg = "#ff9966",command=iPrescription)
        self.btnPrescription.grid(row=0,column=0)

        self.btnReceipt=Button(ButtonFrame,text="Receipt",font=("cambria",12,"bold"),width=24,bd=4,bg = "#ff9966",command=iReceipt)
        self.btnReceipt.grid(row=0,column=1)

        self.btnDelete=Button(ButtonFrame,text="Delete",font=("cambria",12,"bold"),width=24,bd=4,bg = "#ff9966",command=iDelete)
        self.btnDelete.grid(row=0,column=2)

        self.btnReset=Button(ButtonFrame,text="Reset",font=("cambria",12,"bold"),width=24,bd=4,bg = "#ff9966",command=iReset)
        self.btnReset.grid(row=0,column=3)

        self.btnExit=Button(ButtonFrame,text="Exit",font=("cambria",12,"bold"),width=24,bd=4,bg = "#ff9966",command=iExit)
        self.btnExit.grid(row=0,column=4)

        #...........................................................................................................................#

        self.lblLabel=Label(FrameDetail,font=("cambria",10,"bold"),pady=8,text="Name of Tablet \tReference No. \tDoseage \tNo.of Tablets \tLot \tIssue Date \tExp. Date \tStrength\tStorage Adv. \tNHS Number \tPatient Name\t DOB\t Address",)
        self.lblLabel.grid(row=0,column=0)

        self.txtFrameDetail=Text(FrameDetail,font=("cambria",12,"bold"),width=141,height=4,padx=2,pady=4)
        self.txtFrameDetail.grid(row=1,column=0)



if __name__ == '__main__':
    main()

