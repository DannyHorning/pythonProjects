class Building:
    def __init__(self, name, location, floors, building_type):
        self.__name = name
        self.__location = location
        self.floors = floors
        self.building_type = building_type

    def get_name(self):
        return self.__name
    
    def get_location(self):
        return self.__location
    
    def get_floors(self):
        return self.floors
    
    def get_building_type(self):
        return self.building_type
    
    def set_builder(cls, builder):
        cls.builder = builder
    
    def get_builder(cls):
        return cls.builder
    
    def __str__(self):
        return f'{self.__name} is located at {self.__location}. It has {self.floors} floors. The building type is {self.building_type}'

class Building_Manager:
    def __init__(self):
        self.building = []
    
    def add_building(self, building):
        self.building.append(building)
    
    def remove_building(self, building):
        self.building.remove(building)
    
    def get_building_by_type(self, building_type):
        building_type_list = []
        for type in self.building:
            if type == building_type:
                building_type_list.append(type)
        print(building_type_list)
    
    def get_total_floors(self):
        total_floors = 0
        for floors in self.building:
            total_floors += self.floors 
        return total_floors
    
    def get_building_with_most_floors(self):
        most_floors = 0
        for floors in self.building:
            if floors > most_floors:
                most_floors = floors
            else:
                continue
        return floors
    
    def get_building_with_the_fewest_floors(self):
        fewest_floors = 10000
        for floors in self.building:
            if floors < fewest_floors:
                fewest_floors = floors
            else:
                continue
        return floors
    

manager = Building_Manager()
building1 = Building('Danny', '123 fake st', 3, 'condo')
building2 = Building('Annie', '456 real st', 7, 'apartment')
building3 = Building('Harry', '789 Dinosaur st', 20, 'skyscraper')
building4 = Building('Sam', '745 TREX st', 10, 'apartment')
building5 = Building('KD', '235 little st', 4, 'condo')

manager.add_building(building2)
manager.add_building(building3)
manager.add_building(building1)
manager.add_building(building4)
for x in manager.building:
    print(x)
manager.get_building_by_type('apartment')
print(manager.get_building_with_most_floors())
print(manager.get_building_with_the_fewest_floors())