class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.big<=0:
                return False
            self.big -= 1
            return True

        if carType == 2:
            if self.medium<=0:
                return False
            self.medium -= 1
            return True

        if carType == 3:
            if self.small<=0:
                return False
            self.small -= 1
            return True
            
