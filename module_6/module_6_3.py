from random import randrange


class Animal:
    _DEGREE_OF_DANGER = 0  # Степень опасности

    live = True             #
    sound = None            # Звук (изначально отсутствует)

    def __init__(self, speed=None, _cords=None):
        if _cords is None:
            _cords = [0, 0, 0]
        self._cords = _cords
        self.speed = speed

    def move(self, dx, dy, dz):
        if dz < 0:
            print("It's too deep, i can't dive :(")
            return
        self._cords = [dx * self.speed, dy * self.speed, dz * self.speed]

    def get_cords(self):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you O_O")

    def speak(self):
        print(self.sound)

class Bird(Animal):
    _DEGREE_OF_DANGER = 3

    beak = True

    def lay_eggs(self):
        print(f"Here are(is) {randrange(1, 5)} eggs fo you")

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self._cords[2] -= int(abs(dz) * self.speed / 2)

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):
    sound = "Click-click-click"


if __name__ == "__main__":
    db = Duckbill(10)

    print(db.live)
    print(db.beak)

    db.speak()
    db.attack()
    db.move(1, 2, 3)
    db.get_cords()
    db.dive_in(6)
    db.get_cords()
    db.lay_eggs()