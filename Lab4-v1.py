# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random
from os import system, name

def limpa_tela():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

# Classe
class Hangman:
	def __init__(self):
		#Limpa a tela como um novo jogo
		limpa_tela()
		#Texto de boas vindas ao usuario
		print('Jogo Forca - Seja bem vindo!')
		print('Adivinhe a palavra abaixo: ')

		#Inicializando os atributos
		self.tentativas = 8
		self.letras_erradas = []
		self.palavra_a_ser_adivinhada = ""
		self.palavra_oculta = ""

		# Board (tabuleiro)
		self.board = [
	        #Estagio 9 (Fim de jogo)
	        """ 
	            ---------
	            |       |
	            |       O
	            |      \\|/
	            |       |
	            |      / \\
	            |
	            -
	        """,
	        #Estagio 8
	        """ 
	            ---------
	            |       |
	            |       O
	            |      \\|/
	            |       |
	            |      / 
	            |
	            -
	        """,
	        #Estagio 7
	        """ 
	            ---------
	            |       |
	            |       O
	            |      \\|/
	            |       |
	            |
	            |
	            -
	        """,
	        #Estagio 6
	        """ 
	            ---------
	            |       |
	            |       O
	            |      \\|/
	            |
	            |
	            |
	            -
	        """,
	        #Estagio 5
	        """ 
	            ---------
	            |       |
	            |       O
	            |      \\|
	            |
	            |
	            |
	            -
	        """,
	        #Estagio 4
	        """ 
	            ---------
	            |       |
	            |       O
	            |       |
	            |
	            |
	            |
	            -
	        """,
	        #Estagio 3
	        """ 
	            ---------
	            |       |
	            |       O
	            |
	            |
	            |
	            |
	            -
	        """,
	        #Estagio 2
	        """ 
	            ---------
	            |       |
	            |
	            |
	            |
	            |
	            |
	            -
	        """,
	        #Estagio 1
	        """ 
	            ---------
	            |
	            |
	            |
	            |
	            |
	            |
	            -
	        """
	    ]

		#lista de possiveis palavras a serem adivinhadas
		self.palavras = [
			'abacaxi', 'banana', 'carro', 'dedo', 'elefante', 'fogo', 'gato', 'hotel', 'igreja', 'janela',
			'kiwi', 'limao', 'macaco', 'navio', 'ostra', 'pato', 'queijo', 'roda', 'sapato', 'tigre',
			'uva', 'vaca', 'xadrez', 'zebra', 'amarelo', 'branco', 'cinza', 'doce', 'escuro', 'fino',
			'grande', 'honesto', 'iluminado', 'jovem', 'kit', 'largo', 'magico', 'nobre', 'ousado', 'puro',
			'quieto', 'rico', 'sabio', 'timido', 'único', 'vivo', 'xarope', 'zeloso', 'amor', 'beleza',
			'coragem', 'desejo', 'esperanca', 'felicidade', 'gratidao', 'harmonia', 'inspiracao', 'justica', 'lealdade',
			'magia', 'natureza', 'orgulho', 'paixao', 'riqueza', 'sabedoria', 'ternura', 'uniao', 'valentia', 'xodo',
			'zero', 'agua', 'bola', 'ceu', 'dente', 'escola', 'fogo', 'gelo', 'hotel', 'ilha',
			'jardim', 'ketchup', 'lua', 'mundo', 'navio', 'ouro', 'papel', 'quarto', 'rosa', 'sol',
			'trem', 'urso', 'vaca', 'xicara', 'zebra'
		]

	#decrementa o numero de tentativas
	def decrementarTentativas(self):
		self.tentativas -= 1

	# Seta a palavra a ser adivinhada
	def setPalavraASerAdivinhada(self):
		#escolha da palavra randomicamente
		self.palavra_a_ser_adivinhada = random.choice(self.palavras)

	# Oculta a palavra a ser adivinhada
	def ocultarPalavra(self):
		self.palavra_oculta = ['_' for letra in self.palavra_a_ser_adivinhada]

	#Verifica se tem um vencedor
	def temVencedor(self):
		if "_" not in self.palavra_oculta:
			return True
		else:
			return False

	#Verifica o status do jogo
	def jogoTerminou(self):
		if "_" in self.palavra_oculta:
			return True
		else:
			return False

	# Pega uma letra do usuário e verifica se existe na palavra
	# a ser adivinhada
	def adivinhaLetra(self):
		while self.tentativas > 0:
			print(self.board[self.tentativas])
			print(" ".join(self.palavra_oculta))
			print("\n")
			print("Tentativas restantes: ", self.tentativas)
			print("Letras erradas:", " ".join(self.letras_erradas))

			letra_digitada = input("\nDigite uma letra: ").lower()

			if (letra_digitada in self.letras_erradas) or (letra_digitada in self.palavra_oculta):
				print("Você já tentou essa letra, digite outra!")
				continue

			if letra_digitada in self.palavra_a_ser_adivinhada:
				index = 0
				for letra in self.palavra_a_ser_adivinhada:
					if letra_digitada == letra:
						self.palavra_oculta[index] = letra
					index += 1
			else:
				self.decrementarTentativas()
				self.letras_erradas.append(letra_digitada)

			if self.temVencedor():
				print("\nVOCÊ VENCEU!!\nA palavra era:", self.palavra_a_ser_adivinhada)
				break
		if self.jogoTerminou():
			print("\nVOCÊ PERDEU, a palavra era: ", self.palavra_a_ser_adivinhada)

if __name__ == "__main__":
	novo_jogo = Hangman()
	novo_jogo.setPalavraASerAdivinhada()
	novo_jogo.ocultarPalavra()
	novo_jogo.adivinhaLetra()