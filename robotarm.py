
class Robot:
    slots = [] 

    def setSize(self, newSize):
        currentSize = len(self.slots)
        if currentSize==0:
            for i in range (0, newSize):
                self.slots.append(0)
        elif newSize > currentSize :
            addSlots = newSize-currentSize
            for i in range (0,addSlots):
                self.slots.append(0)
        elif newSize < currentSize:
            removeSlots = currentSize-newSize
            removedItems = []
            for i in range(0,removeSlots):
                removedItems.append(self.slots.pop())
            return removedItems
            
    def restoreSize(self, removedSlots):
        #used by undo method to restore slots removed with blocks present
        print('robot class {}'.format(removedSlots))
        self.slots.extend(removedSlots)
        #for i in removedSlots:
        #    self.slots.append(i[0])
        return True
        
    def addBlock(self, target):
        if self.checkTarget(target) == True:
            self.slots[target-1]=self.slots[target-1]+1
            return True
        

    def removeBlock(self, target):
        if self.checkTarget(target):
            if self.slots[target-1] == 0:
                print('slot {} is empty'.format(target))
            else:
                self.slots[target-1]=self.slots[target-1]-1
                return True

    def moveBlock(self, src, dest):
        if self.checkTarget(dest):
                retValue = self.removeBlock(src)
                if retValue == True:
                    self.addBlock(dest)
    
    def checkTarget(self,target):
        if len(self.slots) < target or target == 0:
            print('no slot exists at {}\n'.format(target))
            return False
        else:
            return True
 
    def printStack(self):
        print self.slots
        for x in range (0,len(self.slots)):
            blocks = self.slots[x]
            printedBlocks = ''
            printedSlot = 0
            for y in range(0, blocks):
                printedBlocks=printedBlocks+'X'
            
            printedSlot=x+1
            print('{}: {}'.format(printedSlot,printedBlocks))