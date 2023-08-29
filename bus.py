class Bus:
    def __init__(self, input_route_number, input_destination):
        self.route_number = input_route_number
        self.destination = input_destination
        self.passengers = []

    def drive(self): #might have to change this so that is happens whenever the bus moves
        return "Brum brum" #maybe next this in another def

    def passenger_count(self): #returning the number of passengers
        return len(self.passengers)

    def pick_up(self, input_passenger): #would this be person? passenger.name
        self.passengers.append(input_passenger)

    def drop_off(self, input_pasenger):
        self.passengers.remove(input_pasenger)

    def empty_bus(self): #want to remove them until the bus is empty
        self.passengers.clear()

    # def pick_up_from_stop(self, bus_station_queue):
    #     for x in :
    #         return


# Try writing a method that the bus would call, to collect 
# all of the passengers from a stop. This might look like 
# bus.pick_up_from_stop(self, bus_stop_1). This should take 
# all of the passengers waiting in line at the stop, and put 
# them inside of the bus. So the stop will now have nobody in 
# the queue, and the number of people on the bus will increase 
# by however many people the stop had at it.