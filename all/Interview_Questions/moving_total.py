class MovingTotal:
    def __init__(self):
        self.data = []
        self.sums = {}

    def append(self, numbers):
        """
        :param numbers: (list) The list of numbers.
        """
        i = len(self.data) - 2 if self.data else 0
        self.data.extend(numbers)
        while True:
            slice = self.data[i:i+3]
            if len(slice) != 3:
                break
            self.sums[sum(slice)] = 1
            i += 1

    def contains(self, total):
        """
        :param total: (int) The total to check for.
        :returns: (bool) If MovingTotal contains the total.
        """
        return total in self.sums


if __name__ == "__main__":
    movingtotal = MovingTotal()

    movingtotal.append([1, 2, 3, 4])
    print(movingtotal.contains(6))
    print(movingtotal.contains(9))
    print(movingtotal.contains(12))
    print(movingtotal.contains(7))

    movingtotal.append([5])
    print(movingtotal.contains(6))
    print(movingtotal.contains(9))
    print(movingtotal.contains(12))
    print(movingtotal.contains(7))
