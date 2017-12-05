from Tkinter import *
from PIL import Image, ImageTk

#create a widget called app, adding its size, title, and background color
app = Tk()
app.geometry("600x600")
app.title("Aquatic Chrono-converter")
app.configure(background="#4ED")

#I create 4 arrays to merge and create all the events in swimming
strokes = ["Butterfly", "Backstroke", "Breastroke", "Freestyle", "IM"]
strokeDistance = ["50", "100", "200"]
imDistance = ["100", "200", "400"]
freestyleDistance = ["50", "100", "200", "400/500", "800/1000", "1500/1650"]

#add an empty array to accept all the merged items from the arrays above
EVENTS = []

#This function will run to create the array events to list all the events in swimming
def createEvents():
    #for each stroke in the array strokes concatinate the apropriate distance with stroke
    for stroke in strokes:
        #in swimming not every stroke has the same distances, so I created if statements to seperate the different distances of stroke
        if stroke == "Freestyle":
            for dist in freestyleDistance:
                #add the event to the list EVENTS
                EVENTS.append(dist + " " + stroke)
        elif stroke == "IM":
            for dista in imDistance:
                EVENTS.append(dista + " " + stroke)
        else:
            for distance in strokeDistance:
                EVENTS.append(distance + " " + stroke)
#run function to create EVENTS list
createEvents()

#The items in course are the different pool types in swimming
#LCM: Long Course Meters (Olympic size pool), SCM: Short Course Meters (international norm pool), and SCY: Short Course Yards (college size pool for America)
COURSE = ["LCM","SCM","SCY"]

#create a variable to start an option menu and to call back the selection from the option menu
variableEvent = StringVar(app)
variableEvent.set("Select Event")

#create the option menu by using the tuple function to add all items in the EVENTS list as an option
#set to grid, place it, and change background color
events = apply(OptionMenu, (app, variableEvent) + tuple(EVENTS))
events.grid()
events.place(x=0, y=0)
events.configure(background="#4ED")

#same procedure as before accept now applying a option menu to the COURSE array
variableCourse = StringVar(app)
variableCourse.set("Select Course")

course = apply(OptionMenu, (app, variableCourse) + tuple(COURSE))
course.grid()
course.place(x=450, y=0)
course.configure(background="#4ED")

#Texts are bellow---------------------------------------------------------------
#create a text assigned to the variable colon
colon = Text(app, height=1, width=1)
#insert the text ":" and place it
colon.insert(INSERT, ":")
colon.place(x=45, y=80)
colon.configure(background="#4ED", highlightbackground="#4ED")

#create a text assigned to the variable period
period = Text(app, height=1, width=1)
#insert the text "." and place it
period.insert(INSERT, ".")
period.place(x=96, y=88)
period.configure(background="#4ED", highlightbackground="#4ED")

#add the first conversion text box, which the first converted time will be inserted in
convert1 = Text(app, height=1, width=25)
convert1.place(x=400, y=70)

#add the second conversion text box, which the second converted time will be inserted in
convert2 = Text(app, height=1, width=25)
convert2.place(x=400, y=110)

time1 = Text(app, height=1, width=80)
time1.place(x=10, y=250)

time2 = Text(app, height=1, width=80)
time2.place(x=10, y=300)

time3 = Text(app, height=1, width=80)
time3.place(x=10, y=350)

time4 = Text(app, height=1, width=80)
time4.place(x=10, y=400)

time5 = Text(app, height=1, width=80)
time5.place(x=10, y=450)

#Entries are bellow-------------------------------------------------------------
#add an entry text box for the user to input desired minutes of their time to convert and assign it to minutes
minutes = Entry(app, width=3)
#place it
minutes.place(x=10, y=80)
#dont insert anything in text box prior to input from user
minutes.insert(0, "")
minutes.configure(highlightbackground="#4ED")

#add an entry text box for the user to input desired seconds of their time to convert and assign it to seconds
seconds = Entry(app, width=3)
seconds.place(x=60, y=80)
seconds.insert(0, "")
seconds.configure(highlightbackground="#4ED")

#add an entry text box for the user to input desired hundreths of their time to convert and assign it to hundreths
hundreths = Entry(app, width=3)
hundreths.place(x=110, y=80)
hundreths.insert(0, "")
hundreths.configure(highlightbackground="#4ED")

#Radio buttons are bellow-------------------------------------------------------
radioButton = IntVar()

#add a radio button designated for a sprinter
sprintButton = Radiobutton(app, text="Sprint", variable=radioButton, value=1)
sprintButton.place(x=10, y=150)
sprintButton.configure(background="#4ED")

#add a radio button designated for mid-distance swimmers
midButton = Radiobutton(app, text="Mid-Distance", variable=radioButton, value=2)
midButton.place(x=230, y=150)
midButton.configure(background="#4ED")

#add a radio button designated for distance swimmers
distButton = Radiobutton(app, text="Distance", variable=radioButton, value=3)
distButton.place(x=500, y=150)
distButton.configure(background="#4ED")

#Converter is bellow------------------------------------------------------------
#create a function get time to get the time inputted by user
def getTime():
    #set the inputted minutes to the variable minute
    minute = minutes.get()
    #set the inputted seconds to the variable second
    second = seconds.get()
    #set the inputted hundreths to the variable hundreth
    hundreth = hundreths.get()
    #if the user did not input a minute, second, or hundreth then default to zero, since this is most likely what the user means
    if minute == "":
        minute = 0
    else:
        #take the minutes and convert it to seconds and make it an integer
        minute = int(minute)*60

    if second == "":
        second = 0
    else:
        #make the seconds an integer
        second = int(second)
    if hundreth == "":
        hundreth = 0
    else:
        #take the hundreths, make it a float, and convert it to seconds
        hundreth = int(hundreth)/float(100)
    #this function will return the total seconds of the minutes, seconds, and hundreths inputted by the user
    return minute+second+hundreth

#create a function to get the event inpputed by user
def getEvent():
    #get the event inputted and assign it to evt
    evt = variableEvent.get()
    #create a event multiplier to multiply the total time
    evtMultiplier = 1
    #for each item in the list EVENTS check which one matches the inputted event
    for event in EVENTS:
        if evt == event:
            index = EVENTS.index(evt)
            #once the event is found find which stroke is being swam
            if index < 3:
                #based on the stroke we can decide how much the swimmer is likely to slow down and edit the event multiplier apropriately
                evtMultiplier = 1.002
            elif index > 2 and index < 6:
                evtMultiplier = 1.001
            elif index > 5 and index < 9:
                evtMultiplier = 1.001
            elif index > 14 and index < 18:
                evtMultiplier = 1.002
    #the function will return the event multiplier
    return evtMultiplier

#create a function to convert the time
def convert():
    #get the inputted course and assign it to course
    course = variableCourse.get()
    #check the selected radio button and assign the value to pref
    pref = radioButton.get()
    #run function getTime and assign the return to time
    time = getTime()
    #run function getEvent and assign the return to event
    event = getEvent()
    #find the course selected through if statements
    if course == "LCM":
        #if the user selected sprinter or mid distance swimmer apply all multipliers to time and convert apropriately
        if pref is 1 or pref is 2:
            out1 = float(0.88*time*event)
            out2 = float(0.98*time*event)
            #pass the times to function checkDistance
            checkDistance(out1,out2)
        else:
            out1 = float(1.001*0.88*time*event)
            out2 = float(1.001*0.98*time*event)
            checkDistance(out1,out2)
    #same process follows for each type of pool
    elif course == "SCM":
        if pref is 2:
            out1 = float(1.03*time*event)
            out2 = float(0.9*time*event)
            checkDistance(out1,out2)
        else:
            out1 = float(1.001*1.03*time*event)
            out2 = float(1.001*0.9*time*event)
            checkDistance(out1,out2)
    else:
        if pref is 2 or pref is 3:
            out1 = float(1.13*time*event)
            out2 = float(1.11*time*event)
            checkDistance(out1,out2)
        else:
            out1 = float(1.001*1.13*time*event)
            out2 = float(1.001*1.11*time*event)
            checkDistance(out1,out2)

#create function checkDistance to check distance of inputted event and apply conversions accordingly
def checkDistance(c1,c2):
    #get the inputted event and assign it to evt
    evt = variableEvent.get()
    #get inputted course and assign it to course
    course = variableCourse.get()
    for event in EVENTS:
        if evt == event:
            index = EVENTS.index(evt)
            if course == "LCM" or course == "SCM":
                #check to see if the inputted event is a distance free event
                #in swimming the different pools adjust lengths to be different for the same event
                if index is 12:
                    #divide the time by a common denominator between the differentiating lengths of the event
                    check1 = c1/4
                    check1 *= 5
                    check2 = c2
                elif index is 13:
                    check1 = c1/8
                    check1 *= 10
                    check2 = c2
                elif index is 14:
                    check1 = c1/15
                    check1 *= 16.5
                else:
                    check1 = c1
                    check2 = c2
            #same process for a SCY pool
            elif course == "SCY":
                if index is 12:
                    check1 = c1/5
                    check1 *= 4
                    check2 = c2/5
                    check2 *= 4
                elif index is 13:
                    check1 = c1/10
                    check1 *= 8
                    check2 = c2/10
                    check2 *= 8
                elif index is 14:
                    check1 = c1/16.5
                    check1 *= 15
                    check2 = c2/16.5
                    check2 *= 15
                else:
                    check1 = c1
                    check2 = c2
    #pass the checked times to convertOutput function
    convertOutput(check1,check2)

#create funciton convertOutput to convert the converted times back to the original format
def convertOutput(o1,o2):
    #convert the time back to the original format
    #get the number of minutes out of the total time
    min1 = float(o1)/60
    #make minutes an integer to drop the hundreths
    min1 = int(min1)
    #take the minutes out of the total time and assign it to seconds
    sec1 = float(o1)-(min1*60)
    #round the seconds to two decimals
    sec1 = round(sec1,2)
    #if the seconds are lower than 10 add a zero in front of the seconds for formatting purposes
    if sec1 < 10:
        sec1 = "0" + str(sec1)
    #format the minutes and seconds accordingly, put them in one string assigned to the first converted time
    time1 = str(min1) + ":" + str(sec1)
    #repeat the process for the first conversion to the second time
    min2 = float(o2)/60
    min2 = int(min2)
    sec2 = float(o2)-(min2*60)
    sec2 = round(sec2,2)
    if sec2 < 10:
        sec2 = "0" + str(sec2)
    time2 = str(min2) + ":" + str(sec2)
    #pass the two converted times to function displayTime
    displayTime(time1,time2)

#create function displayTime to display the converted times inside of the convert1 and convert2 textboxes
def displayTime(t1,t2):
    #get the inputted course
    course = variableCourse.get()
    #change the converted times to strings
    t1 = str(t1)
    t2 = str(t2)
    #check what distance the user would like to convert from
    if course == "LCM":
        #create a string for the converted times and assign them to ouput1 and output2
        output1 = "Time (SCY): " + t1
        output2 = "Time (SCM): " + t2
    elif course =="SCM":
        #same process as others, but for different distances
        output1 = "Time (LCM): " + t1
        output2 = "Time (SCY): " + t2
    else:
        output1 = "Time (LCM): " + t1
        output2 = "Time (SCM): " + t2
    #delete whatever text is in convert1
    convert1.delete(1.0, END)
    #insert the output for the converted times in convert1
    convert1.insert(INSERT, output1)
    #delete whatever text is in convert2
    convert2.delete(1.0, END)
    #insert the output for the converted times in convert2
    convert2.insert(INSERT, output2)
#-------------------------------------------------------------------------------
lines = []
def save():
    conversion1 = convert1.get("1.0",END)
    conversion2 = convert2.get("1.0",END)
    minute = minutes.get()
    second = seconds.get()
    hundreth = hundreths.get()
    course = variableCourse.get()
    event = variableEvent.get()
    time = minute + ":" + second + "." + hundreth
    save = event+' | '+'Time ('+course+'): '+time+', '+conversion1+', '+conversion2
    save = save.replace('\n', '')
    lines.append(save+"\n")
    f = open("times.txt", "w")
    f.writelines(lines)
    f.close
    viewConversions()

def viewConversions():
    time1.insert(INSERT, lines[0])
    time2.insert(INSERT, lines[1])
    time3.insert(INSERT, lines[2])
    time4.insert(INSERT, lines[3])
    time5.insert(INSERT, lines[4])

#create a button to convert the inputted time, place it, and change highlighted background
converterButton = Button(app, text="convert", command=convert)
converterButton.place(x=150, y=80)
converterButton.configure(highlightbackground="#4ED")

saveConversion = Button(app, text="save conversion", command=save)
saveConversion.place(x=230, y=0)
saveConversion.configure(highlightbackground="#4ED")
#-------------------------------------------------------------------------------

app.mainloop()
