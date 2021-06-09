<p align="center">
   <img src="readme/python.png" width="500" />
</p>

<h2 align="center">
  Curso Python - Alura
</h2>

[![Autor](https://img.shields.io/badge/Student-FelipeRRPereira-A1A1A1?style=flat-square)](https://github.com/FelipeRRPereira)
[![Languages](https://img.shields.io/github/languages/count/FelipeRRPereira/learning-python?color=A1A1A1&label=Langueges&style=flat-square)](#)
[![GitHub issues](https://img.shields.io/github/issues/FelipeRRPereira/learning-python?color=A1A1A1&label=Issues&style=flat-square)](https://github.com/FelipeRRPereira/typescript-bank/issues)
[![GitHub forks](https://img.shields.io/github/forks/FelipeRRPereira/learning-python?color=A1A1A1&label=Forks&style=flat-square)](https://github.com/FelipeRRPereira/typescript-bank/network)
[![GitHub stars](https://img.shields.io/github/stars/FelipeRRPereira/learning-python?color=A1A1A1&label=Stars&style=flat-square)](https://github.com/FelipeRRPereira/typescript-bank/stargazers)


## Índice

<ul>
  <li><a href="#-iniciando-projeto">Iniciando projeto</a></li>
  <li><a href="#">Em construção...</a></li>
</ul>

## 🚀 Iniciando no projeto

---

### Pré-requisitos

- Para rodar o projeto será necessário instalar o [Python](https://www.python.org/).
- Clonar este repositório para sua maquina local.

```powershell
git clone https://github.com/FelipeRRPereira/
```

### Comentários

Para fazer comentários na linguagem Python é utilizado as opções de `#` para comentar uma unica linha e `...` para comentar mais de uma linha.

```python
# Comentários de uma unica linha

'''
Comentários de varias linhas.
1 linha
2 linha
'''

"""
Comentários de varias linhas.
1 linha
2 linha
"""
```

### Tipagem dinâmica

Como JavaScript o Python atribui sua tipagem dinamicamente o que ocorre quando um valor é atribuído a uma variável.

```python
pais = "Brasil"
type(pais)
---------------
Retorno:
<class 'str'>
```

Convenção padrão de declaração de variáveis é o **Snake_Case**:

```python
data_nascimento = "10/10/1930"
recibos_em_atraso = 20
```

Outra questão importante do Python é a sua indentação, pois é por ela que são definidos os blocos de código como no *"então"* de uma condição. Exemplo.:

```python
secret_number = 43
attempt = input("Digite o seu numero: ")
print("Você digitou ", attempt)

if (secret_number == int(attempt)):
    print("Você acertou!")
else:
    print("Você errou!")
```

Notasse também que não é utilizado `;` no fim da linha. O `if` tem a estrutura de `()`, que não é obrigatório, com `:` para o *"então"* e no `else` também se usa `:`.

Outro ponto sobre tipagem é sobre o seguinte código que ao ser executado gera um erro de uma operação com tipos diferentes o que demostra que a linhagem não tem conversão de tipos na atribuição de uma operação.

```python
idade1 = 10
idade2 = "20"
print(idade1 + idade2)
---------------------------
Retorno:
unsupported operand type(s) for +: 'int' and 'str'
```

### Diferenças entre Python2 x Python3

Na troca de versão do Python2 para Python3 ouve mudanças importantes na linguagem e uma das coisas foram a obrigatoriedade do use de `()` em funções. 

```python
# Python2
print "Mensagem no console."
```

```python
# Python3
print("Mensagem no console.")
```

Outra mudança é a possibilidade de passagem de mais de um argumento separado por `,`, separador entre os argumentos pela opção `sep` e a opção `end` para finalizar script na função `print()`.

```python
# Python2
print "Mensagem no console."
# ou
print("Mensagem no console.")
```

```python
# Python3
print("Mensagem", "no", "console", sep=" ", end=".\n")
```

### Condicionais

São basicamente 3 operadores principais como o `if`, `elif` e o `else`. Segue exemplos:

```python
# If
if (true):
		print("Verdade")
# ------------------
if true:
		print("Verdade")
# Elif
elif (true):
		print("Verdade")
# Else
else:
		print("Verdade")
```

Os operadores de comparação são os seguintes:

- **`<`** - menor que
- **`>`** - maior que
- **`<=`** - menor ou igual a
- **`>=`** - maior ou igual a
- **`==`** - igual a
- **`!=`** - diferente de

### Laços de repetição

Em *Python* existem basicamente dois tipos de `while` e `for`. Segue exemplos:

```python
# while
while (count <= 5):
	print(count)

# for
for i range(5):
	print(i)

# while com else
while count <= 5:
    print(count)
    count += 1
else:
    print('após iteração')

# for com else
for i in range(5):
    print(i)
else:
    print('após iteração')

# while com continue e break
while count <= 5:
    print(count)
    count += 1
    if count > 3: break

# for com continue e break
for count in range(1, 5 + 1):
    print(count)
    count += 1
    if count > 3: break
```

### Interpolação de String

Para interpolar *string* no *Python* utilizamos de uma função presente no tipo *string*. Veja:

```python
print("Tentativa {} de {}".format(roundNumber, number_attempts))

print("R$ {:f}".format(1.59))
# Retorno:
# R$ 1.590000

print("R$ {:.2f}".format(1.59))
# Retorno:
# R$ 1.59

print("R$ {:7.2f}".format(1234.50))
# Retorno
# R$ 1234.50

print("Data {:02d}/{:02d}".format(9, 4))
# Retorno:
# Data 09/04
```

**Diferenças entre Python2 x Python3 no uso de interpolação**

Note a diferença do uso de interpolação no *Python2* e *Python3* onde no primeiro exemplo se usa a `%d` e no segundo exemplo `{}`.

```python
# Python2
"%d %d" % (1, 2)
```

```python
# Python3
"{} {}".format(1, 2)
```

Já no *Python3.6+* temos um novo recurso onde ao adicionar um `f` antes de uma *string* basta informar o nome da variável que deseja ser interpolada. Veja:

```python
# Python3.6+
nome = 'Felipe'
print(f'Meu nome é {nome}')
# Retorno:
Meu nome é Felipe
```

### Funções build-in e módulos

Como em outras linguagens de programação, muitas funções são chamadas de *build-in*, ou seja, já estão embutidas na linguagem e outras não. As funções que não são embutidas, são chamadas de módulos no *Python* ou bibliotecas em outras linguagens como *JavaScript*. Para disponibiliza-las para uso em seu programa usamos o recurso de `import`. Veja:

```python
import random
number = random.randrange(1, 101)
print(number)
```

**Curiosidade Pseudo-Random**

No exemplo acima, usamos o módulo *random* para gerar nossos números aleatórios de 1 a 100, porém na documentação do módulo define que essa função é uma pseudo random, ou seja, é um aleatório não tão aleatório. Para gerar o número o modulo utiliza um recuso chamado *seed* que é os milissegundos do computador para gerar números diferentes, e a possibilidade de alterar o mesmo. Veja a seguir:

```python
import random
random.seed(100)
number = random.randrange(1, 101)
print(number) # retorno sempre vai ser o mesmo.
```

**Curiosidade Bool**

Na função *build-in* *bool* podemos utilizar do conceito chamado de "*Truth Value Testing*" ou seja, validar se o valor é vazio. Note que os valores nulos ou vazios e zeros retorno false como resultado. Isso diminuem alguns caracteres de validações normalmente feitas em outras linguagens. Veja a seguir:

```python
>>> bool(0)
False
>>> bool("")
False
>>> bool(None)
False
>>> bool(1)
True
>>> bool(-100)
True
>>> bool(13.5)
True
>>> bool("teste")
True
>>> bool(True)
True
```

**Diferenças entre Python2 x Python3 no uso de *round***

A função de arredondamento no *Python2* retorna um número de tipo *float*, já no *Python3* é retornado um número do tipo *int*. Veja:

```python
# Python2
round(40.5)
# Retorno: 41.0
```

```python
# Python3
round(40.5)
# Retorno: 40
```

### Divisão de Float e Integer

Quando dividimos(`x / y`) dois números no Python, sempre será retornado um valor de tipo *float* e isso é chamado de *float division*. Veja:

```python
print(3 / 2)
# Retorno: 1.5
```

Porém existe uma opção de divisão onde o retorno é um valor inteiro, ou seja, *integer division*. Veja:

```python
print(3 // 2)
# Retorno: 1
```

### Definindo funções

Para definirmos uma função no Python utilizamos a palavra reservada ou o recurso build-in da linguagem `def` seguido do nome. Veja a seguir:

```python
def nome_funcao():
	print("Função definida!")
```

Preste atenção na estrutura do `def` nome da função mais os `():`.

Outro exemplo com parâmetros:

```python
def somar(a, b):
	return a + b
```

**Parâmetros nomeados e opcionais**

No *Python* temos uma funcionalidade que não está presente em todas as linguagens de programação. Nas funções *Python* podemos declarar parâmetros nomeados e opcionais, tirando a necessidade de manter a passagem de parâmetro em ordem e de tornar opcional informar algum valor. Veja a seguir:

```python
# Declaração da função
def carrega_palavra_secreta(nome_arquivo = "palavras.txt", primeira_linha_valida = 0):
	pass

# Função com valor pardão tirando a obrigatoriedade de informar.
carrega_palavra_secreta(nome_arquivo="frutas.txt", primeira_linha_valida= 5)
# A mesma função com ordem de passagem diferente devido a funcionalidade de parâmetros 
# nomeados.
carrega_palavra_secreta(primeira_linha_valida=5, nome_arquivo="frutas.txt")
```

### Tipo Str ou String

No Python o tipo *String,* é chamado de *str,* o qual disponibiliza uma serie de funções para utilização nas comuns *strings.* As *str* podem ser declaradas com aspas simples, duplas e triplas. Veja o exemplo:

```python
# aspas simples
nome = 'Felipe'
# aspas duplas
sobre_nome = "Pereira"
# aspas triplas - armazena todos os espaços e quebras de linha.
nome_completo = '''
Felipe 
Pereira
'''
```

**Alguns Métodos do Str**

Alguns métodos com funcionalidades interessantes estão presentes na biblioteca do Python. Funcionalidades como *capitalize, casefold, title, endswith* e *find*. Veja exemplos:

```python
# Capitalize - Converte primeira letra em maiuscula
nome = 'felipe'
nome.capitalize()
# Retorno: Felipe

# Casefold - Converte todas as letras maiúsculas para minúsculas
nome = 'FELIPE'
nome.casefold()
# Retorno: felipe

# Title - Converte todas as iniciais para maiúsculas
nome = 'felipe pereira'
nome.title()
# Retorno: Felipe Pereira

# Endswith - Retorna True se a string final for igual a passada por parâmetro
nome = 'Felipe Pereira'
nome.endswith('ira')
# Retorno: True

# Find - Busca uma string passada por parâmetro e retorna o primeiro indice encontrado
nome = 'Felipe Pereira'
nome.find('ira')
# Retorno: 11
```

### Tipos de Sequências - List, tuple e range

Como na maioria das linguagens, estruturas de dados listas estão presentes também no Python porém são chamadas de sequencias e estão distribuídas em três tipos, list, tuple e range.

```python
# List - Transforma uma sequencia de string em um array ou list.
list('abc')
# Retorno: ['a', 'b', 'c']

# Tuple - Também transforma uma sequencia de caracteres em uma tuple, porém imutável.
tuple('123')
# Retorno: ('1', '2', '3')

# Range - Sequência do inicio 0 até o valor passado por parâmetro e também é imutável.
range(3)
# Retorno: range(0, 3)
```

**Funções**

Alguns das funções build-in que podem ser utilizadas em tipos de sequências, min(), max(), len() entre outras. Veja a seguir:

```python
# Min - Retorna o menor valor de uma lista
valores = [0, 1, 2, 3]
min(valores)
# Retorno: 0

# Max - Retorna o maior valor de uma lista
valores = [0, 1, 2, 3]
max(valores)
# Retorno: 3

# Len - Retorna a quantidade de elementos em uma lista
valores = [0, 1, 2, 3]
len(valores)
# Retorno: 4

# Count - Retorna a quantidade de vezes que um elemento existe em uma lista
valores = [0, 1, 2, 3, 3, 3]
print(valores.count(3))
# Retorno: 3

# Index - Retorna o indíce do elemento passado por parâmetro
valores = ['A', 'B', 'C', 'D']
print(valores.index('B'))
# Retorno: 1
```

**List Comprehension**

Compreensão de lista é um funcionalidade com uma sintaxe simples e enxuta que o Python oferece para realizar criação de novas listas com a necessidade de uso de laços.

```python
palavra = 'List Comprehension'

# Laço adicionando um _ em cada posição da palavra
for letra in palavra
	letras_secretas.append('_')

# Mesmo laço com a sintaxe do List Comprehension
letras_corretas = ['_' for letra in palavra_secreta]
```

Veja um outro exemplo utilizando uma condição:

```python
# Retornar um array com os números pares
inteiros = [1,3,4,5,7,8,9]
pares = []
for numero in inteiros:
    if numero % 2 == 0:
        pares.append(numero)

# Mesmo objetivo com o uso do List Comprehension
inteiros = [1,3,4,5,7,8,9]
pares = [x for x in inteiros if x % 2 == 0]
```

### **Leituras de arquivo**

No Python temos a função build-in *Open* para trabalharmos com arquivos. Para uso da função precisamos passar uma *string* com o nome do arquivo e o modo de manipulação do arquivo. Veja os exemplos a seguir:

```python
# Criação de arquivo e escrita
arquivo = open('palavra.txt', 'a')
arquivo.write('banana')
arquivo.close()

# Leitura de arquivo
# O método read() quando executado efetua a leitura do arquivo completo posicionando 
# o ponteiro no final do arquivo. Caso seja necessario ler o arquivo novamento é preciso
# reabrir o arquivo.
arquivo = open('palavra.txt', 'r')
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

# Leitura de uma linha do arquivo
arquivo = open('palavra.txt', 'r')
linha = arquivo.readline()
print(linha)
arquivo.close()
```

**With**

Ao utilizar as sintaxe de manipulação de arquivo acima, repare o uso do `close()` para cada `open()`, porém ao realizar um procedimento abrindo um arquivo e o mesmo retorne um erro capaz de parar o processamento de leitura, a instancia ficaria aberta. Para resolver isso o *Python* criou o `with`, veja a seguir:

```python
with open("palavras.txt") as arquivo:
    for linha in arquivo:
        print(linha)
```

Observe que no `with` não tem a necessidade de executar o método `close()`.

### Orientação a Objeto

Como em muitas linguagens de programação, a orientação a objetos também está presente na linguagem Python e por ela podemos utilizar dos recursos poderosos do paradigma OO. O paradigma de orientação a objeto tem por objetivo tornar as funcionalidades parecidas como o mundo real. Um exemplo disso, é uma maquina de café. A mesma tem alguns atributos que recebe e com esses atributos e uma funcionalidade especifica gera uma saída que é uma maravilhoso liquido.

**Classe - *class***

A classe é responsável por centralizar ou agrupar atributos e funcionalidades de um determinado objeto, como o exemplo da cafeteira. Veja sintaxe:

```python
class Cafeteira:
	pass
```

Notem que a primeira letra da classe é maiúscula, isso é uma convenção chamada [CamelCase](https://www.google.com/search?q=CamelCase).

**Construtor - *constructor***

Construtores são como o botão de ligar de uma cafeteira seguindo o exemplo acima, nele podemos determinar os atributos mínimos para que ela exista. No caso computacional, ao iniciar uma classe é criado uma referência da memoria onde foi criado a classe. Veja a seguir:

```python
class Cafeteira:
	def __init__(self):
    super().__init__()
```

O *init* nada mais é que o construtor dessa classe e o parâmetro self é a referência de memoria passada para este novo objeto.

Para cada classe criada provavelmente teremos a necessidade de gerar instâncias com valores específicos. Veja a seguir:

```python
class Cafeteira:
  def __init__(self, filtro, qtde_cafe, qtde_agua = 250):
    self.filtro = filtro
    self.qtde_cafe = qtde_cafe
    self.qtde_agua = qtde_agua
```

Observe que no parâmetro qtde_agua foi adicionado um valor padrão, tirando a necessidade de passar tal informação ao criar uma classe. Veja a seguir:

```python
cafeteira = Cafeteira(papel, 2)
```

**Métodos**

São funcionalidades responsáveis por realizar ações de uma determinada classe. Para especifica-las tente pensar em ações que um objeto real funciona. Exemplo de uma cafeteira. Veja a seguir:

```python
class Cafeteira:
	def __init__(self, filtro, qtde_cafe = 2, qtde_agua = 250):
		self.filtro = filtro
    self.qtde_cafe = qtde_cafe
    self.qtde_agua = qtde_agua
	
	def fazerCafe(self, pessoas):
		self.qtde_cafe *= pessoas
		self.qtde_agua *= qtde_agua
		print(
			"Para fazer café para {} pessoas foi utilizado {} clolheres de café e {} ml de água."
			.format(pessoas, self.qtde_cafe, self.qtde_agua)
		)
```

Observe que o método `fazerCafe` recebe um parâmetro `self` que representa a referência da memória para o objeto instanciado. 

**Coletor de Lixo - *garbage collector***

Processo que realiza a limpeza dos objetos instanciados que estão inutilizados na memória. Esse processo está presente na maioria das maquinas virtuais das linguagens de programação como Java, C# e etc.

**None**

O *none* tem a finalidade de retirar a referencia da variável que tem por referencia um objeto da memoria, retirando o vinculo entre objeto e variável.

```python
cafeteiraZ = Cafeteira('Papel')
cafeteiraZ
# Retorno
# <__main__.Cafeteira object at 0x0000015F2EDF7CA0>
cafeteiraZ = None
cafeteiraZ
# Retorno é vazio.
```

**Atributos Privados**

No *Python* o encapsulamento dos atributos de uma classe são tratados adicionando o dois *underscore* `"__"`. Ou seja, os atributos com *underscore* são vistos como privados e só podem ser acessados na classe. Veja a seguir:

```python
class Cafeteira:
	def __init__(self, filtro, qtde_cafe = 2, qtde_agua = 250):
		self.__filtro = filtro
    self.__qtde_cafe = qtde_cafe
    self.__qtde_agua = qtde_agua
```

Quando adicionado o *underscore* nos atributos o *Python* cria por *"debaixo dos panos"* um atributo que permite o acesso porém com uma sintaxe intuitiva que avisa o desenvolvedor que é um atributo privado. Ex.: `cafeteira._Cafeteira__filtro`.

**Encapsulamento**

Conceito usado para manter atributos, métodos e restrições de acesso encapsulado em um objeto. Veja estrutura padrão:

 

```python
class Cafeteira:
	def __init__(self, filtro, qtde_cafe = 2, qtde_agua = 250):
	  self.__filtro = filtro
    self.__qtde_cafe = qtde_cafe
    self.__qtde_agua = qtde_agua
	
	def fazerCafe(self, pessoas):
		self.__qtde_cafe *= pessoas
		self.__qtde_agua *= qtde_agua
		print(
			"Para fazer café para {} pessoas foi utilizado {} clolheres de café e {} ml de água."
			.format(pessoas, self.qtde_cafe, self.qtde_agua)
		)
```

Note que os atributos estão com *underscore* e quando é necessário a referência de si mesmo usasse o `self`.