def brutal_print(alf, p = "")
  if p.size == alf.size
    puts p
    return
  end

  alf.each do |l|
    brutal_print(alf, p+l)
  end
end

puts "Brutal Print"
brutal_print(["a", "b", "c"])
