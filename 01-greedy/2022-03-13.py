data = map(int, input().split())

data.sort()  # 객체 그대로 오름차순 정렬
result = 0
count = 0

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0  # 그룹이 생성된 순간 사람을 더 영입하지 않아야 제일 많은 그룹을 만들 수 있다.

print(result)
