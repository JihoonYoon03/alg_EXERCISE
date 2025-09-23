array = [
       46,      82,      21,      58,      22,      54,      71,     215,      99,     227, 
       73,      24,      17,      44,     244,      78,      25,      66,      47,       3, 
       87,      33,     312,     242,      42,      61,     348,     346,      98,      92, 
       83,     100,      94,      40,       5,     458,     364,      26,      64,     635, 
       90,     489,      72,     504,      88,      97,     226,     218,     186,     268, 
]

def sort_bubble(arr):
  print('=' * 60)
  print(f'before: {arr}')

  for i in range(len(arr) - 1, 0, -1):
      for j in range(0, i):
          if arr[j] > arr[j + 1]:
              arr[j], arr[j + 1] = arr[j + 1], arr[j]

  print(f'after : {arr}')

def sort_select(arr):
  print('=' * 60)
  print(f'before: {arr}')

  for i in range(len(arr) - 1): # i는 루프마다 +1되어 정렬된 값을 제외하고 탐색
      min_idx = i
      for j in range(i + 1, len(arr)): # i 다음 인덱스부터 끝까지 증가
          if arr[j] < arr[min_idx]: # 더 작은 값을 찾았다면
              min_idx = j # 갱신
      if min_idx != i: # 최소값 인덱스가 바뀌었다면 값을 스왑해야 함
          arr[i], arr[min_idx] = arr[min_idx], arr[i]

  print(f'after : {arr}')

def sort_insert(arr):
    print('=' * 60)
    print(f'before: {arr}')
    for i in range(1, len(arr), 1): # 0번 인덱스는 이미 정렬된 배열로 보고 제외
        v = arr[i]
        j = i - 1 # j는 정렬된 배열의 가장 끝 인덱스부터 시작함
        while j >= 0 and arr[j] > v: # j가 0 이상이고 현재 주인공 값보다 큰 동안 반복
            arr[j + 1] = arr[j] # 한 칸씩 뒤로 밀기
            j -= 1 # 뒤로 밀었다면 다음 값으로 넘어가기

        arr[j + 1] = v

    print(f'after : {arr}')

def sort_shell(arr):
  print('=' * 60)
  print(f'before: {arr}')

  GAPS = [23, 10, 4, 1]

  # 삽입 정렬이 포함된 알고리즘인데, 다만 gap만큼 떨어진 값 끼리 비교해야 함
  for gap in GAPS:
      for i in range(gap, len(arr), 1):
          v = arr[i]
          j = i - gap  # j는 정렬된 배열 가장 끝 인덱스
          while j >= 0 and arr[j] > v:
              arr[j + gap] = arr[j]  # gap만큼 뒤로 밀기
              j -= gap
          arr[j + gap] = v

  print(f'after : {arr}')

def main():
  sort_bubble(array[:])
  sort_insert(array[:])
  sort_select(array[:])
  sort_shell(array[:])

if __name__ == '__main__':
  main()