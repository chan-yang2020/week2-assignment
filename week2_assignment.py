def calculate(min, max):
    sum=0
    for i in range(min, max+1):
        sum+=i
    print(sum)
calculate(1, 3) 
calculate(4, 8) 

def avg(data):
    sum=0
    for i in range(len(data['employees'])):
        sum=sum+data['employees'][i]['salary']
    print(sum/len(data['employees']))

avg({"count":3,"employees":[{"name":"John","salary":30000},{"name":"Bob","salary":60000},{"name":"Jenny","salary":50000}]}) 

def maxProduct(*nums):
    find_max_list=list(*nums)
    find_min_list=list(*nums)
    x=max(find_max_list)
    max_index=find_max_list.index(x)
    del find_max_list[max_index]
    y=max(find_max_list)
    x1=min(find_min_list)
    min_index=find_min_list.index(x1)
    del find_min_list[min_index]
    y1=min(find_min_list)
    if x*y>x1*y1:
        print(x*y)
    elif x*y<x1*y1:
        print(x1*y1)
    elif x*y==x1*y1:
        print(x*y)
    #用sorted的解法，答案一樣
    # y_asc=sorted(*nums, reverse = True)
    # y_desc=sorted(*nums)
    # x1=y_asc[0]*y_asc[1]
    # x2=y_desc[0]*y_desc[1]
    # if x1>x2:
    #     print(x1)
    # elif x1<x2:
    #     print(x2)
    # elif x1==x2:
    #     print(x1)
maxProduct([5, 20, 2, 6]) 
maxProduct([10, -20, 0, 3]) 

def twoSum(nums,target):
    for i in range(len(nums)):
        rest = nums[i+1:]
        for j in range(len(rest)):
            if (nums[i] + rest[j]) == target:
                return i, j+i+1
result=twoSum([2, 11, 7, 15],9)
print(result) 