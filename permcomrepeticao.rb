def printa_permutacoes(alfabeto, palavra="")
  if alfabeto.size == 0
    puts palavra
  else
    sem_duplicata(alfabeto).each_char do |letra|
      new_alf = alfabeto.sub(letra, "")
      printa_permutacoes(new_alf, palavra+letra)
    end
  end
end

def sem_duplicata(alfabeto)
  alfabeto.chars.uniq.join
end


printa_permutacoes("aabc")
