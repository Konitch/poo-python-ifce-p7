"""
    Módulo notafiscal -
    Classe NotaFiscal -
        Atributos :
            id        - informado.
            codigo    - informado.
            data      - informado.
            cliente   - informado.
            items     - informado
            valornota - calculado.
"""
from datetime import *
from cliente import Cliente
from produto import Produto
from itemnotafiscal import ItemNotaFiscal


class NotaFiscal():
    def __init__(self, Id, codigo, cliente):
        self._Id = Id
        self._codigo = codigo
        self._cliente = cliente
        self._data = datetime.now()
        self._itens = []
        self._valorNota = 0.0

    def setCliente(self, cliente):
        if isinstance(cliente, Cliente):
            self._cliente = cliente

    def adicionarItem(self, item):
        if isinstance(item, ItemNotaFiscal):
            self._itens.append(item)

    def calcularNotaFiscal(self):
        valor = 0.0
        for item in self._itens:
            valor = valor + item._valorItem
        self.valorNota = valor

    def imprimirNotaFiscal(self):
        print("--------------------------------------------------------------------")
        print("NOTA FISCAL                                                ", self._data.strftime("%d/%m/%y"))
        print("Cliente: ", self._cliente._codigo,"   Nome: ", self._cliente._nome)
        print("CPF / CNPJ: ", self._cliente._cnpjcpf)
        print("--------------------------------------------------------------------")
        print("ITENS")
        print("--------------------------------------------------------------------")
        print("Seq          Descrição           QTD       Valor Unit       Preço")
        print("------- -------------------- ----------- ---------------- ---------- ")
        for item in self._itens:
            print('%03.3d' % item._id, "    ", '%17.32s' % item._descricao, '%8.2s' % item._quantidade, "           ", item._valorUnitario, "          ", item._valorItem)
        pass
