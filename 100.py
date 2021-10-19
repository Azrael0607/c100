class Car:
    def __init__(self,model,color,company,speed_limit):
        self.color = color
        self.company = company
        self.speed_limit = speed_limit
        self.model = model

    def Start(self):
        print('Started')
    def Accelerate(self):
        print('Accelerate')
    def Stop(self):
        print('Stop')

audi = Car('A6','red','audi','150')
print(audi.color)
##Car.Stop(audi)
