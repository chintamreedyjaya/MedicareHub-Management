import time
import random
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

class Doctor():
       def __init__(self,root):
              self.root = root
              self.root.title("Dr Appoinment System")
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
              Title = Label(self.root , text = "Doctor Management System", font = ("cambria",42,"bold"), bd = 5,
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


       
if __name__ == "__main__":
       root = Tk()
       app = Doctor(root)
       root.mainloop()


