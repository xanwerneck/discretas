<?php 


//$alfabeto = ["A" , "B" , "C" , "D" , "E" , "F" , "G" , "H" , "I" , "J" , "K" , "L" , "M" , "N" , "O" , "P" , "Q" , "R" , "S" , "T" , "U" , "V" , "W" , "X" , "Y" , "Z"];

class Teste{

	public $temp = [];
	public $n    = 3;
	public $alf;

	public function Gera($alfabeto,$tam){

		if ($tam == 0) {
			echo join("",$this->temp)."\n";
			return;		
		}

		for ($i=0; $i < count($alfabeto); $i++) { 
			
			$this->temp[$this->n - $tam] = $alfabeto[$i];				
			$this->Perm($alfabeto,$tam-1);
			
		}

	}

	public function Geracao($i,$alfabeto){

		if ($i == 0) {
			echo join("",$p);
		}else{
			for($j=0;$j<count($alfabeto);$j++) {
				$p[$this->n - $i] = $alfabeto[$j];
				$this->Geracao($i-1,$alfabeto);
			}
		}

	}

	public function Perm($alfabeto,$tam){

		if ($tam == 0) {
			echo join("",$this->temp)."\n";
			return;		
		}

		for ($i=0; $i < count($alfabeto); $i++) { 
			
			$this->temp[$this->n - $tam] = $alfabeto[$i];
			$tm[0] = $alfabeto[$i];	
			$alfabet = array_diff($alfabeto, $tm);
			$this->Perm($alfabet,$tam-1);
			
		}

	}


}
$tp = new Teste();


$alfabeto = ["a","b","c"];
$p = [];
$n = 3;
function Geracao($i,$alfabeto){
	global $p,$n;
	if ($i == 0) {
		echo join("",$p)."\n";
	}else{
		for($j=0;$j<count($alfabeto);$j++) {
			$p[$n - $i] = $alfabeto[$j];
			Geracao($i-1,$alfabeto);
		}
	}

}

function Permuta($alfabeto){
	global $p,$n;
	if (count($alfabeto) == 0) {
		echo join("",$p)."\n";
	}else{
		for ($i=0; $i < count($alfabeto); $i++) { 
			$p[$n - count($alfabeto)] = $alfabeto[$i];
			$tp = $alfabeto;
			unset($tp[$i]);
			Permuta(array_values($tp));
		}
	}
}

echo Permuta($alfabeto);
echo Geracao(3,$alfabeto);


 ?>