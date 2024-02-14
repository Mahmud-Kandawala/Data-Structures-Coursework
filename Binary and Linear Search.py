import random
import array

content = array.array("i", [])

for i in range(0, 5000):
    content.append(random.randint(0,20000))
    print(content)
    content = (sorted(content))

### Linear Search
while True:
    number = int(input('\nLinear Search ==> Enter a number in the range 0 to 20000: '))
    if number < 0 or number > 20000:
        print("-1") 
        continue
    else:
        found = content.count(number)
        if found == 1:
            print(number, "was found", found, "time in the array.")
            break
        else:
            print(number, "was found", found, "times in the array.")
            break


### Binary Search
number = int(input('\nBinary Search ==> Enter a number in the range 0 to 20000: '))
low = 0
high = len(content)-1
answer = -1

while low <= high:
    mid = (low + high)//2
    if content [mid] == number:
        answer = mid
        break
    elif content [mid] > number:
        high = mid - 1
    else:
        low = mid + 1

if answer == -1:
    print("Sorry,", number, "is not found in the array.")
else:
    print(number,"Is Found At", answer)


# Since it takes O(n) time in the worst case, linear search is not recommended for large arrays.
# Binary Search is a better option because, in the worst case, it only requires O(log n) time.