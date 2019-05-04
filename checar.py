import re

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

archivo = 'f1233.3232.3232_SIILv14.3.4.sql'
if not checar(archivo):
    print('nombre incorrecto')
else:
    print('nombre correcto')
