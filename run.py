from flight_parent_class import  *
from people_class import *
from passenger_class import *
from employee_class import *


passanger1 = Passenger("Miles","Eastwood","Board123")
passanger2 = Passenger("Sam","Forestter","Board321")
passanger3 = Passenger("Jack", "Wallace", "Board356")
#print(passanger2.f_name,passanger2.l_name,passanger2.ticket_num)



flight1 = Flight('EK454',"Turkey","UK","15:00")
flight2 = Flight('EK787',"Ibiza", "UK", "16:00")

flight1.add_passanger(passanger1)
flight2.add_passanger(passanger2)
flight1.add_passanger(passanger3)

list_of_flights =  [flight1,flight2]


for flight in list_of_flights:
    #print(self.flight_number)
    passangers = flight.getPassenger_list()
    print(passangers)

    #for passanger in passangers:
        #print(passanger.show())



# list of passengers
# first_passenger = Passenger('ek454', 'Dubai', 'London', '10am', '12553', 'Miles', 'Eastwood', 'Board123')
# second_passenger = Passenger('ek454', 'Dubai', 'London', '10am', '89375', 'Sam', 'Forestter', 'dub-lon132')
# first_flight = Flight('EK454', 'Dubai', 'London', '10am')
#
#
# first_employee = Employee('ek454', 'Dubai', 'London', '10am', '12553', 'Miles', 'Eastwood', 'dub-lon132')
#
# passenger_list = first_flight.all_passengers('Miles', 'Eastwood', 'Board123')
# print(passenger_list)
# #print(Flight.all_passengers('Miles', 'Eastwood', 'Board123'))
# total_passengers = [first_passenger, second_passenger]
# print(total_passengers)

# # Print checks
# check_flight = Flight('ek454', 'Dubai', 'London', '10am')
# #print(first_employee.flight_number)
#
# passenger_check = check_flight.check_in(int(input('Please enter passport number: ')))
# print(passenger_check)
# passenger_count = 0
# plane_capacity = 14
# while passenger_count < 1:
#     if passenger_check == 'Passport number accepted':
#         passenger_count += 1
#         print('Number of passengers on plane ' + str(passenger_count))
#     else:
#         if passenger_count >= 1:
#             break

# passenger_count = 0
# plane_capacity = 14
# while passenger_count != plane_capacity:
#     if passenger_check == 'Passport number accepted':
#         passenger_count += 1
#         print(passenger_count)
#     else:
#         break







#print(first_employee.check_in(12556))

