from estoque import Estoque
from produto import Produto

#Criação de produtos
produto1 = Produto('Bateria', 2, 32, 'eletronico')
produto2 = Produto('Celular', 45, 2500, 'eletronico')
produto3 = Produto('Geladeira', 54, 3000, 'eletrodomestico')

#Criação do estoque
estoque = Estoque()

#Adicionando itens ao estoque
estoque.estocagem(produto1.id, produto1.nome, produto1.preco, produto1.categoria)
print(f"""PRIMEIRA ADIÇÃO\nValor do estoque: {estoque.valor},
Quantidade de produtos: {estoque.quantidade_produtos},
Lista de produtos: {estoque.lista_prod}, 
Lista de preços: {estoque.lista_preco}, 
Lista de categorias: {estoque.lista_categoria}, 
Lista de ID: {estoque.lista_id}\n""")

estoque.estocagem(produto2.id, produto2.nome, produto2.preco, produto2.categoria)
print(f"""SEGUNDA ADIÇÃO
Valor do estoque: {estoque.valor}, 
Quantidade de produtos: {estoque.quantidade_produtos}, 
Lista de produtos: {estoque.lista_prod}, \nLista de preços: {estoque.lista_preco}, 
Lista de categorias: {estoque.lista_categoria}, 
Lista de ID: {estoque.lista_id}\n""")


#retirando item do estoque
estoque.retirada(produto2.id)
print(f"""PRIMEIRA REMOÇÃO
Valor do estoque: {estoque.valor}, 
Quantidade de produtos: {estoque.quantidade_produtos}, 
Lista de produtos: {estoque.lista_prod}, \nLista de preços: {estoque.lista_preco}, 
Lista de categorias: {estoque.lista_categoria}, 
Lista de ID: {estoque.lista_id}\n""")

estoque.retirada('Fogão')

#adicionando item ao estoque
estoque.estocagem(produto3.id, produto3.nome, produto3.preco, produto3.categoria)
print(f'TERCEIRA ADIÇÃO\nValor do estoque: {estoque.valor}, \nQuantidade de produtos: {estoque.quantidade_produtos}, \nLista de produtos: {estoque.lista_prod}, \nLista de preços: {estoque.lista_preco}, \nLista de categorias: {estoque.lista_categoria}, \nLista de ID: {estoque.lista_id}')

estoque.retirada(produto1.id)

estoque.estocagem(1, 'caderno', 30, 'objeto')
estoque.estocagem(1, 'caderno', 30, 'objeto')
estoque.estocagem(80, 'cadeira', 90, 'objeto')
estoque.estocagem(120, 'sofá', 400, 'objeto')

print(estoque.lista_id, estoque.lista_prod, estoque.lista_preco, estoque.lista_categoria)
estoque.principal_categoria()

estoque.desc_valor()