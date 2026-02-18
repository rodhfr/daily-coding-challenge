# author: Rodolfo Franca de Souza
# mail: souzafrodolfo@gmail.com
# date: 2026-02-16
# license: GPLv3
# topics: arrays
# difficulty: medium
#

import math


arr = [1, 2, 3, 4, 5]

# cada elemento na nova array tem que ser produto de todos os numeros
# da array original menos o index do i atual.
# [3,2,1] to [2,3,6]

# o que quero fazer
# quero pegar a nova lista sem o index e ai eu
# reduzo ela na multiplicacao

# excluir o index da lista
# reduce com a multiplicacao de tds os outros

res = list()

tmp_arr = arr

for i in range(len(arr)):
    tmp_arr = arr[:]
    print(i)
    del tmp_arr[i]
    print(tmp_arr)
    res.append(math.prod(tmp_arr))

print(res)
