from connection import conn

my_coonection = conn.get_conn()
# my_cursor = my_coonection .cursor()
# my_cursor.fetchall()

class Queries:
    def __init__(self,connection):
        self.connection = connection


    def high_priority_movement_alert(self):
        with self.connection.cursor() as cursor:
            cursor.execute(
            """SELECT entity_id ,target_name ,priority_level ,movement_distance_km
                FROM targets
                WHERE priority_level IN (1,2)
                AND movement_distance_km > 5""")

            return cursor.fetchall()


    def analysis_intelligence_sources(self):
        with self.connection.cursor() as cursor:
            cursor.execute(
                """SELECT signal_type ,COUNT(*) as total_Intelligence_signal
                    FROM intel_signals
                    GROUP BY signal_type
                    ORDER BY COUNT(*) DESC""")

            return cursor.fetchall()

    def finding_new_targets(self):
        with self.connection.cursor() as cursor:
            cursor.execute(
                """SELECT entity_id ,COUNT(*) as total_reports 
                    FROM intel_signals
                    WHERE priority_level = 99
                    GROUP by entity_id 
                    ORDER by COUNT(*) DESC
                    LIMIT 3""")

            return cursor.fetchall()





q = Queries(my_coonection)
print(q.finding_new_targets())