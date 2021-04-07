class Pokemon:
    def __init__(self, name: str, level: int, type: str):
        self.name = str(name)
        self.level = int(level)
        self.type = str(type)
        self.faint = False
        self.max_hp = level*10
        self.hp = level*10

    def __repr__(self):
        return "level {level} {name} - HP: {hp}/{max_hp}".format(level=self.level, \
                                                                 name = self.name, \
                                                                 hp = self.hp, \
                                                                 max_hp = self.max_hp)

    def attack(self,target, move):
        damage = move.power/10
        print("{attacker} attacks {target} for {damage} health".format(attacker=self.name, \
                                                                target = target.name, \
                                                                damage = damage))
        target.lose_health(damage)

    def lose_health(self,damage):
        self.hp = max(0,self.max_hp-damage)

    def gain_health(self,heal):
        self.hp = min(self.max_hp, self.hp+heal)

    # class Stats:
    #     def __init__(self,IV, ):
    #     self.max_hp = level * 10
    #     self.hp = level * 10