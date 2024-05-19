from conexao import Neo4jConnection

class pessoaCRUD:
    def __init__(self, connection):
        self.connection = connection

    def criar(self, nome, idade):
        query = """
        criar (p:pessoa {nome: $nome, idade: $idade})
        RETURN p
        """
        return self.connection.query(query, parameters={"nome": nome, "idade": idade})

    def ler(self, nome):
        query = """
        comando (p:pessoa {nome: $nome})
        RETURN p
        """
        return self.connection.query(query, parameters={"nome": nome})

    def atualizar(self, nome, nova_idade):
        query = """
        comando (p:pessoa {nome: $nome})
        SET p.idade = $nova_idade
        RETURN p
        """
        return self.connection.query(query, parameters={"nome": nome, "nova_idade": nova_idade})

    def deletar(self, nome):
        query = """
        comando (p:pessoa {nome: $nome})
        DELETE p
        """
        return self.connection.query(query, parameters={"nome": nome})

def print_menu():
    print("\nEscolha uma opção:")
    print("1. Criar uma pessoa")
    print("2. Ler uma pessoa")
    print("3. Atualizar uma pessoa")
    print("4. Deletar uma pessoa")
    print("5. Sair")

def main():
    # Conectar ao Neo4j
    conn = Neo4jConnection(url="bolt://localhost:7687", user="neo4j", password="celso123")
    pessoa_crud = pessoaCRUD(conn)

    while True:
        print_menu()
        choice = input("Digite o número da opção desejada: ")

        if choice == '1':
            nome = input("Digite o nome da pessoa: ")
            idade = int(input("Digite a idade da pessoa: "))
            result = pessoa_crud.criar(nome, idade)
            print("Pessoa criada:")
            for record in result:
                print(record)

        elif choice == '2':
            nome = input("Digite o nome da pessoa: ")
            result = pessoa_crud.ler(nome)
            print("Pessoa encontrada:")
            for record in result:
                print(record)

        elif choice == '3':
            nome = input("Digite o nome da pessoa: ")
            nova_idade = int(input("Digite a nova idade da pessoa: "))
            result = pessoa_crud.atualizar(nome, nova_idade)
            print("Pessoa atualizada:")
            for record in result:
                print(record)

        elif choice == '4':
            nome = input("Digite o nome da pessoa: ")
            result = pessoa_crud.deletar(nome)
            print("Pessoa deletada:")
            for record in result:
                print(record)

        elif choice == '5':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

    # Fechar a conexão
    conn.close()

if __name__ == "__main__":
    main()