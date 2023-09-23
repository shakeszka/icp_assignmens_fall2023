position = input("Enter a chess board position: ")

column = position[0]
row = int(position[1])

def square_color(column, row):
    # convert the column letter to its corresponding position in the alphabet
    column_index = ord(column) - ord('A')
    
    # if the sum of the column_index and row is even, it's a white square.
    if (column_index + row) % 2 == 0:
        return "white"
    else:
        return "black"

# starting the function
color = square_color(column, row)

# result
print(f"This case is {color}")
