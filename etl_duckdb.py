import duckdb
import time

def create_duckdb():
    result = duckdb.sql(
        """
        SELECT
            cidade,
            MIN(temperatura) AS temp_minima,
            CAST(AVG(temperatura) AS DECIMAL(3,1)) AS temp_media,
            MAX(temperatura) AS temp_maxima
        FROM 
            read_csv(
                'data/measurements.txt',
                AUTO_DETECT=TRUE,
                sep=';',
                columns={'cidade': 'VARCHAR', 'temperatura': 'DECIMAL(3,1)'})
        GROUP BY
            cidade
        ORDER BY
            cidade
        """
    )
    
    result.show()

    result.write_parquet('data/measurements_summary.parquet')


if __name__ == '__main__':
    start_time = time.time()
    create_duckdb()
    took = time.time() - start_time
    print(f'Duckdb took: {took:.2f} sec')



