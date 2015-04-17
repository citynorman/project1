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

    def prevent_sql_injection_string(self, value ):
        if (value is None):# or str(value).strip()=''):
            value = 'null'
        else:
            if isinstance(value, str) == False:
                value = value.string
            value = MySQLdb.escape_string(value)
            value = "'%s'" % str(value)
 #           print(value)
        return value    


    def saveToDB(self, db): #The database stuff should be refactored!
    #Create a connection
    #Insert into tblForm13F values (nameOfIssuer, titleOfClass, cusip, ...) 
        
    # prepare a cursor object using cursor() method
        cursor = db.cursor()

    # convert inputs
        self.holdingDate = self.prevent_sql_injection_string(self.holdingDate)
        self.holdingCompanyCIK = self.prevent_sql_injection_string( self.holdingCompanyCIK )
        self.nameOfIssuer  = self.prevent_sql_injection_string( self.nameOfIssuer)
        self.titleOfClass  = self.prevent_sql_injection_string( self.titleOfClass)
        self.cusip = self.prevent_sql_injection_string( self.cusip)
        self.valueInThousands  = self.prevent_sql_injection_string( self.valueInThousands)
        self.shrsOrPrn  = self.prevent_sql_injection_string( self.shrsOrPrn)
        self.shPrn  = self.prevent_sql_injection_string( self.shPrn)
        self.putCall  = self.prevent_sql_injection_string( self.putCall)
        self.investmentDiscretion  = self.prevent_sql_injection_string( self.investmentDiscretion  )
        self.otherManager  = self.prevent_sql_injection_string( self.otherManager  )
        self.soleVotingAuthority  = self.prevent_sql_injection_string( self.soleVotingAuthority  )
        self.sharedVotingAuthority  = self.prevent_sql_injection_string( self.sharedVotingAuthority  )
        self.noneVotingAuthority  = self.prevent_sql_injection_string( self.noneVotingAuthority  )


        sql = "INSERT INTO tblForm13f (holdingDate, holdingCompanyCIK, nameOfIssuer, \
           titleOfClass, cusip, valueInThousands, shrsOrPrnAmt, shPrn, putCall, investmentDiscretion, otherManager, \
           soleVotingAuthority, sharedVotingAuthority, noneVotingAuthority) \
           VALUES ( %s,%s,%s,%s,%s, %s,%s,%s,%s,%s, %s,%s,%s,%s);"% (
               self.holdingDate, self.holdingCompanyCIK, self.nameOfIssuer, self.titleOfClass, self.cusip, self.valueInThousands,
               self.shrsOrPrn, self.shPrn, self.putCall, self.investmentDiscretion, self.otherManager, self.soleVotingAuthority,
               self.sharedVotingAuthority, self.noneVotingAuthority)
        

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
    
