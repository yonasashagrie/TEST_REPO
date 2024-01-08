i=0
count=0
sign=('*')
#iterate range from 0 to 9
for i in range (9):
    # Check if i is less than or equal to 4
    if i<=4:
        #increasing count by 1 till i becomes 4
       count += 1
       print(count * sign)
    else:
        count -= 1
        #decreasing count by 1 till i reaches 9 from 4
        print(count * sign)
        