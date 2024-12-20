require 'matrix'

def read_input
    file = File.open("input")
    file_data = file.readlines.map { |line| line.chomp.split("") }
    file.close
    return file_data
end

@direction = Matrix[[-1,0],[0,1]]

def find_value(grid, element)
    grid.each_with_index do | row, y |
        x = row.index(element)
        return y, x if x
    end
end

def get_coord(data, row, col)
    if row.between?(0, data.size - 1) and col.between?(0, data[row].size - 1)
        return data[row][col]
    end
end

def find_path
    position = @start.dup
    direction = @direction.dup
    grid = read_input

    visited = Set[]
    while get_coord(grid, position[0], position[1])
        visited << position.clone
        if get_coord(grid, position[0] + direction[0,0], position[1] + direction[0,1]) == "#"
            direction = direction.rotate_entries(:counter_clockwise)
        end
        position[0] += direction[0,0]
        position[1] += direction[0,1]
    end
    visited
end

def has_cycle?(obstacle)
    position = @start.dup
    direction = @direction.dup
    grid = read_input

    grid[obstacle[0]][obstacle[1]] = "#"

    visited = Set[]
    while get_coord(grid, position[0], position[1])
        visited << [position.clone, [direction[0,0], direction[0,1]]]
        if get_coord(grid, position[0] + direction[0,0], position[1] + direction[0,1]) == "#"
            direction = direction.rotate_entries(:counter_clockwise)
        end
        position[0] += direction[0,0]
        position[1] += direction[0,1]
        return true if visited.include?([position, [direction[0,0], direction[0,1]]])
    end
    false
end

def print_board(grid)
    for r in grid
        puts r.join("")
    end
end

# part 1
@file_data = read_input
@start = find_value(@file_data, "^")
path = find_path
puts path.size
# 5461

# part 2
obstacles = path.map { |p| has_cycle?(p)}.count(true)
puts obstacles
