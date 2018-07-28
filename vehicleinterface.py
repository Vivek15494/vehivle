from truck import truck

truck_obj =truck(100, 60, 6, 40, 1500, 10, "red")
print(truck_obj.max_load)
print(truck_obj.speed_limit)
print(truck_obj.load)
truck_obj.unload()
truck_obj.stop()
print(truck_obj.no_of_wheels)
