def second_sol():
    list_ = list(map(int,input().split()))
    list_.sort()

    ans = 0
    for i in range(100):
        curr_count = 0
        temp = i
        for j in range(5,-1,-1):
            value = list_[j]
            count = temp // value
            curr_count += count
            temp -= value * count
        ans += curr_count

    print(ans / 100.0)
second_sol()
