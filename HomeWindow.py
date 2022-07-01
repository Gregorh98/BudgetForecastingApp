import tkinter
from os.path import exists
from tkinter import *
from tkinter import messagebox, ttk

from Incomes import generalIncomeSources
from Expenses import generalExpenses, budgetedSpending, plannedSpending
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
        self.committedSpending  = plannedSpending()
        self.categories         = [self.incomeSources, self.expenseSources, self.savingsSources, self.budgetedSpending, self.committedSpending]

    def draw(self):
        self.root.title(self.title)

        tabsystem = ttk.Notebook(self.root)
        dataEntryTab = Frame(tabsystem)
        monthlyBudgetTab = Frame(tabsystem)

        tabsystem.add(dataEntryTab, text='Data')
        tabsystem.add(monthlyBudgetTab, text='Monthly Budget')
        tabsystem.pack(expand=1, fill="both")

        col = 0

        for x in self.categories:
            x.drawRootComponent(dataEntryTab, 0, col)
            col += 1

        if exists("save.json"):
            self.load()

        sidePanel = LabelFrame(dataEntryTab, text="Functions Panel")
        sidePanel.grid(row=1, column=0, columnspan=col, sticky="ew", padx=2, pady=2)

        Button(sidePanel, text="Calculate\nBudget", command=self.calculateBudget).grid(column=0, row=0, padx=2, pady=2)

        Button(sidePanel, text="Save", command=self.save).grid(column=1, row=0, padx=2, pady=2)
        Button(sidePanel, text="Load", command=self.load).grid(column=2, row=0, padx=2, pady=2)

        self.run()

    def save(self):
        if exists("save.json"):
            confirmOverwrite = messagebox.askyesno("Overwrite Save", "A previous save has been located, do you wish to overwrite?")
            if confirmOverwrite:
                Functions.save(self.categories)
        else:
            Functions.save(self.categories)

    def load(self):
        save = Functions.load()
        for x in self.categories:
            x.sources = save[x.saveName]
            x.updateListbox()

    def calculateBudget(self):
        incomeTotal = self.sumSource(self.incomeSources.sources)
        expensesTotal = self.sumSource(self.expenseSources.sources)
        print("%s - %s = %s" % (incomeTotal, expensesTotal, incomeTotal-expensesTotal))

    def sumSource(self, source):
        total = 0
        for x in source:
            total += float(source[x]["amount"])
        return total

    def run(self):
        while True:
            self.root.update()
