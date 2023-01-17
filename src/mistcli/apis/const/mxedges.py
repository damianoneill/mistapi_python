from mistcli import Session

def get_mxedge_events_definitions(mist_session:Session):
    uri = "/api/v1/const/mxedge_events"
    resp = mist_session.mist_get(uri)
    return resp


def get_mxedge_models(mist_session:Session):
    uri = "/api/v1/const/mxedge_models"
    resp = mist_session.mist_get(uri)
    return resp
