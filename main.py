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

oneCm = [1, 0.393701, 0.0328084, 0.0108361, 0.0000062137]
oneIn = [2.54, 1, 0.08333, 0.0277778, 0.000015783]
oneFt = [30.48, 12, 1, 0.333333, 0.000189394]
oneYd = [91.44, 36, 3, 1, 0.000568182]
oneMi = [160934, 63360, 5280, 1760, 1]
'''
# Data for the top left portion (Imperial - Distance)
topLeftData = [0.0,0.0,0.0,0.0,0.0]

# IMPERIAL UNIT CONVERSIONS ====================================================================================
units = ["centimeters", "inches", "feet", "yards", "miles"]
rates = ["second", "minute", "hour"]

# Dictionary to associate the matrix [x][] position in the matrix unit conversion array
N_units = ["cm", "in", "ft", "yd", "mi"]
# Dictionary to associate in/out rates with their respective values 
N_rates = [("sec", 1), ("min", 60), ("hr", 3600)]
# Dictionary to associate output rate with respective values
N_outRates = [("Per second", 1), ("Per minute", 60), ("Per hour", 3600)]

#             cm       in         ft          yd          mi
allUnits =  [[1,       0.393701,  0.0328084,  0.0108361,  0.0000062137], # cm
             [2.54,    1,         0.08333,    0.0277778,  0.000015783],  # in
             [30.48,   12,        1,          0.333333,   0.000189394],  # ft
             [91.44,   36,        3,          1,          0.000568182],  # yd
             [160934,  63360,     5280,       1760,       1]]            # mi

# END IMPERIAL UNIT CONVERSIONS ====================================================================================           

# Perform calculations for the top left section
def N_topLeftCalculate():
    if tLeftInput.get() == "": # see if input is just empty spaces, ifSo: do nothing and send no errors 
            return False
    try:
        inputValue = float(tLeftInput.get()) # see if we can convert the input to float
    except:                                  # ifNot -> except (Means string was entered and can't convert to float value)
        tempVariable = tLeftInput.get() # temp variable of the input value     
        for i in range(1,30):           # loop through the multiple concatinations to see if multiple empty spaces are entered
            if tempVariable == " "*i:   # ifSo, no big deal and send no error message
                return False            
  
        if tempVariable[0:7] == "Invalid": # prevents the invalid response to be stacked onto itself
            return False

        tLeftInput.insert(0, "Invalid -> ") # otherwise and invalid string has been entered into the field
        return False                        # thus show error on input field and do no calculations
    # the reason for not caring about empty strings before or after numeric input is that the program can still do calculations with empty spaces before or after

    inputValue = float(tLeftInput.get()) 
    inputUnit = impSpeed_dropdownSelected_inputUnits.get()  
    inputRate = impSpeed_dropdownSelected_inputRates.get()
    outputRate = impSpeed_radioSelected_outputRates.get()
    matrix = 0

    # set units to the corresponding unit matrix
    for i in range(len(N_units)): # go thru each index of N_units array
        if N_units[i] == inputUnit: # see if the current index in array is equal to the current input unit string
            matrix = i  # ifSo, set matrix value equal to the current index of i since they are 1.1 linked
            break # done, end loop

    # set input rate
    for i in range(len(N_rates)): # go thru the N_rates array
        if N_rates[i][0] == inputRate: # see if the current index at position ZERO is equal to the inputted rate string 
            inputRate = N_rates[i][1] # ifSo, set inputRate = the current index in N_rates at position ONE
            break # done, end loop
    # had to use matrix style list since we have a string associated to a value
    # [i][0] is the 1.1 where the string will match to seek what is inputted
    # [i][1] is the associated value to what was inputted

    # set output rate
    for i in range(len(N_rates)): # go thru N_rates
        if N_outRates[i][0] == outputRate: # see if the current index at position ZERO == the inputted outputRate from user
            outputRate = N_outRates[i][1] # ifSo, set outputRate = the current index of list at position 1 
            break # done
    # [i][0] is the 1.1 where the string will match to seek what is inputted
    # [i][1] is the associated value to what was inputted

    # perform calculation
    for i in range(len(topLeftData)): # go through each index in the topLeftData list
        topLeftData[i] = (inputValue / inputRate) * allUnits[matrix][i] * outputRate
        # at current index in data list, set it equal to the inputted int value divided by its rate (1 / 60 / 3600 --> sec / min / hour) respectively
        #   then multiply that by the allUnits matrix at the set MATRIX at position i
        #       the way the allUnits is essentially a table that has all the conversions for a desired unit in each index with respect to an input unit
        #   lastly multiply by the outputRate (1 / 60 / 3600 --> sec / min / hour) respectively

    # display the data
    topLeftDisplay(topLeftData)
        
# called by the clear button to clear the top left output fields
def topLeftClear():
    for currIndex in range(len(topLeftData)): # go through each index in the data list
        topLeftData[currIndex] = 0  # set current index = 0
        tLeftInput.delete(0, END) # clears the integer entry field 
    topLeftDisplay(topLeftData) # display the cleaned output fields (the entry will update itself from above .delete method)

# Top left output displays Imperial - Speed
def topLeftDisplay(data):
    selectedOutRate = impSpeed_radioSelected_outputRates.get()
    displayOutRate = ""
    # set output rate
    for i in range(len(rates)): # go thru rates
        if N_outRates[i][0] == selectedOutRate: # see if the current index at position == desired output rate
            displayOutRate = rates[i] # ifSo, set outputRate = the current index of list
            break # done
        
    currRow = 10 # currRow is the row in which the label will be displayed for the output
    for currOutput in range(5): # currOutput is the current data entry being moved from the data to the respective row
        # this label below is to clear out any residual text that would otherwise remain since it is not associated with a variable
        Label(topLeftFrame_impSpeed, text = "                                                                                                    "
              , bg = "lightgray").grid(row = currRow, column = 0, padx = 7, pady = 3, sticky = "w") 
        # the label below is the data
        # ARG1: data[currOutput] is the data taken from the current index of the data passed from topLeftData
        # ARG2: is the current unit that will be displayed in the iteration respective to the row
        # ARG3: is a "per" string output to be between the unit "per" rate
        # ARG4: is the displayOutRate which is obtained from the for loop above this current one
        Label(topLeftFrame_impSpeed, text = (str(data[currOutput]), units[currOutput], "per", displayOutRate), bg = "lightgray").grid(row = currRow, column = 0, padx = 7, pady = 3, sticky = "w")
        currRow += 1 # move onto the next row, used for the lable grid position arguement where row = currRow


# Top left Frame that contains all the imperial speed inputs and outputs
topLeftFrame_impSpeed = LabelFrame(root, text = "Imperial - Speed", bg = "lightgray")
topLeftFrame_impSpeed.pack(padx = 5, pady = 5)

# Text above the input box
Label(topLeftFrame_impSpeed, text = "Input", bg = "lightgray").grid(row = 0, column = 0, padx = 5, pady = 3, sticky = "w")

# Input box where the user enters the value
tLeftInput = Entry(topLeftFrame_impSpeed, font = "Helvetica 17", width = 25)
tLeftInput.grid(row = 1, column = 0, padx = 5, pady = 0)

# Text above the dropdown box for input units
Label(topLeftFrame_impSpeed, text = "Unit", bg = "lightgray").grid(row = 0, column = 1)

# Options for the input units dropdown box
impSpeed_dropdownUnits = ["cm",
                          "in", 
                          "ft", 
                          "yd", 
                          "mi"]
impSpeed_dropdownSelected_inputUnits = StringVar()
impSpeed_dropdownSelected_inputUnits.set(impSpeed_dropdownUnits[0])

# Dropdown box object for the input units                                                                                 
impSpeed_dropdownBox_inputUnits = OptionMenu(topLeftFrame_impSpeed, impSpeed_dropdownSelected_inputUnits, *impSpeed_dropdownUnits)
impSpeed_dropdownBox_inputUnits.config(relief = "flat")
impSpeed_dropdownBox_inputUnits.grid(row = 1, column = 1)

# Text above the dropdown box for input rates
Label(topLeftFrame_impSpeed, text = "Rate", bg = "lightgray").grid(row = 0, column = 2)

# Options for the dropdown box for the input rates
impSpeed_dropdownRates = ["sec", 
                          "min", 
                          "hr"]
impSpeed_dropdownSelected_inputRates = StringVar()
impSpeed_dropdownSelected_inputRates.set(impSpeed_dropdownRates[0])

# Dropwdown box object for the input rates
impSpeed_dropdownBox_inputRates = OptionMenu(topLeftFrame_impSpeed, impSpeed_dropdownSelected_inputRates, *impSpeed_dropdownRates)
impSpeed_dropdownBox_inputRates.config(relief = "flat")
impSpeed_dropdownBox_inputRates.grid(row = 1, column = 2, padx = 4)

# Spacer
Label(topLeftFrame_impSpeed, text = "", bg = "lightgray", font = "Helvetica 1").grid(row = 2, column = 0, sticky = "w")

Label(topLeftFrame_impSpeed, text = "Output rate", bg = "lightgray").grid(row = 3, column = 0, padx = 5, sticky = "w")

# Options for the radio buttons
impSpeed_radio_ratesOptions = [("Per second", "Per second"), 
                               ("Per minute", "Per minute"), 
                               ("Per hour    ", "Per hour")]
impSpeed_radioSelected_outputRates = StringVar()
impSpeed_radioSelected_outputRates.set("Per second")

# Loop to create each radio button option
i = 4
for text, selected in impSpeed_radio_ratesOptions:
    Radiobutton(topLeftFrame_impSpeed, text = text, variable = impSpeed_radioSelected_outputRates, value = selected, command = N_topLeftCalculate,bg = "lightgray").grid(row = i, column = 0, padx = 5, sticky = "w")
    i += 1

# Spacer
Label(topLeftFrame_impSpeed, text = "", bg = "lightgray", font = "Helvetica 1").grid(row = 7, column = 0, sticky = "w")

# Text above the output fields
Label(topLeftFrame_impSpeed, text = "Results", bg = "lightgray").grid(row = 9, column = 0, padx = 7, pady = 0, sticky = "w")

# Calculate button
Button(topLeftFrame_impSpeed, text = "CALCULATE", command = N_topLeftCalculate).grid(row = 8, column = 0, padx = 7, pady = 5, sticky = "w")

# Clear button
Button(topLeftFrame_impSpeed, text = "CLEAR", command = topLeftClear).grid(row = 8, column = 0, padx = 90, pady = 5, sticky = "w")

# Display the output fields to not have empty space and be somewhat jarring if the user calculates an input and sees the output appear out of nowhere
topLeftDisplay(topLeftData)


# Display the mainloop of tkinter
root.mainloop()