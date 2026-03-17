import matplotlib.pyplot as plt
import io

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


    def get_target_trajectory(self,entity_id):
        with self.connection.cursor() as cursor:

            sql =   """SELECT reported_lat ,reported_lon
                    FROM intel_signals
                    WHERE entity_id = %s
                    ORDER by timestamp
                    """
            cursor.execute(sql,(entity_id,))

            return cursor.fetchall()


    def visualization_target_trajectory(self,entity_id):
        res = self.get_target_trajectory(entity_id)
        fig = plt.figure()
        x = [r[0] for r in res]
        y = [r[1] for r in res]
        plt.plot(x, y, 'o:r')
        plt.title(f"visualization_target_trajectory entity_id: {entity_id}")
        plt.xlabel("Lat")
        plt.ylabel("Lon")
        img_buf = io.BytesIO()
        plt.savefig(img_buf, format='png')
        plt.close(fig)
        return img_buf


    def identification_awakened_cells(self):
        with self.connection.cursor() as cursor:
            cursor.execute(
                """with t_day as(SELECT entity_id ,day(timestamp) as day ,sum(distance_from_last) as total
                FROM intel_signals
                WHERE hour(timestamp) BETWEEN 8 and 20
                GROUP by entity_id ,day(timestamp)) ,


                t_nith as(SELECT entity_id ,day(timestamp) as day ,sum(distance_from_last) as total
                FROM intel_signals
                WHERE hour(timestamp) BETWEEN 20 and 8
                GROUP by entity_id ,day(timestamp))


                SELECT t_day.entity_id
                FROM t_day 
                inner join t_nith
                on t_day.entity_id = t_nith.entity_id and t_day.day = t_nith.day
                WHERE t_day.total = 0 and t_nith.total > 10
                """)

            return cursor.fetchall()
