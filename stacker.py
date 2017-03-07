import readline
import shlex
import robotarm

from robotarm import Robot


print('Welcome to the robot mover. Type exit to quit`.')


robot = Robot()
history = []
inverse = []

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
            print returnedItems
            
            inverse.append('restoreSize {}'.format(returnedItems))
            history.append('setSize {}'.format(size))
            robot.printStack()
        else:
            print('you must provide a single argument to set the number of slots.')
        
    elif cmd=='add':
        if len(args)==1:
            dest = int(args[0])
            robot.addBlock(dest)
            inverse.append('removeBlock {}'.format(dest))
            history.append('addBlock {}'.format(dest))
            robot.printStack()
        else:
            print('add command requires one argument.')

    elif cmd=='mv':
        if len(args)==2:
            src, dest = args
            src = int(src)
            dest = int(dest)
            robot.moveBlock(src,dest)
            history.append('addBlock {}'.format(src, dest))
            robot.printStack()
        else:
            print('mv command requires two arguments.')
    
    elif cmd=='rm':
        if len(args)==1:
            dest = args[0]
            robot.removeBlock(int(dest))
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
                    print history[x]
                    tokens = shlex.split(history[x])
                    func = getattr(Robot, tokens[0])

                    #ugly checking of number of tokens but we know there should only be one or two..
                    #with more time this needs to be less "hard-coded" and the casting should be removed
                    #a better solution would have been to store objects instead of text values...
                    if len(tokens)==2:
                        func(robot,int(tokens[1]))
                    elif len(tokens==3):
                        func(robot,int(tokens[1]),int(tokens[2]))
                
            robot.printStack()

        else:
            print('replay command requires one argument.')

#assumption: undo command does not amend the history list with the actions it performs
#assumption: argument given to undo command signifies 1-n command to execute

    elif cmd=='undo':
        if len(args)==1:
            numCommands = int(args[0])
            inverseLength = len(inverse)-1

            if numCommands != 0:
                start = inverseLength - numCommands

                for x in range(inverseLength, start, -1):
                    print inverse[x]
                    tokens = shlex.split(inverse[x])
                    func = getattr(Robot, tokens[0])

                    #even uglier hard-coding to check for restoreSize, casting to int caught up with me already. :)
                    #definitely need to make this more intuitive, would likely create a more robust state machine
                    #class for both replay and undo

                    if tokens[0]=='restoreSize':
                        argument=''
                        for chars in range(1,len(tokens)):
                            argument=argument+chars
                        func(robot,argument)
                    elif len(tokens)==2:
                        func(robot,int(tokens[1]))
                    elif len(tokens==3):
                        func(robot,int(tokens[1]),int(tokens[2]))
                
            robot.printStack()

    elif cmd =='history':
        func = robot.getHistory()
        print func

    elif cmd=='print':
        robot.printStack()

    else:
        print('Unknown command: {}'.format(cmd))


