class Soldier:
    """Class that represents an individual soldier."""
    
    def __init__(self, soldier):
        # soldier number
        self.soldier = soldier
        # next soldier in a circle
        self.next = None
        # previous soldier in a circle
        self.prev = None
        
class Army:
    """Class Army represents the circle of soliders."""
    def __init__(self, n):
        # n - number of soldiers
        self.circle = [Soldier(i) for i in range(1, n+1, 1)] # create all the Soldier objects
        # connect all soldiers into circular doubly linked list.
        for sol in range(0, n-1, 1):
            self.circle[sol].next = self.circle[sol+1]
            self.circle[sol].prev = self.circle[sol-1]
        self.circle[-1].next = self.circle[0]
        self.circle[-1].prev = self.circle[-2]
        
        # number of alive soldiers
        self.soldiers_alive = n 
        
            
    def advance(self, soldier):
        # function that excludes (kill) the soldier from the circular list
        soldier.prev.next = soldier.next
        soldier.next.prev = soldier.prev
    
    def kill_all(self, k):
        soldier = self.circle[k-1] # first soldier to kill
        
        # kill soldiers as long as only 1 remain
        while self.soldiers_alive-1:
            self.advance(soldier) # killing the soldier
            print("Soldier {0} is killed.".format(soldier.soldier))
            for i in range(k):
                soldier = soldier.next
            # number of soldiers alive is now reduced by 1
            self.soldiers_alive -= 1
        print("The last remaining soldier is {0}.".format(soldier.soldier))
            
    
num_of_soldiers = int(input("Enter number n of soliders, at least 2: "))
spacing_between = int(input("Enter spacing between victims, between 1 and {}: ".format(num_of_soldiers)))
army = Army(num_of_soldiers)
army.kill_all(spacing_between)
