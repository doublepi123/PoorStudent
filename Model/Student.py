class Student:
    stuid = ''
    name = ''
    age = ''
    people = ''
    costForFood = 0
    costForOther = 0

    def __init__(self, stuid, name, age, people, costForFood, costForOther):
        self.stuid = stuid
        self.name = name
        self.age = age
        self.people = people
        self.costForFood = costForFood
        self.costForOther = costForOther
