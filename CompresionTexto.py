
string = 'HOLADANIELA'

# CONTAR LAS REPETICIONES DENTRO DE LA CADENA
class ARBOL(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def hijos(self):
        return (self.left, self.right)

    def nodos(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)


def CodigoOrden_huffman(nodo, left=True, binario=''):
    if type(nodo) is str:
        return {nodo: binario}
    (l, r) = nodo.hijos()
    d = dict()
    d.update(CodigoOrden_huffman(l, True, binario + '0'))
    d.update(CodigoOrden_huffman(r, False, binario + '1'))
    return d

#CALCULAR LA CANTIDAD DE REPETICIONES
freq = {}
for c in string:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

nodos = freq

while len(nodos) > 1:
    (key1, c1) = nodos[-1]
    (key2, c2) = nodos[-2]
    nodos = nodos[:-2]
    nodo = ARBOL(key1, key2)
    nodos.append((nodo, c1 + c2))

    nodos = sorted(nodos, key=lambda x: x[1], reverse=True)

codigoHuffman = CodigoOrden_huffman(nodos[0][0])

print(' LETRA|  CODIGO ')
for (letra, frequencia) in freq:
    print(' %-4r |%12s' % (letra, codigoHuffman[letra]))

# %-4r  denotar tabla
# %12s denotar tabla    
            


