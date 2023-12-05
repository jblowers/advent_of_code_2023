#!/usr/bin/env python3
import sys


def main():
    
    
    filepath = "./full_input.txt"
    
    lines = []
    with open(filepath) as file:
        for line in file:
            lines.append(line)
    # print(lines)
    cal_vals = []
    nums = []
    for line in lines:
        for ind,char in enumerate(line):
            if char.isnumeric():
                print("found alnum: ",char)
                nums.append(char)
        # have all nums from this line
        firstDig = nums[0]
        lastDig = nums[len(nums)-1]
        
        print(firstDig,lastDig)
        
        nums = []
        cal_vals.append(int(firstDig+lastDig))
    sum = 0
    for val in cal_vals:
        sum = sum + val
    print(sum)
    # for num in nums:
        # num[0]
                
                
                
                
if __name__ == "__main__":
    main()