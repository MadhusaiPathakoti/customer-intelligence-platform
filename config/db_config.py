from sqlalchemy import create_engine

def get_engine():
    engine = create_engine(
        # "mysql+pymysql://USERNAME:PASSWORD@HOST:3306/customer_intelligence"
        "mysql+pymysql://sql12817317:pcdW1whp9N@sql12.freesqldatabase.com:3306/sql12817317"
    )
    return engine
