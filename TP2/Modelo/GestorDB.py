import psycopg2
'''
De momento creare aqui funciones para dar valor a ciertas columnas
'''

#1 Conexion DB
conn = psycopg2.connect("dbname=tp1_p3_paradigmas_db user=postgres password=matecocido")

#Funcion para calcular precios totales &set                      %(variable)s para utilizar variables 
def set_preciototal(id):

    cur = conn.cursor()

    cur.execute('''SELECT ubicacion 
        FROM lotes 
        WHERE id = %(id)s ''', {'id':id})
    ubicacion=cur.fetchone()[0]
    print(ubicacion)

    cur.execute('''SELECT factor 
        FROM factor_ubicaciones
        WHERE ubicacion =%(ubicacion)s ''',{'ubicacion':ubicacion})
    #print(cur.fetchall())
    factor=cur.fetchone()[0]
    print(factor)

    cur.execute('''SELECT medida_m2 
        FROM lotes 
        WHERE id = %(id)s ''', {'id':id})
    medida=cur.fetchone()[0]
    print(medida)

    cur.execute(''' 
    UPDATE lotes
    SET precio_total = %(factor)s * %(medida)s
    WHERE id=%(id)s
    ''',{'id':id,'factor':factor,'medida':medida})

    conn.commit()
    cur.close()

#Funcion para calcular anticipos &set 
def set_anticipo(id):

    cur = conn.cursor()
    
    cur.execute('''SELECT precio_total 
        FROM lotes 
        WHERE id = %(id)s ''', {'id':id})
    precio_total=cur.fetchone()[0]
    
    cur.execute(''' 
    UPDATE lotes
    SET precio_anticipo = %(precio_total)s *0.1
    WHERE id=%(id)s
    ''',{'id':id,'precio_total':precio_total})

    conn.commit()
    cur.close()


def get_all_lotes():

    cur=conn.cursor()
    
    cur.execute('SELECT * FROM lotes')
    DB=cur.fetchall()
    cur.close()

    return DB

def get_column_names():
    columns=[]
    cur=conn.cursor()    
    cur.execute('SELECT * FROM lotes')
    for columna in cur.description:
        columns.append(columna.name)
    return(columns)

def get_id_m2_ubic_precio_estado_duenio():

    cur=conn.cursor()
    cur.execute('''SELECT id,
        medida_m2,
        ubicacion,
        precio_total,
        estado,
        duenio_dni 
    FROM lotes''')
    return(cur.fetchall())
#set_preciototal(2)
#set_anticipo(2)
#get_all_lotes()
#columns=get_column_names()

