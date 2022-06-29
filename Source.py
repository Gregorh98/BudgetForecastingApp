import tkinter
from tkinter import LabelFrame, Listbox, Button, Toplevel, Label, Entry


class Source:
    def drawRootComponent(self, root, row, col):
        self.root = root
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

        Label(addWindow, text="Name").grid(row=1, column=0, sticky="w");        Entry(addWindow).grid(row=1, column=1)
        Label(addWindow, text="Amount").grid(row=2, column=0, sticky="w");      Entry(addWindow).grid(row=2, column=1)
        Label(addWindow, text="Frequency").grid(row=3, column=0, sticky="w");   Entry(addWindow).grid(row=3, column=1)

        Button(addWindow, text="Add", command=self.addRecord).grid(row=4, column=0, columnspan=2)

    def drawEditWindow(self):
        editWindow = Toplevel(self.root)
        Label(editWindow, text="Edit " + self.name[:-1]).grid(row=0, column=0, columnspan=2)

        Label(editWindow, text="Name").grid(row=1, column=0, sticky="w");
        nameEntry = Entry(editWindow)
        nameEntry.grid(row=1, column=1)

        Label(editWindow, text="Amount").grid(row=2, column=0, sticky="w");
        amountEntry = Entry(editWindow)
        amountEntry.grid(row=2, column=1)

        Label(editWindow, text="Frequency").grid(row=3, column=0, sticky="w");
        frequencyEntry = Entry(editWindow)
        frequencyEntry.grid(row=3, column=1)

        Button(editWindow, text="Update", command=self.editRecord).grid(row=4, column=0, columnspan=2)

    def removeRecord(self):
        return

    def addRecord(self):
        return

    def editRecord(self):
        return