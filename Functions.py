import json

def save(incomes, expenses, savings):
    save = {"incomes":incomes, "expenses":expenses, "savings":savings}

    with open("save.json", "w") as f:
        json.dump(save, f)

def load():
    with open("save.json", "r") as f:
        save = json.load(f)
        return save