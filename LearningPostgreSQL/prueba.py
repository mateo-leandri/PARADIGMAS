import psycopg2

conn = psycopg2.connect("dbname=prueba1_db user=postgres password=matecocido")

cur = conn.cursor()


#CREANDO TABLA 
cur.execute(""" CREATE TABLE IF NOT EXISTS mi_tabla (
    id SERIAL,
    nombre VARCHAR(60) NOT NULL,
    edad SMALLINT NOT NULL,
    correo VARCHAR(150) 
    );
    """)

#INSERTANDO DATOS - %s por cuestiones de seguridad
try:
    query=("INSERT INTO mi_tabla (nombre,edad,correo) VALUES(%s,%s,%s);")
    param=("Pedro",22,"elbiko28@pepe.com")
    cur.execute(query,param)
    conn.commit()

except psycopg2.Error as e:
    print("ALARMMMM " , e )


#VISUALIZANDO DATOS 

try:
    cur.execute("SELECT * FROM mi_tabla;")
    lista=cur.fetchall()
    for rows in lista:
        print(rows)

except psycopg2.Error as e:
    print("ALARMMMM " , e )



# CERRAR EL CURSOR Y LA CONEXION
finally:
    cur.close()
    conn.close()




