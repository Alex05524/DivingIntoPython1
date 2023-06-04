def print_tree(height):
    for i in range(1, height+1):
        print(''*(height-i)+'*'*(2*i-1))
        
print_tree(5)