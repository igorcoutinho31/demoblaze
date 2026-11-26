# Roteiro de fala — A3 Demoblaze (Grupo 2)

Anotações de cada slide da apresentação (`docs/slides/index.html`).

## Slide 1 — Testando o Demoblaze

Apresentar o grupo. Uma frase: testamos a loja Demoblaze, automatizamos 14 casos e encontramos 5 defeitos. A linha do terminal é o resultado real da execução final de 25/11.

## Slide 2 — Uma loja de eletrônicos de demonstração

Explicar o site em uma frase. Os três fluxos são os que o guia do professor pediu, na ordem em que um cliente usa a loja. Fora do escopo: a regra da disciplina proíbe teste de carga, e escolhemos só o Chrome.

## Slide 3 — Cinco atributos, dois priorizados

Consideramos cinco atributos da ISO/IEC 25010. Priorizamos dois, que têm testes automatizados: adequação funcional, porque é uma loja, e segurança, porque o site recebe senha e cartão. Usabilidade, confiabilidade e eficiência de desempenho foram observadas durante a execução, sem testes específicos; por exemplo, o atraso no carregamento das páginas exigiu esperas explícitas. Mostrar o CA02 como exemplo de critério Dado / Quando / Então. São 7 critérios (CA01 a CA07), todos com teste automatizado.

## Slide 4 — O que podia atrapalhar, e como tratamos

Os cinco primeiros riscos são do projeto: coisas que podiam atrapalhar os testes, como o site instável ou os alertas do navegador. Os três últimos são riscos do produto, e cada um tem casos de teste que o verificam. Severidade é o impacto do problema; prioridade é a urgência de tratar.

## Slide 5 — 14 casos, duas técnicas de projeto

PE separa entradas válidas e inválidas, como usuário novo e usuário repetido. VL testa o limite: 0 caractere na compra, senha de 7 para um mínimo de 8, mês 13 para um máximo de 12. As réguas mostram esses dois limites: em verde o que é válido, em laranja o valor testado. Os CT12 a CT14 foram feitos para encontrar defeitos. CT10 e CT11 foram propostos pela Julia.

## Slide 6 — Como cada caso foi especificado: o CT13

Este é o formato usado no capítulo 3 do relatório para os 14 casos. Os fluxos alternativos são variações do caso, para executar separadamente quando fizer sentido. No CT13, o resultado esperado não aconteceu: o site confirmou a compra, e isso virou o defeito DF02.

## Slide 7 — Python, Selenium e pytest com Page Objects

Seguir o diagrama da esquerda para a direita: o teste descreve o cenário, o Page Object sabe onde clicar, o Selenium controla o Chrome, e o Chrome abre o Demoblaze. Embaixo, as três decisões que deixaram os testes estáveis. Repositório: github.com/igorcoutinho31/demoblaze.

## Slide 8 — 11 testes aprovados, 3 reprovados

As linhas aparecem em ordem numérica (na execução real, o CT09 roda junto com os testes de login, logo depois do CT04). Os 11 testes de comportamento esperado passaram. Os 3 reprovados são os de validação, e aqui a falha é do site. Contar também a primeira execução de 18/11: 3 testes falharam porque o teste esperava “Product added.” com ponto e o site mostra sem ponto. Era erro do teste, e corrigimos o teste, não o resultado. O print real do terminal está no relatório, Figura 3.

## Slide 9 — 5 defeitos, 4 deles no fluxo de compra

Cada defeito tem passos, esperado, obtido e evidência no relatório, seção 4.1. Os dois de severidade alta envolvem dados de cartão.

## Slide 10 — Um comprovante, três defeitos

Este print foi salvo automaticamente pelo CT13. As marcações laranja aparecem em cima do número do cartão e da data. O teste encontrou o DF02. Analisando o print, o grupo encontrou o DF04 e o DF05. O print do CT14 mostra a mesma data errada e o cartão inteiro, então os dois se repetem.

## Slide 11 — O site funciona com dados certos e falha com dados errados

Ler os três números. A barra mostra a proporção da execução final: 11 aprovados e 3 reprovados. A conclusão: os fluxos principais funcionam, mas o site não se protege de dados incorretos, e o problema se concentra justamente onde tem dinheiro e cartão.

## Slide 12 — Quem é prejudicado

Em um sistema real, quem paga o preço é o consumidor, que tem menos informação para perceber o problema. Responsabilidade: na primeira execução a falha era nossa e corrigimos o teste; nos CT12 a CT14 a falha é do site, e mantivemos os testes falhando, como pede a disciplina.

## Slide 13 — O que evitaria esses defeitos

Cada recomendação responde a um defeito, indicado em verde no topo do cartão. A última é a mais importante para quem testa: o teste automatizado só protege se rodar sempre.

## Slide 14 — Obrigado. Perguntas?

Agradecer e abrir para perguntas. Se perguntarem sobre IA: o uso está declarado no relatório, e o grupo rodou todos os testes, conferiu no site e revisou o texto.
