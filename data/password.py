import random as rnd

class Password:
    def __init__(self, *args, **kwargs):
        self.airplane_n = rnd.randint(21, 29)
        self.departure_time = rnd.randint(7, 12)
        self.sigsauer_rifles = rnd.randint(10, 99)
        self.atomic_bombs = rnd.randint(20, 45)
        self.lmg_rifles = rnd.randint(1, 5)
        self.lmg_caliber = rnd.choice([22, 30, 40, 45, 50])
        self.arrival_time = rnd.randint(13, 21)