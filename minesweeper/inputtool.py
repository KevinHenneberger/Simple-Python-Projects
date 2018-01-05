class InputTool:

    def __init__(self, options):
        self.options = options

    def getInput(self):
        while True:
            self.input = input("[OPTIONS] || " + (" | ".join([option + " (" + key + ")" for key, option in self.options.items()])) + " || - ")

            if (self.input in self.options.keys()):
                return self.input
