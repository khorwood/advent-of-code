file = File.open("input")
file_data = file.readlines.map { |line| line.chomp.split('') }
file.close

def get_coord(data, row, col)
    if row.between?(0, data.size - 1) and col.between?(0, data[row].size - 1)
        return data[row][col]
    end
end

diags = (-1..1)
xmas = 0
x_mas = 0
for row in 0...file_data.size
    for col in 0...file_data[row].size
        if file_data[row][col] == "X"
            for dr in diags
                for dc in diags
                    next if dr.zero? and dc.zero?
                    word = (0...4).map { |i| get_coord(file_data, row + dr * i, col + dc * i) }.join
                    xmas += 1 if word == "XMAS"
                end
            end
        elsif get_coord(file_data, row, col) == "A"
            d1 = diags.map { |i| get_coord(file_data, row + i, col + i) }.join
            d2 = diags.map { |i| get_coord(file_data, row + i, col - i) }.join
            x_mas += 1 if (d1 == "MAS" or d1 == "SAM") and (d2 == "MAS" or d2 == "SAM")
        end
    end
end
puts xmas
puts x_mas
# 2434
# 1835
