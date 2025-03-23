n = int(input())
ext_count = {}  # 확장자별 개수를 세기 위한 딕셔너리

for t in range(n):
    hjj = input().split('.')[1]

    # 확장자가 이미 있으면 개수 증가, 없으면 새로 추가
    if hjj in ext_count:
        ext_count[hjj] += 1
    else:
        ext_count[hjj] = 1

# 확장자 키를 알파벳 순으로 정렬하고 출력
for ext in sorted(ext_count.keys()):
    print(f"{ext} {ext_count[ext]}")