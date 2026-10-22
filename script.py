import sys

# print(sys.argv)
# sys.argv[1] # nome do arquivo
# sys.argv[2] #caractere a ser alterado
# parm = sys.argv[1]
# print(parm)

arq = open(sys.argv[1], 'r+')
while True:
    c = arq.read(1)
    if c == sys.argv[2]:
        arq.seek(arq.tell()-1)
        arq.write('_')
    elif c == '':
        break