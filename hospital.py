import random
import time
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import mysql.connector

class Hospital():
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1700x900+0+0")
        self.root.configure(background="black")


        self.Date_of_Registration = StringVar()
        self.Date_of_Registration.set(time.strftime("%d/%m/%y"))
        self.Ref = StringVar()
        self.cmbTabletNames = StringVar()
        self.HospitalCode = StringVar()
        self.Number_of_Tablets = StringVar()
        self.Lot = StringVar()
        self.IssuedDate = StringVar()
        self.ExpiryDate = StringVar()
        self.DailyDose = StringVar()
        self.SideEffects = StringVar()
        self.MoreInformation = StringVar()
        self.StorageAdvice = StringVar()
        self.Medication = StringVar()
        self.PatientId = StringVar()
        self.PatientNHnumver = StringVar()
        self.Patientname = StringVar()
        self.Dateofbirth = StringVar()
        self.PatientAddress = StringVar()
        self.Prescription = StringVar()
        self.NHSnumber = StringVar()

        self.connection = mysql.connector.connect(
              host="localhost",
              user="root",
              password="Nilu@07_",
              database="hospital")
        
        self.cursor = self.connection.cursor()

        print("Connection established: ", self.connection)

        def insert_data(self):
            DateOfRegistration = self.Date_of_Registration.get()
            ReferenceID = self.Ref.get()
            PatientName = self.Patientname.get()
            DateOfBirth = self.Dateofbirth.get()
            NHSNumber = self.NHSnumber.get()
            TabletName = self.cmbTabletNames.get()
            NumberOfTablets = self.Number_of_Tablets.get()
            IssuedDate = self.IssuedDate.get()
            ExpiryDate = self.ExpiryDate.get()
            DailyDose = self.DailyDose.get()
            StorageAdvice = self.StorageAdvice.get()
            PatientID = self.PatientId.get()   

            insert_query = "INSERT INTO hospital.PrescriptionData (DateOfRegistration,ReferenceID,PatientName,DateOfBirth ,NHSNumber ,TabletName,NumberOfTablets,IssuedDate,ExpiryDate ,DailyDose, StorageAdvice,PatientID ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            data = (DateOfRegistration, ReferenceID, PatientName, DateOfBirth, NHSNumber, TabletName, NumberOfTablets, IssuedDate, ExpiryDate, DailyDose, StorageAdvice, PatientID)

            self.cursor.execute(insert_query, data)
            self.connection.commit()

            tkinter.messagebox.showinfo("Success", "Data inserted into database successfully!")


        def Reference_numfunc():
            ranumber = random.randint(10000, 9999999)
            randomnumber = str(ranumber)
            self.Ref.set(randomnumber)

        def prescriptionfunc(TextPrescription):
            Reference_numfunc()
            TextPrescription.insert(END, "Patient ID: \t\t" + self.PatientId.get() + "\n")
            TextPrescription.insert(END, "Patient Name: \t\t" + self.Patientname.get() + "\n")
            TextPrescription.insert(END, "Tablet: \t\t" + self.cmbTabletNames.get() + "\n")
            TextPrescription.insert(END, "Number of tablet: \t\t" + self.Number_of_Tablets.get() + "\n")
            TextPrescription.insert(END, "Daily Dose: \t\t" + self.DailyDose.get() + "\n")
            TextPrescription.insert(END, "Issued Date: \t\t" + self.IssuedDate.get() + "\n")
            TextPrescription.insert(END, "Expiry Date: \t\t" + self.ExpiryDate.get() + "\n")
            TextPrescription.insert(END, "Storage: \t\t" + self.StorageAdvice.get() + "\n")
            TextPrescription.insert(END, "More Information: \t\t" + self.MoreInformation.get() + "\n")
            return

        def exitbtn():
            exitbtn = tkinter.messagebox.askyesno("Hospital Management System", "Are you sure you want to exit?")
            if exitbtn > 0:
                root.destroy()
            return

        def deletefunc():
            self.Ref.set("")
            self.cmbTabletNames.set("")
            self.HospitalCode.set("")
            self.Number_of_Tablets.set("")
            self.Lot.set("")
            self.IssuedDate.set("")
            self.ExpiryDate.set("")
            self.DailyDose.set("")
            self.SideEffects.set("")
            self.MoreInformation.set("")
            self.StorageAdvice.set("")
            self.Medication.set("")
            self.PatientId.set("")
            self.PatientNHnumver.set("")
            self.Patientname.set("")
            self.Dateofbirth.set("")
            self.PatientAddress.set("")
            self.Prescription.set("")
            self.NHSnumber.set("")
            TextPresciption.delete("1.0", END)
            TextPresciptionData.delete("1.0", END)
            return

        def resetfunc():
            self.Ref.set("")
            self.cmbTabletNames.set("")
            self.HospitalCode.set("")
            self.Number_of_Tablets.set("")
            self.Lot.set("")
            self.IssuedDate.set("")
            self.ExpiryDate.set("")
            self.DailyDose.set("")
            self.SideEffects.set("")
            self.MoreInformation.set("")
            self.StorageAdvice.set("")
            self.Medication.set("")
            self.PatientId.set("")
            self.PatientNHnumver.set("")
            self.Patientname.set("")
            self.Dateofbirth.set("")
            self.PatientAddress.set("")
            self.Prescription.set("")
            self.NHSnumber.set("")
            TextPresciption.delete("1.0", END)
            return
        def prescriptiondatafunc():
            Reference_numfunc()
            insert_data(self)
            TextPresciptionData.insert(END, f"{self.Date_of_Registration.get()}\t{self.Ref.get()}\t{self.Patientname.get()}\t{self.Dateofbirth.get()}\t{self.NHSnumber.get()}\t{self.cmbTabletNames.get()}\t{self.Number_of_Tablets.get()}\t{self.IssuedDate.get()}\t{self.ExpiryDate.get()}\t{ self.DailyDose.get()}\t{self.StorageAdvice.get() }\t{self.PatientId.get()}\n")

        title = Label(self.root, text="Hospital ManagementSystem", font=("monotype corsiva", 42, "bold"), bd=5,
                      relief=GROOVE, bg="#2eb8b8", fg="black")
        title.pack(side=TOP, fill=X)

        Manage_Frame = Frame(self.root, width=1510, height=400, bd=5, relief=RIDGE, bg="#0099cc")
        Manage_Frame.place(x=10, y=80)

        Button_Frame = Frame(self.root, width=1510, height=55, bd=4, relief=RIDGE, bg="#328695")
        Button_Frame.place(x=10, y=460)

        Data_Frame = LabelFrame(self.root, width=1510, height=270, bd=4, relief=RIDGE, bg="#266e73")
        Data_Frame.place(x=10, y=510)

        Data_FrameLeft = LabelFrame(Manage_Frame, width=1050, text="General Information",
                                   font=("arial", 20, "italic bold"), height=390, bd=7, relief=RIDGE, bg="#0099cc")
        Data_FrameLeft.pack(side=LEFT)

        Data_FrameRight = LabelFrame(Manage_Frame, width=1050, text="Prescription",
                                    font=("arial", 15, "italic bold"), height=390, bd=7, relief=RIDGE, bg="#0099cc")
        Data_FrameRight.pack(side=RIGHT)

        Data_Framedata = LabelFrame(Data_Frame, width=1050, text="Prescription Data",
                            font=("arial", 12, "italic bold"), height=390, bd=4, relief=RIDGE, bg="#3eb7bb")
        Data_Framedata.grid(row=0, column=0, sticky=W)


        Datelbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), text="Date", padx=2, bg="#0099cc")
        Datelbl.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        Datetxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=self.Date_of_Registration)
        Datetxt.grid(row=0, column=1, padx=10, pady=5, sticky=E)

        Reflbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), text="Reference Number", padx=2)
        Reflbl.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        Reftxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, state=DISABLED, textvariable=self.Ref)
        Reftxt.grid(row=1, column=1, padx=10, pady=5, sticky=E)

        PatientIdlbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), text="Patient Id", padx=2)
        PatientIdlbl.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        PatientIdtxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=self.PatientId)
        PatientIdtxt.grid(row=2, column=1, padx=10, pady=5, sticky=E)

        PatientNamelbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), text="Patient Name", padx=2)
        PatientNamelbl.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        PatientNametxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=self.Patientname)
        PatientNametxt.grid(row=3, column=1, padx=10, pady=5, sticky=E)

        Dateofbirthlbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), text="Date of Birth", padx=2)
        Dateofbirthlbl.grid(row=4, column=0, padx=10, pady=5, sticky=W)
        Dateofbirthtxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=self.Dateofbirth)
        Dateofbirthtxt.grid(row=4, column=1, padx=10, pady=5, sticky=E)

        Addresslbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), text="Address", padx=2)
        Addresslbl.grid(row=5, column=0, padx=10, pady=5, sticky=W)
        Addresstxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=self.PatientAddress)
        Addresstxt.grid(row=5, column=1, padx=10, pady=5, sticky=E)

        NHSnumberlbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), text="NHS unique number", padx=2)
        NHSnumberlbl.grid(row=6, column=0, padx=10, pady=5, sticky=W)
        NHSnumbertxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=self.NHSnumber)
        NHSnumbertxt.grid(row=6, column=1, padx=10, pady=5, sticky=E)

        Tabletlbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), text="Tablet", padx=2)
        Tabletlbl.grid(row=7, column=0, padx=10, pady=5, sticky=W)

        Tabletcmb = ttk.Combobox(Data_FrameLeft, textvariable=self.cmbTabletNames, width=25, state="readonly",
                                 font=("arial", 12, "bold"))
        Tabletcmb['values'] = ("", "Paracetamol", "Dan-p", "Dio-l One", "Calpol", "Amlodipine Besylate", "Nexium",
                               "Singulair", "Plavix", "Amoxicillin", "Azithromycin", "Limcin-900")
        Tabletcmb.current(0)
        Tabletcmb.grid(row=7, column=1, padx=10, pady=5)

        No_of_Tabletslbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), text="Number of Tablets", padx=2)
        No_of_Tabletslbl.grid(row=8, column=0, padx=10, pady=5, sticky=W)
        No_of_Tabletstxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=self.Number_of_Tablets)
        No_of_Tabletstxt.grid(row=8, column=1, padx=10, pady=5, sticky=E)

        Hospitalcodelbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), text="Hospital code", padx=2)
        Hospitalcodelbl.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        Hospitalcodetxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=self.HospitalCode)
        Hospitalcodetxt.grid(row=0, column=3, padx=10, pady=5, sticky=E)

        StorageaAdvicelbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), text="Storage Advice", padx=2)
        StorageaAdvicelbl.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        StorageAdvicecmb = ttk.Combobox(Data_FrameLeft, textvariable=self.StorageAdvice, width=25, state="readonly")
        StorageAdvicecmb['values'] = ("", "Under room temp", "below 5*C", "below 0*C", "Refrigeration")
        StorageAdvicecmb.current(0)
        StorageAdvicecmb.grid(row=1, column=3, padx=10, pady=5, sticky=E)

        Lot_nolbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), text="Lot number", padx=2)
        Lot_nolbl.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        Lot_notxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=self.Lot)
        Lot_notxt.grid(row=2, column=3, padx=10, pady=5, sticky=E)

        IssuedDatelbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), text="Date of Issue", padx=2)
        IssuedDatelbl.grid(row=3, column=2, padx=10, pady=5, sticky=W)
        IssuedDatetxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=self.IssuedDate)
        IssuedDatetxt.grid(row=3, column=3, padx=10, pady=5, sticky=E)

        ExpiryDatelbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), text="Date of Expiry", padx=2)
        ExpiryDatelbl.grid(row=4, column=2, padx=10, pady=5, sticky=W)
        ExpiryDatetxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=self.ExpiryDate)
        ExpiryDatetxt.grid(row=4, column=3, padx=10, pady=5, sticky=E)

        Dailydoselbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), text="Daily Dosage", padx=2)
        Dailydoselbl.grid(row=5, column=2, padx=10, pady=5, sticky=W)
        Dailydosetxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=self.DailyDose)
        Dailydosetxt.grid(row=5, column=3, padx=10, pady=5, sticky=E)

        SideEffectslbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), text="SideEffects", padx=2)
        SideEffectslbl.grid(row=6, column=2, padx=10, pady=5, sticky=W)
        SideEffectstxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=self.SideEffects)
        SideEffectstxt.grid(row=6, column=3, padx=10, pady=5, sticky=E)

        MoreInformationlbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), text="More Information", padx=2)
        MoreInformationlbl.grid(row=7, column=2, padx=10, pady=5, sticky=W)
        MoreInformationtxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=self.MoreInformation)
        MoreInformationtxt.grid(row=7, column=3, padx=10, pady=5, sticky=E)

        Medicationlbl = Label(Data_FrameLeft, font=("arial", 12, "bold"), text="Medication", padx=2)
        Medicationlbl.grid(row=8, column=2, padx=10, pady=5, sticky=W)
        Medicationtxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), width=27, textvariable=self.Medication)
        Medicationtxt.grid(row=8, column=3, padx=10, pady=5, sticky=E)

        TextPresciption = Text(Data_FrameRight, font=("arial", 12, "bold"), width=55, height=17, padx=3, pady=5)
        TextPresciption.grid(row=0, column=0)

        TextPresciptionData = Text(Data_Framedata, font=("arial", 12, "bold"), width=203, height=12)
        TextPresciptionData.grid(row=0, column=0)

        Prescriptionbtn = Button(Button_Frame, text="Prescription", bg="#ffaab0", activebackground="#fcceb2",
                                 font=("arial", 15, "bold"), width=22, command=prescriptionfunc(TextPresciption))
        Prescriptionbtn.grid(row=0, column=0, padx=15)

        Receiptbtn = Button(Button_Frame, text="Reciept", bg="#ffaab0", activebackground="#fcceb2",
                            font=("arial", 15, "bold"), width=22, command=prescriptiondatafunc)
        Receiptbtn.grid(row=0, column=1, padx=15)

        Resetbtn = Button(Button_Frame, text="Reset", bg="#ffaab0", activebackground="#fcceb2",
                          font=("arial", 15, "bold"), width=22, command=resetfunc)
        Resetbtn.grid(row=0, column=2, padx=15)

        Deletebtn = Button(Button_Frame, text="Delete", bg="#ffaab0", activebackground="#fcceb2",
                           font=("arial", 15, "bold"), width=22, command=deletefunc)
        Deletebtn.grid(row=0, column=3, padx=15)

        Exitbtn = Button(Button_Frame, text="Exit", bg="#ffaab0", activebackground="#fcceb2",
                         font=("arial", 15, "bold"), width=22, command=exitbtn)
        Exitbtn.grid(row=0, column=4, padx=15)

        Prescriptiondatarow = Label(Data_Framedata, bg="white", font=("arial", 12, "bold"),
                                    text="Date\tReference Id\tPatient Name\tData of Birth\tNHS Number\tTablet\tNo of Tablet\tIssued Date\tExpiry Date \tDaily Dose\tStorage Advice\tPatient Id")
        Prescriptiondatarow.grid(row=0, column=0, sticky=W)


if __name__ == "__main__":
    root = Tk()
    app = Hospital(root)
    root.mainloop()
