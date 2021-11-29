import yaml
from demo_objects import DemoHero

class Hero:

    def __repr__(self):
        return "%s(name=%r, hp=%r, sp=%r)" % (
            self.__class__.__name__, self.name, self.hp, self.sp)

# hero = Hero("Stu", 154, 500)

# hero = yaml.load(open("objects.yaml"), Loader=yaml.FullLoader)  # for one record only

heroes = []

for hero in yaml.load_all(open("objects.yaml").read(), Loader=yaml.Loader):
    heroes.append(hero)

print(heroes)
