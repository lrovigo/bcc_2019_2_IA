## Sobre a implementação:
Os itens do trabalho foram implementados utilizando:
- `Python 3.7.4`
- A execução foi realizada através da biblioteca ´Matplotlib´
- Sistema operacional `Windows 10`

Foi implementado um ´Agente Reativo Simples´ de um aspirador o qual irá andar por um caminho de uma matriz 4x4 procurando por 
sujeiras, ao encontra-las irá executar a ação aspirar para remover a sujeira da matriz.

Também foi implementado um ´Agente Baseado em Objetivo´ do aspirador com o objetivo de remover todas as sujeiras da matriz, esse ao ter todas as sujeiras removidas irá parar de se mover.

# Perguntas
## A sua solução é extensível para um mundo 3 x 3? E para um mundo 6 x 6? Explique sua resposta

Sim, ao alterar o tamanho da matriz o aspirador sempre andara onde não possuir paredes variando até onde ele pode ir levando em consideração o tamanho da matriz.


## É possível ter todo o espaço limpo efetivamente? Justifique sua resposta.

Sim, pois foi implementado algoritmo com base no problema do carteiro chinês onde sempre será calculado o melhor caminho antes do aspirador começar a se mover.
