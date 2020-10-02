from tkinter import *
import random
import webbrowser
import datetime

def chooseTask():
    tasks = ["Exercise outside", "Learn a new hobby", "Eat a piece of fruit", "Write or read a story", "Drink water"]
    print("Chosen task is: ", random.choice(tasks), "\n")

def checkSymptom():
    if option.get() == "Cough" or option.get() == "Fever" or option.get() == "Loss of taste/smell":
        print(option.get(), "is a symptom of Covid19. Guidance is to self-isolate.\n")
    elif option.get() == "Breathless":
        print(option.get(), "is a serious symptom of Covid19. Guidance is to call NHS 111.\n")
    else:
        print(option.get(), "is NOT a symptom of Covid19.\n")

def giveSupport():
    quotes = ["You're doing us proud!", "Stay strong, keep it up!", "You're an inspiration!"]
    print(random.choice(quotes))

def watchVid():
    urls = ["https://www.youtube.com/watch?v=A3GVPKzlOxo", "https://www.youtube.com/watch?v=fWfU3qoREcs", "https://www.youtube.com/watch?v=1UcGv5PJET0"]
    webbrowser.open(random.choice(urls))
    

#GUI
master = Tk()
master.title("Coronavirus App")

Label(master, text="CURE CORONAVIRUS BOREDOM").grid(row=0, column=0, padx=10)
Label(master, text="STAY HOME > PROTECT THE NHS > SAVE LIVES", fg="blue", bg="white").grid(row=1, column=0, padx=10)

Label(master, text="Do I have symptoms?").grid(row=2, pady=10)
option = StringVar(master)
option.set("View")
#updated symptoms list 02/10/2020
symptom = OptionMenu(master,option, "Breathless", "Continuous Cough", "Fever", "Loss/change of taste/smell", "Shivering") #alphabetised
symptom.grid(row=2, column=1, sticky=W)

Button(master, text='Check Symptom', command=checkSymptom).grid(row=2, column=2, sticky=W, pady=10)

Label(master, text="Choose a task").grid(row=3)
Button(master, text='Click here', command=chooseTask).grid(row=3, column=1, sticky=W, pady=10)

Label(master, text="Get Support").grid(row=4)
Button(master, text='Get quote', command=giveSupport).grid(row=4, column=1, sticky=W, pady=10)

Label(master, text="Watch a Nice Video").grid(row=5)
Button(master, text='View video', command=watchVid).grid(row=5, column=1, sticky=W, pady=10)

mainloop()
