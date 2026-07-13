class car:
    def __init__(self):
        self._speed = 45

    def inc_speed(self,add):
        self._speed += add

class s_car(car):
    def show_speed(self):
        return self._speed
        



c = s_car()
c.inc_speed(25)
print(c._speed)

