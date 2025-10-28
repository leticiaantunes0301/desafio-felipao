def definir_elo_invocador(vitorias, derrotas):
    
    
    pdl = (vitorias - derrotas)
    nivel = ""

    if vitorias < 10: 
        nivel = "Ferro"  
    elif vitorias <= 20: 
        nivel = "Bronze" 
    elif vitorias <= 50: 
        nivel = "Prata" 
    elif vitorias <= 80:
        nivel = "Ouro" 
    elif vitorias <= 90: 
        nivel = "Platina" 
    elif vitorias <= 100: 
        nivel = "Esmeralda" 
    elif vitorias <= 150:
        nivel = "Diamante"
    elif vitorias <= 200: 
        nivel = "Mestre"
    elif vitorias <= 270: 
        nivel = "Grão-Mestre"
    else: 
        nivel = "Desafiante"
    
    print(f"O Invocador tem um PDL de {pdl} e está no nível {nivel}")


print("--- Analisador de Elo (LoL) ---")
definir_elo_invocador(70, 20)  
definir_elo_invocador(100, 10) 
definir_elo_invocador(180, 50) 
definir_elo_invocador(300, 50) 