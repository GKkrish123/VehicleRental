from database.db_conn import get_session
from mock_db_tables import create_mock_tables, delete_mock_tables
from response.response import get_response
from router import mockdb_api

@mockdb_api.post("/")
def create_mock_db_tables():
    try:
        session = get_session()
        create_mock_tables(session)
        return get_response("MOCK_RES001", None, 200)
    except Exception as e:
        print("create_mock_db_tables exception : ", e)
        return get_response("MOCK_ERR001", None, 409)

@mockdb_api.delete("/")
def delete_mock_db_tables():
    try:
        delete_mock_tables()
        return get_response("MOCK_RES002", None, 200)
    except Exception as e:
        print("delete_mock_db_tables exception : ", e)
        return get_response("MOCK_ERR002", None, 409)
