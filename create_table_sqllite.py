from sqlalchemy import create_engine,MetaData,Table,Column,Integer,String
from sqlalchemy.sql import select

engine = create_engine('sqlite:///college.db')

meta = MetaData()

students = Table('students',meta,
                Column('id',Integer,primary_key=True),
                Column('name',String),
                Column('lastname',String),
                )
 
meta.create_all(engine)
conn = engine.connect()

#for inserting single value at a time
#ins = students.insert().values(name='Vishal',lastname='Rathod')
#result = conn.execute(ins)

#for inserting multiple values at a time
##result = conn.execute(students.insert(),[
##    {'name':'Virendra','lastname':'Bahadure'},
##    {'name':'Chandu','lastname':'Shitole'},
##    ])

#sel = students.select()
sel = students.select().where(students.c.id>5)
#sel = select([students])
result = conn.execute(sel)

for row in result:
    print(row)
