file = File.open("input")
file_data = file.readlines.map { |line| line.chomp.split("") }
file.close

# part 1
freqs = Hash.new([])
file_data.each_with_index{|a,y| a.each_with_index{|v,x| freqs[v] += [[x,y]] if v != "."}}

h = file_data.size
w = file_data[0].size

# part 1
antinodes = Set.new
for f in freqs.values()
    for c1 in f
        for c2 in f
            dx = c1[0] - c2[0]
            dy = c1[1] - c2[1]
            nx = c1[0] + dx
            ny = c1[1] + dy
            next if c1[0] == c2[0] and c1[1] == c2[1]
            if nx >= 0 and ny >= 0 and nx < w and ny < h
                antinodes.add([nx,ny])
            end
        end
    end
end
puts antinodes.count
# 423

# part 2
antinodes = Set.new
for f in freqs.values()
    for c1 in f
        for c2 in f
            dx = c1[0] - c2[0]
            dy = c1[1] - c2[1]
            nx = c1[0].dup
            ny = c1[1].dup
            next if c1[0] == c2[0] and c1[1] == c2[1]
            while nx >= 0 and ny >= 0 and nx < w and ny < h
                antinodes.add([nx,ny])
                nx += dx
                ny += dy
            end
        end
    end
end
puts antinodes.count
