import cx_Oracle
import sys
import weakref
import traceback



class DBConnection:
    def __init__(self,str_hostname,int_port,str_PortID):
            self.str_hostname=str_hostname
            self.int_port=int_port
            self.str_PortID=str_PortID
    connect_DB=None
    def __del__(self):
        print "destructor called" 
    def dbConnect(self):       
        
        
        try:
            strDSN=cx_Oracle.makedsn(self.str_hostname,self.int_port,self.str_PortID)
            print strDSN
            connect_DB=cx_Oracle.connect('VLDSYS_TH','VLDSYS_TH',strDSN)
        except(cx_Oracle.DatabaseError):
            print 'Invalid username/Password'
        if connect_DB==None:
            Print ("Print connection is not extablised ")
        else:
            print ("Connection is established")
            return connect_DB
    def dbGetcount(self,strTableName):
        
       
        try:
            connect_DB=self.dbConnect()
            print (connect_DB)
            strQuery='Select count(*) from '+strTableName
            print(strQuery)
            cursor= connect_DB.cursor()
            cursor.execute(strQuery)
            numberOfRows = cursor.fetchall()[0][0]
            return numberOfRows
        except:  
           print "Error :"+str(traceback.format_exc())

        finally :
            connect_DB.close
            connect_DB=None
            print ("connect_DB Closed")
    def dbGetdata(self,strTableName):
        strQuery='Select * from '+strTableName
        print(strQuery)
        try:
            connect_DB=self.dbConnect()
            cur= connect_DB.cursor()
            cur.execute(strQuery)
            print(cur.fetchall())
        except:  
           print "Error :"+str(traceback.format_exc())

        finally :
            connect_DB.close
            connect_DB=None
            print ("connect_DB Closed")

calss ConnectImpala:
    
 
            






        
#objDbConnect=DBConnection('dayrheqmsi002.enterprisenet.org',1521,'SIRQAZ1')
#Intcount=objDbConnect.dbGetcount('VLDRAWDATA_MX.BUFFERSTORES')
#objDbConnect=None

