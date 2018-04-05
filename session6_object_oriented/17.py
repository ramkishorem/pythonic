"""
Instances as attributes

Take a general car service station. you have to keep a database 
of cars and the services done on each car.

Doing this all in a single class can become complex. Let us 
split it up into two simple classes.
"""

class Car:
    """A model for customer cars"""
    def __init__(self, brand, model, make, number):
        """ initialise car basic info"""
        self.brand = brand
        self.model = model
        self.make = make
        self.number = number
    
    def view_info(self):
        """print information about the car"""
        print('{} {} ({}) numbered {}'.format(
            self.brand,
            self.model,
            self.make,
            self.number,
        ))

class Service:
    """a model for a service performed"""
    def __init__(self, car, date, odometer, bill):
        """initialise service details"""
        self.car = car
        self.date = date
        self.odometer = odometer
        self.bill = bill
    
    def view_details(self):
        """print details about the car"""
        self.car.view_info()
        print('\tServiced on : {}'.format(self.date))
        print('\tOdometer    : {} km'.format(self.odometer))
        print('\tBill Amount : Rs. {}'.format(self.bill))
    
car1 = Car('Toyota','Corolla','2016','TN1234')
service1 = Service(car1, '2018-03-03', 18000, 4550)
service1.view_details()
# Output:
# Toyota Corolla (2016) numbered TN1234
#         Serviced on : 2018-03-03
#         Odometer    : 18000 km
#         Bill Amount : Rs. 4550


service2 = Service(car1, '2018-07-03', 21500, 4890)
service2.view_details()
# Output:
# Toyota Corolla (2016) numbered TN1234
#         Serviced on : 2018-07-03
#         Odometer    : 21500 km
#         Bill Amount : Rs. 4890

"""
We established a relationship between the Car and its services
using the car instance as attribute in services.

We are able to link multiple services to a car.

Using this technique we can create complex multilevel relationships
among many models.
Examples:
  You can create a customer model and have multiple cars 
    under the customer.
  You can create a brand model and link all the cars belonging 
    to that brand.
  You can create branch model, have multiple branches, link 
    services with branches.

You can model requirements of any magnitude this way.
"""