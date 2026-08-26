import re

def QuestionsMarks(strParam):

    # code goes here
    nums = [(i, int(c)) for i, c in enumerate(strParam) if c.isdigit()]

    ten_pairs = [
        strParam[i1+1:i2].count('?') == 3
        for (i1, d1), (i2, d2) in zip(nums, nums[1:]) 
        if d1 + d2 == 10 
]
    return "true" if ten_pairs and all(ten_pairs) else "false"

# keep this function call here 
print(QuestionsMarks(input()))