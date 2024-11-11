from pathlib import Path

def proceso_calificaciones(entrada, salida):
    """
    Procesar el archivo con las calificaciones y genera uno
    nuevo con el nombre promedios en el que se muestran los 
    alumnos en el formato: apellido en mayúsculas, nombre: 
    promedio
    """
    archivo_entrada = Path(entrada)
    archivo_salida = Path(salida)

    with open(archivo_entrada,"r", encoding="utf8") as f_in:
        with open(archivo_salida, "w", encoding="utf8") as f_out:
            for linea in f_in:
                elementos = linea.strip().split()
                nombre = elementos [0]
                apellido = elementos [1]
                calificaciones = []
                for calificacion in elementos [2:]:
                    calificaciones.append(int(calificacion))
                promedio = sum(calificaciones)/len(calificaciones)
                promedio_decimal = round(promedio,1)

                formato = f"{apellido.upper()}, {nombre}: {promedio_decimal}\n"

                f_out.write(formato)

entrada = "data/calificaciones.txt"
salida = "data/promedios.txt"
proceso_calificaciones(entrada, salida)
           




