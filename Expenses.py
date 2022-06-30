from Source import Source

class generalExpenses(Source):
    def __init__(self):
        self.name = "Expenses"
        self.rootListbox = None

class committedSpending(Source):
    def __init__(self):
        self.name = "Committed Spending"
        self.rootListbox = None

class budgetedSpending(Source):
    def __init__(self):
        self.name = "Budgeted Spending"
        self.rootListbox = None