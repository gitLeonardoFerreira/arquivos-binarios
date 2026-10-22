import pickle
# arq = open('teste.bin', 'rb')
# a = pickle.load(arq)
# arq.close()
# print(a)

nome = 'léo'

def arquivo (obj, string):
    arq = open(string, 'wb')
    pickle.dump(obj, arq )

def recebimento (string):
    arq = open(string, 'rb')
    pickle.load(arq)

arquivo(nome, 'teste.bin')
recebimento('teste.bin')
    
