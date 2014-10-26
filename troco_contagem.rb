def contagem_troco(moedas, valor)
  if valor == 0
    return 1
  elsif moedas.empty?
    return 0
  else
    moeda = moedas.first
    novas_moedas = moedas - [moeda]
    sum = 0
    for i in 0..(valor/moeda)
      sum += contagem_troco(novas_moedas, valor - moeda*i)
    end
    return sum
  end
end

puts contagem_troco([9, 7, 4, 1], 100)
