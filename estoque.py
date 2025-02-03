class Estoque:
    def __init__(self):
        self.valor = 0
        self.quantidade_produtos = 0
        self.lista_prod = []
        self.lista_preco = []
        self.lista_categoria = []
        self.lista_id = []

    def estocagem(self, id, produto, valor, categoria):
        if id not in self.lista_id:
            self.valor += valor
            self.quantidade_produtos += 1
            self.lista_id.append(id)
            self.lista_prod.append(produto)
            self.lista_preco.append(valor)
            self.lista_categoria.append(categoria)
        else:
            print('Produjo já adicionado')

    def retirada(self, id):
        if id in self.lista_id:
            self.valor -= self.lista_preco[self.lista_id.index(id)]
            self.quantidade_produtos -= 1
            self.lista_preco.remove(self.lista_preco[self.lista_id.index(id)])
            self.lista_categoria.remove(self.lista_categoria[self.lista_id.index(id)])
            self.lista_prod.remove(self.lista_prod[self.lista_id.index(id)])
            self.lista_id.remove(id)
        else:
            print('Produto não disponivel\n')

    def principal_categoria(self):
        principal = ''
        q_a = self.lista_categoria.count(self.lista_categoria[0])
        for item in self.lista_categoria:
            q = self.lista_categoria.count(item)
            if q > q_a:
                q_a = q
                principal = item
        if principal == '':
            print('Não há nenhuma categoria principal', self.lista_categoria)
            return
        print(principal)

    def desc_valor(self, maximo=True):
        if maximo == True:
            print(max(self.lista_preco))
        else:
            print(min(self.lista_preco))

