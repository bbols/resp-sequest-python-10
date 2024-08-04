from sqlalchemy import select,insert,Column,Integer,String,create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#engine = create_engine("sqlite:///:memory:",echo=True)
engine = create_engine("sqlite:///test_orm.db",echo=True)
Base = declarative_base()

class base(Base):
    __tablename__="base"
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String)
    region=Column(String)
    key_skill=Column(String)

    def __init__(self,name,region,key_skill):
        self.name=name
        self.region=region
        self.key_skill=key_skill

    def __str__(self):
        return f"СТРОКА str || {self.name} || {self.region} || {self.key_skill}"
    def __repr__(self):
        return f"СТРОКА repr || {self.name} || {self.region} || {self.key_skill}"

stmt = insert(base).values(name="python developer", region="Moscos",key_skill="python")
print(stmt)
stmt = select(base).where()
print(stmt)
Base.metadata.create_all(engine)

#create session
Session = sessionmaker(bind=engine)

session = Session()

#db=base(name="python developer",region="Moscos",key_skill="python")
#session.add(db)
#session.commit()
#db=base(name="java developer",region="Ekaterinburg",key_skill="python")
#session.add(db)
#session.commit()

#просмотр данных
q_query = session.query(base)
for row in q_query:
    print(row)

q=session.query(base).all()
print(q)
q=session.query(base).filter(base.name=="python developer").all()
print(q)
