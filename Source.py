import _tkinter
import datetime
import tkinter
from tkinter import LabelFrame, Listbox, Button, Toplevel, Label, Entry, messagebox, ttk

import tkcalendar as tkcalendar


class Source:
    def __init__(self):
        self.sources = {}

    def drawRootComponent(self, root, row, col):
        self.root = root
        rootFrame = LabelFrame(root, text=self.name)
        rootFrame.grid(row=row, column=col, padx=2, pady=2)
        columns = ('nameOfSource', 'amountOfSource', 'dateOfSource')

        self.tree = ttk.Treeview(rootFrame, columns=columns, show='headings')

        self.tree.column("# 1", anchor=tkinter.W, stretch=True, width=150)
        self.tree.heading('nameOfSource', text='Name')

        self.tree.column("# 2", anchor=tkinter.E, stretch=True, width=75)
        self.tree.heading('amountOfSource', text='Amount')

        self.tree.column("# 3", anchor=tkinter.E, stretch=False, width=75)
        self.tree.heading('dateOfSource', text='Date')

        self.tree.grid(row=0, column=0, columnspan=3, sticky='nw')

        # add a scrollbar
        scrollbar = ttk.Scrollbar(rootFrame, orient=tkinter.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=4, sticky='ns')

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
            selection = self.tree.item(self.tree.focus())["values"]
            print(selection)
        except _tkinter.TclError:
            print("Select an Item")
            return

        editWindow = Toplevel(self.root)
        Label(editWindow, text=f"Edit '{selection[0]}'").grid(row=0, column=0, columnspan=2)

        Label(editWindow, text="Amount").grid(row=2, column=0, sticky="w")
        amountEntry = Entry(editWindow)
        amountEntry.insert(0, selection[1][1:])
        amountEntry.grid(row=2, column=1)

        Label(editWindow, text="Date").grid(row=3, column=0, sticky="w")
        dateEntry = tkcalendar.DateEntry(editWindow)
        dateEntry.set_date(datetime.date.fromisoformat(selection[2]))
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
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            record = item['values'][0]
            self.sources.pop(str(record))
            self.updateListbox()

    def addRecord(self, name, amount, date):
        if self.validateInput(name, amount, date):
            self.sources[name] = {"name":name, "amount": amount, "date": date}
            self.updateListbox()
        else:
            messagebox.showerror("Cannot validate input")


    def editRecord(self, name, amount, date):
        if self.validateInput(name, amount, date):
            self.sources[name] = {"name":name, "amount": amount, "date": date}
            self.updateListbox()

    def updateListbox(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        records = []
        for key in sorted(self.sources.keys()):
            records.append((f'{self.sources[key]["name"]}', f"{'£{:.2f}'.format(float(self.sources[key]['amount']))}", f'{self.sources[key]["date"]}'))

        # add data to the treeview
        for record in records:
            self.tree.insert('', tkinter.END, values=record)
