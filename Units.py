def second_sol():
    list_ = list(map(int,input().split()))
    list_.sort()

    answer = 0
    for i in range(100):
        curr_count = 0
        temp = i
        for j in range(5,-1,-1):
            value = list_[j]
            count = temp // value
            curr_count += count
            temp -= value * count
        answer += curr_count

    print(answer / 100.0)
second_sol()
