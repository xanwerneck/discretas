def exp(n, e)
  if e == 0
    return 1
  end

  single = 1
  result = n
  while e > 1
    if e.odd?
      single *= result
    end
    result *= result
    e /= 2
  end
  result * single
end

# Testando
def caso_falhou?(caso)
  n = caso[0]
  e = caso[1]
  exp(n, e) != n ** e
end

casos_de_teste = [[8,0], [8,1], [8,2], [8,3], [8,4], [8,5], [8,6], [8,10], [8,11], [8,12], [8,15]]

caso_que_falhou = casos_de_teste.find{|caso| caso_falhou?(caso)}

if caso_que_falhou.nil?
  puts "Os testes passaram!"
else
  n = caso_que_falhou[0]
  e = caso_que_falhou[1]
  puts "O teste (#{n}, #{e}) falhou. Retornou #{exp(n, e)} mas deveria ter retornado #{n ** e}"
end
