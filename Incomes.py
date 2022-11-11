from Source import Source

class generalIncomeSources(Source):
    def __init__(self):
        self.name           = "Income Sources"
        self.saveName       = "generalIncome"
        self.rootListbox    = None
        self.description    = "Money coming\nin this month"