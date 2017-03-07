class HistoryItem:

#very basic class to maintain history objects, we'll approximate a simple state machine
    def __init__(self,command,argument,inverseCommand,inverseArgument=0):
        self.command=command
        self.argument=argument
        self.inverseCommand=inverseCommand
        print inverseArgument
        self.inverseArgument=inverseArgument