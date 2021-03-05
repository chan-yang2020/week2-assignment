def calculate(min, max):
    sum=0
    for i in range(min, max+1):
        sum+=i
    print(sum)
calculate(1, 3) 
calculate(4, 8) =

def avg(data):
    sum=0
    for i in range(len(data['employees'])):
        sum=sum+data['employees'][i]['salary']
    print(sum/len(data['employees']))

avg({"count":3,"employees":[{"name":"John","salary":30000},{"name":"Bob","salary":60000},{"name":"Jenny","salary":50000}]}) 

def maxProduct(*nums):
    y=sorted(*nums, reverse = True)
    x=y[0]*y[1]
    print(x)
    #不用sorted的解法，答案一樣
    # new_list=list(nums)
    # x=max(new_list)
    # index=new_list.index(x)
    # del new_list[index]
    # y=max(new_list)
    # print(x*y)
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