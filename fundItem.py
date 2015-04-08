import dataTable
#Needs a lot of work. Not currently working.

class FundItem(dataTable):
#tblFundID
#cikNumber
#fundName

    name = 'fundName'

    def __init__(self,
                 cikNumber,
                 fundName
         ):
        self.cikNumber = cikNumber
        self.fundName = fundName
        pass

    def __init__(self, cikNumber):
        self.cikNumber = cikNumber
        pass

	def __init__(self, db, cikNumber):
		self.db = db
		self.dbc = self.db.cursor()
        self.cikNumber = cikNumber

	def __iter__(self):
		"""overriding the superclass's iterator"""
		q = "select cikNumber, fundName from %s" % (self.name)
		self._query(q)
		# an Iterator is an object with a next() method
		return self
       


        
    def loadAllFromDB(self, cikNumber): #Would this have been better done statically?

        db = MySQLdb.connect("localhost","rb","password","mytestdb") #Should not be duplicated!
        
        
    # prepare a cursor object using cursor() method
        cursor = db.cursor()

        sql = "select cikNumber, fundName from tblFund;"# where cikNumber ='"+ cikNumber + "');"

#        print (sql)
        
        try:
       # Execute the SQL command
            cursor.execute(sql)
            rows = c.fetchall()
            for eachRow in rows:
                fi = fundItem(row[0], row[1])
                
        except Exception, e:
       # In case there are any exceptions...
            print str(e)
       
        # disconnect from server
        db.close()

        cikNumber = cik
    
    

    def saveToDB(self):
    #Create a connection
    #Insert into tblForm13F values (nameOfIssuer, titleOfClass, cusip, ...) 

    # Open database connection
        db = MySQLdb.connect("localhost","testuser","password","mytestdb")
        
    # prepare a cursor object using cursor() method
        cursor = db.cursor()

        sql = "INSERT INTO tblFund (cikNumber, fundName) \
           VALUES ("

        # This is an absolute mess, but Python doesn't really use nulls in the conventional sense anyways.
        # There is also likely a more efficient way to do the string-building.
        if self.cikNumber is None:
            sql += "null,"
        else:
            sql += "'" + self.cikNumber+ "',"

        if self.fundName is None:
            sql += "null,"
        else:
            sql += "'" + self.fundName+ "',"
        sql +=");"
    


#        print (sql)
        
        try:
       # Execute the SQL command
            cursor.execute(sql)
       # Commit your changes in the database
            db.commit()
        except Exception, e:
       # Rollback in case there is any error
            print str(e)
            db.rollback()
       
        # disconnect from server
        db.close()
    

#testing
if __name__=='__main__':
	db = MySQLdb.connect(user="testuser", passwd="password", db="mytestdb")
	funds = fundItem(db, "tblFunds")
	for fund in funds:
		print fund
