import tkinter
from os.path import exists
from tkinter import *
from tkinter import messagebox, ttk

from Incomes import generalIncomeSources
from Expenses import generalExpenses, budgetedSpending, plannedSpending
from Savings import generalSavings
from test import Test
from Tabs import *
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
        self.test = Test()
        self.categories         = [self.incomeSources, self.expenseSources, self.budgetedSpending, self.committedSpending, self.savingsSources]

    def draw(self):
        self.root.title(self.title)

        tabsystem = ttk.Notebook(self.root)
        dataEntryTab = Frame(tabsystem)
        monthlyBudgetTab = Frame(tabsystem)
        fitnessTab = Frame(tabsystem)

        tabsystem.add(dataEntryTab, text='Data')
        tabsystem.add(monthlyBudgetTab, text='Monthly Budget')
        tabsystem.add(fitnessTab, text='Financial Fitness')
        tabsystem.pack(expand=1, fill="both")

        drawDataEntryTab(self, dataEntryTab)
        drawBudgetTab(self, monthlyBudgetTab)
        drawFitnessTab(self, fitnessTab)

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
            #try:
            x.updateListbox()
            #except:
            #    pass

    def calculateBudget(self):
        incomeTotal = self.sumSource(self.incomeSources.sources)
        expensesTotal = self.sumSource(self.expenseSources.sources)
        print("%s - %s = %s" % (incomeTotal, expensesTotal, incomeTotal-expensesTotal))

    def sumSource(self, source):
        total = 0
        for x in source:
            total += float(source[x]["amount"])
        return round(total, 2)

    def run(self):
        while True:
            self.root.update()
