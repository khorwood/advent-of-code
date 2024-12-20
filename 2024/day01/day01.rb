file = File.open("input")
file_data = file.readlines.map { |line| line.split(' ').map(&:to_i) }
file.close

# part 1
data = file_data.transpose
data = data.each { |item| item.sort! }
length = data.transpose.map { |k,v| (k-v).abs }
puts length.sum
# 2580760

# part 2
data = file_data.transpose
products = data[0].map { |item| item * data[1].count(item) }
puts products.sum
# 25358365
