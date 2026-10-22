# arq = open('aula.txt', 'r+')
# while True:
#     c = arq.read(1)
#     if c == 'a':
#         arq.seek(arq.tell()-1)
#         arq.write('A')
#     elif c == '':
#         break

# arq.close()

import pickle

l = [10, 5, 7, 9 ,1 ,0]

arq = open('teste.bin',  'wb')

pickle.dump(l, arq)
arq.close()