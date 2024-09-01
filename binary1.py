#binary method 1 
#condtition: list has to be in sorted order 

numbers = [1,2,3,4,5,6,7,8]
finding_item = 7

start = 0 
end = len(numbers)-1

flag = False

while start<= end:
    mid = (start+end)//2

    if numbers[mid]==finding_item:
        print("we got it!")
        flag = True
        break
    elif numbers[mid] > finding_item: #looking in first half of list 
        end = mid-1
    else: #looking in second half of the list 
        start = mid+1

if flag == False:
    print("we never got ur number ")

