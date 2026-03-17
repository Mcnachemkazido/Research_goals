from fastapi import APIRouter , Response, BackgroundTasks ,HTTPException
from db.connection import Connection
from db.dal import Queries
from db.app_config import AppConfig



connection = Connection(AppConfig.get_host(),int(AppConfig.get_port()),AppConfig.get_user()
                  ,AppConfig.get_password(),AppConfig.get_db())


queries= Queries(connection.get_conn())
router = APIRouter()

@router.get('/high_priority_movement_alert')
def get_high_priority_movement_alert():
    try:
        return queries.high_priority_movement_alert()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500,detail=e)

@router.get('/analysis_intelligence_sources')
def get_analysis_intelligence_sources():
    try:
        return queries.analysis_intelligence_sources()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=e)

@router.get('/finding_new_targets')
def get_finding_new_targets():
    try:
        return queries.finding_new_targets()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=e)

@router.get('/identification_awakened_cells')
def get_identification_awakened_cells():
    try:
        return queries.identification_awakened_cells()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=e)

@router.get('/visualization_target_trajectory')
def get_visualization_target_trajectory(background_tasks: BackgroundTasks,entity_id: str):
    try:
        img_buf = queries.visualization_target_trajectory(entity_id)
        background_tasks.add_task(img_buf.close)
        headers = {'Content-Disposition': 'inline; filename="out.png"'}
        return Response(img_buf.getvalue(), headers=headers, media_type='image/png')
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=e)