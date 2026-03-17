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


    def visualization_target_trajectory(self,entity_id):
        with self.connection.cursor() as cursor:

            sql =   """SELECT reported_lat ,reported_lon
                    FROM intel_signals
                    WHERE entity_id = %s
                    ORDER by timestamp
                    """
            cursor.execute(sql,(entity_id,))

            return cursor.fetchall()



# q = Queries(my_coonection)
# res = q.visualization_target_trajectory('TGT-003')
#
# import matplotlib.pyplot as plt
#
#
# x = [i[0] for i in res]
# y = [i[1] for i in res]
# plt.plot(x, y,'o:r')
#
# plt.show()
