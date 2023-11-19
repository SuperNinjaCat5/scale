import tkinter as tk
import serial,time
from tkinter.ttk import Label
from tkinter.messagebox import showinfo
import datetime
import sys
import random
#SERIALPORT = "/dev/ttyUSB0"  #Real Sparfun Open Scale
SERIALPORT = "/dev/ttyACM0"  #Dummy Sparfun Open Scale on Arduino

BAUDRATE = 9600

#ser = serial.Serial(SERIALPORT, BAUDRATE, timeout =1)

root = tk.Tk()
root.geometry('1000x500')
root.resizable(True, True)
root.title('Troop 30 Food Drive Weigh Station')


root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)


scout = tk.StringVar(root)
weight_to_display = tk.StringVar(root)
ScoutType = tk.StringVar(root)
ScoutType.set("Scout")
Bigtotal = tk.StringVar(root)
Bigtotal.set("0")

#def get_serial(StringToSend):
#    print("StringToSend = "+StringToSend)
#    weight_string = ""
#    weight = 00.0
#    miliseconds = 0
#    Data_Ready = 0
#    
#    ser.reset_input_buffer()
#    ser.reset_output_buffer()
#    
#    #ser.write(bytearray("W",'ascii'))
#    ser.write(StringToSend.encode('utf-8'))
#    
#    #time.sleep(.1)
#    while (Data_Ready == 0):
#        Data_Ready = ser.inWaiting()
#        pass
#    
#    input_string =""
#    
#    input_string = ser.readline().decode('utf-8')
#    print (input_string)
#    
#    try:
#        split_input_string = input_string.split(",")
#        print("weight splitting")
#        print (split_input_string[0])
#        print (split_input_string[1])
#        weight_string = split_input_string[0]
#        weight_string = weight_string.rstrip()
#        weight_string = weight_string.rstrip('lbs')
#        
#        print("weight_string = "+ weight_string)
#        weight = float(weight_string)
#        
#        print("weight = "+ str(weight))
#        
#        #miliseconds_string = split_input_string[0].strip()
#        #miliseconds = int(miliseconds_string)
#        
#        print("milliseconds = " + str(miliseconds))
#              
#        return weight
#        
#    except:
#        print("Not Weight Data")
#        print (split_input_string[0])
        
    
   


def write_to_file():
    #print("Saving")
    ct = 0
    
    bt = 0.0
    ScoutName = ""
    ScoutTypeDisplay = ""
    weight_to_file = ""
    
    print("ScoutName = ")
    ScoutName=str(scout.get())
    ScoutName = str.title(ScoutName)
    print(ScoutName)
                 
    print("ScoutType = ")
    ScoutTypeDisplay=str(ScoutType.get())
    ScoutTypeDisplay=ScoutTypeDisplay.rstrip('\r\n')
    print(ScoutTypeDisplay)
    
    print("Donation Weight = ")
    weight_to_file = str(weight_to_display.get())
    weight_to_file = weight_to_file.rstrip(" lbs.")
    print(weight_to_file)
    
    
    
    
    if ScoutName != "":

        #hs = open("/home/pi/Desktop/Food_Pantry_Donations.csv","a") #RPI400
        hs = open("C:/Users/nicos/Documents/Food_Pantry_Donations.csv","a") #Laptop
        ct = datetime.datetime.now()
        
        hs.write(ScoutName)
        hs.write(",")
        
        hs.write(ScoutTypeDisplay)
        hs.write(",")
    
        hs.write(weight_to_file)
        hs.write(",")
        
        hs.write("lbs")
        hs.write(",")
        
        
        bt = float(Bigtotal.get())
        bt = round(bt + float(weight_to_file),2)
        Bigtotal.set(str(bt))
        print("Bigtotal=" + Bigtotal.get())
        hs.write(str(bt))
        hs.write(",")
        
        hs.write("lbs")
        hs.write(",")
        
        
        hs.write(str(ct))
        hs.write(" \n")
    
        hs.close
        
        scout.set(ScoutName)
        
        
        
    
        showinfo(
            title='Saved',
            message=ScoutName+', thank you for your '+weight_to_file+' lbs. donation!'
            )
        
            
    else:
        showinfo(
            title='Error not saved',
            message='Please Name The '+ ScoutTypeDisplay
            
            )
        
        
def Tare_The_Scale():
    tare = 0
    #Tare = get_serial("x") #gives error with dummy weight
    
    #Tare = get_serial("1")
    
    #Tare = get_serial("x")



    
    
btnSaveToFile = tk.Button(
            root,text = "Save To File",
            font=("Helvetica", 60),command = write_to_file,)

btnSaveToFile.grid(row = 4, column = 2, columnspan = 1, rowspan = 3)

btnTare = tk.Button(
            root,text = "Tare",
            font=("Helvetica", 20),command = Tare_The_Scale)

btnTare.grid(row = 3, column = 2, columnspan = 1, rowspan = 3)


label1 = tk.Label(
        root,
        textvariable=(weight_to_display),
        font=("Helvetica", 200))

label1.grid(row = 0, column = 0,columnspan = 3,rowspan = 3)
      
        
label2 = tk.Label(
        root,
        textvariable=(Bigtotal),
        font=("Helvetica", 60))

label2.grid(row = 3, column = 2,columnspan = 1,rowspan = 1)       
        
label3 = tk.Label(
        root,
        text=("200 lbs. maxiumum on scale."),
        font=("Helvetica", 40))

label3.grid(row = 3, column = 1,columnspan = 1,rowspan = 1)


NameEntry = tk.Entry(root,text = "boy",
                     textvariable  = scout,
                     font=("Helvetica", 60))

NameEntry.grid(row = 4,column = 1,columnspan=1,rowspan = 3)



    

r1 = tk.Radiobutton(root, text='Scout', font=("Helvetica", 20), value='Scout', variable=ScoutType)
r1.grid(row = 3, column = 0) 

r2 = tk.Radiobutton(root, text='Webelo', font=("Helvetica", 20), value='Webelo', variable=ScoutType)
r2.grid(row = 4, column = 0) 

r3 = tk.Radiobutton(root, text='Other', font=("Helvetica", 20), value='Other', variable=ScoutType)
r3.grid(row = 5, column = 0)

def adjust_font_size(event=None):
    # Calculate a new font size based on the window width and height
    new_font_size = int((root.winfo_width() + root.winfo_height()) // 50)  # Adjust this formula as needed
    
    # Set the new font size for all relevant widgets
    btnSaveToFile.config(font=("Helvetica", int(new_font_size // 1.5)))
    btnTare.config(font=("Helvetica", new_font_size // 2))
    label1.config(font=("Helvetica", new_font_size))
    label2.config(font=("Helvetica", new_font_size))
    label3.config(font=("Helvetica", int(new_font_size // 1.3)))
    NameEntry.config(font=("Helvetica", new_font_size))
    r1.config(font=("Helvetica", new_font_size // 4))
    r2.config(font=("Helvetica", new_font_size // 4))
    r3.config(font=("Helvetica", new_font_size // 4))

def my_mainloop():
    print("Main Loop")
    
    #weight= get_serial("0") #Real Weight
    weight= random.randint(1,110) #Fake weight
    data0 = str(weight)
    #data0 = data0 + " lbs."
    weight_to_display.set(data0 + " lbs.")
    
    print("weight_to_display = "+ data0 )
        
    root.after(1000, my_mainloop)
    
    
root.after(1000, my_mainloop)

adjust_font_size(0)
root.bind("<Configure>", adjust_font_size)

root.mainloop(
)
  

  

