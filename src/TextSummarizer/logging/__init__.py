import os #permite interactuar con sistema operativo
import sys #Manejamos recursos del sistema
import logging #para configurar y usar registros del sistema

logging_srt = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]" #Define como se veran los mensajes registrados
#creamos el directorio de los registros,si no esta lo cremaos
log_dir= "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True) #no nos dara erros siesque ya esta creado

#ahora procedemos a configurar lel loggin en especifo

logging.basicConfig(
    level = logging.INFO, #nivel minimo del mensaje
    format = logging_srt, #formato del registro

    #donde se registran los mensajes
    handlers = [
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout) #imprime los registros de la salida estandar
    ]

)
logger = logging.getLogger("textSummarizerLogger") #utilizamos para registrar los mensajes