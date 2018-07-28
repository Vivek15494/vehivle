from vehicle import vehicle

class bike(vehicle):
      handle = True
      is_gear = True

      def __init__(self,handle,is_gear,no_of_wheels,speed,weight,mileage,color):
               self.handle=handle
               self.is_gear=is_gear
               super().__init__(no_of_wheels,speed,weight,mileage,color)
 
      def wheelie(self):
               print("the bike has started a wheelie")

      def stoppie(self):
               print("the bike has started a stoppie")




