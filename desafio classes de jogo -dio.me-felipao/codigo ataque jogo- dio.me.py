class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo
    
    
    def atacar(self):
        ataque = ""

        
        if self.tipo == "mago":
            ataque = "magia"
        
        elif self.tipo == "guerreiro":
            ataque = "espada"
            pass 
            
        elif self.tipo == "monge":
            ataque = "artes marciais"
            pass 
            
        elif self.tipo == "ninja":
            ataque = "shuriken"
            pass 
            
        else:
            ataque = "um ataque desconhecido" 

        # A saída final
        print(f"o {self.tipo} atacou usando {ataque}")

mago = Heroi("Gandalf", 1000, "mago")
guerreiro = Heroi("link", 16, "guerreiro")
monge = Heroi("Chun-Li", 28, "monge")
ninja = Heroi("Naruto", 20, "ninja")

# Chamando o método atacar para ver o output
mago.atacar()
guerreiro.atacar()
monge.atacar()
ninja.atacar()