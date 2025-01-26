"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

import pandas as pd
import re

def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requerimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minúsculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.

    """

    def process_line(line):
        return re.sub(r'\s+', ' ', line.strip()).replace('.', '').strip()

    def process_header(headers):
        return [header.lower().replace(" ", "_") for header in headers]

    def process_value(line, current_value):
        split_line = re.split(r'\s{2,}', line)
        if split_line[0].isdigit():
            values.append(current_value[:])
            current_value.clear()
            current_value.extend([
                int(split_line[0]),
                int(split_line[1]),
                float(split_line[2].split()[0].replace(',', '.'))
            ])
            percentage = line.find('%')
            current_value.append(process_line(line[percentage + 1:]))
        else:
            current_value[-1] += " " + process_line(line)

    with open("files/input/clusters_report.txt") as file:
        lines = [line.strip() for line in file.readlines() if "---" not in line]

    header = re.split(r"\s{2,}", lines[0])
    header[1] += " palabras clave"
    header[2] += " palabras clave"

    values = []
    current_value = header

    for line in lines[2:]:
        if line:
            process_value(line, current_value)

    values.append(current_value)
    values[0] = process_header(values[0])

    dataframe = pd.DataFrame(data=values[1:], columns=values[0])
    return dataframe

pregunta_01()


    
