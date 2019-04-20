from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


host='127.0.0.1'
user='root'
password = 'root'
dbName = 'shopweb_db'
Base = declarative_base()
'''
class User(Base):
    __tablename__ = 'user'
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
'''
def getSession(user,password,host,dbName):
    s='mysql+pymysql://{}:{}@{}:3306/{}'.format(user,password,host,dbName)
    engine = create_engine(s)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    session.commit()
    return session


#session.close()

##进行查询
#session = DBSession()
#user = session.query(User).filter(User.id=='4').one()
#session.close()

if __name__=='__main__':
    getSession('user','pwd','host','dbname')