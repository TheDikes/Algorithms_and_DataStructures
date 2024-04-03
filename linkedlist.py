class ParkingSpace:
    def __init__(self, vehicle):
        self.vehicle = vehicle #the data part of the node (parking space)
        self.next = None # reference to the next node(parking space) in the linked list(Parking lot)


class ParkingLot:
    def __init__(self):
        self.head = None #initialize an empty linked list (parking lot)

    def append(self, vehicle):
        new_parking = ParkingSpace(vehicle) # Create a new parking space with the given vehicle data

        #if the linkedlist(parking lot) is empty, make the new parking space the head of the list(first parking in the parking lot)
        if self.head is None:
            self.head = new_parking
            return
        
        # Traverse the list(lot) to find the last parking space
        last_parking = self.head
        while last_parking.next:
            last_parking = last_parking.next

        # Park the new vehicle in the last parking space    
        last_parking.next = new_parking


    def prepend(self, vehicle):
        new_parking = ParkingSpace(vehicle)

        new_parking.next = self.head
        self.head = new_parking

    
    def display(self):
        current_parking = self.head
        
        while current_parking:
            print(current_parking.vehicle, end=" -> ")
            current_parking = current_parking.next

        print('end')




parking_lot = ParkingLot()
parking_lot.append("Car")
parking_lot.append("Bike")
parking_lot.append("Truck")

parking_lot.prepend("Motorcycle")
parking_lot.display()


# Removing a vehicle(parking space from the parking lot)
#    def leave(self, vehicle):
#         current_parking = self.head
#         prev_parking = None

#         # Search for the parking space containing the vehicle to leave
#         while current_parking and current_parking.vehicle != vehicle:
#             prev_parking = current_parking
#             current_parking = current_parking.next

#         # If the vehicle is found, remove it from the parking lot
#         if current_parking:
#             if prev_parking:
#                 prev_parking.next = current_parking.next
#             else:
#                 self.head = current_parking.next
#             del current_parking
