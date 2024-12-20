file = File.open("input")
file_data = file.readlines.map {|l| l.chomp.split('').map(&:to_i)}
file.close

trail_heads = []
file_data.each_with_index{|r,i| r.each_with_index{|v,j| trail_heads.push([i,j]) if v == 0}}

# part 1
def get_coord(data, row, col)
    if row.between?(0, data.size - 1) and col.between?(0, data[row].size - 1)
        return data[row][col]
    end
end

def find_paths(file_data, pos, paths=[], path=[], incl=true)
    x,y = pos[0],pos[1]
    val = file_data[x][y]

    if val == 9
        return if incl and paths.any?{|p| p.include?([x,y])}
        path.push([x,y])
        paths << path
        return
    end

    for d in [[1,0],[-1,0],[0,1],[0,-1]]
        nx, ny = x + d[0], y + d[1]
        next if get_coord(file_data, nx, ny) != val + 1
        next_path = path.clone.push([x,y])
        find_paths(file_data, [nx, ny], paths, next_path, incl)
    end
end

score = 0
for sp in trail_heads
    paths = []
    find_paths(file_data, sp, paths)
    score += paths.size
end
puts score

rating = 0
for sp in trail_heads
    paths = []
    find_paths(file_data, sp, paths, [], false)
    rating += paths.size
end
puts rating
