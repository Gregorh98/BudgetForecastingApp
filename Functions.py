import json

def save(categories):
    save = {}
    for x in categories:
        save[x.saveName] = x.sources

    with open("save.json", "w") as f:
        json.dump(save, f)

def load():
    with open("save.json", "r") as f:
        save = json.load(f)
        return save