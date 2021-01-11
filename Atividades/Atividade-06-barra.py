import matplotlib.pyplot as plt
import csv

arquivo = r'C:\Users\Levi\Documents\IFCE\Programação Orientada a Objetos\poo-python-ifce-p7\Atividades\tabela-06.csv'
funcionarios = []
faltas = []

with open(arquivo) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    count = 0
    for row in csv_reader:
            funcionarios.append(f'{row[0]}')
            faltas.append(int(f'{row[1]}'))

plt.bar(funcionarios, faltas)

plt.title('Relação de Faltas dos Funcionários no Mês')
plt.xlabel('Funcionários')
plt.ylabel('Faltas/Mês')

plt.show()