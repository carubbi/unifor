# UNIFOR
**Nome**: Nome do estudante<br>
**Disciplina**: Raciocínio lógico algorítmico

## Exercício exemplo 1
Implemente e teste um programa que imprima os n primeiros números.

#### Fluxograma
```mermaid
flowchart TD
A([INICIO]) --> B{{Digite um número: }}
B --> C[\n\]
C --> D[\num = 1\]
D --> E{num <= n}
E --FALSE--> I([FIM])
E --TRUE--> F{{"Num", num}}
F --> G[num =+ 1]
G --LOOP--> E
```

#### Pseudocódigo
```java
ALGORITMO print_n_primeiros
DECLARE n, num: INTEIRO
INICIO
  ESCREVA “Digite um número: ”
  LEIA n			// variável de entrada n
  num ← 1			// variável num inicializada
  ENQUANTO num <= n FAÇA	// n iterações
    ESCREVA “Número ”, num
    num ← num + 1		// num =+ 1 (incremento)
  FIM_ENQUANTO
FIM
```

#### Tabela de testes
| it | n  | num | num <= n | Saída      | num =+ 1 |
| -- | -- | --  | --       | --         | --       |
| 1  | 10 | 1   | True     | Número 1   | 2        |
| 2  | 10 | 2   | True     | Número 2   | 3        |
| 3  | 10 | 3   | True     | Número 3   | 4        |
| 4  | 10 | 4   | True     | Número 4   | 5        |
| 5  | 10 | 5   | True     | Número 5   | 6        |
| 6  | 10 | 6   | True     | Número 6   | 7        |
| 7  | 10 | 7   | True     | Número 7   | 8        |
| 8  | 10 | 8   | True     | Número 8   | 9        |
| 9  | 10 | 9   | True     | Número 9   | 10       |
| 10 | 10 | 11  | True     | Número 10  | 11       |
| 11 | 10 | 11  | False    |            |          |

## Exercício exemplo 2
Implemente e teste um programa que some os n primeiros números.

#### Fluxograma
```mermaid
flowchart TD
A([INICIO]) --> B{{Digite um número: }}
B --> C[\n\]
C --> D[\soma = 0\]
D --> E[[i=1 ATÉ n PASSO 1]]
E --> G([FIM])
E --> F[soma =+ i]
F --LOOP--> E
```

#### Pseudocódigo
```java
ALGORITMO	soma_n_numeros()
DECLARE	n, i, soma: INTEIRO
INICIO
  ESCREVA “Digite a quantidade de números: ”
  LEIA n    // variável de entrada n
  soma ← 0    // variável soma inicializada
  PARA i DE 1 ATÉ n PASSO 1 FAÇA
    soma ← soma + i    // soma =+ i (incremento)
  FIM_PARA
  ESCREVA “A soma é igual a ”, soma
10 FIM
```

#### Tabela de testes
| it | n  | soma | i  | soma =+ i |
| -- | -- | --   | -- | --        |
| 1  | 10 | 0    | 1  | 1         |
| 2  | 10 | 1    | 2  | 3         |
| 3  | 10 | 3    | 3  | 6         |
| 4  | 10 | 6    | 4  | 10        |
| 5  | 10 | 10   | 5  | 15        |
| 6  | 10 | 15   | 6  | 21        |
| 7  | 10 | 21   | 7  | 28        |
| 8  | 10 | 28   | 8  | 36        |
| 9  | 10 | 36   | 9  | 45        |
| 10 | 10 | 45   | 10 | 55        | 

## Lista de exercícios 03

### Exercício 01 (2.5 pontos)
Atualize o algoritmo para determinar se um número inteiro e positivo é par ou ímpar, usando uma laço condicional para aceitar apenas números maiores ou iguais a zero. 

#### Fluxograma (1.0 ponto)

```mermaid
flowchart TD
A([INICIO]) --> B{{Digite um número:}}
B --> C[\num\]
C --> D{num < 0}
D --FALSE--> E[resto = num % 2]
E --> H{resto == 0}
H --FALSE--> I{{O número é impar!}}
H --TRUE--> J{{O número é par!}}
I --> Z([FIM])
J --> Z
D --TRUE--> F{{Digite um número maior ou igual a zero:}}
F --> G[/num/]
G --LOOP--> D
```

#### Pseudocódigo (1.0 ponto)

```java
ALGORTIMO verifica_par_impar
DECLARE numero, resto: INTEIRO
ESCREVA "Digite um número: "
INICIO
  LEIA numero
  SE numero >= 0 ENTAO                  // verifica se o inteiro é positivo
    resto ← numero % 2                 // calcula o resto da divisão por 2
    SE resto == 0 ENTAO                // verifica se o resto é igual a zero
      ESCREVA "O número é par!"
    SENAO
      ESCREVA "O número é impar!"
    FIM_SE
  SENAO                                // caso inteiro for negativo (condição linha 5)
    ESCREVA "O número deve ser postivo!"
  FIM_SE
FIM
```

#### Tabela de testes (0.5 ponto)

| num | num < 0 | num | resto | resto == 0 | saída             | 
| --  | --      | --  | --    | --         | --                | 
| -1  | True    | 0   | 0     | True       | O número é par!   |
| 1   | False   |     | 1     | False      | O número é impar! |
| 2   | False   |     | 0     | True       | O número é par!   |

### Exercício 02 (2.5 pontos)
Faça um algoritmo que exiba na tela uma contagem de 0 até 30, exibindo apenas os múltiplos de 3.

#### Fluxograma (1.0 ponto)

```mermaid
flowchart TD
A([INICIO]) --> B{{Digite a quantidade de números: }}
B --> C[\n\]
C --> E[[i=0 ATÉ n-1 PASSO 3]]
E --> G([FIM])
E --> F{{ESCREVA i}}
F --LOOP--> E
```

#### Pseudocódigo (1.0 ponto)

```java
ALGORTIMO MultiploTres
DECLARE n: INTEIRO
INICIO
  ESCREVA "Digite a quantidade de números:"
  LEIA n
  PARA i DE 0 ATÉ n-1 PASSO 3 FAÇA
    ESCREVA i
  FIM_PARA
FIM
```

#### Tabela de testes (0.5 ponto)

| it | n   | i  | saida | 
| -- | --  | -- | --    |    
| 1  | 7   | 0  | 0     |
| 2  | 7   | 3  | 3     |
| 3  | 7   | 6  | 6     |

### Exercício 03 (2.5 pontos)
Dada uma sequência de números inteiros, calcular a sua soma. 
Por exemplo, para a sequência {12, 17, 4, -6, 8, 0}, o seu programa deve escrever o número 35.

#### Fluxograma 1

```mermaid
flowchart TD
A([INICIO]) --> B{{"Digite a quantidade de números:"}}
B --> C[\n\]
C --> D[i = 1]
D --> E[soma = 0]
E --> F{i <= n}
F --FALSE--> G{{A soma dos número é, soma}}
G --> L([FIM])
F --TRUE--> H{{Digite o número, i,:}}
H --> I[\num\]
I --> J[soma = soma + num]
J --> K[i = i + 1]
K --LOOP--> F
```

#### Fluxograma 2
```mermaid
flowchart TD
A([INICIO]) --> B{{"Digite a quantidade de números:"}}
B --> C[\n\]
C --> D[soma = 0]
D --> E[[i=1 ATE n, PASSO 1]]
E --FALSE--> F{{A soma dos número é, soma}}
F --> L([FIM])
E --TRUE--> G{{Digite o número, i,:}}
G --> H[\num\]
H --> I[soma = soma + num]
I --LOOP--> E
```

#### Pseudocódigo (1.0 ponto)

```java
ALGORITMO SomaValores
DECLARE n,i: INTEIRO; soma,num: REAL
INICIO
  ESCREVA "Digite a quantidade de números:"
  LEIA n
  soma <- 0
  i <- 1
  ENQUANTO i <= n FAÇA
    ESCREVA "Digite o número", i,":"
    LEIA num
    soma <- soma + num
    i <- i + 1
  FIM_ENQUANTO
  ESCREVA "A soma dos número é", soma
FIM
```

#### Tabela de testes (0.5 ponto)

| n  | soma | i  | i <= n | num | soma + num | i + 1   | saída                      |  
| -- | --   | -- | --     | --  | --         | --      | --                         |
| -1 | 0    | 1  | False  |     |            |         | A soma dos número é 0      |
| 0  | 0    | 1  | False  |     |            |         | A soma dos número é 0      |
| 3  | 0    | 1  | True   | 10  | 0+10 = 10  | 1+1 = 2 |                            |
| 3  | 10   | 2  | True   | 20  | 10+20 = 30 | 2+1 = 3 |                            |
| 3  | 30   | 3  | True   | 30  | 30+30 = 60 | 3+1 = 4 |                            |
| 3  | 60   | 4  | False  |     |            |         | A soma dos número é 60     |

### Exercício 04 (2.5 pontos)
Escreva um programa que leia a nota de diversos alunos, até que seja digitada uma nota negativa. 
Nesse momento, ele mostra a média aritmética de todas as notas lidas e quantas notas foram lidas. 
Ex. Foram lidas 14 notas. A média aritmética é 6.75!

#### Fluxograma

```mermaid
flowchart TD
A([INICIO]) --> B([soma = 0])
B --> C[quant = 0]
C --> D[nota = 0]
D --> E{nota >= 0}
E --FALSE--> F{quant > 0}
F --FALSE--> M([FIM])
F --TRUE--> K[media = soma / quant]
K --> L{{Foram lidas, quant, notas. <br>A média aritmética é, media!}}
L --> M
E --TRUE--> G{{"Digite a nota do aluno <br>(nota negativa encerra o algortimo): "}}
G --> H[/nota/]
H --> I[soma += nota]
I --> J[quant += 1]
J --LOOP--> E
```

#### Pseudocódigo

```java
ALGORTIMO QuantMedia
DECLARE quant: INT; soma, nota, media: REAL
INICIO
  soma <- 0
  quant <- 0
  nota <- 0
  ENQUANTO nota >= 0 FAÇA
    ESCREVA "Digite a nota do aluno (nota negativa encerra o algortimo:"
    LEIA nota
    soma <- soma + nota
    quant <- quant + 1
    SE quant > 0 ENTAO
      media <- soma / quant
  ESCREVA "Foram lidas", quant, "notas. A média aritmética é", media, "!"
FIM
```

#### Tabela de testes (0.5 ponto)

| it  | soma | quant | nota | nota  | soma + nota | quant + 1 | media    | saída                                         | 
| --  | --   | --    | --   | --    | --          | --        | --       | --                                            |
| 1   | 0    | 0     | 0    | 0     | 0           | 0+1=1     | 0/1=0    |                                               |
| 2   | 0    | 0     | 0    | -1    |             |           |          |                                               |
| 1   | 0    | 0     | 0    | -1    |             |           |          |                                               |
| 1   | 0    | 0     | 0    | 40    | 0+40=40     | 0+1=1     |          |                                               |
| 2   | 0    | 0     | 0    | 60    | 40+60=100   | 1+1=2     |          |                                               |
| 3   | 0    | 0     | 0    | 20    | 100+20=120  | 2+1=3     |          |                                               |
| 4   | 0    | 0     | 0    | -1    |             |           | 120/3=40 | Foram lidas 3 notas. A média aritmética é 40! |
