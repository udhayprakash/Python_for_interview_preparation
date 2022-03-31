def parse_csv(csv, separator=',', quote='"'):
    print([each.split(separator) for each in csv.splitlines()])
    return [each.split(separator) for each in csv.splitlines()]


assert parse_csv("1,2,3\n4,5,6") == [
    ['1', '2', '3'], ['4', '5', '6']]


assert parse_csv("1\t2\t3\n4\t5\t6", "\t") == [
    ['1', '2', '3'], ['4', '5', '6']]


assert parse_csv("1,\"two was here\",3\n4,5,6") == [
    ['1', 'two was here', '3'], ['4', '5', '6']]