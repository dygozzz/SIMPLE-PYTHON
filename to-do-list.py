class ToDoList:
    def __init__(self):
        self.tasks = []

    def adicionar_tarefa(self, tarefa):
        self.tasks.append(tarefa)

    def remover_tarefa(self, tarefa):
        if tarefa in self.tasks:
            self.tasks.remove(tarefa)
        else:
            print("Tarefa não encontrada na lista.")

    def listar_tarefas(self):
        if self.tasks:
            print("Tarefas:")
            for i, tarefa in enumerate(self.tasks, 1):
                print(f"{i}. {tarefa}")
        else:
            print("Nenhuma tarefa na lista.")

lista_de_tarefas = ToDoList()

while True:
    print("\nOpções:")
    print("1. Adicionar Tarefa")
    print("2. Remover Tarefa")
    print("3. Listar Tarefas")
    print("4. Sair")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == "1":
        tarefa = input("Digite a tarefa a ser adicionada: ")
        lista_de_tarefas.adicionar_tarefa(tarefa)
    elif escolha == "2":
        tarefa = input("Digite a tarefa a ser removida: ")
        lista_de_tarefas.remover_tarefa(tarefa)
    elif escolha == "3":
        lista_de_tarefas.listar_tarefas()
    elif escolha == "4":
        break
    else:
        print("Escolha inválida. Tente novamente.")
