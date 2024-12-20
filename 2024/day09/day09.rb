file = File.open("input")
file_data = file.read.chomp.split("").map {|n| n.to_i}
file.close

block = Struct.new(:id, :size)

blocks = []
for i in (0...file_data.size)
    for j in 1..file_data[i]
        blocks << block.new(i.even? ? i/2 : nil, file_data[i])
    end
end

# part 1
j = blocks.size - 1
for i in (0...blocks.size)
    if blocks[i].id == nil and blocks[j].id != nil
        # swap i,j
        blocks[i], blocks[j] = blocks[j], blocks[i]
        while blocks[j].id == nil
            j -= 1
        end
    end
    break if i == j
end
checksum = blocks.filter{|b| b.id != nil}.each_with_index.map{|b,i| b.id * i}.sum
puts checksum
# 6225730762521

# part 2
blocks = []
for i in (0...file_data.size)
    blocks << block.new(i.even? ? i/2 : nil, file_data[i])
end

for j in (blocks.size - 1).downto(0)
    for i in (0...blocks.size)
        if blocks[i].id == nil and blocks[j].id != nil
            size_i, size_j = blocks[i].size, blocks[j].size
            if size_i > size_j
                # swap i,j with remainder after j
                blocks[i], blocks[j] = blocks[j], blocks[i]
                blocks[j].size = size_j
                blocks.insert(i+1, block.new(nil, size_i - size_j))
                break
            elsif size_i == size_j
                blocks[i], blocks[j] = blocks[j], blocks[i]
                break
            end
        end
        break if i == j
    end
end
i, sum = 0, 0
for block in blocks
    for c in 1..block.size
        sum += block.id == nil ? 0 : block.id * i
        i += 1
    end
end
puts sum
# 6250605700557
