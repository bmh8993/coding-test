# N, K을 공백을 기준으로 구분하여 int로 변환(map)
n, k = map(int, input().split())

result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n // k) * k
    result += n - target  # 1을 빼는 연산의 개수를 result에 더하기
    n = target

    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break

    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
# n이 1보다 크다면, 그만큼 빼줘야한다. 그 회수를 result에 더한다.
result += (n - 1)
print(1)
