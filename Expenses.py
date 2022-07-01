from Source import Source

class generalExpenses(Source):
    def __init__(self):
        self.name           = "Expenses"
        self.saveName       = "generalExpenses"
        self.rootListbox    = None

class plannedSpending(Source):
    def __init__(self):
        self.name           = "Planned Spending"
        self.saveName       = "plannedSpending"
        self.rootListbox    = None

class budgetedSpending(Source):
    def __init__(self):
        self.name           = "Budgeted Spending"
        self.saveName       = "budgetedSpending"
        self.rootListbox    = None