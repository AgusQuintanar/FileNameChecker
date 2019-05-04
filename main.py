#-*- coding:utf-8 -*-
import os
import re

path = '/Users/agusquintanar/Desktop/Grupo Luthe/'

resultado = open('README.md','w',encoding='utf-8')

def encontrarRepositorios(path):
    repositorios = []
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            files.append(os.path.join(r, file))

    for f in files:
        arcDir = f.replace(path,"")
        repositorio = arcDir.split("/")[0]
        if repositorio not in repositorios and "." not in repositorio:
            repositorios.append(repositorio)

    return repositorios

def checar(archivo):
   nombresCorrectos = [
        ['AutorizacionProyecto_Cliente_Proyecto_v','.docx',r"((\*)|([0-9]+(\.((\*)|([0-9]+(\.((\*)|([0-9]+)))?)))?))"],
        ['SolicitudCambio_Caso_Cliente_v','.docx',r"((\*)|([0-9]+(\.((\*)|([0-9]+(\.((\*)|([0-9]+)))?)))?))"],
        ['CM_ElementosEnConfiguración_Cliente_Proyecto','.xlsx',""],
        ['PP_Plan_Cliente_Proyecto_v','.xlsx',r"((\*)|([0-9]+(\.((\*)|([0-9]+(\.((\*)|([0-9]+)))?)))?))"],
        ['PlanCliente_Cliente_Proyecto_v','.docx',r"((\*)|([0-9]+(\.((\*)|([0-9]+(\.((\*)|([0-9]+)))?)))?))"],
        ['PlanCliente_Cliente_Proyecto_v','.pdf',r"((\*)|([0-9]+(\.((\*)|([0-9]+(\.((\*)|([0-9]+)))?)))?))"],
        ['LB_Planeacion_v','.zip',r"((\*)|([0-9]+(\.((\*)|([0-9]+(\.((\*)|([0-9]+)))?)))?))"],
        ['Analisis_Cliente_Proyecto_v','.docx',r"((\*)|([0-9]+(\.((\*)|([0-9]+(\.((\*)|([0-9]+)))?)))?))"],
        ['Analisis_Cliente_Proyecto_v','.pdf',r"((\*)|([0-9]+(\.((\*)|([0-9]+(\.((\*)|([0-9]+)))?)))?))"],
        ['LB_Analisis_v','.zip',r"((\*)|([0-9]+(\.((\*)|([0-9]+(\.((\*)|([0-9]+)))?)))?))"],
        ['Diseño_Cliente_Proyecto_v','.docx',r"((\*)|([0-9]+(\.((\*)|([0-9]+(\.((\*)|([0-9]+)))?)))?))"],
        ['APEX5_EstandaresV','.docx',r"((\*)|([0-9]+(\.((\*)|([0-9]+(\.((\*)|([0-9]+)))?)))?))"],
        ['Pruebas_Caso_v','.xlsx',r"((\*)|([0-9]+(\.((\*)|([0-9]+(\.((\*)|([0-9]+)))?)))?))"],
        ['Actualizar_Implantar_Cliente_','.xlsx',r"([12]\d{3}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01]))"],
        ['f','_SIILv','.sql',r"((\*)|([0-9]+(\.((\*)|([0-9]+(\.((\*)|([0-9]+)))?)))?))",r"((\*)|([0-9]+(\.((\*)|([0-9]+(\.((\*)|([0-9]+)))?)))?))"],
        ['Entrega_Cliente_Proyecto_v','.docx',r"((\*)|([0-9]+(\.((\*)|([0-9]+(\.((\*)|([0-9]+)))?)))?))"],
        ['LB_Entrega_v','.zip',r"((\*)|([0-9]+(\.((\*)|([0-9]+(\.((\*)|([0-9]+)))?)))?))"]
    ]

    for y in range(len(nombresCorrectos)):
        nombreArchivo = ''
        for x in range(len(nombresCorrectos[y])//2):
            nombreArchivo += nombresCorrectos[y][x]
            nombreArchivo += nombresCorrectos[y][len(nombresCorrectos[y])//2+1+x] 
        nombreArchivo += nombresCorrectos[y][len(nombresCorrectos[y])//2]
     
        if re.compile(nombreArchivo).match(archivo):
            return True
    return False

def generarArchivoSalida(repositorios,path):
    resultado.write('# Resultados de la prueba\n')

    for repositorio in repositorios:
        resultado.write('### Repositorio: '+repositorio+'\n')
        resultado.write('Archivos con nombre incorrecto | Ruta\n')
        resultado.write('--- | ---\n')

        rutaRepositorio = path+repositorio
        archivos = []
        rutas = []
        for r, d, f in os.walk(rutaRepositorio):
            for file in f:
                if '.' in file and not checar(file):
                    archivos.append(file)
                    rutas.append(os.path.join(r, file))

        for f in range(len(archivos)):
            resultado.write(archivos[f]+'|'+rutas[f].replace(path,"") +'\n')

        resultado.write('---\n')


generarArchivoSalida(encontrarRepositorios(path),path)

