import mysql.connector
from mysql.connector import errorcode
from daatetima import date

codigo = 0
descricao = ''
idade = 0
especie = ''
nome = ''
arvore = ''
informacao = ''
peso = 0

pagina=open("cadastro.html", "w")
pagina.write("""
<html lang=\"pt-BR\">
<head>
<title>Gerenciador do pomar </title>
</head>
<body>
    <ul>
        <li> <a href="cadastro.html">CADASTRO</a> </li>
        <li> <a href="colheita.html">COLHEITA</a></li>
        <li> <a href="relatorio.html">RELATÓRIO</a> </li> 
    </ul>  
    <section>
        <h1> Cadastro: </h1>
        <form name="form-cadastro" method="POST" action="inserirproduto">
        
        <label for="codigo"><strong>Código*</strong></label>
        <input type="text" name="codigo" required placeholder="Digite o código de árvore"> <br>
        
        <label for="descricao"><strong>Descrição*</strong></label>
        <input type="text" name="descricao" required placeholder="Digite a descrição"> <br>
        
        <label for="idade"><strong>Idade*</strong></label>
        <input type="text" name="idade" required placeholder="Digite a idade"> <br>
        
        <label for="especie"><strong>Espécie*</strong></label>
        <input type="text" name="especie" required placeholder="Digite a espécie"> <br>
        
        <label for="nome"><strong>Nome*</strong></label>
        <input type="text" name="nome" required placeholder="Digite o nome da árvore"> <br>
        
        <label for="arvore"><strong>Árvore*</strong></label>
        <input type="text" name="arvore" required placeholder="Digite o tipo de árvore"> <br>
        
        <label for="informacaoes"><strong>Informações*</strong></label>
        <input type="text" name="informacoes" required placeholder="Digite a informação"> <br>
        
        <label for="peso"><strong>Peso*</strong></label>
        <input type="text" name="peso" required placeholder="Digite o peso de árvore"> <br>
        
        <input type="submit" value="ENVIAR">
        </form>
    </section>
""")

class GerenciadorCadastro(App):
    def conexaobd()
        try:
                db_connection = mysql.connector.connect(host='localhost', user='root', password='1234', database='bd')
                print("Conexao OK!")
        except mysql.connector.Error as error:
                if error.errno == errorcode.ER_BAD_DB_ERROR:
                        print("Database não existe")
                        pagina.write("<p>BD não existe</p>\n" % l)
                elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                        print("Usuario ou senha invalido)
                        pagina.write("<p>Usuario ou senha invalida</p>\n" % l)
                else:
                        print(error)
                        pagina.write("<p>Falha na conexão com o BD</p>\n" % l)
        else:
                db_connection.close()
            
    def inserirproduto()
        db_connection = mysql.connector.connect(host="localhost", user="root", passwd="1234", database="bd")
        cursor = db_connection.cursor()
        sql = "INSERT INTO arvore (codigo, descricao, idade, especie, nome, arvore, informacao, peso) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (codigo, descricao, idade, especie, nome, arvore, informacao, peso)
        cursor.execute(sql, values)
        current_date = date.today()
        formatted_date = current_data.strftime('%d/%m/%Y')
        db_connection.commit()
        db_connection.close()
    
pagina.write("""
</body>
</html>
""")
pagina.close()

app = GerenciadorCadastro(App)
app.run
