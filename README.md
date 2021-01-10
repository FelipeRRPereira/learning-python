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