from Source import Source

class generalExpenses(Source):
    def __init__(self):
        self.name           = "Expenses"
        self.saveName       = "generalExpenses"
        self.rootListbox    = None
        self.description    = "Fixed expenses like bills, loans, etc..."

class plannedSpending(Source):
    def __init__(self):
        self.name           = "Planned Spending"
        self.saveName       = "plannedSpending"
        self.rootListbox    = None
        self.description    = "Planned expenses that are coming up this\nmonth like car MOT, or boiler service"

class budgetedSpending(Source):
    def __init__(self):
        self.name           = "Budgeted Spending"
        self.saveName       = "budgetedSpending"
        self.rootListbox    = None
        self.description    = "Budgeted expenses like food or petrol"