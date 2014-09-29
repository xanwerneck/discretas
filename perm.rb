def permutacoes_print(full_alf, nalf=nil, p = "")
  nalf ||= full_alf

  if p.size == full_alf.size
    puts p
    return
  end

  nalf.each do |l|
    permutacoes_print(full_alf, nalf - [l], p+l)
  end
end

puts "Permutações Print"
permutacoes_print(["a", "b", "c"])
