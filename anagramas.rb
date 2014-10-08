def get_anagramas(alphabet, anagrama="", anagramas=[])
  if alphabet.empty?
    anagramas << anagrama
  else
    used = {}
    alphabet.each.with_index do |c, i|
      if !used[c]
        used[c] = true
        new_anagrama = anagrama + c
        if !ends_with_two_vowels?(new_anagrama)
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
  word =~ /[AEIOU]{2}$/
end

words = File.readlines("anagramas.txt")

anagramas = words.map do |word|
  get_anagramas(word.strip.upcase.split(//))
end

File.open("saida.txt", "w"){|f| f.write anagramas.flatten.join("\n")}
