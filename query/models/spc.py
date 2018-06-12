#!/usr/bin/env python

"""
  ____   ____  _____  ____   ____  _      _                                _    _ _______ ____  __  __       _______ _____ ____  _   _ 
 |  _ \ / __ \|  __ \|  _ \ / __ \| |    | |        /\                /\  | |  | |__   __/ __ \|  \/  |   /\|__   __|_   _/ __ \| \ | |
 | |_) | |  | | |__) | |_) | |  | | |    | |       /  \              /  \ | |  | |  | | | |  | | \  / |  /  \  | |    | || |  | |  \| |
 |  _ <| |  | |  _  /|  _ <| |  | | |    | |      / /\ \            / /\ \| |  | |  | | | |  | | |\/| | / /\ \ | |    | || |  | | . ` |
 | |_) | |__| | | \ \| |_) | |__| | |____| |____ / ____ \          / ____ \ |__| |  | | | |__| | |  | |/ ____ \| |   _| || |__| | |\  |
 |____/ \____/|_|  \_\____/ \____/|______|______/_/    \_\        /_/    \_\____/   |_|  \____/|_|  |_/_/    \_\_|  |_____\____/|_| \_|
                                                                                                                                       
 +------------------------------------------------------------------------------------------------------------------------------------+
 |                                                                                                                                    |
 |  Module Name    : Models                                                                                                           |
 |  Module Purpose : Mysql Database Design , and model relationship , for database functioning                                        |
 |  Inputs  : ORM class                                                                                                               |
 |  Outputs : Create code , database Object                                                                                           |
 |  Author : Borbolla Automation Inc                                                                                                  |
 |  Email : ingenieria@borbolla-automation.com                                                                                        |
 |  webpage : www.borbolla-automation.com                                                                                             |
 +------------------------------------------------------------------------------------------------------------------------------------+
"""

import peewee
import datetime

#database =  peewee.SqliteDatabase("QR_code.db")
database = peewee.MySQLDatabase(host = "localhost" , port = 3306 , user = "mkdc" , password = "MKDC" , database = "SPC_Data")




class BaseModel(peewee.Model):
    class Meta:
        database = database

class Machine(BaseModel):
    name = peewee.CharField()
    basic_value = peewee.FloatField()
    range_up    = peewee.FloatField()
    range_down  = peewee.FloatField()
    date_added = peewee.DateTimeField(default = datetime.datetime.now)

class Gauge(BaseModel):
    _id = peewee.CharField(max_length = 4)
    name = peewee.CharField(max_length = 6)
    date_added = peewee.DateTimeField(default = datetime.datetime.now)
    machine = peewee.ForeignKeyField(Machine , backref = 'gauges')

class Value(BaseModel):
    seq_num = peewee.IntegerField()
    gauge = peewee.ForeignKeyField(Gauge , backref = 'values')
    result = peewee.CharField(max_length = 3)
    reg_date = peewee.DateTimeField(default = datetime.datetime.now)
    date_added = peewee.DateTimeField(default = datetime.datetime.now)




if __name__ == '__main__':

    database.create_tables([Machine , Gauge , Value])
    
    model = 'ST170125'
    for number in range(4):
        Machine.create(name = '%s-%s'%(model,number+1) , basic_value = 92.2 , range_up = 92.2+0.05 ,range_down = 92.2-0.05)
