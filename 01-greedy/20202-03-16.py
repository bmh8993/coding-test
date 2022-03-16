data = input()

cnt = [0, 0]
temp = int(data[0])
cnt[temp] += 1

for i in range(1, len(data)):
    if temp == int(data[i]):
        continue
    else:
        temp = int(data[i])
        cnt[temp] += 1


print(min(cnt))
