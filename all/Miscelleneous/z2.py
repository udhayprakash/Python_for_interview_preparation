while True:
    count = int(input())
    if count == -1:
        break
    total = 0
    prev_time_elapsed = 0
    for _ in range(count):
        speed, time_elapsed = map(int, input().split())
        if total == 0:
            total += speed * time_elapsed
        else:
            total += speed * (time_elapsed - prev_time_elapsed)
        prev_time_elapsed = time_elapsed
    print(total, "miles")

while True:
    count = int(input())
    if count == -1:
        break
    maxVotes = 0
    total = 0
    personSerial = 0
    for i in range(count):
        votes = int(input())
        if votes > maxVotes:
            maxVotes = votes
            personSerial = i + 1
        total += votes
    print(f"{total = } {maxVotes =}")
    winner = ""
    if maxVotes > total:
        winner = "majority winner %d" % (personSerial)
    elif maxVotes < total:
        winner = "minority winner %d" % (personSerial)
    else:
        winner = "no winner"
    print(winner)
