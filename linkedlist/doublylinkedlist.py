class TrainCar:
    def __init__(self, cargo):
        self.cargo = cargo
        self.prev = None
        self.next = None


class Train:
    def __init__(self):
        self.head = None #initialize an empty linked list (train)
        self.tail = None # maintain a reference to the last car in the train
        

    def append(self, cargo):
        new_carriage = TrainCar(cargo) # Create a new carriage space with the given cargo data

        #if the linkedlist(Train) is empty with no cargo, set the new car as both head and tail
        if self.head is None: 
            self.head = new_carriage
            self.tail = new_carriage
            return
        
         # Link the new car to the tail and update the tail reference
        new_carriage.prev = self.tail
        self.tail.next = new_carriage
        self.tail = new_carriage  # Update the tail to the new car


    def prepend(self, cargo):
        new_carriage = TrainCar(cargo)

        new_carriage.next = self.head
        self.head = new_carriage


    def insert_at_position(self, position, cargo):
        if position < 0:
            print ("Invalid position")
        
        new_carriage = TrainCar(cargo)

        if position == 0:
            new_carriage.next = self.head
            self.head = new_carriage
            return
        
        # Traversing down the list
        current = self.head
        
        count = 0
        while current:
            if count == position - 1: # This checks if the current position is one less than the desired inserted position.
                new_carriage.next = current.next
                current.next = new_carriage
                break

            current = current.next
            count +=1

        else:
            print("Position out of range.")


    
    # Removing a cargo (carriage from the train)
    def detach(self, cargo):
        current_carriage = self.head
        prev_carriage = None

        # Search for the carriage space containing the cargo to remove
        while current_carriage and current_carriage.cargo != cargo:
            prev_carriage = current_carriage
            current_carriage = current_carriage.next

        # If the cargo is found, remove it from the Train
        if current_carriage:
            if prev_carriage:
                prev_carriage.next = current_carriage.next
            else:
                self.head = current_carriage.next
            del current_carriage


    
    def display(self):
        current_carriage = self.head
        
        while current_carriage:
            print(current_carriage.cargo, end=" <=> ")
            current_carriage = current_carriage.next

        print('end')




train = Train()
train.append("Passenger Car ")
train.append("Dining Car")
train.append("Swimming Car")
train.prepend("Pilot Car")
train.prepend("Gas Car")
train.detach("Gas Car")

train.insert_at_position(3, "Kitchen Car")

train.display()
