from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

DIALECT = 'oracle'
SQL_DRIVER = 'cx_oracle'
USERNAME = 'billapp' #enter your username
PASSWORD = 'billapp' #enter your password
HOST = '10.2.17.20' #enter the oracle db host url
PORT = 1521 # enter the oracle port number
SERVICE = 'bpdr' # enter the oracle db service name
ENGINE_PATH_WIN_AUTH = DIALECT + '+' + SQL_DRIVER + '://' + USERNAME + ':' + PASSWORD +'@' + HOST + ':' + str(PORT) + '/?service_name=' + SERVICE

engine = create_engine(ENGINE_PATH_WIN_AUTH)

SessionLocal = sessionmaker(bind=engine)

#jdbc:oracle:thin:@(DESCRIPTION = (ADDRESS = (PROTOCOL = TCP)(HOST = 10.2.17.20)(PORT = 1521)) (CONNECT_DATA = (SERVER = DEDICATED) (SERVICE_NAME = bpdr)))