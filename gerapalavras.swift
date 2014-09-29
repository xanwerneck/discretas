// Gera Palavras Swift
// Patrick Sava

    let n = 3 //let = constante
    var alfabeto:[String] = [ "a", "b", "c" ]
	var palavra:[String] = [ "", "", ""]
	
	/* 
	 * func <nomedafuncao>(p1:Tipo withOutroParametro p2:Tipo 
	 *	outroParametro p3:Tipo atecansar pN:Tipo) -> TipoRetorno{}
	 */
	func executa(i:Int){
	    if(i == 0){
	        var combination = palavra[0] + palavra[1] + palavra[2]
	        println(combination)
	    } else {
	        var j = 1
	        for j in 1...n { 
	        // for i in x..y  => for( x <= i <  y )
	        // for i in x...y => for( x <= i <= y )
	            palavra[n-i] = alfabeto[j-1]
	            var k:Int = i-1; //; sempre opcional
	            executa(k)
	        }
	    }
	        
	}

    executa(3)
