from sqlalchemy import create_engine

DB_URI = 'mysql+pymysql://root:z96172300@localhost:3306/bs_db'

bs_db = create_engine(DB_URI, encoding='utf-8')