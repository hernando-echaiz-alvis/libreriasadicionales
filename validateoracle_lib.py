import cx_Oracle
import os
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
import json
from s3_lib import readAndWriteS3
import params_lib as pl

def leer_configuracion():
    ruta_parametros = "./config/ParametrosIngesta.json"
    with open(ruta_parametros) as f:
        try:
            parametrosIngesta = json.load(f)
        except IOError as e:
            e = ("El archivo de configuración no puede ser leido.")
            raise Exception(e)
    return parametrosIngesta

# Prepara nombre del dataset
def prepara_nombre(parametrosIngesta, nombreArchivoParametro, periodoEjecutado, rutaArchivoParametro, extensionParametro):
    nombreArchivoParametro = pl.validar_parametros(
        nombreArchivoParametro, "El parametro nombreArchivo es obligatorio.")
    nombreArchivo = pl.validar_parametros(
        parametrosIngesta["name"][nombreArchivoParametro], "nombreArchivo no esta definido en el archivo de configuración.")
    periodoEjecutado = pl.validar_parametros(
        periodoEjecutado, "El periodoEjecutado es obligatorio.")
    rutaArchivoParametro = pl.validar_parametros(
        rutaArchivoParametro, "El parametro rutaArchivoParametro es obligatorio.")
    rutaArchivo = pl.validar_parametros(
        parametrosIngesta["paths"][rutaArchivoParametro], "rutaArchivo no esta definido en el archivo de configuración.")
    extensionParametro = pl.validar_parametros(
        extensionParametro, "El parametro extension es obligatorio.")
    extension = pl.validar_parametros(
        parametrosIngesta["paths"][extensionParametro], "extension no esta definido en el archivo de configuración.")
    nombreArchivoPreparado = nombreArchivo + periodoEjecutado + extension
    print(nombreArchivoPreparado)
    rutaArchivoPreparada = os.path.join(rutaArchivo, periodoEjecutado)
    print(rutaArchivoPreparada)
    return rutaArchivoPreparada + '/' + nombreArchivoPreparado

# Cargar data


def prepara_nombre_dataset(periodoEjecutado, parametrosIngesta):
    print("Seteando Parametros Inactividad_Prepago")
    periodoEjecutado = pl.validar_parametros(
        periodoEjecutado, "El parametro periodoEjecutado es obligatorio.")
    return prepara_nombre(parametrosIngesta, "Name_Raw_Data", periodoEjecutado, "Ruta_Raw_Data",  "ExtCSV")


def validateDatabaseTable():
    userName = os.environ.get("oracleUser")
    password = os.environ.get("oraclePwd")
    host = os.environ.get("oracleHostIp")
    port = os.environ.get("oraclePort")
    sid = os.environ.get("oracleDbName")
    tableSchemaName = os.environ.get("oracleSchema")
    tableNamePattern = os.environ.get("oracleTableName")
    valueOfMonth = os.environ.get("monthofProcessValue")
    stringOfMonth = str(valueOfMonth)
    shortMonth = str(stringOfMonth)[2:]
    prevMonthValue = (datetime.strptime(stringOfMonth + "01",
                      "%Y%m%d") + relativedelta(days=-1)).strftime("%Y%m")
    month_2_Value = (datetime.strptime(prevMonthValue + "01",
                     "%Y%m%d") + relativedelta(days=-1)).strftime("%Y%m")
    tableName = tableNamePattern.format(oracleSchema=tableSchemaName, monthOfProcess_n=month_2_Value[2:],
                                        monthOfProcess=shortMonth)
    flagRecords = int(os.environ.get("recordsControlFlag"))
    recordsVariationLimit = int(os.environ.get("recordsVariationThreshold"))
    dsn = cx_Oracle.makedsn(host, port, sid)
    connection = cx_Oracle.connect(userName, password, dsn)
    cursor = connection.cursor()
    cursor.execute(f"SELECT COUNT(1) FROM ALL_TABLES WHERE CONCAT(CONCAT(OWNER,'.'),\
                   TABLE_NAME)='{tableName.upper()}'")
    firstresult = cursor.fetchone()[0]
    parametrosIngesta = leer_configuracion()
    prm_aws_endpoint = pl.validar_parametros(
        parametrosIngesta["s3access"]["aws_endpoint"], "El parametro bucket es obligatorio.")
    prm_aws_s3_bucket = pl.validar_parametros(
        parametrosIngesta["s3access"]["aws_s3_bucket"], "El parametro bucket es obligatorio.")
    prm_aws_access_key_id = pl.validar_parametros(
        parametrosIngesta["s3access"]["aws_access_key_id"], "El parametro access_key_id es obligatorio.")
    prm_aws_secret_access_key = pl.validar_parametros(parametrosIngesta["s3access"]["aws_secret_access_key"], "El parametro secret_access_key es obligatorio.")

    try:
        nombreDataset = prepara_nombre_dataset(prevMonthValue, parametrosIngesta)
        df = readAndWriteS3(prm_aws_endpoint, prm_aws_s3_bucket, prm_aws_access_key_id,
                            prm_aws_secret_access_key, nombreDataset)
        flagRecords = 1
    except Exception as err1:
        try:
            nombreDataset = prepara_nombre_dataset(month_2_Value, parametrosIngesta)
            df = readAndWriteS3(prm_aws_endpoint, prm_aws_s3_bucket, prm_aws_access_key_id,
                                prm_aws_secret_access_key, nombreDataset)
            flagRecords =1 
        except Exception as err2:
            print("No se tiene archivos de meses anterior, sólo se validará completitud para el presente mes")

    if firstresult == 0:
        msg = f"La tabla {tableName} no existe por lo que no se podrá continuar \
        con la ejecución mensual"
    else:
        cursor.execute("SELECT COUNT(1) FROM " + tableName)
        secondresult = cursor.fetchone()[0]
        if flagRecords == 1:
            thirdresult = df.shape[0]
            recordsvariationrate = abs(
                round((secondresult-thirdresult)*100/thirdresult, 2))
            if recordsvariationrate <= recordsVariationLimit:
                msg = "1"
            else:
                msg = f"La variación porcentual en el número de registros es del \
                      {str(recordsvariationrate)}%,el cual excede el umbral \
                      permitido el cual es del {recordsVariationLimit}%"
        else:
            if secondresult > 0:
                msg = "1"
            else:
                msg = f"La tabla {tableName} no cuenta con registros por lo que no podrá continuar \
                con la ejecución mensual"

    with open("/airflow/xcom/return.json", "w") as file:
        json.dump({"return_value": msg}, file)

    cursor.close()
    connection.close()

def main():
    validateDatabaseTable()

main()
