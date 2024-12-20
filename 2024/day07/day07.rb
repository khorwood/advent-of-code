file = File.open("input")
file_data = file.readlines.map{|line| line.chomp.sub!(":","").split().map(&:to_i)}
file.close

# part 1
def is_valid(item, current_value, index)
    expected = item[0]
    next_value = item[index + 1]
    if !next_value
        return true if current_value == expected
        return false
    end
    is_valid(item, current_value + next_value, index + 1) || is_valid(item, current_value * next_value, index + 1)
end

sum = file_data.filter{|i| is_valid(i, i[1], 1)}.map{|i| i[0]}.sum
puts sum
# 2314935962622

# part 2
def cat(a, b)
    mult = 10
    while mult <= b
        mult *= 10
    end
    a * mult + b
end

def is_valid_concat(item, current_value, index)
    expected = item[0]
    next_value = item[index + 1]
    if !next_value
        return true if current_value == expected
        return false
    end
    is_valid_concat(item, current_value + next_value, index + 1) || is_valid_concat(item, current_value * next_value, index + 1) || is_valid_concat(item, cat(current_value, next_value), index + 1)
end

sum = file_data.filter{|i| is_valid_concat(i, i[1], 1)}.map{|i| i[0]}.sum
puts sum
# 401477450831495
