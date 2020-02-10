from Objects.Subject import Subject
import mysql.connector

class Subject_controller:
    def __init__(self, con):
        self.con = con

    def Add(self, obj : Subject) -> int:
        cursor = self.con.cursor()
        cursor.execute("insert into Subjects (SubjectID, SubjectName, LabCount) "
                         "values (%s, %s, %s)", (obj.SubID, obj.Name, obj.LabCount))
        self.con.commit()
        # self.con.close()
        return cursor.rowcount

    def Get_all(self) -> list:
        cursor = self.con.cursor()
        cursor.execute("select * from Subjects")
        l : list = []
        for st in cursor:
            xx = Subject(st[0], st[1], st[2])
            l.append(xx)
        return l

    def Get_by_id(self, obj : int) -> Subject:
        cursor = self.con.cursor()
        cursor.execute("select * from Subjects where SubjectID = " + str(obj))
        st = cursor.fetchone()
        stan = Subject(st[0], st[1], st[2])
        # self.con.close()
        return stan

    def Get_by_Name(self, obj : str) -> Subject:
        cursor = self.con.cursor()
        cursor.execute("select * from Subjects where SubjectName = '" + obj + "'; ")
        st = cursor.fetchone()
        stan = Subject(st[0], st[1], st[2])
        # self.con.close()
        return stan

    def Update(self, obj : Subject) -> int:
        cursor = self.con.cursor()
        sql = "UPDATE Subjects SET SubjectName = %s, LabCount = %s WHERE SubjectID = %s"
        val = (obj.Name,  obj.LabCount,  obj.SubID)

        cursor.execute(sql, val)
        self.con.commit()
        return cursor.rowcount


    def Delete(self, obj : int) -> int:
        cursor = self.con.cursor()
        sql = "DELETE FROM Subjects WHERE SubjectID = " + str(obj)

        cursor.execute(sql)
        self.con.commit()
        return cursor.rowcount