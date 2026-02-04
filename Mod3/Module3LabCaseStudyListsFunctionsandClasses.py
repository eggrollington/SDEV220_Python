# Module3LabCaseStudyListsFunctionsandClasses.py
# Michael Webb
# this program defines a Vehicles class and an Automobile subclass. It prompts the user for vehicle details and displays them.
class Vehicles:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

           
class Automobile(Vehicles):
    def __init__(self,vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display_info(self):
        print("\n___ Vehicle Details ___")
        print(f"Vehicle type: {self.vehicle_type}")
        print(f"year: {self.year}")
        print(f"make: {self.make}")
        print(f"model: {self.model}")
        print(f"doors: {self.doors}")
        print(f"roof: {self.roof}")

def main():
    vehicle_type = "car"
    year = input("Enter the vehicle's year: ")
    make = input("Enter the vehicle's make: ")
    model = input("Enter the vehicle's model: ")
    doors = input("Enter the number of doors (2 or 4): ")
    roof = input("Enter the type of roof (solid or sunroof): ")
    my_automobile = Automobile(vehicle_type, year, make, model, doors, roof)
    my_automobile.display_info()
if __name__ == "__main__":
    main()
    