def alarm(hour,minute):
    remaining_min = (minute - 45)
    if remaining_min < 0:
        hour-=1
    return hour%24,remaining_min%60

hour,minute = map(int,input().split())

ans = alarm(hour,minute)
print(ans[0],ans[1])