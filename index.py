import mysql.connector
from mysql.connector import errorcode

pagina=open("index.html", "w")
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
""")

class GerenciadorIndex(App):
    def teste():
        try:
            db_connection = mysql.connector.connect(host='localhost', user='root', password='1234', database='bd')
            print("Conexão com BD ok!")
            db_connection.close()
        except:
            print("Sem conexão com o BD")


pagina.write("""
</body>
</html>
""")
pagina.close()

app = GerenciadorIndex(App)
app.run

