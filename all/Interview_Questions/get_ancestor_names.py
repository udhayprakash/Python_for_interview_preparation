class Person:
    def __init__(self, name, mother, father) -> None:
        self.name = name
        self.mother = mother
        self.father = father

    def getNamesOfAllAncestors(self, resultArray=None):
        # write this function
        if not resultArray:
            resultArray = []
        resultArray.append(self.name)
        if self.mother:
            self.mother.getNamesOfAllAncestors(resultArray)
        if self.father:
            self.father.getNamesOfAllAncestors(resultArray)
        return resultArray


john = Person(
    "John",
    Person("Jane", Person("Jill", None, None), Person("Jack", None, None)),
    Person("Jim", Person("Josephine", None, None), Person("Joe", None, None)),
)
ancestors = john.getNamesOfAllAncestors()
print(",".join(ancestors))
# John,Jane,Jill,Jack,Jim,Josephine,Joe
