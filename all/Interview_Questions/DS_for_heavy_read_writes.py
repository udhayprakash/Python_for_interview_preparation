class MyDS:
    def __init__(self):
        self.ds = {}

    def get(self, key):
        vals = self.ds.get(key)
        if vals:
            if isinstance(vals, list):
                return sum(vals) / len(vals)
            else:
                return vals
        else:
            # when key not present
            if len(self.ds) == 1:
                raise Exception("Insufficient data")
            elif key < min(self.ds) and key > max(self.ds):
                raise Exception("OutOfBounds")
            else:
                nbrVal1, nbrVal2 = self.nearest_neighbours(key)
                self.ds[key] = self.interpolation(nbrVal1, nbrVal2, key)
                return self.ds[key]

    def nearest_neighbours(self, givenKey):
        distances = sorted(
            ((key, abs(key - givenKey)) for key in self.ds), key=lambda x: x[1]
        )
        return [val for val, _ in distances[:2]]  # return nearest two values

    def interpolation(self, v1, v2, key):
        """
        # 41              45
        #    1 - 42 ---3

        # get(41)* 1/4  = get(45)* 3/4
        """
        total_distance = abs(v2 - v1)
        return (
            self.get(v1) * abs(key - v1) + self.get(v2) * abs(v2 - key)
        ) // total_distance

    def add(self, key, val):
        if key in self.ds:
            if isinstance(self.ds[key], list):
                self.ds[key].append(val)
            else:
                self.ds[key] = [self.ds[key], val]
        else:
            self.ds[key] = val


if __name__ == "__main__":
    # Adding
    pool = MyDS()
    pool.add(40, 9000)
    pool.add(44, 9100)
    pool.add(80, 9400)
    pool.add(80, 9500)
    pool.add(90, 9600)

    # Getting
    print("pool.get(44)", pool.get(44))  # returns 9100
    print("pool.get(80)", pool.get(80))  # get the average # return 9450
    print("pool.get(42)", pool.get(42))  # return 9050
    print("pool.get(43)", pool.get(43))  # return 9075
    print("pool.get(41)", pool.get(41))  # return 9025
    print("pool.get(81)", pool.get(81))  # return 9585.0
