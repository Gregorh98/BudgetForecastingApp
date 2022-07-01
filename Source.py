import _tkinter
import datetime
import tkinter
from tkinter import LabelFrame, Listbox, Button, Toplevel, Label, Entry, messagebox

import tkcalendar as tkcalendar


class Source:
    def drawRootComponent(self, root, row, col):
        self.root = root
        self.sources = {}
        rootFrame = LabelFrame(root, text=self.name)
        rootFrame.grid(row=row, column=col, padx=2, pady=2)

        self.rootListbox = Listbox(rootFrame)
        self.rootListbox.grid(row=1, column=0, columnspan=3, padx=2, pady=2)

        Button(rootFrame, text="Add", command=self.drawAddWindow).grid(row=2, column=0, padx=2, pady=4)
        Button(rootFrame, text="Remove", command=self.removeRecord).grid(row=2, column=1, padx=2, pady=4)
        Button(rootFrame, text="Edit", command=self.drawEditWindow).grid(row=2, column=2, padx=2, pady=4)

    def drawAddWindow(self):
        addWindow = Toplevel(self.root)
        Label(addWindow, text="Add " + self.name).grid(row=0, column=0, columnspan=2)

        Label(addWindow, text="Name").grid(row=1, column=0, sticky="w")
        nameEntry = Entry(addWindow)
        nameEntry.grid(row=1, column=1)

        Label(addWindow, text="Amount").grid(row=2, column=0, sticky="w")
        amountEntry = Entry(addWindow)
        amountEntry.grid(row=2, column=1)

        Label(addWindow, text="Date").grid(row=3, column=0, sticky="w")
        dateEntry = tkcalendar.DateEntry(addWindow)
        dateEntry.grid(row=3, column=1, sticky="WE")

        Button(addWindow, text="Add", command=lambda: self.addRecord(nameEntry.get(), amountEntry.get(), str(dateEntry.get_date()))).grid(row=4, column=0, columnspan=2)

    def drawEditWindow(self):
        try:
            selection = self.rootListbox.get(self.rootListbox.curselection())
        except _tkinter.TclError:
            print("Select an Item")
            return

        editWindow = Toplevel(self.root)
        Label(editWindow, text=f"Edit '{selection}'").grid(row=0, column=0, columnspan=2)

        Label(editWindow, text="Amount").grid(row=2, column=0, sticky="w")
        amountEntry = Entry(editWindow)
        amountEntry.insert(0, self.sources[selection]["amount"])
        amountEntry.grid(row=2, column=1)

        Label(editWindow, text="Date").grid(row=3, column=0, sticky="w")
        dateEntry = tkcalendar.DateEntry(editWindow)
        dateEntry.set_date(datetime.date.fromisoformat(self.sources[selection]["date"]))
        dateEntry.grid(row=3, column=1, sticky="WE")

        Button(editWindow, text="Update", command=lambda: self.editRecord(selection, amountEntry.get(), str(dateEntry.get_date()))).grid(row=4, column=0, columnspan=2)

    def validateInput(self, name, amount, date):
        print(date)
        #try:
        name        = str(name)
        amount      = float(amount)
        date        = str(date)
       # except:
        #    return False

        if name == "":
            return False
        if amount <= 0:
            return False
        if datetime.date.today() > datetime.date.fromisoformat(date):
            return False

        return True

    def removeRecord(self):
        selection = self.rootListbox.get(self.rootListbox.curselection())
        self.sources.pop(selection)
        self.updateListbox()

    def addRecord(self, name, amount, date):
        if self.validateInput(name, amount, date):
            self.sources[name] = {"name":name, "amount": amount, "date": date}
            self.updateListbox()


    def editRecord(self, name, amount, date):
        if self.validateInput(name, amount, date):
            self.sources[name] = {"name":name, "amount": amount, "date": date}
            self.updateListbox()

    def updateListbox(self):
        self.rootListbox.delete(0, tkinter.END)
        for key in sorted(self.sources.keys()):
            self.rootListbox.insert(0, self.sources[key]["name"])
