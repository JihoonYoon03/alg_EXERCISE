import random

names = [

    "윤지훈",

    "김민준", "이도현", "박서준", "정현우", "최지호",

    "장우진", "윤태현", "조민성", "오준호", "한시우",

    "김서연", "이지민", "박하윤", "정다은", "최예린",

    "장수아", "윤지아", "조하늘", "오소율", "한은채",

    "서지후", "배도윤", "임하람", "강유진", "노은서",

    "문채린", "신예준", "류아린", "홍지호", "곽서현"

]

def index(arr):
    idx = 0
    for name in arr:
        if name == "윤지훈":
            print(f"Index of my name is: {idx}")
            break;
        else:
            idx += 1

def sort_insert(arr, start, end_inclusive):
    for i in range(start, end_inclusive + 1, 1):  # 0번 인덱스는 이미 정렬된 배열로 보고 제외
        v = arr[i]
        j = i - 1  # j는 정렬된 배열의 가장 끝 인덱스부터 시작함
        while j >= 0 and arr[j] > v:  # j가 0 이상이고 현재 주인공 값보다 큰 동안 반복
            arr[j + 1] = arr[j]  # 한 칸씩 뒤로 밀기
            j -= 1  # 뒤로 밀었다면 다음 값으로 넘어가기
        arr[j + 1] = v

def sort_merge(arr, start, end_inclusive):
    if end_inclusive <= start: return # 값이 하나이면 return
    elif end_inclusive - start < 5: sort_insert(arr, start, end_inclusive) # 5개 원소 이하이면 삽입정렬
    else:
        mid = (start + end_inclusive) // 2
        sort_merge(arr, start, mid) # start부터 mid까지(inclusive) 정렬
        sort_merge(arr, mid + 1, end_inclusive) # mid + 1부터 end_inclusive까지 정렬
        merge(arr, start, mid + 1, end_inclusive) # start부터 mid, mid + 1부터 end_inclusive까지의 배열 병합

def merge(arr, first, second, end_inclusive):
    merged = []
    f, s = first, second
    while f < s and second <= end_inclusive: # 지정 범위 내에서만 정렬
        if arr[f] <= arr[s]:
            merged.append(arr[f])
            f += 1
        else:
            merged.append(arr[s])
            s += 1

    while f < second:   # 왼쪽에 데이터가 남아있다.
        merged.append(arr[f])
        f += 1

    while s <= end_inclusive: # 오른쪽에 데이터가 남아있다.
        merged.append(arr[s])
        s += 1

    arr[first:end_inclusive + 1] = merged


def partition(arr, left, right):
    pivot = arr[random.randint(left, right)] # right = inclusive

    front = left
    last = right + 1

    while True:
        while True:
            if front > last or front > right or arr[front] > pivot:
                break # last와 엇갈리거나, 데이터 끝이거나, 피봇보다 큰 경우 멈춤
            else:
                front += 1

        while True:
            last -= 1
            if last < front or last < left or arr[last] < pivot:
                break # 피봇보다 작은 값을 찾은 경우, 멈춤

        if front >= last: break # 엇갈린 시점에서 중단

        arr[front], arr[last] = arr[last], arr[front] # 값 교환

    return last # = 피봇의 최종 위치


def sort_quick(arr, start, end_inclusive):
    if start >= end_inclusive: return
    if end_inclusive - start < 5:
        sort_insert(arr, start, end_inclusive)
        return
    pivot = partition(arr, start, end_inclusive)
    sort_quick(arr, start, pivot)
    sort_quick(arr, pivot + 1, end_inclusive)




def main():

    last = len(names) - 1

    arr = names[:]

    print('=' * 60)

    print(f'ME< {arr}')
    index(arr)

    sort_merge(arr, 0, last)

    print(f'ME> {arr}')
    index(arr)

    arr = names[:]

    print('=' * 60)

    print(f'QU< {arr}')
    index(arr)

    sort_quick(arr, 0, last)

    print(f'QU> {arr}')
    index(arr)

    print(f'My name index = {arr.index(names[0])}')

if __name__ == '__main__':
    main()