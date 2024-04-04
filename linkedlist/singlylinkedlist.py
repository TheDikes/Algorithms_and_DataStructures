class TrainCar:
    def __init__(self, cargo):
        self.cargo = cargo # the data part of the node (train car)
        self.next = None # Reference to the next node(train car) in the linked list (Train)


class Train:
    def __init__(self):
        self.head = None #initialize an empty linked list (train)

    def append(self, cargo):
        new_carriage = TrainCar(cargo) # Create a new carriage space with the given cargo data

        #if the linkedlist(Train) is empty with no cargo, make the new carriage space the head of the list(first cargo on the Train)
        if self.head is None:
            self.head = new_carriage
            return
        
        # Traverse the list(Train) to find the last carriage 
        last_carriage = self.head
        while last_carriage.next:
            last_carriage = last_carriage.next

        # Park the new carriage in the last carriage space    
        last_carriage.next = new_carriage 


    def prepend(self, cargo):
        new_carriage = TrainCar(cargo)

        new_carriage.next = self.head
        self.head = new_carriage

    
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
            print(current_carriage.cargo, end=" -> ")
            current_carriage = current_carriage.next

        print('end')




train = Train()
train.append("Car 1")
train.append("Car 2")
train.append("Car 3")

train.prepend("Car 0")
# train.detach("Car 2")
train.display()
