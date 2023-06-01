class Prueba:
    def __init__(self,letra):
        self._letra=letra


obj=Prueba("ABCDE")
print(obj._letra)

obj._letra= "ccc"
print(obj._letra)


'''
En Python, la falta de atributos privados estrictos puede plantear algunos desafíos en cuanto a la encapsulación y la confianza en el acceso adecuado a los atributos. 
Sin embargo, hay algunas consideraciones a tener en cuenta:

1) Convención: En Python, la convención es utilizar un guion bajo (_) como prefijo en el nombre de los atributos para indicar que son considerados privados. 
Esto es ampliamente aceptado por los desarrolladores de Python y sirve como una señal para indicar que los atributos no deben ser accedidos directamente desde fuera de la clase.
 Seguir esta convención y confiar en la responsabilidad de los desarrolladores es esencial para mantener una buena práctica de programación.

2) Documentación: Es importante documentar adecuadamente las clases y los atributos, incluyendo información sobre el acceso y la manipulación de los mismos. 
Esto ayuda a los desarrolladores que utilizan la clase a comprender cómo deben interactuar con los atributos y qué comportamiento esperar.

3) Métodos de acceso: En lugar de acceder directamente a los atributos, se pueden proporcionar métodos de acceso (getters) y métodos de modificación (setters) para manipular los atributos.
 Esto permite un mejor control y validación de los valores asignados a los atributos, y también facilita la encapsulación y el mantenimiento del código.

4) Herencia y subclases: Aunque los atributos "privados" no están completamente protegidos en Python, el uso del doble guion bajo (__atributo) puede generar un "name mangling" 
que cambia el nombre del atributo para evitar colisiones con atributos en subclases. Esto proporciona una cierta medida de protección y evita conflictos de nombres.

En resumen, aunque no hay atributos privados estrictos en Python, siguiendo las convenciones de nomenclatura, 
documentando adecuadamente los atributos, proporcionando métodos de acceso y confiando en la responsabilidad de los desarrolladores, se puede lograr una encapsulación efectiva y mantener una buena práctica de programación en Python.



'''