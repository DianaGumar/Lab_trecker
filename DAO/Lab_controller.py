from Objects.Lab import Lab
import mysql.connector

class Lab_controller:
    def __init__(self, con):
        self.con = con

    def Add(self, obj : Lab) -> int:
        a = self.Get_by_id(obj.LabID)
        if(a != None):
            return self.Update_by_id(obj)
        else:
            cursor = self.con.cursor()
            cursor.execute("insert into Labs (SubjectID, LabNumber, IsMaked) "
                             "values (%s, %s, %s)", (obj.SubID, obj.Number, obj.IsMaked))
            self.con.commit()
            # self.con.close()
            return cursor.rowcount

    def Get_all(self) -> list :
        cursor = self.con.cursor()
        cursor.execute("select * from Labs")
        l : list = []
        for st in cursor:
            xx = Lab(st[0], st[1], st[2], st[3])
            l.append(xx)
        return l

    def Get_all_by_subject(self, id : int) -> list :
        cursor = self.con.cursor()
        cursor.execute("select * from Labs where SubjectID = " + str(id))
        l : list = []
        for st in cursor:
            xx = Lab(st[0], st[1], st[2], st[3])
            l.append(xx)
        return l

    def Get_by_id(self, obj : int) -> Lab:
        cursor = self.con.cursor()
        cursor.execute("select * from Labs where LabID = " + str(obj))
        st = cursor.fetchone()
        stan = None
        if(st != None):
            stan = Lab(st[0], st[1], st[2], st[3])
        # self.con.close()
        return stan

    def Get_by_Name(self, lab_number : int, sub_id : int) -> Lab:
        cursor = self.con.cursor()
        cursor.execute("select * from Labs where LabNumber = " + str(lab_number) + " and SubjectID = " + str(sub_id))
        st = cursor.fetchone()
        stan = None
        if(st != None):
            stan = Lab(st[0], st[1], st[2], st[3])
        # self.con.close()
        return stan

    def Update_by_id(self, obj : Lab) -> int:
        cursor = self.con.cursor()
        sql = "UPDATE Labs SET SubjectID = %s, LabNumber = %s, IsMaked = %s WHERE LabID = %s"
        val = (obj.SubID,  obj.Number, obj.IsMaked, obj.LabID)

        cursor.execute(sql, val)
        self.con.commit()
        return cursor.rowcount

    def Update(self, obj: Lab) -> int:
        cursor = self.con.cursor()
        sql = "UPDATE Labs SET SubjectID = %s, LabNumber = %s, IsMaked = %s WHERE LabNumber = %s and SubjectID = %s"
        val = (obj.SubID, obj.Number, obj.IsMaked, obj.Number, obj.SubID)

        cursor.execute(sql, val)
        self.con.commit()
        return cursor.rowcount

    def Delete(self, obj : int) -> int:
        cursor = self.con.cursor()
        sql = "DELETE FROM Labs WHERE LabID = " + str(obj)

        cursor.execute(sql)
        self.con.commit()
        return cursor.rowcount