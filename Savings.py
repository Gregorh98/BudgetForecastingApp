from tkinter import *
import tkcalendar
from Source import Source

class generalSavings(Source):
    def __init__(self):
        self.name           = "Savings"
        self.saveName       = "generalSavings"
        self.rootListbox    = None
        self.description    = "Money being added to savings this month"

    def drawAddWindow(self):
        addWindow = Toplevel(self.root)
        Label(addWindow, text="Add " + self.name).grid(row=0, column=0, columnspan=2)

        Label(addWindow, text="Name001").grid(row=1, column=0, sticky="w")
        nameEntry = Entry(addWindow)
        nameEntry.grid(row=1, column=1)

        Label(addWindow, text="Amount").grid(row=2, column=0, sticky="w")
        amountEntry = Entry(addWindow)
        amountEntry.grid(row=2, column=1)

        Label(addWindow, text="Date").grid(row=3, column=0, sticky="w")
        dateEntry = tkcalendar.DateEntry(addWindow)
        dateEntry.grid(row=3, column=1, sticky="WE")

        var = IntVar()
        rFrame = Frame(addWindow)
        R1 = Radiobutton(rFrame, text="Option 1", variable=var, value=1,
                         command=sel)
        R1.pack(anchor=W)

        R2 = Radiobutton(rFrame, text="Option 2", variable=var, value=2,
                         command=sel)
        R2.pack(anchor=W)
        rFrame.grid(row=4, column=0)

        Button(addWindow, text="Add", command=lambda: self.addRecord(nameEntry.get(), amountEntry.get(), str(dateEntry.get_date()))).grid(row=5, column=0, columnspan=2)