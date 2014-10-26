def troco_enumeracao(moedas, valor, quantidade_moedas=Hash.new(0))
  if valor == 0
    quantidade_moedas.each_pair do |moeda, quantidade|
      print "#{quantidade} moeda(s) de #{moeda}, "
    end
    print "\n"
  elsif !moedas.empty?
    moeda = moedas.first
    novas_moedas = moedas - [moedas.first]
    for i in 0..(valor/moeda)
      quantidade_moedas[moeda] += i
      troco_enumeracao(novas_moedas, valor-moeda*i, quantidade_moedas)
      quantidade_moedas[moeda] -= i
    end
  end
end

troco_enumeracao([3, 1], 10)
