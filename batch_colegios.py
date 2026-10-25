from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# 1. Inicializar la sesión de Spark para Batch
spark = SparkSession.builder \
    .appName("Tarea3BatchColegios") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# 2. Cargar el archivo CSV descargado
df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv("colegios.csv")

print("--- 1. ESQUEMA DEL CONJUNTO DE DATOS ---")
df.printSchema()

print("--- 2. PRIMERAS FILAS DEL DATAFRAME ---")
df.show(3, truncate=False)

print("--- 3. ANÁLISIS: TOTAL DE COLEGIOS POR ZONA (Urbana / Rural) ---")
conteo_zona = df.groupBy("zona").count().orderBy(col("count").desc())
conteo_zona.show(truncate=False)

print("--- 4. ANÁLISIS: TOTAL DE COLEGIOS POR CALENDARIO ---")
conteo_calendario = df.groupBy("calendario").count().orderBy(col("count").desc())
conteo_calendario.show(truncate=False)

# Detener la sesión de Spark
spark.stop()
