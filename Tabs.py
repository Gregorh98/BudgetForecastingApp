from math import floor
from os.path import exists
from tkinter import LabelFrame, Button, Label


def drawDataEntryTab(self, dataEntryTab):
    col = 0
    row = 0

    for x in self.categories:
        if col > 2:
            col = 0
            row += 1
        x.drawRootComponent(dataEntryTab, row, col)
        col += 1

    if exists("save.json"):
        self.load()

    sidePanel = LabelFrame(dataEntryTab, text="Functions Panel")
    sidePanel.grid(row=row+1, column=0, columnspan=3, sticky="ew", padx=2, pady=2)

    Button(sidePanel, text="Calculate\nBudget", command=self.calculateBudget).grid(column=0, row=0, padx=2, pady=2)

    Button(sidePanel, text="Save", command=self.save).grid(column=1, row=0, padx=2, pady=2)
    Button(sidePanel, text="Load", command=self.load).grid(column=2, row=0, padx=2, pady=2)

def drawBudgetTab(self, budgetTab):
    row = 0
    Label(budgetTab, text="Income").grid(column=0, row=row, sticky="w")
    Label(budgetTab, text=f"{self.sumSource(self.incomeSources.sources)}").grid(column=1, row=row, sticky="e")
    row += 1
    Label(budgetTab, text="Expenses").grid(column=0, row=row, sticky="w")
    Label(budgetTab, text=f"{self.sumSource(self.expenseSources.sources)}").grid(column=1, row=row, sticky="e")
    row += 1
    Label(budgetTab, text="Budgeted Spending").grid(column=0, row=row, sticky="w")
    Label(budgetTab, text=f"{self.sumSource(self.budgetedSpending.sources)}").grid(column=1, row=row, sticky="e")
    row += 1
    Label(budgetTab, text="Savings").grid(column=0, row=row, sticky="w")
    Label(budgetTab, text=f"{self.sumSource(self.savingsSources.sources)}").grid(column=1, row=row, sticky="e")
    row += 1
    Label(budgetTab, text="Remaining").grid(column=0, row=row, sticky="w")
    Label(budgetTab, text=f"{round(self.sumSource(self.incomeSources.sources)-self.sumSource(self.expenseSources.sources)-self.sumSource(self.budgetedSpending.sources)-self.sumSource(self.savingsSources.sources), 2)}").grid(column=1, row=row, sticky="e")

def drawProjectionTab(self, projectionTab):
    return None

def drawFitnessTab(self, fitnessTab):
    row = 0
    Label(fitnessTab, text="Income").grid(column=0, row=row, sticky="w")
    Label(fitnessTab, text=f"{self.sumSource(self.incomeSources.sources)}").grid(column=1, row=row, sticky="e")
    row += 1
    Label(fitnessTab, text="Needs").grid(column=0, row=row, sticky="w")
    Label(fitnessTab, text=f"{self.sumSource(self.expenseSources.sources)+self.sumSource(self.budgetedSpending.sources)}").grid(column=1, row=row, sticky="e")
    row += 1
    Label(fitnessTab, text="Wants").grid(column=0, row=row, sticky="w")
    Label(fitnessTab, text=f"{self.sumSource(self.budgetedSpending.sources)}").grid(column=1, row=row, sticky="e")
    row += 1
    Label(fitnessTab, text="Savings").grid(column=0, row=row, sticky="w")
    Label(fitnessTab, text=f"{self.sumSource(self.savingsSources.sources)}").grid(column=1, row=row, sticky="e")
    row += 1