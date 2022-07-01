from Source import Source

class generalExpenses(Source):
    def __init__(self):
        self.name           = "Expenses"
        self.saveName       = "generalExpenses"
        self.rootListbox    = None

class committedSpending(Source):
    def __init__(self):
        self.name           = "Committed Spending"
        self.saveName       = "committedSpending"
        self.rootListbox    = None

class budgetedSpending(Source):
    def __init__(self):
        self.name           = "Budgeted Spending"
        self.saveName       = "budgetedSpending"
        self.rootListbox    = None