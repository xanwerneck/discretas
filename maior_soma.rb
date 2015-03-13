def hkey(range)
  if range.exclude_end?
    :"#{range.begin}-#{range.end-1}"
  else
    :"#{range.begin}-#{range.end}"
  end
end

def bigger_sum(a, b=nil,e=nil, sums={})
  n = a.size
  if b.nil?
    b = 0
    e = a.size
  end
  if e - b > 2
    lb = b
    le = b+(e-b)/2
    rb = le
    re = e
    lsum = bigger_sum(a, lb, le, sums)
    rsum = bigger_sum(a, rb, re, sums)
    sums[hkey(lb...le)] = lsum
    sums[hkey(rb...re)] = rsum
    lcross = rsum
    for i in 1...(le-lb)
      j = le - i
      lcross += a[j]
      sums[hkey(j...le)] = lcross
    end

    rcross = lsum
    for i in rb...(re-1)
      rcross += a[i]
      sums[hkey(rb..i)] = rcross
    end

    sum = lsum + rsum
    sums[hkey(b...e)] = sum

    if b == 0 && e == n
      bigger = 0
      bigger_range = nil
      sums.each do |range, sum|
        if sum > bigger
          bigger = sum
          bigger_range = range
        end
      end
      bigger_range.to_s.split("-").map(&:to_i)
    else
      sum
    end
  elsif e - b == 2
    sums[hkey(b..b)] = a[b]
    sums[hkey((e-1)..(e-1))] = a[e-1]
    a[b] + a[e-1]
  else
    sums[hkey(b..b)] = a[b]
    a[b]
  end
end

TEST_CASES = [
  [[1, 2, 3], [0,2]],
  [[-1, 2, 3], [1,2]],
  [[1, -2, 3], [2,2]],
  [[1, -2, 100, -91, 40, 50], [2,2]]
]

failed = TEST_CASES.find{|(array, expected)| bigger_sum(array) != expected}
if failed.nil?
  puts "Os testes passaram"
else
  array = failed[0]
  expected = failed[1]
  puts "O caso #{array.inspect} falhou, retornou #{bigger_sum(array).inspect} mas deveria ser #{expected.inspect}"
end
