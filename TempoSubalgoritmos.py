# Versão do algoritmo BuscarSolitario.py feita para mostrar os tempos de execução de cada subalgoritmo
import time

def buscarSolitario(vetor, inicio, fim):
    inicio_execucao = time.time()

    if inicio > fim:
        fim_execucao = time.time()
        print(f"Chamada [{inicio}, {fim}] - Retorno -1 - Tempo: {fim_execucao - inicio_execucao:.10f} segundos")
        return -1
    elif inicio == fim:
        fim_execucao = time.time()
        print(f"Chamada [{inicio}, {fim}] - Encontrado: {vetor[inicio]} - Tempo: {fim_execucao - inicio_execucao:.10f} segundos")
        return vetor[inicio]
    else:
        meio = (inicio + fim) // 2
        meio -= meio % 2

        if vetor[meio] == vetor[meio + 1]:
            fim_execucao = time.time()
            print(f"Chamada [{inicio}, {fim}] - Par encontrado ({vetor[meio]}, {vetor[meio + 1]}), indo para [{meio + 2}, {fim}] - Tempo: {fim_execucao - inicio_execucao:.10f} segundos")
            return buscarSolitario(vetor, meio + 2, fim)
        elif vetor[meio] == vetor[meio - 1]:
            fim_execucao = time.time()
            print(f"Chamada [{inicio}, {fim}] - Par encontrado ({vetor[meio - 1]}, {vetor[meio]}), indo para [{inicio}, {meio - 2}] - Tempo: {fim_execucao - inicio_execucao:.10f} segundos")
            return buscarSolitario(vetor, inicio, meio - 2)
        else:
            fim_execucao = time.time()
            print(f"Chamada [{inicio}, {fim}] - Elemento solitário: {vetor[meio]} - Tempo: {fim_execucao - inicio_execucao:.10f} segundos")
            return vetor[meio]

# Vetores de teste
vet1 = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10]
vet2 = [1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10]
vet3 = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,17,17,18,18,19,19,20,20]
vet4 = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18,19,19,20,20,21,21,22,22,23,23,24,24,25,25,26,27,27,28,28,29,29,30,30,31,31,32,32,33,33,34,34,35,35,36,36,37,37,38, 38,39,39,40,40]

# Execuções com marcação de tempo total
print("===== Vetor 1 =====")
time1 = time.time()
elemSolitario1 = buscarSolitario(vet1, 0, len(vet1) - 1)
time11 = time.time()
print(f"Elemento solitário do 1º vetor: {elemSolitario1}")
print(f"Tempo total de execução: {time11 - time1:.10f} segundos\n")

print("===== Vetor 2 =====")
time2 = time.time()
elemSolitario2 = buscarSolitario(vet2, 0, len(vet2) - 1)
time22 = time.time()
print(f"Elemento solitário do 2º vetor: {elemSolitario2}")
print(f"Tempo total de execução: {time22 - time2:.10f} segundos\n")

print("===== Vetor 3 =====")
time3 = time.time()
elemSolitario3 = buscarSolitario(vet3, 0, len(vet3) - 1)
time33 = time.time()
print(f"Elemento solitário do 3º vetor: {elemSolitario3}")
print(f"Tempo total de execução: {time33 - time3:.10f} segundos\n")

print("===== Vetor 4 =====")
time4 = time.time()
elemSolitario4 = buscarSolitario(vet4, 0, len(vet4) - 1)
time44 = time.time()
print(f"Elemento solitário do 4º vetor: {elemSolitario4}")
print(f"Tempo total de execução: {time44 - time4:.10f} segundos\n")

