def troco_enumeracao(moedas, valor, conjunto=Hash.new(0))
  if valor == 0
    p conjunto
  elsif !moedas.empty?
    moeda = moedas.first
    novas_moedas = moedas - [moedas.first]
    for i in 0..(valor/moeda)
      conjunto[moeda] += i
      troco_enumeracao(novas_moedas, valor-moeda*i, conjunto)
      conjunto[moeda] -= i
    end
  end
end

troco_enumeracao([3, 1], 10)
