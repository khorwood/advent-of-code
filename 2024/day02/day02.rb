file = File.open("input")
file_data = file.readlines.map { |line| line.split(' ').map(&:to_i) }
file.close

def check_is_safe(item)
    changes = item.each_cons(2).map { |k,v| v - k }
    is_safe = changes.any? { |item| item < 0 } ^ changes.any? { |item| item > 0 } ? true : false
    is_safe = changes.any? { |item| item.abs > 3 or item.abs == 0 } ? false : is_safe
    return is_safe
end

# part 1
safe_list = Array.new
for item in file_data
    safe_list.push(check_is_safe(item))
end
puts safe_list.count(true)
# 598

# part 1
safe_list = Array.new
for item in file_data
    is_safe = check_is_safe(item)
    if !is_safe
        for i in 0..item.length - 1
            it = item.clone
            it.delete_at(i)
            is_safe = check_is_safe(it)
            if is_safe
                break
            end
        end
    end
    safe_list.push(is_safe)
end
puts safe_list.count(true)
# 634
