class Car (object):
    def __init__(self,model,color,company,speed_limit) :
        self.model=model
        self.color=color
        self.company=company
        self.speed_limit=speed_limit

    def start (self):
        print("Started")

    def stop (self):
        print("Stop")
    
    def accelerate(self):
        print("Accelerated")

audi=Car ("A6","black","Audi",100)   
print(audi.start())


