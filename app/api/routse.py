from fastapi import APIRouter , Response, BackgroundTasks
from app.db.connection import Connection
from app.db.dal import Queries
from app.app_config import AppConfig



connection = Connection(AppConfig.get_host(),int(AppConfig.get_port()),AppConfig.get_user()
                  ,AppConfig.get_password(),AppConfig.get_db())


queries= Queries(connection.get_conn())
router = APIRouter()

@router.get('/high_priority_movement_alert')
def get_high_priority_movement_alert():
    return queries.high_priority_movement_alert()

@router.get('/analysis_intelligence_sources')
def get_analysis_intelligence_sources():
    return queries.analysis_intelligence_sources()

@router.get('/finding_new_targets')
def get_finding_new_targets():
    return queries.finding_new_targets()


@router.get('/visualization_target_trajectory')
def get_visualization_target_trajectory(background_tasks: BackgroundTasks,entity_id):
    img_buf = queries.visualization_target_trajectory(entity_id)
    background_tasks.add_task(img_buf.close)
    headers = {'Content-Disposition': 'inline; filename="out.png"'}
    return Response(img_buf.getvalue(), headers=headers, media_type='image/png')