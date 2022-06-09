# ref: https://www.tutorialspoint.com/data_structures_algorithms/tower_of_hanoi.htm

# Recursive Python function to solve tower of hanoi


def TowerOfHanoi(n, source, destination, auxilliary):
    if n == 1:
        print(f"Move disk 1 from source {source} to destination {destination}")
        return
    TowerOfHanoi(n - 1, source, auxilliary, destination)
    print(f"Move disk {n} from source {source} to destination {destination}")
    TowerOfHanoi(n - 1, auxilliary, destination, source)


# Driver code
n = 4
TowerOfHanoi(n, "A", "B", "C")
# A, C, B are the name of rods
