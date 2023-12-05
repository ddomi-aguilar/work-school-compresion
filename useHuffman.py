from huffman import HuffmanCoding
import sys

op = int(input("¿QUIERES COMPRIMIR O DESCOPRIMIR? \n 1)COMPRIMIR \n 2)DESCOMPRIMIR ->>"))


if op ==1:
    
    path=input("¿QUE ARCHIVO QUIERES COMPRIMIR?->> ")#"sample.txt"
    h = HuffmanCoding(path)
    output_path = h.compress()
    print("Compressed file path: " + output_path)
    
    
if op==2:    
    path=input("¿QUE ARCHIVO QUIERES DESCOMPRIMIR?->> ")#"sample.txt"
    h = HuffmanCoding(path)
    decom_path = h.decompress(output_path)
    print("Decompressed file path: " + decom_path)