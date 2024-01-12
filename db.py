from database.database import SessionLocal
import cx_Oracle 
import platform

cx_Oracle.init_oracle_client(lib_dir=r"D:\OracleClient\instantclient_19_9")

# Dependency
def get_db():
    dsn_tns = cx_Oracle.makedsn('10.2.17.20', '1521', service_name='bpdr')
    db = cx_Oracle.connect(user=r'billapp', password='billapp', dsn=dsn_tns) 
    try:
        yield db
    finally:
        db.close()