# snake_case, lowercase, meaningful variables
# denote data type
# comment to make sense of functions
# no obvious comments
# enumerate/zip where possible
# no try except pass?

import os
import random
from tkinter import HORIZONTAL, Text, Toplevel, Listbox, Label, Button, END, ttk
from tkinter.ttk import Progressbar
import json
from time import time, strftime
import time
import datetime
from tkinter.messagebox import askyesno
import tkinter.messagebox
import tkinter
import matplotlib.pyplot as plt
import numpy as np

text1 = """                                           ABOUT
Deep Focus Logbook was inspired by productivity books such as "Deep Work" and "Digital Minimalism" by Cal Newport, "Atomic Habits" by James Nestor and "Peak" by Anders Ericson and Robert Pool. These books, among many others, affirm the importance of deliberate, focused attention in order to efficiently study and work in high-value fields.

Fields such as programming, creative writing can benefit from deep focus the most. It takes time and concentration to keep track and get into the code or a narrative. Maintaining concentration for extended periods of times can be very fruitful.

Deep Focus Logbook is a way to monitor the time spent on focused work. It will  not protect you against outside distractions if you work at an office or a busy home, but it can act as a motivator to keep away from  social media and any other distracting online activities, at least for the duration of the timer. When the concentration is broken or work is done, simply click the stop button to add the time to the list. You can use the logbook to monitor your performance between days as well.

Deep Focus Logbook's goal is to instrumentalize and gamify the learning process by assigning and tracking the time spent on focused work. Challenge yourself to spend time on one task only while the timer is ticking."""

text2 = """                                   HOW TO USE THE TIMER
The timer keeps the times that are at least 23 minutes and 15 seconds long and anything less is discarded. This is because spending less time on an activity could hardly be considered deep focus. According to a study at the University of California (https://www.ics.uci.edu/~gmark/chi08-mark.pdf) on average it takes 23 minutes and 15 seconds for the mind to completely recover from distractions and get back to full productivity."""

text3 = """                                   Kristijonas Jankauskas 2022 June
                                              Deep Focus Logbook v1.0
                                              Github.com/Chrysipus"""

List_Of_Quotes = [
    "I’m a great believer in luck, and I find the harder I work, the more I have of it. ~ Thomas Jefferson",
    "We think, mistakenly, that success is the result of the amount of time we put in at work, instead of the quality of time we put in. ~ Ariana Huffington",
    "Inaction breeds doubt and fear. Action breeds confidence and courage. If you want to conquer fear, do not sit home and think about it. Go out and get busy. ~ Dale Carnegie",
    "Without labor, nothing prospers. ~ Sophocles",
    "Success is best when it’s shared. ~ Howard Schultz",
    "Doing the best at this moment puts you in the best place for the next moment. ~ Oprah",
    "Would you like me to give you a formula for success? It’s quite simple, really: Double your rate of failure. You are thinking of failure as the enemy of success. But it isn’t at all. You can be discouraged by failure or you can learn from it, so go ahead and make mistakes. Make all you can. Because remember that’s where you will find success. ~ Thomas J. Watson",
    "The three great essentials to achieve anything worth while are: Hard work, stick-to-itiveness, and common sense. ~ Thomas Edison",
    "It’s not about money or connection — it’s the willingness to outwork and outlearn everyone. ~ Mark Cuban",
    "If you really look closely, most overnight successes took a long time. ~ Steve Jobs",
    "Success is not final; failure is not fatal. It is the courage to continue that counts. ~ Winston S. Churchill",
    "The successful warrior is the average man, with laser-like focus. ~ Bruce Lee",
    "Success isn’t always about greatness. It’s about consistency. Consistent hard work leads to success. Greatness will come. ~ Dwayne “The Rock” Johnson",
    "Keep on going, and the chances are that you will stumble on something, perhaps when you are least expecting it. I never heard of anyone ever stumbling on something sitting down. ~ Charles F. Kettering",
    "I never did anything worth doing by accident, nor did any of my inventions come indirectly through accident, except the phonograph. No, when I have fully decided that a result is worth getting I go about it, and make trial after trial until it comes. ~ Thomas Edison",
    "I learned the value of hard work by working hard. ~ Margaret Mead",
    "Chop your own wood and it will warm you twice. ~ Henry Ford",
    "All big things come from small beginnings. The seed of every habit is a single, tiny decision. ~ James Clear, Atomic Habits",
    "Every action you take is a vote for the type of person you wish to become.  ~ James Clear, Atomic Habits",
    "The best is the enemy of the good. ~ Voltaire",
    "Once your pride gets involved, you’ll fight tooth and nail to maintain your habits. ~ James Clear, Atomic Habits",
]
More_Quotes_List = [
    "✔ Moderation in all things, including moderation... More!",
    "✔ I'll have another one.",
    "✔ Just one more.",
    "✔ Is there such a thing as too much inspiration..?",
    "✔ More. I have seen this one before.",
    "✔ My inspiration meter is still dry.",
    "✔ The last one, I promise.",
    "✔ I wonder if I got them all.",
    "✔ You won't make me quit.",
    "✔ Continue to grow and evolve.",
    "✔ When the going gets tough, the tough gets going.",
    "✔ I should keep going just to see what happens.",
    "✔ I want more!",
    "✔ I'm loving this.",
    "I learn not from other's mistakes but from other's success"]
Enough_Quotes_List = [
    "✖ Understandable, have a nice day.",
    "✖ That was one too many, bye.",
    "✖ Inspiration overflow, need to act on it.",
    "✖ That last one was rubbish, I need to recover.",
    "✖ Hmm, I need to meditate on this.",
    "✖ How about no.",
    "✖ No thanks.",
    "✖ Thank you but no thank you.",
    "✖ I already thought the last one was the last one!",
    "✖ This only makes me more distracted!",
    "✖ Reading about doing stuff is not the same as doing it!",
    "✖ I quit.",
    "✖ Exit.",
    "✖ I am saturated.",
    "✖ Maybe later.",
    "✖ Yeah this isn't working for me.",
    "✖ Just  how many ways to say no are there?",
    "✖ It is so hard to leave - until you leave",
    "✖ Every end is a new beginning",
    "✖ I regret nothing.",
    "✖ What has a beginning has an end..",
    "✖ Inspiration is for those who are unmotivated.",
    "✖ No time for this.",
    "✖ I identify as a quitter.",
    "✖ I am filled with determination.",
    "✖ It's a beautiful day outside.",
    "I can do it. I shall do it"]

main = tkinter.Tk()
main.geometry("400x700")
# main.resizable(0, 0)                  //Uncomment to disable window resizing.
main.title('Deep Focus Logbook ')
main.configure(bg='#2c2825')

Minutes = []
Results = {}
Chart_Date_Entry = 0
Totalseconds = 0
Listplace = 1
second = 0
second2 = 0
Time_Table_Sum = []

timelist = Listbox(
    main,
    relief='solid',
    background='#705e52',
    foreground='#fdcb53',
    selectbackground='#fdcb53',
    highlightbackground='#fdcb53')
daytimelist = Listbox(
    main,
    relief='solid',
    width=30,
    background='#705e52',
    foreground='#fdcb53',
    selectbackground='#fdcb53',
    highlightbackground='#fdcb53')

style = ttk.Style()
style.theme_use('alt')
style.configure("yellow.Horizontal.TProgressbar",
                foreground='#ff4626',
                background='#ff4626')
bar = Progressbar(main, orient=HORIZONTAL, length=125,
                  style="yellow.Horizontal.TProgressbar")

WatchSpace = Label(main,
                   font=('Caladea', 30, 'bold'),
                   pady=20,
                   foreground='#fdcb53',
                   background='#2c2825')
ChronoField = Label(main,
                    font=("Terminal 22"),
                    pady=50,
                    foreground='#fdcb53',
                    background='#2c2825',
                    text="0:00:00")
TotalTime = Label(main,
                  font=('Cambria', 12, 'bold'),
                  pady=5,
                  text="Total: 0:00:00",
                  foreground='#fdcb53',
                  background='#2c2825')
BarPercentage = Label(main,
                      font=('Cambria', 12, 'bold'),
                      pady=5,
                      text="0.0%",
                      foreground='#fdcb53',
                      background='#2c2825')


def writeResults(Results, Totalseconds, Chart_Date_Entry, second):
    try:
        if Chart_Date_Entry in Results:
            currentseconds = Results[Chart_Date_Entry] + second
            Results[Chart_Date_Entry] = currentseconds
            j = json.dumps(Results)
            with open("FocusLogbook.json", 'w') as f:
                f.write(j)
                f.close()
            daytimelist.delete(0, END)
            Results = json.load(open('FocusLogbook.json'))
            for key, value in Results.items():
                value = datetime.timedelta(seconds=value)
                daytimelist.insert(0, f"{key}, Total Time: {value}")
        else:
            Results[Chart_Date_Entry] = Totalseconds
            j = json.dumps(Results)
            with open("FocusLogbook.json", 'w') as f:
                f.write(j)
                f.close()
            daytimelist.delete(0, END)
            for key, value in Results.items():
                value = datetime.timedelta(seconds=value)
                daytimelist.insert(0, f"{key}, Total Time: {value}")
    except BaseException:
        pass


def readResults():
    global Results
    try:
        Results = json.load(open('FocusLogbook.json'))
        for key, value in Results.items():
            value = datetime.timedelta(seconds=value)
            daytimelist.insert(0, f"{key}, Total Time: {value}")
    except BaseException:
        pass


def TimeMachine():
    global second, second2
    if running:
        timenow = time.time()
        second = round(timenow) - round(chronostart)
        if second > second2:
            second2 = second
            BarProgressing()
        ChronoField.config(text=f"{str(datetime.timedelta(seconds=second))}")
        if second <= 1395:
            BarPercentage.config(
                text=f"{round((second / 1395) * 100, 1)}% to deep focus!")
        if second > 1395:
            BarPercentage.config(text="Deep focus engaged!")
        ChronoField.after(222, TimeMachine)
    if running == 0:
        return running


def ChronoStop():
    global running, Listplace, Time_Table_Sum, Totalseconds, second, Results, second2, percent
    running = False
    BarPercentage.config(text="0.0%")
    bar['value'] = 0
    if second >= 1395:
        timelist.insert(
            Listplace,
            f"{Listplace} {str(datetime.timedelta(seconds=second))}")
        Listplace = Listplace + 1
        Time_Table_Sum.append(second)
        Totalseconds = Totalseconds + second
        TotalTime.config(
            text=f"Total: {(str(datetime.timedelta(seconds=sum(Time_Table_Sum))))}")
        Chart_Date_Entry = datetime.datetime.now()
        Chart_Date_Entry = str(Chart_Date_Entry.strftime("%d%b%Y"))
        writeResults(Results, Totalseconds, Chart_Date_Entry, second)
    second = 0
    second2 = 0


def ChronoStart():
    global running, chronostart
    bar['value'] = 0
    chronostart = time.time()
    running = True
    TimeMachine()


def InformationField():
    informationwindow = Toplevel()
    informationwindow.geometry("700x700")
    # informationwindow.resizable(0, 0)
    informationwindow.title('Information')
    informationwindow.configure(bg='#2c2825')
    aboutinfo = Text(
        informationwindow,
        height=19,
        width=87,
        font=(
            'Terminal',
            10,
        ),
        foreground='#fdcb53',
        background='#2c2825',
        spacing1=4,
        wrap='word',
        tabstyle='wordprocessor',
        autoseparators=1,
        spacing2=4,
        spacing3=4)
    aboutinfo.insert('1.0', text1)
    aboutinfo.place(x=0, y=0)
    aboutinfo3 = Text(
        informationwindow,
        height=7,
        width=87,
        font=(
            'Terminal',
            10,
        ),
        foreground='#fdcb53',
        background='#2c2825',
        spacing1=4,
        wrap='word',
        tabstyle='wordprocessor',
        autoseparators=1,
        spacing2=4,
        spacing3=4)
    aboutinfo3.insert('1.0', text2)
    aboutinfo3.place(x=0, y=395)
    aboutinfo2 = Text(
        informationwindow,
        height=3,
        width=87,
        font=(
            'Terminal',
            10,
        ),
        foreground='#fdcb53',
        background='#2c2825',
        spacing1=4,
        wrap='word',
        tabstyle='wordprocessor',
        autoseparators=1,
        spacing2=4,
        spacing3=4)
    aboutinfo2.insert('1.0', text3)
    aboutinfo2.place(x=0, y=600)


def clockwatch():
    StringOfTime = strftime('%H:%M:%S %p')
    WatchSpace.config(text=StringOfTime)
    WatchSpace.after(1000, clockwatch)


def ConfirmSaveFileDelete():
    if os.path.exists("FocusLogbook.json"):
        answer = askyesno(
            title='Confirmation',
            message='Are you sure you want to delete the history of your total times?')
        if answer:
            DeleteSaveFile()
    else:
        tkinter.messagebox.showinfo(
            "No file found",
            "Save file doesn't exist. Unable to delete.")


def DeleteSaveFile():
    global Results, Totalseconds
    os.remove('FocusLogbook.json')
    daytimelist.delete(0, END)
    Results = {}
    Totalseconds = 0


def Chart():
    global Minutes
    keys = list(Results.keys())
    values = list(Results.values())
    for entry in values:
        Minutes.append(round(entry / 60))
    if len(Minutes) >= 2:
        ChartDays = np.arange(len(keys))
        plt.style.use("_classic_test_patch")
        fig, ax = plt.subplots()
        hbars = ax.barh(
            ChartDays,
            Minutes,
            xerr=0,
            align='center',
            edgecolor='#fdcb53',
            color='#fdcb53',
            facecolor='#fdcb53')
        ax.set_yticks(
            ChartDays,
            labels=keys,
            fontsize=19,
            color="#fdcb53",
            fontname="Gabriola")
        ax.invert_yaxis()
        ax.set_xlabel(
            'MINUTES',
            fontsize=18,
            color="#fdcb53",
            fontname="Gabriola")
        ax.tick_params(
            axis='x',
            colors='#fdcb53',
            labelsize=12,
            grid_color='#fdcb53',
            labelcolor='#fdcb53')
        ax.bar_label(hbars)
        fig.set_size_inches(12, 6)
        fig.patch.set_facecolor('#2c2825')
        ax.set_facecolor('#705e52')
        ax.set_xticks(ticks=[0, 60, 120, 180, 240, 300, 360, 420])
        plt.tight_layout()
        plt.grid(axis='x')
        plt.show()
        Minutes = []
    else:
        Minutes = []
        tkinter.messagebox.showinfo(
            "Chart must contain at least two entries.",
            "Not enough entries. Must be at lest two days in history.")


def BarProgressing():
    global second2, second, percent
    bar['value'] = second2 / 13.95
    if second <= 1395:
        percent = f"{round((second / 1395) * 100, 1)}%"
    elif second > 1395:
        percent = "100%"
    else:
        pass


def Inspiration():
    Quotes_Window = Toplevel()
    Quotes_Window.geometry("700x400")
    Quotes_Window.resizable(0, 0)
    Quotes_Window.title('Information')
    Quotes_Window.configure(bg='#2c2825')
    Inspirational_Text = Text(
        Quotes_Window,
        height=13,
        width=53,
        font=(
            'Terminal',
            12,
            'bold'),
        foreground='#fdcb53',
        background='#2c2825',
        spacing1=4,
        wrap='word',
        tabstyle='wordprocessor',
        autoseparators=1,
        spacing2=4,
        spacing3=4)
    Inspirational_Text.insert('1.0', random.choice(List_Of_Quotes))
    Inspirational_Text.place(x=0, y=0)

    def Change_Text():
        Inspirational_Text.delete('1.0', END)
        Inspirational_Text.insert('1.0', random.choice(List_Of_Quotes))
        Quote_Generator['text'] = random.choice(More_Quotes_List)
        Enough_Button['text'] = random.choice(Enough_Quotes_List)
    Quote_Generator = Button(Quotes_Window,
                             text='More Quotes.',
                             font=('Terminal', 12),
                             foreground='#ff4626',
                             background='#2c2825',
                             command=Change_Text)
    Quote_Generator.place(x=0, y=320)
    Enough_Button = Button(Quotes_Window,
                           text='Enough.',
                           font=('Terminal', 12),
                           foreground='#78AB46',
                           background='#2c2825',
                           command=Quotes_Window.destroy)
    Enough_Button.place(x=0, y=350)


InspirationButton = Button(main,
                           text='Inspiration',
                           font=('Cambria', 12, 'bold'),
                           foreground='#fdcb53',
                           background='#2c2825',
                           command=Inspiration)
InfoButton = Button(main,
                    text='!',
                    font=('Cambria', 20, 'bold'),
                    foreground='#fdcb53',
                    background='#2c2825',
                    command=InformationField)
ExitButton = Button(main,
                    text="EXIT",
                    font=('Terminal', 12, 'bold'),
                    foreground='#fdcb53',
                    background='#2c2825',
                    command=main.destroy)
RunTime = Button(main,
                 text="Start",
                 font=('Cambria', 14, 'bold'),
                 foreground='#fdcb53',
                 background='#2c2825',
                 command=ChronoStart,
                 width=5,
                 height=1)
Chronostop = Button(main,
                    text="Stop",
                    font=('Cambria', 14, 'bold'),
                    foreground='#fdcb53',
                    background='#2c2825',
                    command=ChronoStop,
                    width=5,
                    height=1)
ClearDictionary = Button(main,
                         text="X",
                         font=('Terminal', 8, 'bold'),
                         foreground='#fdcb53',
                         background='#2c2825',
                         command=ConfirmSaveFileDelete)
InitiateChart = Button(main,
                       text="Chart",
                       font=('Caladea', 12, 'bold'),
                       foreground='#fdcb53',
                       background='#2c2825',
                       command=Chart)

WatchSpace.place(x=90, y=0)
ExitButton.place(x=328, y=672)
InfoButton.place(x=0, y=0)
ChronoField.place(x=140, y=220)
RunTime.place(x=78, y=300)
Chronostop.place(x=255, y=300)
ClearDictionary.place(x=335, y=483)
InitiateChart.place(x=150, y=464)
TotalTime.place(x=5, y=665)
timelist.place(x=10, y=500)
daytimelist.place(x=150, y=500)
bar.place(x=10, y=470)
BarPercentage.place(x=5, y=433)
InspirationButton.place(x=210, y=464)
readResults()
clockwatch()
main.mainloop()
