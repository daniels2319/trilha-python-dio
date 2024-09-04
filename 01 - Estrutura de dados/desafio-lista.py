# First challenge below
"""
import statistics

def analise_vendas(vendas):
    # TODO: Calcule o total de vendas e realize a média mensal:
    total_vendas = sum(vendas)
    media_vendas = statistics.mean(vendas)

    return f"{total_vendas}, {media_vendas:.2f}"

def obter_entrada_vendas():
    # Solicita a entrada do usuário em uma única linha
    entrada = input()
    entrada = entrada.split(',')

    # TODO: Converta a entrada em uma lista de inteiros:
    vendas = list(map(int, entrada))

    return vendas

vendas = obter_entrada_vendas()
print(analise_vendas(vendas))
"""

"""
# Second challenge below
def produto_mais_vendido(produtos):
    contagem = {}
    
    for produto in produtos:
        produto = produto.strip()
        if produto in contagem:
            contagem[produto] += 1
        else:
            contagem[produto] = 1
    
    max_produto = None
    max_count = 0
    
    # for produto, count in contagem.items():
    #     # TODO: Encontre o produto com a maior contagem:
    max_count = max(contagem.values())
    max_produto = {i for i in contagem if contagem[i]==max_count}
    max_produto = list(max_produto)[0].strip()
        
    return max_produto

def obter_entrada_produtos():
    # Solicita a entrada do usuário em uma única linha
    entrada = input()
    # TODO: Converta a entrada em uma lista de strings, removendo espaços extras:
    produtos = entrada.split(',')
    # produtos = produtos.strip()
    produtos = list(map(str, produtos))

    return produtos

produtos = obter_entrada_produtos()
print(produto_mais_vendido(produtos))
# print(produtos)
"""