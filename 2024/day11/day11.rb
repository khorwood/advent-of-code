file = File.open("input")
file_data = file.read.split().map{|i| [i, 1]}.to_h
file.close


def blink(input, times)
    times.times do
        tmp = Hash.new { 0 }
        input.entries.each do |n, c|
            if n == ?0
                tmp[?1] += c
            elsif n.size.even?
                tmp[n[0..(n.length/2-1)]] += c
                tmp[n[n.length/2..].to_i.to_s] += c
            else
                tmp[(n.to_i * 2024).to_s] += c
            end
        end
        input = tmp
    end
    input.values.sum
end
puts blink(file_data, 25)
puts blink(file_data, 75)
