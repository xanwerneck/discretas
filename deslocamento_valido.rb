def matching(p, t)
  m = p.size
  n = t.size
  valids = []
  for i in 0..(m-n)
    is_valid = true
    for j in 0...n
      if p[i+j] != t[j]
        is_valid = false
        break
      end
    end
    valids << i if is_valid
  end
  valids
end


TEST_CASES = [
  [[1,2,3,4,5], [1,2], [0]],
  [[1,2,3,4,5,1,2], [1,2], [0,5]],
  [[1,2,3,4,5,1,2], [1,2,3], [0]],
  [[1,2,3,4,5,1,2], [1,2,3,9], []],
  [[1,2,3,4,5,1,2,1], [1], [0,5,7]]
]

failing_case = TEST_CASES.find{|(p, t, expected)| matching(p,t) != expected}
if failing_case.nil?
  puts "Todos os testes passaram"
else
  p = failing_case[0]
  t = failing_case[1]
  expected = failing_case[2]

  puts "O caso (#{p.inspect},#{t.inspect}) falhou. retornou #{matching(p,t).inspect} mas deveria ser #{expected.inspect}"
end
