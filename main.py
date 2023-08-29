import time

start_int = int(time.time())

rounding_amount = int(input("Random Number Digits (up to 10): "))

rounding_amount = rounding_amount - rounding_amount * 2

timestamp_list = [int(i) for i in str(start_int)]

timestamp_list = timestamp_list[rounding_amount:]

output = ''

for x in timestamp_list:
    output += '' + str(x)

print(output)