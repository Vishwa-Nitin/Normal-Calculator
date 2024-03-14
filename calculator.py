import PySimpleGUI as sg

#layout
layout  =   [
    [sg.InputText(default_text=" ", size=(20,2), key="input")], #display
    [sg.Button("7", size=(4,2),key="7"), sg.Button("8", size=(4,2),key="8"),    #1st row
     sg.Button("9", size=(4,2),key="9"), sg.Button("/", size=(4,2),key="/"),],  
    [sg.Button("4", size=(4,2),key="4"), sg.Button("5", size=(4,2),key="5"),    #2nd row
     sg.Button("6", size=(4,2),key="6"), sg.Button("*", size=(4,2),key="*")],
    [sg.Button("1", size=(4,2),key="1"), sg.Button("2", size=(4,2),key="2"),    #3rd row
     sg.Button("3", size=(4,2),key="3"), sg.Button("-", size=(4,2),key="-")],
    [sg.Button("0", size=(4,2),key="0"), sg.Button(".", size=(4,2),key="."),    #4th row
     sg.Button("=", size=(4,2),key="equal"), sg.Button("+", size=(4,2),key="+")]
]


#window
calculator = sg.Window("Calculator",layout  =   layout, resizable=True,
             font=("Times New Roman",24))

#function
def update(events):                             #for getting events
    input_element   =   calculator["input"]     #input element out
    current_value   =   input_element.get()     #7
    input_element.update(current_value+events)  #7+1

def calculate(events):                          
    input_element   =   calculator["input"]   #input element out
    current_value   =   input_element.get()   #7
    try:                                     #try for use to acccepting the values
        ans =   eval(current_value)         #eval(evaluate) is use for making events like add,sum,etc.
        input_element.update(ans)
    except:                                     #except is use for like we type someting extra
                                                # the display became blank
        input_element.update(" ")               #update answer like 7+2=9


#loop
while True:
    events, values = calculator.read()
    if events == sg.WIN_CLOSED:
        break
    if events in "0123456789.+-*/":     #input when clicking on a button
        update(events)
    if events   ==   "equal":           #to calculate the numbers
        calculate(events)



    
#window close
calculator.close()