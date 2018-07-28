from vehicle import vehicle 

class car(vehicle):
      ac = True
      steering_wheel = 0
      seatbelt = True
      audio_player = True

      def __init__(self,ac,steering_wheel,seatbelt,audio_player):
             self.ac=ac
             self.steering_wheel=steering_wheel
             self.seatbelt=seatbelt
             self.audio_player=audio_player
             super().__init__(no_of_wheels,speed,weight,mileage,color)

      def drift(self):
             print("the car is drifting")

      def deploy_airbags(self):
             print("the air bags are deployed")
