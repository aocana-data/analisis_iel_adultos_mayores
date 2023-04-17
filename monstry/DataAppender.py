import os
from datetime import datetime
from .modules.export_modules.export_matriz import insercion_data

class DataAppender:
    
    __slots__ = []

    def __init__(self) -> None:
        print("Se ha inicializado el objeto unificador de datasets")

    def __str__(self):
        return f"Appender con {len(self.__slots__)} datasets ingresados en el objeto"

    def dataset_appender(self,*args):

        if len(args) == 0:
            print('\033[93mNo se agregó ningún dataset al objeto')
            return 
        
        try:

            for index,dataset in enumerate(args):
                appender_data_set = {
                    'nombre':dataset.nombre_tabla if dataset.nombre_tabla is not None else f'tabla_desconocida_{index}',
                    'dataset':dataset

                    }
                self.__slots__.append(appender_data_set)
        
            print(f'Se agregaron: \t{len(args)} DataSets')
            
            return
        
        except Exception as e:
            print(e)
        
        return 

    def dataset_remover(self, nombre_dataset:str)->None:

        nombre_dataset = nombre_dataset.strip()

        if nombre_dataset in ['',None]: return

        nombres_disponibles = [dataset.nombre_tabla for dataset in self.__slots__]

        if nombre_dataset not in nombres_disponibles:
            print('El nombre del dataset seleccionado no pertenece a ninguno de los datasets almacenados')
            return 

        self.__slots__ = [dataset for dataset in self.__slots__ if dataset.nombre_tabla != nombre_dataset.strip()] 

        return
    
    def get_preview(self):
        for dataset in self.__slots__:
            dataset.get_resumen()

            
    def data_printer(self, file_name = None):

        BASE_DIR = os.path.dirname(os.path.dirname(__file__))

        folder_name = 'output'
        folder_path = os.path.join(BASE_DIR,folder_name) 

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        file_path = "monstry/modules/export_modules/matriz_evaluacion_calidad_datos.template.xlsx"


        if file_name is None:
            file_output_path = f"matriz_evaluacion.{datetime.today().strftime('%b_%d_%Y')}_output.xlsx"
        else:
            file_output_path = f"{file_name}.xlsx"
        

        template_path = os.path.join(BASE_DIR,file_path)
        output_data = os.path.join(folder_path,file_output_path)

        worksheet_config = {
            'template_wb_matriz' : template_path,
            'sheet' : '2.1 Calidad por Variable',
            'output': output_data,
            'completitud':self.completitud,
            'exactitud':self.exactitud,
            'data_columnas':self.data_columnas(),
            'data_builder': self.builder_config
        }

        try:
            insercion_data(worksheet_config)
        except Exception as e:
            print(e)

        return None