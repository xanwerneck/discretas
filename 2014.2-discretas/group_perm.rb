def print_groups(alf, r, group="")
  n = alf.size
  if r == 0
    puts group
  else
    for i in 0..(n-r)
      new_alf = alf[(i+1)..-1]
      print_groups(new_alf, r-1, group+alf[i])
    end
  end
end

print_groups("abcde", 3)
