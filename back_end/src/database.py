from sqlalchemy import create_engine

DB_URI = 'mysql+pymysql://root:root@localhost:3306/SE_db'

bs_db = create_engine(DB_URI, encoding='utf-8')