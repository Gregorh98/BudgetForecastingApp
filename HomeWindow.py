import tkinter
from tkinter import *
from tkinter import messagebox

from Incomes import generalIncomeSources
from Expenses import generalExpenses, budgetedSpending, committedSpending
from Savings import generalSavings
import Functions

class HomeWindow():
    def __init__(self):
        self.title  = "Budget App"
        self.root   = Tk()
        self.incomeSources      = generalIncomeSources()
        self.expenseSources     = generalExpenses()
        self.savingsSources     = generalSavings()
        self.budgetedSpending   = budgetedSpending()
        self.committedSpending  = committedSpending()

    def draw(self):
        self.root.title(self.title)

        col = 0

        for x in [self.incomeSources, self.expenseSources, self.savingsSources, self.budgetedSpending, self.committedSpending]:
            x.drawRootComponent(self.root, 0, col)
            col += 1

        sidePanel = LabelFrame(self.root, text="Functions Panel")
        sidePanel.grid(row=1, column=0, columnspan=col, sticky="ew", padx=2, pady=2)

        Button(sidePanel, text="Calculate\nBudget").grid(column=0, row=0, padx=2, pady=2)

        Button(sidePanel, text="Save", command=self.save).grid(column=1, row=0, padx=2, pady=2)
        Button(sidePanel, text="Load", command=self.load).grid(column=2, row=0, padx=2, pady=2)

        self.run()

    def save(self):
        confirmOverwrite = messagebox.askyesno("Overwrite Save", "A previous save has been located, do you wish to overwrite?")
        if confirmOverwrite:
            Functions.save(self.incomeSources.sources, self.expenseSources.sources, self.savingsSources.sources)

    def load(self):
        save = Functions.load()
        self.incomeSources.sources = save["incomes"]
        self.expenseSources.sources = save["expenses"]
        self.savingsSources.sources = save["savings"]

        self.incomeSources.updateListbox()
        self.expenseSources.updateListbox()
        self.savingsSources.updateListbox()

    def run(self):
        while True:
            self.root.update()
