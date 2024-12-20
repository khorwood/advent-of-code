file = File.open("input")
file_data = file.readlines.map { |line| line.chomp }
file.close

def parse_file(data)
    rules = Array.new
    updates = Array.new
    for line in data
        rules.push line.split("|").map(&:to_i) if line.include? "|"
        updates.push line.split(",").map(&:to_i) if line.include? ","
    end
    return rules, updates
end

rules, updates = parse_file(file_data)

part_1 = 0
part_2 = 0
for update in updates
    sorted = update.sort { |a,b| rules.any? { |r| r[0] == a and r[1] == b } ? -1 : rules.any? { |r| r[0] == b and r[1] == a } ? 1 : 0 }
    part_1 += update[update.size / 2] if update == sorted
    part_2 += sorted[update.size / 2] if update != sorted
end
puts part_1
puts part_2
# 5452
# 4598
