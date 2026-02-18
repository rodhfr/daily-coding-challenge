# author: Rodolfo Franca de Souza
# mail: souzafrodolfo@gmail.com
# date: 2026-02-17
# license: GPLv3
# topics: trees, recursion
# difficulty: medium
#
# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

# For example, given the following Node class
#
# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# The following test should pass:
#
# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'


# serialize:
# converter a estrutura inteira da árvore (valores + forma) em um texto linear, de modo que essa string contenha informação suficiente para reconstruir exatamente a mesma árvore depois.
# Pre order algorithm with null markers "#":
# “Sempre vou o mais fundo possível pra esquerda.
#  Quando não dá mais, marco #.
#  Quando termina um nó, volto.”
#
# deserializes:
# converter o texto linear em uma binary tree


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursão é quando uma função chama ela mesma.
# A função sabe resolver um pedaço pequeno do problema
# e pede ajuda para resolver o resto.
# Visao de pilha:
# f(2)
#  └─ f(1)
#      └─ f(0)
#      ↑
#  └─↑
# ↑
# Ele nunca “volta” para a função.
# Ele já estava lá o tempo todo, só estava pausado esperando as chamadas filhas terminarem.
# f(2)  ← pausada aqui
#  └─ f(1) ← pausada aqui
#      └─ f(0) ← executando


def serialize(node):
    if node is None:
        return "#"
    return str(node.val) + " " + serialize(node.left) + " " + serialize(node.right)


## Para a arvore:
#    [1]
#   /   \
# [2]   [3]

## Stack view:
# serialize(1)  ← pausado
#  └─ serialize(2) ← pausado
#      └─ serialize(None) ← termina
#      └─ serialize(None) ← termina
#      └─ retorna "2 # #"
#  └─ serialize(3) ← pausado
#      └─ serialize(None)
#      └─ serialize(None)
#      └─ retorna "3 # #"
# retorna "1 2 # # 3 # #"

# Exemplo executando
left = Node(2)
right = Node(3)
root = Node(1, left, right)
print(serialize(root))  # Output: 1 2 # # 3 # #
