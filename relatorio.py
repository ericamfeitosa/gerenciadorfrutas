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
datacolheita = 0
peso = 0
arvore = ''

pagina=open("relatorio.html", "w")
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
        <h1> Relatorio da colheita: </h1>
        <form name="form-relatori" method="POST" action="atualizacolheita">
        <label for="filtro"><strong>Filtrar por*</strong></label>
        <select name="Assunto">
          <option value="especie">Espécie</option>
          <option value="arvore" selected>Árvore</option>
          <option value="periodo" selected>Período</option>

        <input type="submit" value="ENVIAR">
        </form>
    </section>
""")

class GerenciadorRelatorio(App):
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
        sql = ("SELECT codigo, descricao, idade, especie, nome, arvore, informacao, datacolheita, peso  FROM arvore")
        cursor.execute(sql)

        for (id, datacolheita, especie, grupo) in cursor:
            print(id, datacolheita, especie, grupo)
            pagina.write("<p>%codigo[]</p>\n" % l)
            pagina.write("<p>%descricao[]</p>\n" % l)
            pagina.write("<p>%idade[]</p>\n" % l)
            pagina.write("<p>%especie[]</p>\n" % l)
            pagina.write("<p>%nome[]</p>\n" % l)
            pagina.write("<p>%arvore[]</p>\n" % l)
            pagina.write("<p>%informacao[]</p>\n" % l)
            pagina.write("<p>%datacolheita[]</p>\n" % l)
            pagina.write("<p>%peso[]</p>\n" % l)
        cursor.close()
        db_connection.commit()
        db_connection.close()
        x
pagina.write("""
</body>
</html>
""")
pagina.close()

app = GerenciadorRelatorio(App)
app.run
