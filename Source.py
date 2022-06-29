from tkinter import LabelFrame, Listbox, Button, Toplevel, Label, Entry, messagebox


class Source:
    def drawRootComponent(self, root, row, col):
        self.root = root
        self.sources = {}
        rootFrame = LabelFrame(root, text=self.name)
        rootFrame.grid(row=row, column=col, padx=2, pady=2)

        self.rootListbox = Listbox(rootFrame)
        self.rootListbox.grid(row=1, column=0, columnspan=3, padx=2, pady=2)

        Button(rootFrame, text="Add", command=self.drawAddWindow).grid(row=2, column=0, padx=2, pady=4)
        Button(rootFrame, text="Remove", command=self.removeRecord).grid(row=2, column=1, padx=2, pady=4)
        Button(rootFrame, text="Edit", command=self.drawEditWindow).grid(row=2, column=2, padx=2, pady=4)

    def drawAddWindow(self):
        addWindow = Toplevel(self.root)
        Label(addWindow, text="Add " + self.name).grid(row=0, column=0, columnspan=2)

        Label(addWindow, text="Name").grid(row=1, column=0, sticky="w")
        nameEntry = Entry(addWindow)
        nameEntry.grid(row=1, column=1)

        Label(addWindow, text="Amount").grid(row=2, column=0, sticky="w")
        amountEntry = Entry(addWindow)
        amountEntry.grid(row=2, column=1)

        Label(addWindow, text="Frequency").grid(row=3, column=0, sticky="w")
        frequencyEntry = Entry(addWindow)
        frequencyEntry.grid(row=3, column=1)

        Button(addWindow, text="Add", command=lambda: self.addRecord(nameEntry.get(), amountEntry.get(), frequencyEntry.get())).grid(row=4, column=0, columnspan=2)

    def drawEditWindow(self):
        editWindow = Toplevel(self.root)
        Label(editWindow, text="Edit " + self.name[:-1]).grid(row=0, column=0, columnspan=2)

        Label(editWindow, text="Amount").grid(row=2, column=0, sticky="w")
        amountEntry = Entry(editWindow)
        amountEntry.grid(row=2, column=1)

        Label(editWindow, text="Frequency").grid(row=3, column=0, sticky="w")
        frequencyEntry = Entry(editWindow)
        frequencyEntry.grid(row=3, column=1)

        Button(editWindow, text="Update", command=lambda: self.addRecord(nameEntry.get(), amountEntry.get(), frequencyEntry.get())).grid(row=4, column=0, columnspan=2)

    def validateInput(self, name, amount, frequency):
        try:
            name        = str(name)
            amount      = float(amount)
            frequency   = str(frequency)
        except:
            return False

        if name == "":
            return False
        if amount <= 0:
            return False
        if frequency == "":
            return False

        return True

    def removeRecord(self):
        return

    def addRecord(self, name, amount, frequency):
        if self.validateInput(name, amount, frequency):
            self.sources[name] = {"amount": amount, "frequency": frequency}
            print(self.sources)


    def editRecord(self, name, amount, frequency):
        if self.validateInput(name, amount, frequency):
            if self.sources[name]:
                self.sources[name] = {"amount": amount, "frequency": frequency}
                print(self.sources)