def bigger_sum(a)
  somas = Hash.new(0)
  n = a.size
  a.each_with_index do |_, i|
    for j in i...n
      somas[i..j] += somas[i..(j-1)] + a[j]
    end
  end
  maior = 0
  range_maior = nil
  somas.each do |range, soma|
    if soma > maior
      maior = soma
      range_maior = range
    end
  end
  [range_maior.begin, range_maior.end]
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
