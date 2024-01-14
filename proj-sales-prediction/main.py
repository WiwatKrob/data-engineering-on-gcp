import configparser


CONFIG_FILE = "pipeline.conf"
parser = configparser.ConfigParser()
parser.read(CONFIG_FILE)

database = parser.get("mysql_config", "database")
user = parser.get("mysql_config", "username")
password = parser.get("mysql_config", "password")
host = parser.get("mysql_config", "host")
port = parser.get("mysql_config", "port")

print(database, user, password, host, port)

import sqlalchemy
from sqlalchemy import textcd

uri = f"mysql+pymysql://{user}:{password}@{host}/{database}"
engine = sqlalchemy.create_engine(uri)
with engine.connect() as conn:
        conn.execute(text(f"show table"))