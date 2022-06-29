from tkinter import *
from IncomeSources import IncomeSources
from ExpenseSources import ExpenseSources
from SavingsSources import SavingsSources

class HomeWindow():
    def __init__(self):
        self.title  = "Budget App"
        self.root   = Tk()
        self.incomeSources = IncomeSources()
        self.expenseSources = ExpenseSources()
        self.savingsSources = SavingsSources()

    def draw(self):
        self.root.title(self.title)

        self.incomeSources.drawRootComponent(self.root, 0, 0)
        self.incomeSources.rootListbox.insert(0, "1")

        self.expenseSources.drawRootComponent(self.root, 0, 1)
        self.expenseSources.rootListbox.insert(0, "2")

        self.savingsSources.drawRootComponent(self.root, 0, 2)
        self.savingsSources.rootListbox.insert(0, "3")

        sidePanel = LabelFrame(self.root, text="Side Panel")
        sidePanel.grid(row=0, column=4, rowspan=3, sticky="ns", padx=2, pady=2)

        Button(sidePanel, text="Calculate Budget").grid(row=0, column=0, padx=2, pady=2)


        self.run()

    def run(self):
        while True:
            self.root.update()
