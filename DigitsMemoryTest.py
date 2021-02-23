"""
Independent Project
Thomas Martin
West Chester University
Digits Memory Test
CSC 480
"""
import os
import random
import shutil
import time
import tkinter as tk
import tkinter.font as tkFont
from datetime import date
from datetime import datetime
from timeit import default_timer as timer
import tkinter.messagebox as tm
from tkinter import ttk
import pygame
from pygame import mixer
import xlrd
import csv

absFilePath = os.path.abspath(__file__)
print(absFilePath)
fileDir = os.path.dirname(os.path.abspath(__file__))
print(fileDir)

today = date.today()
newPath = os.path.join(fileDir, 'Data_' + str(today) + '.csv')

if newPath:
    exactTime = datetime.now()
    exactTime = exactTime.strftime("%H-%M")
    newPath = os.path.join(fileDir, 'Data_' + str(today) + '_' + str(exactTime) + '.csv')

f = open(newPath, 'w')
f.truncate()
f.write("--------------------Digits Memory Test--------------------\n")
f.write("--------------------Test " + str(today) + "--------------------\n")

path0 = os.path.join(fileDir, 'mp3Folder')

turn = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
random.shuffle(turn)
correctans = ['454557', '563544', '594763', '782767', '996421', '662474', '167610', '895890', '526381',
              '602110', '262817', '387116', '330900', '715013', '950574', '70351923', '00626275',
              '87102991', '70771338', '99528082', '51860360', '50056473', '24606624', '83678579',
              '19419355', '05805486', '41774965', '56396343', '49898804', '31961887']


class Window(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.customFont = tkFont.Font(family="Times New Roman", size=14)
        tk.Tk.wm_title(self, "Digits Memory Test")
        tk.Tk.state(self, 'zoomed')
        self._frame = None
        self.geometry("400x400")
        self.iconbitmap('logo.ico')
        self.resizable(0, 0)
        self.pack_propagate(0)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.switch_frame(LoginScreen)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()

        self._frame = new_frame
        self._frame.pack()

    def on_closing(self):
        if tm.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()


class LoginScreen(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.tmpID = 0
        title = tk.Label(self, text="Memorization of Digits Tool Login", font=(master.customFont, 44), height=5,
                         width=30)
        title.pack(side="top", fill="x")
        self.login = tk.Entry(self, font=(master.customFont, 16), width=30)
        self.login.focus_set()
        self.login.pack(ipady=10)
        button = ttk.Button(self, text="Start", command=lambda: self.loginButton(master))
        # button.config(width = 20 )
        button.pack(ipadx=10, ipady=10)

    def loginButton(self, master):
        # print("Clicked")
        self.loginID = int(self.login.get())
        id_lists = self.ID_reader()
        print(self.loginID)
        if self.loginID in id_lists:
            tmpID = self.loginID
            f.write("ID: " + str(tmpID) + "\n")
            f.close()
            master.switch_frame(BlankScreen)
            self.login.pack_forget()
        else:
            tm.showerror("Login error", "Incorrect username")

    def ID_reader(self):
        """This Code will Read the Excel Sheet"""
        pathExcel = os.path.join(fileDir, 'Program_Files')
        loc = os.path.join(pathExcel, "ID_List.xlsx")
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_index(0)
        id_list = list()
        sheet.cell_value(0, 0)

        for i in range(sheet.nrows):
            id_list.append(sheet.cell_value(i, 0))
        return id_list



def waiting():
    time.sleep(5)


def waitingNumbers():
    time.sleep(1)


class BlankScreen(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        button = ttk.Button(self, text="Next", width=20, command=lambda: [waiting(), self.testover(master)])
        button.pack(side=tk.LEFT, anchor=tk.CENTER, pady=300, padx=220, ipadx=10, ipady=10)

    def testover(self, master):
        if len(turn) == 0:
            f.close()
            master.switch_frame(EndScreen)
        else:
            master.switch_frame(Test)


class Test(tk.Frame):
    def save(self):
        value = self.t_value
        userTime = (self.start - self.end)
        answerList = list()
        answerList.append(value)
        ans = correctans[self.y - 1]
        with open(newPath, mode='a', newline='') as test_data:
            data_writer = csv.writer(test_data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            data_writer.writerow(
                ['Trial ' + str(self.y), 'Choice: ' + str(value), 'Answer:' + ans, 'Time: ' + str(userTime)])

    def voice(self, master):
        #split = list(correctans[self.y - 1])
        split = list(str(int(self.tmp)))
        print(path0)
        for y in split:
            print(y)
            if y is "0":
                number = os.path.join(path0, 'Number 0.mp3')
                pygame.init()
                pygame.mixer.music.load(number)
                pygame.mixer.music.play()
            if y is "1":
                number = os.path.join(path0, 'Number 1.mp3')
                pygame.init()
                pygame.mixer.music.load(number)
                pygame.mixer.music.play()
            if y is "2":
                number = os.path.join(path0, 'Number 2.mp3')
                pygame.init()
                pygame.mixer.music.load(number)
                pygame.mixer.music.play()
            if y is "3":
                number = os.path.join(path0, 'Number 3.mp3')
                pygame.init()
                pygame.mixer.music.load(number)
                pygame.mixer.music.play()
            if y is "4":
                number = os.path.join(path0, 'Number 4.mp3')
                pygame.init()
                pygame.mixer.music.load(number)
                pygame.mixer.music.play()
            if y is "5":
                number = os.path.join(path0, 'Number 5.mp3')
                pygame.init()
                pygame.mixer.music.load(number)
                pygame.mixer.music.play()
            if y is "6":
                number = os.path.join(path0, 'Number 6.mp3')
                pygame.init()
                pygame.mixer.music.load(number)
                pygame.mixer.music.play()
            if y is "7":
                number = os.path.join(path0, 'Number 7.mp3')
                pygame.init()
                pygame.mixer.music.load(number)
                pygame.mixer.music.play()
            if y is "8":
                number = os.path.join(path0, 'Number 8.mp3')
                pygame.init()
                pygame.mixer.music.load(number)
                pygame.mixer.music.play()
            if y is "9":
                number = os.path.join(path0, 'Number 9.mp3')
                pygame.init()
                pygame.mixer.music.load(number)
                pygame.mixer.music.play()

            waitingNumbers()

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.counter = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                        27, 28, 29, 30]
        self.t_value = tk.StringVar()
        self.y = tk.IntVar()
        self.tmp = tk.IntVar()
        self.check_box_list = []
        self.start = 0
        self.tmpID = 0

        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.var4 = tk.IntVar()
        self.var5 = tk.IntVar()
        self.var6 = tk.IntVar()

        self.y = 1 + turn[0]
        turn.pop(0)
        self.trial = self.getList()
        self.tmp = random.choice(self.trial)
        self.bol = False
        w = self.y
        length = len(self.trial)
        self.check = tk.BooleanVar()
        self.check = False
        # print(trial)
        i = 0
        listvalues = []
        self.voice(master)
        time.sleep(1)
        while i + 1 <= length:
            if i == 0:
                checkbox1 = tk.Checkbutton(master, text=self.trial[i], variable=self.var1, onvalue=1, offvalue=0, font=(master.customFont, 25))
                checkbox1.config(anchor='center')
                checkbox1.pack(side="top", fill="x", pady=10)
                self.check_box_list.append(checkbox1)

            if i == 1:
                checkbox2 = tk.Checkbutton(master, text=int(self.trial[i]), variable=self.var2, onvalue=1, offvalue=0, font=(master.customFont, 25))
                checkbox2.config(anchor='center')
                checkbox2.pack(side="top", fill="x", pady=10)
                self.check_box_list.append(checkbox2)

            if i == 2:
                checkbox3 = tk.Checkbutton(master, text=int(self.trial[i]), variable=self.var3, onvalue=1, offvalue=0, font=(master.customFont, 25))
                checkbox3.config(anchor='center')
                checkbox3.pack(side="top", fill="x", pady=10)
                self.check_box_list.append(checkbox3)

            if i == 3:
                checkbox4 = tk.Checkbutton(master, text=int(self.trial[i]), variable=self.var4, onvalue=1, offvalue=0, font=(master.customFont, 25))
                checkbox4.config(anchor='center')
                checkbox4.pack(side="top", fill="x", pady=10)
                self.check_box_list.append(checkbox4)

            if i == 4:
                checkbox5 = tk.Checkbutton(master, text=int(self.trial[i]), variable=self.var5, onvalue=1, offvalue=0, font=(master.customFont, 25))
                checkbox5.config(anchor='center')
                checkbox5.pack(side="top", fill="x", pady=10)
                self.check_box_list.append(checkbox5)

            if i == 5:
                checkbox6 = tk.Checkbutton(master, text=int(self.trial[i]), variable=self.var6, onvalue=1, offvalue=0, font=(master.customFont, 25))
                checkbox6.config(anchor='center')
                checkbox6.pack(side="top", fill="x", pady=10)
                self.check_box_list.append(checkbox6)
            i += 1
        print(self.var1.get())
        self.start = timer()
        self.end = 0
        submit = ttk.Button(self, text="Submit",
                            command=lambda: [self.boxcheck(), self.save(), self.boolChange(), master.switch_frame(BlankScreen),
                                             self.clear()])
        submit.pack(ipadx=10, ipady=10)

    def boxcheck(self):
        if self.var1.get() == 1:
            self.t_value = int(self.trial[0])
        if self.var2.get():
            self.t_value = int(self.trial[1])
        if self.var3.get():
            self.t_value = int(self.trial[2])
        if self.var4.get():
            self.t_value = int(self.trial[3])
        if self.var5.get():
            self.t_value = int(self.trial[4])
        if self.var6.get():
            self.t_value = int(self.trial[5])

    def clear(self):
        for i in self.check_box_list:
            i.pack_forget()

    def boolChange(self):
        self.check = True
        self.end = timer()

    def getList(self):
        test = list()
        trial = self.excel_reader()
        test = test + trial
        i = 0
        sent = ""
        length = len(test)
        while i + 1 <= length:
            if sent == "":
                sent = str(test[i]) + "\n"
            else:
                sent = sent + "\n" + str(test[i]) + "\n"
            i += 1

        return test

    def excel_reader(self):
        """This Code will Read the Excel Sheet"""
        pathExcel = os.path.join(fileDir, 'Program_Files')
        loc = os.path.join(pathExcel, "MemoryTest.xlsx")
        print(self.y)
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_index(0)
        trial = list()
        w = 1
        while w != 7:
            value = sheet.cell((self.y - 1), w).value
            trial.append(value)
            w += 1
        i = 0
        length = len(trial)
        while i <= (length - 1):
            if trial[i] == "":
                trial.pop(i)
                length -= 1
            else:
                i += 1

        return trial


class EndScreen(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        ttk.Label(self, text="This is the end of the test").pack(side="top", fill="x", pady=10)
        ttk.Button(self, text="Exit",
                   command=lambda: app.destroy()).pack()


if __name__ == "__main__":
    app = Window()
    app.mainloop()
