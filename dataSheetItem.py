import MySQLdb


class DataSheetItem():
    #nameOfIssuer = null
    #titleOfClass = null
    #cusip = null
    #valueInThousands = null
    #shrsOrPrn = null
    #shPrn = null
    #putCall = null
    #investmentDiscretion = null
    #otherManager = null
    #soleVotingAuthority = null
    #sharedVotingAuthority = null
    #noneVotingAuthority = null
    pass

    def __init__(self,
         holdingDate,
         holdingCompanyCIK,
         nameOfIssuer,
         titleOfClass,
         cusip,
         valueInThousands,
         shrsOrPrn,
         shPrn,
         putCall,
         investmentDiscretion,
         otherManager,
         soleVotingAuthority,
         sharedVotingAuthority,
         noneVotingAuthority
         ):
        self.holdingDate = holdingDate
        self.holdingCompanyCIK = holdingCompanyCIK
        self.nameOfIssuer = nameOfIssuer
        self.titleOfClass = titleOfClass
        self.cusip = cusip
        self.valueInThousands = valueInThousands
        self.shrsOrPrn = shrsOrPrn
        self.shPrn = shPrn
        self.putCall = putCall
        self.investmentDiscretion = investmentDiscretion
        self.otherManager = otherManager
        self.soleVotingAuthority = soleVotingAuthority
        self.sharedVotingAuthority = sharedVotingAuthority
        self.noneVotingAuthority = noneVotingAuthority
        pass

    def saveToDB(self): #The database stuff should be refactored!
    #Create a connection
    #Insert into tblForm13F values (nameOfIssuer, titleOfClass, cusip, ...) 

    # Open database connection
        db = MySQLdb.connect("localhost","testuser","password","mytestdb")
        
    # prepare a cursor object using cursor() method
        cursor = db.cursor()

        sql = "INSERT INTO tblForm13f (holdingDate, holdingCompanyCIK, nameOfIssuer, \
           titleOfClass, cusip, valueInThousands, shrsOrPrnAmt, shPrn, putCall, investmentDiscretion, otherManager, \
           soleVotingAuthority, sharedVotingAuthority, noneVotingAuthority) \
           VALUES ("

        # This is messy.
        # There is also likely a more efficient way to do the string-building.
        if self.holdingDate is None:
            sql += "null,"
        else:
            sql += "'" + self.holdingDate + "',"

        if self.holdingCompanyCIK is None:
            sql += "null,"
        else:
            sql += "'" + self.holdingCompanyCIK + "',"

        if self.nameOfIssuer is None:
            sql += "null,"
        else:
            sql += "'" + self.nameOfIssuer.string + "',"

        if self.titleOfClass is None:
            sql += "null,"
        else:
            sql += "'" + self.titleOfClass.string + "',"

        if self.cusip is None:
            sql += "null,"
        else:
            sql += "'" + self.cusip.string + "',"

        if self.valueInThousands is None:
            sql += "null,"
        else:
            sql += "'" + self.valueInThousands.string + "',"

        if self.shrsOrPrn is None:
            sql += "null,"
        else:
            sql += "'" + self.shrsOrPrn.string + "',"

        if self.shPrn is None:
            sql += "null,"
        else:
            sql += "'" + self.shPrn.string + "',"

        if self.putCall is None:
            sql += "null,"
        else:
            sql += "'" + self.putCall.string + "',"

        if self.investmentDiscretion is None:
            sql += "null,"
        else:
            sql += "'" + self.investmentDiscretion.string + "',"

        if self.otherManager is None:
            sql += "null,"
        else:
            sql += "'" + self.otherManager.string + "',"

        if self.soleVotingAuthority is None:
            sql += "null,"
        else:
            sql += "'" + self.soleVotingAuthority.string + "',"

        if self.sharedVotingAuthority is None:
            sql += "null,"
        else:
            sql += "'" + self.sharedVotingAuthority.string + "',"

        if self.noneVotingAuthority is None:
            sql += "null,"
        else:
            sql += "'" + self.noneVotingAuthority.string + "'"
        sql +=");"
    


#        print (sql)
        
        try:
       # Execute the SQL command
            cursor.execute(sql)
       # Commit changes to the database
            db.commit()
        except Exception, e:
       # Rollback in case there is any error
            print str(e)
            db.rollback()
       
        # disconnect from server
        db.close()
    
