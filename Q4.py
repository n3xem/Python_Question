with open('data.txt', 'r') as f:
  str_nums = f.read().split('\n')
  str_nums.pop()
  int_nums = [int(i) for i in str_nums]
  int_nums.sort()

with open('data2.txt', 'w') as fp:
  for i in int_nums:
    print(i, file=fp)
