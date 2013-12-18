cars = 100 #assign cars to 100
space_in_a_car = 4.0 # assign space_in_a_car to be the double 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers # 100 - 30
cars_driven = drivers #two variables both reping 100
carpool_capacity = cars_driven * space_in_a_car #double times int
average_passengers_per_car = passengers / cars_driven #90/100


print "There are", cars, "cars available." #the comma acts as + in java but adds a space
print "There are only", drivers, "drivers available." 
print "There will be", cars_not_driven, "empty cars available."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
