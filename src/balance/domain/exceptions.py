class ClosingGroupNotValid(Exception):
    default = "Closing group not valid"

    def __init__(self, message):
        self.message = message or self.default
        super().__init__(self.message)
