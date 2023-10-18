class Jogador:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

class Tronco(Jogador):
    def __init__(self, altura, largura):
        super().__init__(nome='Ronaldo', idade=36, endereco='Brasil')  
        self.altura = altura
        self.largura = largura

class PernaDireita(Jogador):
    def __init__(self, comprimento, largura):
        super().__init__(nome='messi', idade=40, endereco='Argentina')  
        self.comprimento = comprimento
        self.largura = largura

class PernaEsquerda(Jogador):
    def __init__(self, comprimento, largura):
        super().__init__(nome='Pele', idade=60, endereco='Brasil')  
        self.comprimento = comprimento
        self.largura = largura

class Cabeca(Jogador):
    def __init__(self, tamanho, forma):
        super().__init__(nome='Cafu', idade=58, endereco='Brasil')  
        self.tamanho = tamanho
        self.forma = forma

class Caracteristica:
    def __init__(self):
        self.tronco = None
        self.perna_direita = None
        self.perna_esquerda = None
        self.cabeca = None

    def agregar_tronco(self, altura, largura):
        self.tronco = Tronco(altura, largura)

    def agregar_perna_direita(self, comprimento, largura):
        self.perna_direita = PernaDireita(comprimento, largura)

    def agregar_perna_esquerda(self, comprimento, largura):
        self.perna_esquerda = PernaEsquerda(comprimento, largura)

    def agregar_cabeza(self, tamanho, forma):
        self.cabeca = Cabeca(tamanho, forma)

class MostrarCaract:
    def mostrar_caract(self, jugador):
        if isinstance(jugador, Jogador):
            print(f"Jogador: {jugador.nome}")
            print(f"idade: {jugador.idade}")
            print(f"endereço: {jugador.endereco}")
        if isinstance(jugador, Tronco):
            print(f"Altura do tronco: {jugador.altura}")
            print(f"Largura do tronco: {jugador.largura}")
        if isinstance(jugador, PernaDireita):
            print(f"Comprimento da perna direita: {jugador.comprimento}")
            print(f"Largura da perna esquerda: {jugador.largura}")
        if isinstance(jugador, PernaEsquerda):
            print(f"Comprimento da perna esquerda: {jugador.comprimento}")
            print(f"Largura da perna direita: {jugador.largura}")
        if isinstance(jugador, Cabeca):
            print(f"Tamanho da cabeça: {jugador.tamanho}")
            print(f"Forma da cabeça: {jugador.forma}")


caracteristicas = Caracteristica()
caracteristicas.agregar_tronco(100, 50)
caracteristicas.agregar_perna_direita(200, 40)
caracteristicas.agregar_perna_esquerda(200, 40)
caracteristicas.agregar_cabeza(30, 'Oval')


mostrar = MostrarCaract()
mostrar.mostrar_caract(caracteristicas.tronco)
mostrar.mostrar_caract(caracteristicas.perna_direita)
mostrar.mostrar_caract(caracteristicas.perna_esquerda)
mostrar.mostrar_caract(caracteristicas.cabeca)
