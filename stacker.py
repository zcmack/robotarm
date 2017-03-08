import readline
import shlex
import robotarm
import historyitem

from robotarm import Robot
from historyitem import HistoryItem

print('Welcome to the robot mover. Type exit to quit`.')

#stacker is the main program that interacts with the robot arm as well as history items.
#a further improvement opportunity would be separating state machine operations to another class entirely
#leaving this file to be more strictly bound to the command line interaction

robot = Robot()
history = []


#unfortunately python doesn't have a switch statement. an endless while loop works ok for a CLI
while True:
    tokens = shlex.split(raw_input('>> '))
    cmd, args = tokens[0], tokens[1:]

    if len(robot.slots) == 0 and cmd!='size':
        print('program invalid. size command must run first.')
        break

    if cmd=='exit':
        exit()

    elif cmd=='size':

        if len(args)==1:
            size=args[0]
            currentSize = len(robot.slots)
            returnedItems = robot.setSize(int(size))
            newHistory = HistoryItem('setSize',size,'restoreSize',returnedItems)
            history.append(newHistory)
            robot.printStack()
        else:
            print('you must provide a single argument to set the number of slots.')
        
    elif cmd=='add':
        if len(args)==1:
            dest = int(args[0])
            robot.addBlock(dest)
            newHistory = HistoryItem('addBlock',dest,'removeBlock',dest)
            history.append(newHistory)
            robot.printStack()
        else:
            print('add command requires one argument.')

    elif cmd=='mv':
        if len(args)==2:
            src, dest = args
            src = int(src)
            dest = int(dest)
            robot.moveBlock(src,dest)
            newHistory = HistoryItem('moveBlock', [src,dest], 'moveBlock', [dest,src])
            history.append(newHistory)
            robot.printStack()
        else:
            print('mv command requires two arguments.')
    
    elif cmd=='rm':
        if len(args)==1:
            dest = args[0]
            robot.removeBlock(int(dest))
            newHistory = HistoryItem('removeBlock', dest, 'addBlock', dest)
            history.append(newHistory)
            robot.printStack()
        else:
            print('remove command requires one argument.')  

#assumption: replay command does not amend the history list with the actions it performs
#assumption: argument given to replay command signifies 1-n command to execute

    elif cmd=='replay':
        if len(args)==1:
            numCommands = int(args[0])
            histLength = len(history)

            if numCommands != 0 and numCommands <= histLength:
                start = histLength - numCommands

                for x in range(start,histLength):
                    historyItem = history[x]
                    func = getattr(Robot, historyItem.command)

                    #i don't feel great about the if check and casting here normally but in this contained program we know we're looking for integers
                    if isinstance(historyItem.argument, list):
                        src=int(historyItem.argument[0])
                        if historyItem.command=='moveBlock':
                            dest=int(historyItem.argument[1])
                            func(robot,src,dest)
                        else:
                            func(robot,src)
                    else:
                        func(robot,int(historyItem.argument))
                
            robot.printStack()

        else:
            print('replay command requires one argument.')

#assumption: undo command does not amend the history list with the actions it performs
#assumption: argument given to undo command signifies 1-n command to execute
#assumption: when undo'ing a size command, we need to restore the blocks in the slot

    elif cmd=='undo':
        if len(args)==1:
            numCommands = int(args[0])
            histLength = len(history)

            if numCommands != 0 and numCommands <= histLength:
                start = histLength - numCommands

                for x in range(start,histLength):
                    historyItem = history[x]
                    func = getattr(Robot, historyItem.inverseCommand)

                    #same here, i wish this was cleaner but we can expect integers and a set of predetermined commands
                    #a lot of massaging is required to allow for restoring of the blocks into removed slots
                    if isinstance(historyItem.inverseArgument, list):
                        src=int(historyItem.inverseArgument[0])
                        if historyItem.inverseCommand=='moveBlock':
                            dest=int(historyItem.inverseArgument[1])
                            func(robot,src,dest)
                        elif historyItem.inverseCommand=='restoreSize':
                            print historyItem.inverseArgument
                            for i in range(0,len(historyItem.inverseArgument)-1):
                                historyItem.inverseArgument[i] = int(historyItem.inverseArgument[i])
                            historyItem.inverseArgument.reverse()
                            func(robot,historyItem.inverseArgument)
                        else:
                            func(robot,src)
                    else:
                        func(robot,int(historyItem.inverseArgument))
                
            robot.printStack()

        else:
            print('undo command requires one argument.')

#convenience command for troubleshooting

    elif cmd=='print':
        robot.printStack()

    else:
        print('Unknown command: {}'.format(cmd))


