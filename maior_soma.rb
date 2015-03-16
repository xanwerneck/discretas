def hkey(range)
  if range.exclude_end?
    :"#{range.begin}-#{range.end-1}"
  else
    :"#{range.begin}-#{range.end}"
  end
end

def bigger_sum(a, b=nil,e=nil)
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
    lbig, lbig_range, lsum = bigger_sum(a, lb, le)
    rbig, rbig_range, rsum = bigger_sum(a, rb, re)
    if lbig > rbig
      big = lbig
      big_range = lbig_range
    else
      big = rbig
      big_range = rbig_range
    end

    lcross = rsum
    for i in 1...(le-lb)
      j = le - i
      lcross += a[j]
      if lcross > big
        big = lcross
        big_range = hkey(j...le)
      end
    end

    rcross = lsum
    for i in rb...(re-1)
      rcross += a[i]
      if rcross > big
        big = rcross
        big_range = hkey(rb..i)
      end
    end

    sum = lsum + rsum
    if sum > big
      big = sum
      big_range = hkey(b...e)
    end

    if b == 0 && e == n
      return big_range.to_s.split("-").map(&:to_i)
    else
      return [big, big_range, sum]
    end
  elsif e - b == 2
    lsum = a[b]
    rsum = a[e-1]
    sum = a[b] + a[e-1]
    if lsum > rsum
      big = lsum
      big_range = hkey(b..b)
    else
      big = rsum
      big_range = hkey((e-1)..(e-1))
    end
    if sum > big
      return [sum, hkey(b...e), sum]
    else
      return [big, big_range, sum]
    end
  else
    return [a[b], hkey(b..b), a[b]]
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
