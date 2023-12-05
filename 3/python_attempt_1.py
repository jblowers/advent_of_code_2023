import sys





class tile:
    def __init__(self, char, counted):
        self.char = char
        self.counted = counted
        
    def __str__(self):
        return f"Tile(char='{self.char}', counted={self.counted})"
    
    def is_symbol(self):
        if self.char.isalnum():
            return False
        elif self.char == ".":
            return False
        else:
            return True
        
    def is_number(self):
        return self.char.isalnum()
    
    def is_period(self):
        return self.char == '.'

def main():

    filepath = "./example_schematic.txt"
    lines = []
# first load the data and get into a structure to be able to access
    with open(filepath) as file:
        for line in file:
            lines.append(line)
            # store each as ... an array of characters? 
            # could use a small struct to store whether isSymbol, isNumber at each index ?
    # have data in list of lines
    mat = fill_mat_from_lines(lines)
        
    print_mat(mat)
    sum = 0
    for i, row in enumerate(mat):
        for j, til in enumerate(row):
            if til.is_symbol:
                sum = sum + check_adjacent(mat,i,j)
                # then run the check
# once data is accessible
#  algorithm looks like... iterate until a symbol is found; 
#   for each symbol at [i,j], check:
#   * [i,j-1], [i,j+1], [i-1,j], [i+1,j] -> all adjacent
#   * [i-1,j-1], [i-1,j+1], [i+1,j-1], [i+1,j+1] -> all diagonal
#   when one of those is a number, 
#    then need another algorithm to search left and right for the entire number; store it
#   sum all found part numbers at the end
    print("SUM is: ")
    print(sum)


# recieves 
def check_for_part_number(mat,indi, indj):
    print("enter check for part number")
    # need to look backward until indj is 0, or the char is not number
    j_iter = indj
    while j_iter >= 0:
        if mat[indi][j_iter].is_number():
            j_iter = j_iter -1
        else:
            break
    # print(j_iter)
    # now move forward and construct the number
    str_out = ""
    while mat[indi][j_iter].is_number():
        print("mat.char: ")
        print(mat[indi][j_iter].char)
        str_out = str_out + mat[indi][j_iter].char
        mat[indi][j_iter].counted = True
        j_iter = j_iter+1
    # convert str_out to a number, return this, or return 0
    print("str_out: ")
    print(str_out)
    if len(str_out) > 0:
        return int(str_out)
    else:
        return 0
    
    

def check_adjacent(mat, i, j):
    sum = 0
    adjacent_indices = [[-1,0],[-1,1],[-1,-1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    if i < 1:
        # handle the edge case where you can't subtract 1 from i
        inds_out = []
        for inds in adjacent_indices:
            if inds[0] != -1:
                inds_out.append(inds)
        adjacent_indices = inds_out
                
    
    if i == len(mat[i])-1:
        # case when i is at end of row; can't add 1 to i
        inds_out = []
        for inds in adjacent_indices:
            if inds[0] != 1:
                inds_out.append(inds)
        adjacent_indices = inds_out
    
    if j < 1:
        # handle the edge case where you can't subtract 1 from i
        inds_out = []
        for inds in adjacent_indices:
            if inds[1] != -1:
                inds_out.append(inds)
        adjacent_indices = inds_out
    
    if j == len(mat) - 1:
        # case when i is at end of row; can't add 1 to i
        inds_out = []
        for inds in adjacent_indices:
            if inds[1] != 1:
                inds_out.append(inds)
        adjacent_indices = inds_out
    
    
    # if i > 0 and i < len(mat)-1: # ignoring first and last rows
        # if j > 0 and j < len(mat[i]) - 1: # ignoring first and last columns
            # iterate through the adjacent tiles to check for iis_number
    for inds in adjacent_indices:
        indi = inds[0]+i
        indj = inds[1]+j
        test_til = mat[indi][indj]
        if test_til.is_number() and not test_til.counted:
            # do the check on this tile
            # if sum > 0:
                # print("Adding to sum")
                # print(sum)
            sum = sum + check_for_part_number(mat,indi, indj)
                
                

    
    return sum
    
        

def is_symbol(char, include_period = False):
    # symbs = ['*','#','+',]
    # if char.isalnum():
    #     return False
        
    # if char != '.':
    #     return True
    # elif include_period:
    #     return True
    # else:
        return False
        

def fill_mat_from_lines(lines):
    # ignoring new line at end
    # admittedly fragile, assuming perfectly formatted input
    
    mat = [[tile('.',False) for _ in range(len(lines[0])-1)] for _ in range(len(lines))]
    
    for i_index, line in enumerate(lines):
        for j_index, char in enumerate(line):
            if char != "\n":
                mat[i_index][j_index].char = char
    
    return mat
    

def print_mat(matrix):
    
    for i,row in enumerate(matrix):
        # print(row)
        outs = []
        for j,col in enumerate(row):
            outs.append(col.char)
            # print(col.char)
        print(outs)
        # print("\n")

if __name__ == "__main__":
    main()