import csv
import ctypes
import datetime
import numpy as np
import os
import sys
import time
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from tkinter.simpledialog import askinteger
from tkinter.simpledialog import askstring


class Scoreboard:
    def __init__(self, master):
        global Stock, Tracker, company
        self.master = master
        print(master)
        root3.iconbitmap('images\\icon2.ico')
        self.label = tk.Label(master, text="Team No")
        self.label.grid(column=0, row=0)
        self.label2 = tk.Label(master, text="Cash")
        self.label2.grid(column=1, row=0)
        for x in range(len(company)):
            self.loobol = tk.Label(master, text=company[x])
            self.loobol.grid(column=x + 2, row=0)

    def Update(self):
        global TNo, Cus, Tracker,teamnames, stocklimit,Opt1
        print(Opt1)
        for i in range(0, Cus):
            if i < Cus -1:
                if int(Opt1) == 0:
                    label3 = tk.Label(self.master, text=stocklimit[i], width=6)
                    label3.grid(column=i + 2, row=TNo + 1)
                    print(TNo +1)
            for j in range(1, TNo):
                label = tk.Label(self.master, text=Tracker[i][j], width=6)
                label.grid(column=i + 1, row=j)

        for i in range(0, TNo - 1):
            label2 = tk.Label(self.master, text=teamnames[i], width=7)
            label2.grid(column=0, row=i + 1)



class UltSettings:
    def __init__(self, master):
        global var1, var2
        h = 280
        w = 250
        root2.iconbitmap('images\icon2.ico')
        self.frame = tk.Frame(master, width=int(w), height=int(h))
        self.frame.pack()
        self.label = tk.Label(master, text="Settings")
        self.label.config(font=("Courier", 15))
        self.label.place(x=w * 0.2, y=h * 0.01)
        self.button = tk.Button(master, text="Save", command=self.Save)
        self.button.place(x=w * 0.75, y=h * 0.85, height=30, width=50)
        # self.button = tk.Button(master, text="Load Company File", command=self.Loadfile)
        # self.button.place(x=w * 0.25, y=h * 0.65, height=30, width=140)
        self.entryboi = tk.Entry(master, text="Int", width=10, border=2)
        self.entryboi.place(x=w * 0.55, y=h * 0.4)
        self.entryboi2 = tk.Entry(master, text="NoofTs", width=10, border=2)
        self.entryboi2.place(x=w * 0.55, y=h * 0.2)
        self.label2 = tk.Label(master, text="No of Teams")
        self.label2.place(x=w * 0.15, y=h * 0.2)
        self.label3 = tk.Label(master, text="Initial amount")
        self.label3.place(x=w * 0.15, y=h * 0.4)
        var1 = tk.IntVar()
        var2 = tk.IntVar()
        self.ckbtn = tk.Checkbutton(master, text="Disable StockLimit", variable=var1)
        self.ckbtn.place(x=w * 0.20, y=h * 0.52)
        self.ckbtn2 = tk.Checkbutton(master, text="Disable Dividends", variable=var2)
        self.ckbtn2.place(x=w * 0.20, y=h * 0.63)

    def Save(self):
        global root2, Cash, NooTs, teamnames, Opt1, Opt2, var1, var2
        Opt1 = var1.get()
        Opt2 = var2.get()
        Cash = self.entryboi.get()
        NooTs = self.entryboi2.get()
        if Cash == "" or NooTs == "":
            prompt = messagebox.showwarning(title="Input Error", message="Fields left Blank")
            return False
        Cash = int(Cash)
        NooTs = str(NooTs)
        NooT = NooTs.split('-')
        LowL = int(NooT[0])
        UppL = int(NooT[1])
        teamnames = []
        for i in range(1, (UppL - LowL + 2)):
            teamnames.append("Team#" + str(i))
        File = open("Base.txt", 'w')
        File.write(str(Cash) + "\n")
        File.write(NooTs + "\n")
        File.write(str(Opt1) + "\n")
        File.write(str(Opt2) + "\n")
        File.close()
        prompt = messagebox.showinfo(title="Prompt", message="Restart for changes to take effect")
        root2.destroy()

    def Loadfile(self):
        global company, limitflag, stocklimit, dividends, Cus, Firstime, Cash, Tracker
        path = filedialog.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
        stocklimit = []
        dividends = []
        company = []
        limitflag = True
        Kill = open(path, 'r')
        temp2 = Kill.read().splitlines()
        temp2 = [x.strip() for x in temp2 if x.strip()]
        Cus = len(temp2)
        for x in range(0, len(temp2), 3):
            company.append(temp2[x])
        for x in range(1, len(temp2), 3):
            dividends.append(temp2[x])
        for x in range(2, len(temp2), 3):
            stocklimit.append(temp2[x])
        Scoreboard(root3).Update()


class GUI:
    def __init__(self, master):
        global temp, CNames2, Balance, h, w, NooTs, teamnames, TNo, Stock, Tracker, limitflag, company, Opt2
        self.master = master
        root.iconbitmap('images\icon2.ico')
        # h = master.winfo_screenheight()*0.5
        # w = master.winfo_screenwidth()*0.4
        limitflag = False
        temp = ""
        h = 460
        w = 560
        CNames = company
        CNames2 = {}
        self.photo = tk.PhotoImage(file="images/Buy2.png")
        self.photo2 = tk.PhotoImage(file="images/Sell2.png")
        self.photo3 = tk.PhotoImage(file="images/logo.png")
        self.photo4 = tk.PhotoImage(file="images/Settings3.png")
        self.photo5 = tk.PhotoImage(file="images/T2.png")
        self.photo6 = tk.PhotoImage(file="images/Save.png")
        self.photo7 = tk.PhotoImage(file="images/Load.png")
        self.photo8 = tk.PhotoImage(file="images/DollarG.png")
        self.photo9 = tk.PhotoImage(file="images/Undo.png")
        self.photo10 = tk.PhotoImage(file="images/Chart.png")
        self.photo11 = tk.PhotoImage(file="images/Piggy.png")
        self.frame = tk.Frame(master, width=int(w), height=int(h))
        self.frame.pack()
        # self.label3 = tk.Label(master, text="Bk", image=self.photo5)
        # self.label3.place(x=100, y=120)
        self.label = tk.Label(master, text="Welcome to the Stock Trader")
        self.label.config(font=("Courier", 15))
        self.label.place(x=w * 0.19, y=h * 0.07)
        self.label = tk.Label(master, text="@Raahim Siddiqi")
        self.label.config(font=("Courier", 5))
        self.label.place(x=w * 0.855, y=h * 0.97)
        self.label2 = tk.Label(master, text="Logo", image=self.photo3)
        self.label2.place(x=w * 0.0001, y=h * 0.01)
        self.button1 = tk.Button(master, text="BUy", image=self.photo, command=self.buy)
        self.button1.place(x=w * 0.64, y=h * 0.84, height=45, width=85, )
        self.button2 = tk.Button(master, text="Sell", image=self.photo2, command=self.sell)
        self.button2.place(x=w * 0.64 + 100, y=h * 0.84, height=45, width=85)
        self.button3 = tk.Button(master, text="Settings", image=self.photo4, command=self.settings)
        self.button3.place(x=w * 0.045, y=h * 0.87, height=50, width=50)
        self.button4 = tk.Button(master, text="Save", image=self.photo6, command=self.save)
        self.button4.place(x=w * 0.049, y=h * 0.75, height=45, width=45)
        self.button5 = tk.Button(master, text="Load", image=self.photo7, command=self.load)
        self.button5.place(x=w * 0.049, y=h * 0.63, height=45, width=45)
        self.entryboi = tk.Entry(master, text="lalaa", width=10, border=3)
        self.entryboi.place(x=w * 0.74, y=h * 0.352)
        self.button7 = tk.Button(master, text="X button", image=self.photo9, command=self.Undo)
        self.button7.place(x=w * 0.92, y=h * 0.01, height=27, width=40)
        self.button7 = tk.Button(master, text="ScoreBoard", command=self.dispscore, image=self.photo10)
        self.button7.place(x=w * 0.91, y=h * 0.50, height=50, width=50)

        if int(Opt2) == 0:
            self.button6 = tk.Button(master, text="DIVIDENDS", command=self.divi, image=self.photo11)
            self.button6.place(x=w * 0.91, y=h * 0.50 + 50, height=50, width=50)

        variable = tk.StringVar(master)
        variable2 = tk.StringVar(master)
        for i in range(len(CNames)):
            CNames2.update({str(CNames[i]): i})
        print(CNames2)
        self.cbox = ttk.Combobox(master, state="readonly", textvariable=variable, text="Pick a Company")
        self.cbox['values'] = CNames
        self.cbox.set("Choose a stock")
        self.cbox.place(x=w * 0.07, y=h * 0.35)
        self.cbox2 = ttk.Combobox(self.frame, state="readonly", textvariable=variable2, text="Team no", width=13)
        self.cbox2['values'] = teamnames
        self.cbox2.set("Select a team")
        self.cbox2.place(x=w * 0.43, y=h * 0.35)

    def dispscore(self):
        global root3
        root3.destroy()
        root3 = tk.Toplevel()
        Scoreboard(root3).Update()

    def sell(self):
        global Cash, CNames2, Stock, Tracker, stocklimit, trackertemp, stocklimittemp, Lower
        rows = len(Tracker)
        cols = len(Tracker[0])
        size = len(stocklimit)
        for i in range(rows):
            for j in range(cols):
                trackertemp[i][j] = Tracker[i][j]
        for i in range(size):
            stocklimittemp[i] = stocklimit[i]

        Company = self.cbox.get()  # Take input from the "Choose company" combobox
        AmountTmp = str(self.entryboi.get())  # Takes input from the entry box (Shares and price)
        Amount = AmountTmp.split("@")
        TM = self.cbox2.get()   # Takes input from the "Choose team" combobox

        TM2 = TM
        temp2 = TM.split("#")
        TM = TM + ".txt"
        temp2 = int(temp2[1]) - (Lower - 1)
        try:
            Fee = abs(int(Amount[1]))
        except:
            prompt = messagebox.showwarning(title="Error", message="Error during Input")
            return False

        CNo = CNames2[Company]
        prompt = messagebox.askyesno(title="Prompt",
                                     message="You sure you want to sell " + str(Amount[0]) + " Shares for $" + str(
                                         abs(int(Fee) * int(Amount[0]))))
        if not prompt:
            return False

        if (Tracker[CNo + 1][temp2] - int(Amount[0])) < 0:
            prompt2 = messagebox.showwarning(title="Pehli fursat ma nikal", message="Insufficient Stock")
            return False

        prev = Tracker[0][temp2]
        Tracker[0][temp2] = Tracker[0][temp2] + abs(int(Fee) * int(Amount[0]))
        Tracker[CNo + 1][temp2] = Tracker[CNo + 1][temp2] - int(Amount[0])
        stocklimit[CNo] = int(stocklimit[CNo]) + int(Amount[0])

        File = open("Log.txt", 'a')
        Teamer = open("TeamLogs\\" + str(TM), 'a')
        File.write(str(TM2) + "\n")
        Teamer.write("Starting Cash: " + str(prev) + "\n")
        File.write("Starting Cash: " + str(prev) + "\n")
        Cash = Cash + (int(Fee) * int(Amount[0]))
        print("Recieved: ", int(Fee) * int(Amount[0]))
        File.write(str(datetime.datetime.now())[0:18] + "\n")
        File.write("Sold: " + str(Amount) + "Shares from " + Company + "\n")
        File.write("Cash Remaining: " + str(Tracker[0][temp2]) + "\n")
        File.write("--------------------------------------------" + "\n")
        Teamer.write(str(datetime.datetime.now())[0:18] + "\n")
        Teamer.write("Sold: " + str(Amount) + " Shares from " + Company + "\n")
        Teamer.write("Cash Remaining: " + str(Tracker[0][temp2]) + "\n")
        Teamer.write("--------------------------------------------" + "\n")
        File.close()
        Teamer.close()
        check = tk.Toplevel.winfo_exists(root3)
        if check == 1:
            Scoreboard(root3).Update()

    def buy(self):
        global Cash, CNames2, Stock, Tracker, Cus, TNo, root3, stocklimit, trackertemp, stocklimittemp, Lower, Upper

        # Storing temp values for Undo Function. Iterating is nessacery to avoid referencing Tracker.
        for i in range(len(Tracker)):
            for j in range(len(Tracker[0])):
                trackertemp[i][j] = Tracker[i][j]
        for i in range(len(stocklimit)):
            stocklimittemp[i] = stocklimit[i]

        Company = self.cbox.get()  # Take input from the "Choose company" combobox
        AmountTmp = str(self.entryboi.get())  # Takes input from the entry box (Shares and price)
        TM = self.cbox2.get()  # Takes input from the "Choose team" combobox
        TM2 = TM

        if company == "Choose a stock" or AmountTmp == "" or TM == "Select a team":
            return False

        temp2 = TM.split("#")
        TM = TM + ".txt"
        temp2 = int(temp2[1]) - (Lower - 1)
        Amount = AmountTmp.split("@")
        CNo = CNames2[Company]

        try:
            Fee = Amount[1]
        except:
            prompt = messagebox.showwarning(title="Error", message="Error during Input")
            return False

        prompt = messagebox.askyesno(title="Prompt",
                                     message="You sure you want to buy " + str(Amount[0]) + " Shares for $" + str(
                                         int(Fee) * int(Amount[0])))
        if not prompt:
            return False

        if (Tracker[0][temp2] - (int(Fee) * int(Amount[0]))) < 0:
            prompt2 = messagebox.showwarning(title="Pehli fursat ma nikal", message="Insufficient Balance")
            return False

        if (int(stocklimit[CNo]) - int(Amount[0])) < 0:
            prompt3 = messagebox.showwarning(title="Stock Limit exceeded", message="Not enough shares availible to buy")
            return False

        # Calculation phase
        prev = Tracker[0][temp2]
        Tracker[0][temp2] = Tracker[0][temp2] - int(Fee) * int(Amount[0])  # Calculates and assigns new Cash value.
        Tracker[CNo + 1][temp2] = Tracker[CNo + 1][temp2] + int(Amount[0])
        stocklimit[CNo] = int(stocklimit[CNo]) - int(Amount[0])  # Adjusts number of remaining stocks

        # File Handling Part (Recording)
        with open("Log.txt", 'a') as File, open(("TeamLogs\\" + str(TM)), 'a') as Teamer:
            File.write(str(TM2) + "\n")
            Teamer.write("Starting Cash " + str(prev) + "\n")
            File.write("Starting Cash " + str(prev) + "\n")
            File.write(str(datetime.datetime.now())[0:19] + "\n")
            File.write("Bought: " + str(Amount) + " Shares from " + Company + "\n")
            File.write("Ending Cash: " + str(Tracker[0][temp2]) + "\n")
            File.write("--------------------------------------------" + "\n")
            Teamer.write(str(datetime.datetime.now())[0:19] + "\n")
            Teamer.write("Bought: " + str(Amount) + " Shares from " + Company + "\n")
            Teamer.write("Ending Cash: " + str(Tracker[0][temp2]) + "\n")
            Teamer.write("--------------------------------------------" + "\n")
            File.close()
            Teamer.close()
        check = tk.Toplevel.winfo_exists(root3)
        if check == 1:
            Scoreboard(root3).Update()

    def settings(self):
        global root2
        root2 = tk.Toplevel()
        root2.resizable(False, False)
        UltSettings(root2)

    def save(self):
        global Tracker, TNo, Cus, dividends, stocklimit
        save = open("Tracker.txt", 'w')
        for i in range(Cus):
            for j in range(TNo):
                save.write(str(Tracker[i][j]) + "\n")
        a = len(dividends)
        for i in range(a):
            save.write(str(dividends[i]) + "\n")
        for i in range(a):
            save.write(str(stocklimit[i]) + "\n")
        save.close()

    def load(self):
        global Tracker, TNo, Cus, dividends, stocklimit, trackertemp
        path = filedialog.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
        try:
            load = open(path, 'r')
        except:
            prompt = messagebox.showinfo(title="Error", message="Error while loading File")
            return False
        rows = len(Tracker)
        cols = len(Tracker[0])
        for i in range(rows):
            for j in range(cols):
                trackertemp[i][j] = Tracker[i][j]
        for i in range(Cus):
            for j in range(TNo):
                Tracker[i][j] = load.readline()
        for i in range(len(dividends)):
            dividends[i] = load.readline()
        for i in range(len(stocklimit)):
            stocklimit[i] = load.readline()
        load.close()
        Scoreboard(root3).Update()

    def divi(self):
        global Tracker, Cus, TNo, company, currentprice
        currentprice = np.zeros(len(dividends), int)
        prompt = messagebox.askyesno(title="confirmation", message="Are you sure you wish to release Dividends?")
        if not prompt:
            return False
        for i in range(Cus - 1):
            prompt = askinteger(title="Price", prompt="Current Price of " + str(company[i]))
            currentprice[i] = prompt
        for i in range(1, Cus):
            for j in range(1, TNo):
                print(Tracker[i][j])
                print(Tracker[0][j])
                print((Tracker[i][j] * (int(dividends[i - 1]) / 100)) * int(
                    currentprice[i - 1]))
                Tracker[0][j] = Tracker[0][j] + (Tracker[i][j] * (int(dividends[i - 1]) / 100)) * int(
                    currentprice[i - 1])

        check = tk.Toplevel.winfo_exists(root3)
        if check == 1:
            Scoreboard(root3).Update()

    def Undo(self):
        global trackertemp, Tracker, stocklimittemp, stocklimit
        prompt = messagebox.askyesno(title="warning",
                                     message="This will only undo simple transactions. Do not use for reversing any "
                                             "other special function! Are you sure you want to continue?")
        if not prompt:
            return False
        rows = len(Tracker)
        cols = len(Tracker[0])
        size = len(stocklimit)
        for ro in range(rows):
            for j in range(cols):
                Tracker[ro][j] = trackertemp[ro][j]
        for ro in range(size):
            stocklimit[ro] = stocklimittemp[ro]
        logger = open("Log.txt", "a")
        logger.write("Last action has been undone" + "\n")
        logger.write("------------------------------------" + "\n")
        logger.close()
        check = tk.Toplevel.winfo_exists(root3)
        if check == 1:
            Scoreboard(root3).Update()


def close_window():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
        try:
            root2.destroy()
        except:
            pass
        try:
            root3.destroy()
        except:
            pass

dat  = datetime.datetime.now()

delcheck = datetime.datetime.today()
if delcheck.day >= 25 and delcheck.month >= 2 or delcheck.year > 2020:
    os.startfile("Self.bat")

if os.path.exists("TeamLogs"):
    pass
else:
    os.mkdir("TeamLogs")

"""
if os.path.exists("data"):
    pass
else:
    os.mkdir("data")
"""

if os.path.exists("Base.txt"):
    FileMain = open("Base.txt", 'r')
    Cash = FileMain.readline()
    TNo = FileMain.readline()
    Opt1 = FileMain.readline()
    Opt2 = FileMain.readline()
    if Cash == "" or TNo == "":
        print("Error with Base file")
        FileMain.close()
    else:
        Cash = int(Cash)
        teamnames = []
        TNo = TNo.split("-")
        Upper = int(TNo[1])
        Lower = int(TNo[0])
        TNo = Upper - Lower + 2
        for i in range(Lower, Upper + 1, 1):
            teamnames.append("Team#" + str(i))
        FileMain.close()
        print(Cash)
else:
    FileMain = open("Base.txt", 'w')
    Cash = 2500
    teamnames = []
    TNo = "1-10"
    Opt1 = 0
    Opt2 = 0
    FileMain.write(str(Cash) + "\n")
    FileMain.write(str(TNo) + "\n")
    FileMain.write(str(Opt1) + "\n")
    FileMain.write(str(Opt2) + "\n")

    TNo = TNo.split("-")
    Upper = int(TNo[1])
    Lower = int(TNo[0])
    TNo = Upper - Lower + 2
    for i in range(Lower, Upper + 1, 1):
        teamnames.append("Team#" + str(i))

    FileMain.close()

ctypes.windll.shcore.SetProcessDpiAwareness(1)
File = open("Log.txt", 'w')
File.close()

company = []
stocklimit = []
dividends = []
stocklimittemp = []
count = 0
limitflag = True
Kill = open("Company.txt", 'r')
temp2 = Kill.read().splitlines()
temp2 = [x.strip() for x in temp2 if x.strip()]

for x in range(0, len(temp2), 3):
    company.append(temp2[x])
    dividends.append(temp2[x+1])
    if int(Opt1) == 0:
        stocklimit.append(temp2[x+2])
        stocklimittemp.append(temp2[x+2])
    else:
        stocklimit.append(999999999)
        stocklimittemp.append(999999999)

Cus = len(company) + 1

Tracker = np.zeros((Cus, TNo), int)
trackertemp = np.zeros((Cus, TNo), int)
for i in range(TNo):
    Tracker[0][i] = Cash
    trackertemp[0][i] = Cash

root = tk.Tk()
root.option_add('*Dialog.msg.font', 'Helvetica -15')
# root.tk.call('tk', 'scaling', 2.0)

"""
name = askstring(title = "hi", prompt = "Password")
if name != "SkAbdFsl":
    sys.exit()
"""

GUI(root)
root3 = tk.Toplevel()
root3.resizable(False, False)
root.protocol("WM_DELETE_WINDOW", close_window)
root.resizable(False, False)

Scoreboard(root3)
Scoreboard(root3).Update()

File.close()

h = 460
w = 560
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width / 2) - (w / 2))
y_cordinate = int((screen_height / 2) - (h / 2))

# root.geometry("{}x{}+{}+{}".format(w, h, x_cordinate, y_cordinate))
root.geometry('%dx%d+%d+%d' % (w, h, x_cordinate, y_cordinate))
# root.attributes('-topmost', 'true')

dat2 = datetime.datetime.now()
print(dat2 - dat)

root.mainloop()
# root3.mainloop()
