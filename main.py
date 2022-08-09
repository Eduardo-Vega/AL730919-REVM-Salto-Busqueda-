import math

arr = None
item = None
m = None
p = None
i = None
j = None

def text_prompt(msg):
  try:
    return raw_input(msg)
  except NameError:
    return input(msg)

def upRange(start, stop, step):
  while start <= stop:
    yield start
    start += abs(step)

def downRange(start, stop, step):
  while start >= stop:
    yield start
    start -= abs(step)


arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 55, 77, 89, 101, 201, 256, 780]
item = float(text_prompt('Numero a buscar: '))
m = math.sqrt(16)
p = 0
i = 1
while p == 0:
  if arr[int(i - 1)] != item and arr[int(i - 1)] < item:
    i = i + (m - 1)
  else:
    if arr[int(i - 1)] != item and arr[int(i - 1)] > item or arr[int(i - 1)] == item:
      j_start = float(i - 3)
      for j in (j_start <= float(i)) and upRange(j_start, float(i), 1) or downRange(j_start, float(i), 1):
        if arr[int(j - 1)] == item:
          print('El numero se encuentra en ' + str(j))
          p = 1
        elif j == i and arr[int(j - 1)] != item:
          print('No se encontro el numero')
          p = 1
    else:
      print('No se encontro el numero')
      p = 1
  if False:
    print('No se encontro el numero')
    p = 1