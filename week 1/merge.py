"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    def move_left(line):
        """
        Function to move all the cells to the left
        """
        no_zeros_line = []
        zeros_line = []
        for cell in line:
            if cell != 0:
                no_zeros_line.append(cell)
            else: 
                zeros_line.append(cell)
        return no_zeros_line + zeros_line
    ordered_line = move_left(line)
    merged_line = list(ordered_line)
    merged_flag = 0
    for index in range(0, len(ordered_line)):
        if merged_flag == 1:
            merged_flag = 0
            continue
        if index - 1 >= 0 and ordered_line[index-1] == ordered_line[index]:
            merged_line[index-1] = ordered_line[index-1] + ordered_line[index]
            merged_line[index] = 0
            merged_flag = 1
    
    merged_ordered_line = move_left(merged_line)
    return merged_ordered_line

print merge([2, 0, 2, 4]), "should return [4, 4, 0, 0]"
print merge([0, 0, 2, 2]), "should return [4, 0, 0, 0]"
print merge([2, 2, 0, 0]), "should return [4, 0, 0, 0]"
print merge([2, 2, 2, 2]), "should return [4, 4, 0, 0]"
print merge([8, 16, 16, 8]), "should return [8, 32, 8, 0]"
print merge([8, 8, 8, 2]), "should return [16, 8, 2, 0]"