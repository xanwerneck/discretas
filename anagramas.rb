# get_anagramas(alphabet, anagrama, anagramas)
# parâmetros:
#  - alphabet: (array de caracteres) caracteres do alfabeto.
#  - anagrama: (string) anagrama que está sendo formado através das chamadas recursivas. [opcional]
#  - anagramas: (array) anagramas que já foram formados [opcional]
# retorno: (array) todos os anagramas do alfabeto passado, excluindo os que possuem duas vogais
#          consecutivas.
def get_anagramas(alphabet, anagrama="", anagramas=[])
  if alphabet.empty?
    anagramas << anagrama
  else
    # Hash usado para evitar de passar por dois caracteres iguais
    used = {}
    # Itera por cara letra do alfabeto, onde:
    #  c = letra do alfabeto
    #  i = indice da letra do alfabeto
    alphabet.each.with_index do |c, i|
      if !used[c]
        used[c] = true
        # cria novo anagrama adicionando a letra do alfabeto
        new_anagrama = anagrama + c
        
        # Se o novo anagrama termina com duas vogais, ele é inválido
        if !ends_with_two_vowels?(new_anagrama)
          # cria novo alfabeto, que será igual ao alfabeto anterior, porém
          # sem a letra usada para a formação do novo anagrama.
          new_alphabet = alphabet.clone
          new_alphabet.delete_at(i)
          get_anagramas(new_alphabet, new_anagrama, anagramas)
        end
      end
    end
  end
  anagramas
end

def ends_with_two_vowels?(word)
  # verifica se os dois ultimos caracteres da string são A,E,I,O ou U.
  word =~ /[AEIOU]{2}$/
end

words = File.readlines("anagramas.txt")

# cria uma array formada pelo conjunto de anagramas de cada palavra no input.
anagramas = words.map do |word|
  # transforma a palavra string em uma array de caracteres em letras maiúsculas.
  get_anagramas(word.strip.upcase.chars)
end

# Escreve o resultado no arquivo saida.txt
File.open("saida.txt", "w"){|f| f.write anagramas.flatten.join("\n")}

# Referências:
# Array#each: http://www.ruby-doc.org/core-2.1.3/Array.html#method-i-each
# Array#map: http://www.ruby-doc.org/core-2.1.3/Array.html#method-i-map
# Array#flatten: http://www.ruby-doc.org/core-2.1.3/Array.html#method-i-flatten
# String#strip: http://www.ruby-doc.org/core-2.1.3/String.html#method-i-strip
