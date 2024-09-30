'''Crie um programa que cadastre uma lista de tarefas do dia. Ao final, o programa
deve exibir a lista de tarefas. Obs: não ordenar a lista'''

tarefas = []

while True:
    try:
        nova_tarefa = input("Informe uma nova tarefa ou 'Enter' para exibir a lista de tarefas: ")

        if nova_tarefa:
            tarefas.append(nova_tarefa)
            print(f"{nova_tarefa} foi adicionada.")
            continue
        else:
            break
    except Exception as e:
        print("Não foi possível adicionar nova tarefa. {e}.")

for tarefa in tarefas:
    print(tarefa)
