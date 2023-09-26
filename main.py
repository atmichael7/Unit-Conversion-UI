from tkinter import *

# create root window
root = Tk()
root.title("Mikes Units")
root.config(bg="lightgray")

'''
1 cm = 1 cm
1 cm = 0.393701 inches
1 cm = 0.0328084 feet
1 cm = 0.0108361 yards
1 cm = 0.0000062137 miles
===============================
1 inch = 2.54 cm
1 inch = 1 inch
1 inch = 0.08333 feet
1 inch = 0.0277778 yards
1 inch = 0.000015783 miles
===============================
1 ft = 30.48 cm
1 ft = 12 in
1 ft = 1 ft
1 ft = 0.333333 yd
1 ft = 0.000189394 mi
===============================
1 yd = 91.44 cm
1 yd = 36 in
1 yd = 3 ft
1 yd = 1 yd
1 yd = 0.000568182 mi
===============================
1 mi = 160934 cm
1 mi = 63360 in
1 mi = 5280 ft
1 mi = 1760 yd
1 mi = 1 mi
'''
oneCm = [1, 0.393701, 0.0328084, 0.0108361, 0.0000062137]
oneIn = [2.54, 1, 0.08333, 0.0277778, 0.000015783]
oneFt = [30.48, 12, 1, 0.333333, 0.000189394]
oneYd = [91.44, 36, 3, 1, 0.000568182]
oneMi = [160934, 63360, 5280, 1760, 1]

units = ["centimeters", "inches", "feet", "yards", "miles"]
rates = ["second", "minute", "hour"]

#             cm       in         ft          yd          mi
allUnits =  [[1,       0.393701,  0.0328084,  0.0108361,  0.0000062137], # cm
             [2.54,    1,         0.08333,    0.0277778,  0.000015783],  # in
             [30.48,   12,        1,          0.333333,   0.000189394],  # ft
             [91.44,   36,        3,          1,          0.000568182],  # yd
             [160934,  63360,     5280,       1760,       1]]            # mi 

# WILL NEED TO BE UPDATED AFTER VALUES ARE CHANGED
topLeftData = [0.0,0.0,0.0,0.0,0.0]

def getInputValue():
    return tLeftInput.get()

def getInputUnit():
    return clicked1.get()

def getInputRate():
    return clicked2.get()

def getOutputRate():
    return clicked3.get()

#def updateData(data):
#    topLeftDisplay(data)

# Upper left Imperial Speed
def testUpdateData(data):
    sampleList = [20.0, 15.0, 10.0, 5.0, 1.0]
    for i in range(10):
        for x in range(len(data)):
            sampleList[x-1] = sampleList[x-1]*2
            data[x-1] = sampleList[x-1]
    topLeftDisplay(data)



# Call this function
def topLeftCalculate():
    
    if tLeftInput.get() == "":
            return False
    
    try:
        inputValue = float(tLeftInput.get())
    except:
        tempVariable = tLeftInput.get()
        for i in range(1,30):
            if tempVariable == " "*i:
                return False
        tLeftInput.insert(0, "Invalid -> ")
        return False

    inputValue = float(tLeftInput.get())
    inputUnit = clicked1.get()
    inputRate = clicked2.get()
    outputRate = clicked3.get()


    if inputUnit == "cm":
        matrix = 0
        if inputRate == "sec":
            if outputRate == "Per second":
                for i in range(len(topLeftData)):
                    topLeftData[i-1] = inputValue * allUnits[matrix][i-1] * 1
            elif outputRate == "Per minute":
                for i in range(len(topLeftData)):
                    topLeftData[i-1] = inputValue * allUnits[matrix][i-1] * 60
            else:
                for i in range(len(topLeftData)):
                    topLeftData[i-1] = inputValue * allUnits[matrix][i-1] * (60 * 60)

        elif inputRate == "min":
            if outputRate == "Per second":
                for i in range(len(topLeftData)):
                    topLeftData[i-1] = (inputValue/60) * allUnits[matrix][i-1] * 1
            elif outputRate == "Per minute":
                for i in range(len(topLeftData)):
                    topLeftData[i-1] = (inputValue/60) * allUnits[matrix][i-1] * 60
            else:
                for i in range(len(topLeftData)):
                    topLeftData[i-1] = (inputValue/60) * allUnits[matrix][i-1] * (60 * 60)

        else:
            if outputRate == "Per second":
                for i in range(len(topLeftData)):
                    topLeftData[i-1] = (inputValue/(60*60)) * allUnits[matrix][i-1] * 1
            elif outputRate == "Per minute":
                for i in range(len(topLeftData)):
                    topLeftData[i-1] = (inputValue/(60*60)) * allUnits[matrix][i-1] * 60
            else:
                for i in range(len(topLeftData)):
                    topLeftData[i-1] = (inputValue/(60*60)) * allUnits[matrix][i-1] * (60 * 60)

    
    elif inputUnit == "in":
        matrix = 1
        if inputRate == "sec":
            if outputRate == "Per second":
                for i in range(len(topLeftData)):
                    topLeftData[i-1] = inputValue * allUnits[matrix][i-1] * 1
            elif outputRate == "Per minute":
                for i in range(len(topLeftData)):
                    topLeftData[i-1] = inputValue * allUnits[matrix][i-1] * 60
            else:
                for i in range(len(topLeftData)):
                    topLeftData[i-1] = inputValue * allUnits[matrix][i-1] * (60 * 60)

        elif inputRate == "min":
            if outputRate == "Per second":
                for i in range(len(topLeftData)):
                    topLeftData[i-1] = (inputValue/60) * allUnits[matrix][i-1] * 1
            elif outputRate == "Per minute":
                for i in range(len(topLeftData)):
                    topLeftData[i-1] = (inputValue/60) * allUnits[matrix][i-1] * 60
            else:
                for i in range(len(topLeftData)):
                    topLeftData[i-1] = (inputValue/60) * allUnits[matrix][i-1] * (60 * 60)
        
        else:
            if outputRate == "Per second":
                for i in range(len(topLeftData)):
                    topLeftData[i-1] = (inputValue/(60*60)) * allUnits[matrix][i-1] * 1
            elif outputRate == "Per minute":
                for i in range(len(topLeftData)):
                    topLeftData[i-1] = (inputValue/(60*60)) * allUnits[matrix][i-1] * 60
            else:
                for i in range(len(topLeftData)):
                    topLeftData[i-1] = (inputValue/(60*60)) * allUnits[matrix][i-1] * (60 * 60)


    elif inputUnit == "ft":
        matrix = 2
        if inputRate == "sec":
            if outputRate == "Per second":
                for i in range(len(topLeftData)):
                    topLeftData[i-1] = inputValue * allUnits[matrix][i-1] * 1
            elif outputRate == "Per minute":
                for i in range(len(topLeftData)):
                    topLeftData[i-1] = inputValue * allUnits[matrix][i-1] * 60
            else:
                for i in range(len(topLeftData)):
                    topLeftData[i-1] = inputValue * allUnits[matrix][i-1] * (60 * 60)

        elif inputRate == "min":
            if outputRate == "Per second":
                for i in range(len(topLeftData)):
                    topLeftData[i-1] = (inputValue/60) * allUnits[matrix][i-1] * 1
            elif outputRate == "Per minute":
                for i in range(len(topLeftData)):
                    topLeftData[i-1] = (inputValue/60) * allUnits[matrix][i-1] * 60
            else:
                for i in range(len(topLeftData)):
                    topLeftData[i-1] = (inputValue/60) * allUnits[matrix][i-1] * (60 * 60)
        
        else:
            if outputRate == "Per second":
                for i in range(len(topLeftData)):
                    topLeftData[i-1] = (inputValue/(60*60)) * allUnits[matrix][i-1] * 1
            elif outputRate == "Per minute":
                for i in range(len(topLeftData)):
                    topLeftData[i-1] = (inputValue/(60*60)) * allUnits[matrix][i-1] * 60
            else:
                for i in range(len(topLeftData)):
                    topLeftData[i-1] = (inputValue/(60*60)) * allUnits[matrix][i-1] * (60 * 60)

    
    elif inputUnit == "yd":
        matrix = 3
        if inputRate == "sec":
            if outputRate == "Per second":
                for i in range(len(topLeftData)):
                    topLeftData[i-1] = inputValue * allUnits[matrix][i-1] * 1
            elif outputRate == "Per minute":
                for i in range(len(topLeftData)):
                    topLeftData[i-1] = inputValue * allUnits[matrix][i-1] * 60
            else:
                for i in range(len(topLeftData)):
                    topLeftData[i-1] = inputValue * allUnits[matrix][i-1] * (60 * 60)

        elif inputRate == "min":
            if outputRate == "Per second":
                for i in range(len(topLeftData)):
                    topLeftData[i-1] = (inputValue/60) * allUnits[matrix][i-1] * 1
            elif outputRate == "Per minute":
                for i in range(len(topLeftData)):
                    topLeftData[i-1] = (inputValue/60) * allUnits[matrix][i-1] * 60
            else:
                for i in range(len(topLeftData)):
                    topLeftData[i-1] = (inputValue/60) * allUnits[matrix][i-1] * (60 * 60)
        
        else:
            if outputRate == "Per second":
                for i in range(len(topLeftData)):
                    topLeftData[i-1] = (inputValue/(60*60)) * allUnits[matrix][i-1] * 1
            elif outputRate == "Per minute":
                for i in range(len(topLeftData)):
                    topLeftData[i-1] = (inputValue/(60*60)) * allUnits[matrix][i-1] * 60
            else:
                for i in range(len(topLeftData)):
                    topLeftData[i-1] = (inputValue/(60*60)) * allUnits[matrix][i-1] * (60 * 60)


    else: # input unit == mi
        matrix = 4
        if inputRate == "sec":
            if outputRate == "Per second":
                for i in range(len(topLeftData)):
                    topLeftData[i-1] = inputValue * allUnits[matrix][i-1] * 1
            elif outputRate == "Per minute":
                for i in range(len(topLeftData)):
                    topLeftData[i-1] = inputValue * allUnits[matrix][i-1] * 60
            else:
                for i in range(len(topLeftData)):
                    topLeftData[i-1] = inputValue * allUnits[matrix][i-1] * (60 * 60)

        elif inputRate == "min":
            if outputRate == "Per second":
                for i in range(len(topLeftData)):
                    topLeftData[i-1] = (inputValue/60) * allUnits[matrix][i-1] * 1
            elif outputRate == "Per minute":
                for i in range(len(topLeftData)):
                    topLeftData[i-1] = (inputValue/60) * allUnits[matrix][i-1] * 60
            else:
                for i in range(len(topLeftData)):
                    topLeftData[i-1] = (inputValue/60) * allUnits[matrix][i-1] * (60 * 60)
        
        else:
            if outputRate == "Per second":
                for i in range(len(topLeftData)):
                    topLeftData[i-1] = (inputValue/(60*60)) * allUnits[matrix][i-1] * 1
            elif outputRate == "Per minute":
                for i in range(len(topLeftData)):
                    topLeftData[i-1] = (inputValue/(60*60)) * allUnits[matrix][i-1] * 60
            else:
                for i in range(len(topLeftData)):
                    topLeftData[i-1] = (inputValue/(60*60)) * allUnits[matrix][i-1] * (60 * 60)

    topLeftDisplay(topLeftData)

        
       
def topLeftClear():
    for currIndex in range(len(topLeftData)):
        topLeftData[currIndex-1] = 0
        tLeftInput.delete(0, END)
    topLeftDisplay(topLeftData)

def notifyDisplay():
    topLeftCalculate()
    topLeftDisplay(topLeftData)

# Top left output displays Imperial - Speed
def topLeftDisplay(data):
    i = 10
    outputRateStuff = clicked3.get()
    if outputRateStuff == "Per second":
        outputRateStuff = rates[0]
    elif outputRateStuff == "Per minute":
        outputRateStuff = rates[1]
    else:
        outputRateStuff = rates[2]
        
    for x in range(5):
        outputUnitStuff = units[x]
        Label(tLeftLabel, text = "                                                                      ", bg = "lightgray").grid(row = i, column = 0, padx = 7, pady = 3, sticky = "w")
        Label(tLeftLabel, text = (str(data[x]), outputUnitStuff, "per", outputRateStuff), bg = "lightgray").grid(row = i, column = 0, padx = 7, pady = 3, sticky = "w")
        i += 1


# Upper left
tLeftLabel = LabelFrame(root, text = "Imperial - Speed", bg = "lightgray")
tLeftLabel.pack(padx = 5, pady = 5)
# Input field text
inputBoxText = Label(tLeftLabel, text = "Input", bg = "lightgray")
inputBoxText.grid(row = 0, column = 0, padx = 5, pady = 3, sticky = "w")
# Input field box
tLeftInput = Entry(tLeftLabel, font = "Helvetica 17")
tLeftInput.grid(row = 1, column = 0, padx = 5, pady = 0)
# Input field 2 text
inputBoxText1 = Label(tLeftLabel, text = "Unit", bg = "lightgray")
inputBoxText1.grid(row = 0, column = 1)
# Input field 2 box
options1 = ["cm", 
            "in", 
            "ft", 
            "yd", 
            "mi"]
clicked1 = StringVar()
clicked1.set(options1[0])
dropdown1 = OptionMenu(tLeftLabel, clicked1, *options1)
dropdown1.config(relief = "flat")
dropdown1.grid(row = 1, column = 1)
# Input field 3 text
inputBoxText2 = Label(tLeftLabel, text = "Rate", bg = "lightgray")
inputBoxText2.grid(row = 0, column = 2)
# Input field 3 box
options2 = ["sec", 
            "min", 
            "hr"]
clicked2 = StringVar()
clicked2.set(options2[0])
dropdown2 = OptionMenu(tLeftLabel, clicked2, *options2)
dropdown2.config(relief = "flat")
dropdown2.grid(row = 1, column = 2, padx = 4)
# Input field 4 text 
# Spacer
spacerbox = Label(tLeftLabel, text = "", bg = "lightgray", font = "Helvetica 1")
spacerbox.grid(row = 2, column = 0, sticky = "w")
# End Spacer
inputBoxText4 = Label(tLeftLabel, text = "Output rate", bg = "lightgray")
inputBoxText4.grid(row = 3, column = 0, padx = 5, sticky = "w")
# Input field 4 radio
options3 = [("Per second", "Per second"), 
            ("Per minute", "Per minute"), 
            ("Per hour    ", "Per hour")]
clicked3 = StringVar()
clicked3.set("Per second")

i = 4
for text, selected in options3:
    Radiobutton(tLeftLabel, text = text, variable = clicked3, value = selected, command = notifyDisplay,bg = "lightgray").grid(row = i, column = 0, padx = 5, sticky = "w")
    i += 1


# Output fields
# Spacer
spacerbox = Label(tLeftLabel, text = "", bg = "lightgray", font = "Helvetica 1")
spacerbox.grid(row = 7, column = 0, sticky = "w")
# End Spacer


output1 = Label(tLeftLabel, text = "Results", bg = "lightgray")
output1.grid(row = 9, column = 0, padx = 7, pady = 0, sticky = "w")

topLeftDisplay(topLeftData)


# Calculate button
b1 = Button(tLeftLabel, text = "CALCULATE", command = topLeftCalculate)
b1.grid(row = 8, column = 0, padx = 7, pady = 5, sticky = "w")

# Clear button
b1 = Button(tLeftLabel, text = "CLEAR", command = topLeftClear)
b1.grid(row = 8, column = 0, padx = 90, pady = 5, sticky = "w")





'''
# Create Frame widget
left_frame = Frame(root, width=200, height=800)
left_frame.grid(row=0, column=0, padx=10, pady=5)

# Create frame within left_frame
#tool_bar = Frame(left_frame, width=180, height=185, bg="purple")
#tool_bar.grid(row=2, column=0, padx=5, pady=5)


Label(left_frame, text="Example Text").grid(row=1, column=0, padx=5, pady=5)

'''

root.mainloop()