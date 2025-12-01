from database.DB_connect import DBConnect
from model.hub import Hub

class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """
    # TODO
    @staticmethod
    def read_all_hub():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = 'SELECT * FROM hub'
        cursor.execute(query)
        result = []
        for row in cursor:
            hub = Hub(row['id'], row['codice'], row['name'], row['citta'], row['stato'], row['latitudine'], row['longitudine'])
            result.append(hub)
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def read_tratte_aggregate():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """ SELECT LEAST(id_hub_origine, id_hub_destinazione) as h1,
                           GREATEST(id_hub_origine, id_hub_destinazione) as h2,
                           SUM (valore_merce) AS somma_valori,
                           COUNT(*) AS n_spedizioni
                    FROM spedizione
                    GROUP BY h1,h2"""
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append((row['h1'], row['h2']. row['somma_valori'], row['n_spedizioni']))
        cursor.close()
        conn.close()
        return result