#!/usr/bin/env python3
list = open("input.txt").readlines()
for value1 in list:
  for value2 in list:
      calc = int(value1) + int(value2)
      if calc == 2020:
          print(f"{int(value1) * int(value2)}")
          exit(0)
