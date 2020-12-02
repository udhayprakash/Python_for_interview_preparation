import itertools
import math 
import ipdb
def next_prime(n):
    for num in itertools.count(n + 1):
        for each_num in range(2, num):
            if num % each_num == 0:
                break
        else:
            return num


if __name__ == '__main__':
    print(f'{next_prime(7)  =}\n')
    print(f'{next_prime(11) =}\n')
    print(f'{next_prime(13) =}\n')
    print(f'{next_prime(15) =}\n')
    print(f'{next_prime(18) =}\n')
    print   (f'{next_prime(20) =}\n')
    print(next_prime(76547984763986793869346936739673934990630345718237658237658723685428147581759874812745812745812745128))

    # for i in range(24):
    #     print(i, math.sqrt(i))
