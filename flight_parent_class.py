class Flight():

    def __init__(self, flight_number, destination, origin, time):
        self.flight_number = flight_number
        self.destination = destination
        self.orgin = origin
        self.time = time
        self.passenger_list = []


    def check_in(self, pass_port_num):

        if pass_port_num > 0 and len(str(pass_port_num)) == 5:
            return 'Passport number accepted'
        else:
            return 'Invalid Passport number. DO not let passenger/employee board flight'

    # def all_passengers(self, f_name, l_name, boarding_num):
    #     return 'Passenger: ' + f_name + ' ' + l_name + '. ' + boarding_num +



    def add_passanger(self, passanger):
        return self.passenger_list.append(passanger)

    def getPassenger_list(self):
        return self.passenger_list

