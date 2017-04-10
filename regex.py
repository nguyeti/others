class Car():
    def __init__(self, model="unknown", color="black"):
        self.model = model;
        self.color = color;

    def printInfo(self):
        return self.model + " " + self.color
car1 = Car("Toyota Corolla")

print(car1.printInfo())


class MiniCar(Car):
    def __init__(self, model, color,type="mini"):
        Car.__init__(self,model, color)
        self.type=type
        
    def printInfo(self):
        return Car.printInfo(self) + " " + self.type
miniCar = MiniCar("mini","red")
print(miniCar.printInfo())


        
def fromLine( line):
    fields = line.split('|')
    if (len(fields) == 4):
        characterID = fields[0]
        connections = fields[1].split(',')
        distance = int(fields[2])
        color = fields[3]
    connections = ','.join(connections)
    return '|'.join( (characterID, connections, str(distance), color) )

print(fromLine("332||1|GRAY"))

