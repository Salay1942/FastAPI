from database.database import SessionLocal
import cx_Oracle 
import platform

cx_Oracle.init_oracle_client(lib_dir=r"/home/eurekaapp/OracleClient/instantclient_21_6")

# Dependency
def get_db():
    dsn_tns = cx_Oracle.makedsn('10.0.4.46', '1522', service_name='bpw')
    db = cx_Oracle.connect(user=r'BPAY_WEB', password='BillPayApp158', dsn=dsn_tns) 
    try:
        yield db
    finally:
        db.close()
