class vehicle():

      no_of_wheels= 0
      speed= 0
      weight= 0
      mileage= 0
      color= ' '

      def __init__(self,no_of_wheels,speed,weight,mileage,color):
            self.no_of_wheels=no_of_wheels
            self.speed=speed
            self.mileage=mileage
            self.color=color
     
      def go_forward(self):
            print("the vehicle with {0} wheels has started moving".format(self.no_of_wheels))

      def reverse(self):
            print("the vehicle with {0} wheels has started moving in reverse direction".format(self.no_of_wheels))

      def stop(self):
            print("the vehicle has stopped")
