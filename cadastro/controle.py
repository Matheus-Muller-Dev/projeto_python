# Importa os módulos necessários do PyQt5
from PyQt5 import uic,QtWidgets
import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="cadastro_produtos"
)


# Define a função principal do programa
def funcao_principal():
    # Obtém o texto das três linhas de entrada do formulário
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()
    
    categoria = ""

     # Verifica qual botão de rádio está marcado e imprime a categoria correspondente
    if formulario.radioButton.isChecked() :
        print("Categoria Informatica foi selecionado")
        categoria = "Informatica"
    elif formulario.radioButton_2.isChecked() :
        print("Categoria Alimentos foi selecionado")
        categoria = "Alimentos"
    else :
        print("Categoria Eletronicos foi selecionado")
        categoria = "Eletronicos"

    # Imprime as informações coletadas
    print("Código:",linha1)
    print("Descrição:",linha2)
    print("Preço: $",linha3)

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO produtos (codigo,descricao,preco,categoria) VALUES (%s,%s,%s,%s)"
    dados = (str(linha1), str(linha2), str(linha3), categoria)
    cursor.execute(comando_SQL,dados)
    banco.commit()

# Cria uma instância de aplicação QtWidgets QApplication
app = QtWidgets.QApplication([])

# Carrega o arquivo de interface de usuário (.ui) criado no Qt Designer
formulario = uic.loadUi("formulario.ui")

# Conecta o clique do botão 'pushButton' à função principal 'funcao_principal'
formulario.pushButton.clicked.connect(funcao_principal)

# Exibe o formulário na tela
formulario.show()

# Inicia o loop principal do aplicativo
app.exec()









# criando a tabela

    # """ create table produtos (
    #     id INT NOT NULL AUTO_INCREMENT,
    #     codigo INT,
    #     descricao VARCHAR(50),
    #     preco DOUBLE,
    #     categoria VARCHAR(20),
    #     PRIMARY KEY (id)
    # ); """

# inserindo registro na tabela

# INSERT INTO produtos (codigo,descricao,preco,categoria) VALUES (123,"impresora",500.00"informatica");