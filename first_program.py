##from sqlalchemy import create_engine,MetaData,Table,Column,Integer,String
##from sqlalchemy.orm import mapper
##
##engine = create_engine("mysql://root:root@localhost:3306/vipul")
#sqlite:///college.db
##
##meta = MetaData()
##
##student = Table('students',meta,
##            Column('id',Integer,primary_key = True),
##            Column('name',String),
##            Column('lastname',String),
##)
##
##class Student:
##    def __init__(self,n,l):
##        self.name = n
##        self.lastname = l
##
##mapper(Student,student)
##
##meta.create_all(engine)
##                
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine('mysql://root:root@localhost:3306/vipul', echo = True)
meta = MetaData()

students = Table(
   'students', meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String), 
   Column('lastname', String),
)
meta.create_all(engine)
