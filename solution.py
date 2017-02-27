assignments = []
rows = 'ABCDEFGHI'
cols = '123456789'

def cross(a, b):
    "Cross product of elements in A and elements in B."
    return [s+t for s in a for t in b]

boxes = cross(rows, cols)
row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]

# diagonal
diagonal_units=[]
diagonal_units.append([rows[i]+cols[i] for i in range(0,9)])
diagonal_units.append([rows[i]+cols[8-i] for i in range(0,9)])

unitlist = row_units + column_units + square_units + diagonal_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

def assign_value(values, box, value):
    # Update the values dictionary
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    # Find all instances of naked twins
    for unit in unitlist:
        temp_unit=unit.copy()
        twin_list_values=""
        for element in temp_unit:
            if len(values[element])==2:
                for element1 in temp_unit[temp_unit.index(element)+1:]:
                    if  values[element]==values[element1]:
                        temp_unit.remove(element)
                        temp_unit.remove(element1)
                        twin_list_values=twin_list_values+values[element] 
	
    # Eliminate the naked twins as possibilities for their peers
        if len(temp_unit)!=len(unit) :
            for element in temp_unit:
                for digit in twin_list_values: 
                    assign_value(values, element, values[element].replace(digit,''))                       
    return values

def grid_values(grid):
    # Convert grid string into {<box>: <value>} dict with '123456789' value for empties
    chars = []
    digits = '123456789'
    for c in grid:
        if c in digits:
            chars.append(c)
        if c == '.':
            chars.append(digits)
    assert len(chars) == 81
    return dict(zip(boxes, chars))

def display(values):
    # Display the values as a 2-D grid with the input in dictionary form
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return

def eliminate(values):
    # Eliminate values from peers of each box with a single value
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    for box in solved_values:
        digit = values[box]
        for peer in peers[box]:
            values[peer] = values[peer].replace(digit,'')
    return values

def only_choice(values):
    # Finalize all values that are the only choice for a unit
    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                values[dplaces[0]] = digit
    return values

def reduce_puzzle(values):
    # Apply all the solution reduction strategies to reduce possible solutions
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        # Eliminate Strategy
        values = eliminate(values)
        # Only Choice Strategy
        values = only_choice(values)
        # Naked Twins Strategy
        values = naked_twins(values)
        # Check how many boxes have a determined value
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # Stop the program if all boxes are solved
        stalled = solved_values_after!=27
        # Stop the loop if no new value was added
        stalled = solved_values_before == solved_values_after
        # Return false if there is a box with no available value
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def search(values):
    # Use depth-first search and propagation to create a search tree and solve the sudoku
    values = reduce_puzzle(values)
    if values is False:
        return False
    if all(len(values[s]) == 1 for s in boxes): 
        return values
    
    n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt

def solve(grid):
    # Find the solution to a sudoku grid
    values = grid_values(grid)
    return (search(values))


if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')