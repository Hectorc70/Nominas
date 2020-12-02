from concentrado.modulos.archivos_excel import ArchivoExcel



class ArchivoRecalculo(ArchivoExcel):

    def __init__(self, archivo):
        self.archivo = archivo
        self.columnas_necesarias = ['PERIODO','AÑO','No. CONTROL',
                                    'IMPORTE RECALCULO',
                                    'IMPORTE RECALCULO CON REDONDEO']
        ArchivoExcel.__init__(self, self.archivo)

        
    def ejecutar(self):
        archivo_datos = dict()
        
        for nombre in self.hojas[0].keys():          
            datos = self.extraer_datos(nombre)
            archivo_datos[nombre] = datos
        
        return archivo_datos


    def extraer_datos(self, hoja_lectura):
        """Recupera los datos del archivo
        de recalculo por columna de la str(hoja) pasada como parametro.
        
        
        Retorna: dict{'nombre_columna': list(datos_columna)}"""
        
        datos = list()
        self.leer_titulos(hoja_lectura, 1)
        
        columna_lectura1 = self.claves_columnas[self.columnas_necesarias[0]]
        columna_lectura2 = self.claves_columnas[self.columnas_necesarias[1]]
        columna_lectura3 = self.claves_columnas[self.columnas_necesarias[2]]
        columna_lectura4= self.claves_columnas[self.columnas_necesarias[3]]
        columna_lectura5 = self.claves_columnas[self.columnas_necesarias[4]]

        periodo = self.hojas[0][hoja_lectura][columna_lectura1] 
        anno = self.hojas[0][hoja_lectura][columna_lectura2] 
        control = self.hojas[0][hoja_lectura][columna_lectura3] 
        importe = self.hojas[0][hoja_lectura][columna_lectura4] 
        importe_redon = self.hojas[0][hoja_lectura][columna_lectura5] 
        
        for datos1, datos2,datos3,datos4, datos5 in zip(range(1, len(periodo)),range(1, len(anno)),
                                                range(1, len(control)), range(1, len(importe)),
                                                range(1, len(importe_redon))):                                   
            
            periodo_datos = [periodo[datos1].value][0]
            anno_datos = [anno[datos2].value][0]
            control_datos = [control[datos3].value][0]
            importe_datos = [importe[datos4].value][0]
            importe_redon_datos = [importe_redon[datos5].value][0]


            datos.append([periodo_datos, anno_datos,control_datos, 
                        importe_datos, importe_redon_datos])   
        
        return datos
