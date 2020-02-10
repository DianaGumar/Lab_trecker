from errno import errorcode
import mysql.connector

class Abstract_Connect:

    def Get_connection(self):
        if(self.con == 0):
            self.Create_connection()
        return self.con

    def Create_connection(self):
        try:
            self.con = mysql.connector.connect(
                host = "localhost",
                user = "root",
                passwd= "1111",
                database = "treckerh"
            )
        except mysql.connector.Error as err:
          if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
          elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
          else:
            print(err)
        else:
            return self.con
          # con.close()

    def CloseConnect(self):
        self.con.close()
        con = 0

    con = 0