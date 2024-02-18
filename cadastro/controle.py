from PyQt5 import uic,QtWidgets

def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()
    
    print("Código:",linha1)
    print("Descrição:",linha2)
    print("Preço: $",linha3)

    if formulario.radioButton.isChecked() :
        print("Categoria Informatica foi selecionado")
    elif formulario.radioButton_2.isChecked() :
        print("Categoria Alimentos foi selecionado")
    else :
        print("Categoria Eletronicos foi selecionado")


app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()