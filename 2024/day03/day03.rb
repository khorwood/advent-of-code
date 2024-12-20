file = File.open("input")
file_data = file.read
file.close

# part 1
md = file_data.scan(/mul\((\d+),(\d+)\)/)
sum = md.reduce(0) { |sum,item| sum + item[0].to_i * item[1].to_i }
puts sum
# 162813399

# part 2
md = file_data.scan(/mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))/)
is_do = true
sum = 0
for item in md
    if item[2] == "do()"
        is_do = true
        next
    elsif item[3] == "don't()"
        is_do = false
        next
    end
    if is_do
        sum += item[0].to_i * item[1].to_i
    end
end
puts sum
# 53783319
