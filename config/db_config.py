from sqlalchemy import create_engine

def get_engine():
    engine = create_engine(
        # "mysql+pymysql://USERNAME:PASSWORD@HOST:3306/customer_intelligence"
    )
    return engine
