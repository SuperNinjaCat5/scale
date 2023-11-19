import tkinter as tk
import serial,time
from tkinter.ttk import Label
from tkinter.messagebox import showinfo
import datetime
import sys
#SERIALPORT = "/dev/ttyUSB0"  #Real Sparfun Open Scale
SERIALPORT = "/dev/ttyACM0"  #Dummy Sparfun Open Scale on Arduino

BAUDRATE = 9600

#ser = serial.Serial(SERIALPORT, BAUDRATE, timeout =1)

root = tk.Tk()
root.geometry('2000x1000')
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
    
    ct = 0
    
    bt = 0.0
    ScoutName = ""
    ScoutTypeDisplay = ""
    weight_to_file = ""
    
    print("ScoutName = ")
    ScoutName=str(scout.get())
    print(ScoutName)
                 
    print("ScoutType = ")
    ScoutTypeDisplay=str(ScoutType.get())
    ScoutTypeDisplay=ScoutTypeDisplay.rstrip('\r\n')
    print(ScoutTypeDisplay)
    
    print("Donation Weight = ")
    weight_to_file = str(weight_to_display.get())
    weight_to_file = weight_to_file.rstrip("lbs")
    print(weight_to_file)
    
    
    
    
    if ScoutName != "":

        hs = open("/home/pi/Desktop/Food_Pantry_Donations.csv","a")
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
        
        scout.set("")
        
        
        
    
        showinfo(
            title='Saved',
            message=ScoutName+'  thank You For Your '+weight_to_file+' lbs Donation!'
            )
        
            
    else:
        showinfo(
            title='Error not saved',
            message='Please Name The '+ ScoutTypeDisplay
            
            )
        
        
def Tare_The_Scale():
    tare = 0
    Tare = get_serial("x")
    
    Tare = get_serial("1")
    
    Tare = get_serial("x")
    
    
    
btnSaveToFile = tk.Button(
            root,text = "Save To File",
            font=("Helvetica", 60),command = write_to_file).grid(row = 4,
                                                                 column = 2,
                                                                 columnspan = 1,
                                                                 rowspan = 3)
btnTare = tk.Button(
            root,text = "Tare",
            font=("Helvetica", 20),command = Tare_The_Scale).grid(row = 5,
                                                                 column = 3,
                                                                 columnspan = 1,
                                                                 rowspan = 1)


label1 = tk.Label(
        root,
        textvariable=(weight_to_display),
        font=("Helvetica", 200)).grid(row = 0, column = 0,columnspan = 3,rowspan = 3)
      
        
label2 = tk.Label(
        root,
        textvariable=(Bigtotal),
        font=("Helvetica", 60)).grid(row = 3, column = 2,columnspan = 1,rowspan = 1)       
        
label3 = tk.Label(
        root,
        text=("200lbs maxiumum on scale"),
        font=("Helvetica", 40)).grid(row = 3, column = 1,columnspan = 1,rowspan = 1)


NameEntry = tk.Entry(root,text = "boy",
                     textvariable  = scout,
                     font=("Helvetica", 60)).grid(row = 4,column = 1,columnspan=1,rowspan = 3)



    

r1 = tk.Radiobutton(root, text='Scout', value='Scout', variable=ScoutType).grid(row = 3, column = 0)     
r2 = tk.Radiobutton(root, text='Webelo', value='Webelo', variable=ScoutType).grid(row = 4, column = 0) 
r3 = tk.Radiobutton(root, text='Other', value='Other', variable=ScoutType).grid(row = 5, column = 0)



def my_mainloop():
    print("Main Loop")
    
    weight= get_serial("0")
    data0 = str(weight)
    data0 = data0 + "lbs"
    weight_to_display.set(data0)
    
    print("weight_to_display = "+ data0 )
        
    root.after(1000, my_mainloop)
    
    
root.after(1000, my_mainloop)

root.mainloop(
)
  

  

