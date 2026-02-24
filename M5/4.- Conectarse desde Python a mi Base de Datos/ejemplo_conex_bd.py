#pip install "psycopg[binary]"
# o python -m pip install "psycopg[binary]"

import psycopg
from psycopg.rows import dict_row

DB_HOST = "localhost"
DB_PORT = 5433
DB_NAME = "tienda"
DB_USER = "postgres"
DB_PASS = "1234"

def main():
    # row_factory=dict_row hace que cada fila venga como dict (más cómodo)
    with psycopg.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        row_factory=dict_row
    ) as conn:

        # 1) SELECT simple
        # Abre un cursor (como un "canal" para enviar SQL y recibir resultados)
        with conn.cursor() as cur:
            # Ejecuta una consulta SQL en PostgreSQL
            cur.execute(
            '''SELECT
  cp.localidad,
  COUNT(*) AS ventas,
  SUM(v.monto) AS total
FROM ventas v
JOIN clientes c ON c.dni = v.dni
LEFT JOIN codigos_postales cp ON cp.codigo_postal = c.codigo_postal
WHERE v.fecha >= '2026-02-01'::timestamptz
  AND v.fecha <  '2026-03-01'::timestamptz
GROUP BY cp.localidad
ORDER BY total DESC;'''
                )

            # Trae TODAS las filas devueltas por el SELECT y las guarda en una lista
            clientes = cur.fetchall()
            print("\n=== CLIENTES ===")
            
            # Recorre cada fila (cada cliente) y la imprime
            for c in clientes:
                print(c)


if __name__ == "__main__":
    main()