import copy
class club(object):
    def __init__(self, leader, hero):
        self.leader = leader
        self.hero = hero

class Person(object):
    def __init__(self, name, age):
        self.age = age
        self.name = name

if __name__ == '__main__':
    org = 5
    cpy = org
    cpy = 6
    print(5)
    print(6)

    nums = list(range(0,11))
    cpyNums = nums
    cpyNums[0] = 100
    print()
    print(nums)
    print(cpyNums)

    orgNums = list(range(0,11))
    shallowList = copy.copy(orgNums)
    shallowList[0]= -10
    print()
    print(orgNums)
    print(shallowList)

    #Shallow copy is only 1 level deep, so if you have nested lists or complex objects, it won't copy the whole thing
    #So you need deep copying
    orgNestList = [[1,2,3],[4,5,6],[7,8,9]]
    cpyNestedList = copy.deepcopy(orgNestList)
    cpyNestedList[0][0] = 101
    print()
    print(orgNestList)
    print(cpyNestedList)

    #Shallow copies work for objects that 1 level deep like so:
    p1 = Person('Bruce Wayne', 30)
    p2 = copy.copy(p1)
    p2.name = 'Clark Kent'
    p2.age = 40
    print()
    print(p1.name, p1.age)
    print(p2.name, p2.age)

    #Deep copies won't work for nested objects
    company = club(p1,p2)
    waterCMP = copy.deepcopy(company)

    waterCMP.hero.name = 'Arthur Curry'
    waterCMP.hero.age = 100
    print()
    print(waterCMP.leader.name, waterCMP.leader.age)
    print(waterCMP.hero.name, waterCMP.hero.age)