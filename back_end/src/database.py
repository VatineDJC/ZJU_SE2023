from sqlalchemy import create_engine

DB_URI = 'mysql+pymysql://root:root@localhost:3306/SE'

bs_db = create_engine(DB_URI, encoding='utf-8')