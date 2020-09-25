import mysql.connector
from mysql.connector import errorcode
from daatetima import date


informacao = ''
datacolheita = 0
peso = 0
arvore = ''

pagina=open("colheita.html", "w")
pagina.write("""
<html lang=\"pt-BR\">
<head>
<title>Gerenciador do pomar </title>
</head>
<body>
<body>
    <ul>
        <li> <a href="cadastro.html">CADASTRO</a> </li>
        <li> <a href="colheita.html">COLHEITA</a></li>
        <li> <a href="relatorio.html">RELATÓRIO</a> </li> 
    </ul> 
    <section>
        <h1> Colheita: </h1>
        <form name="form-colheita" method="POST" action="atualizacolheita">
        
        <label for="informacaoes"><strong>Informações*</strong></label>
        <input type="text" name="informacoes" required placeholder="Digite a informação"> <br>
        
        <label for="datacolheita"><strong>Data da colheita*</strong></label>
        <input type="text" name="datacolheita" required placeholder="Digite a data"> <br>
        
        <label for="peso"><strong>Peso*</strong></label>
        <input type="text" name="peso" required placeholder="Digite o peso de árvore"> <br>
        
        <label for="arvore"><strong>Árvore*</strong></label>
        <input type="text" name="arvore" required placeholder="Digite o tipo de árvore"> <br>

        <input type="submit" value="ENVIAR">
        </form>
    </section>
""")

class GerenciadorColheita(App):
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
            
    def atualizarcolheita()
        db_connection = mysql.connector.connect(host="localhost", user="root", passwd="1234", database="bd")
        cursor = db_connection.cursor()
        sql = ("UPDATE informacao, datacolheita, peso, arvore  FROM arvore")
        cursor.execute(sql)  
        cursor.close()
        db_connection.commit()
        db_connection.close()

pagina.write("""
</body>
</html>
""")
pagina.close()

app = GerenciadorColheita(App)
app.run
