from DAO.Lab_controller import Lab_controller
from DAO.Subject_controller import Subject_controller
from DAO.Abstract_connect import Abstract_Connect
from Objects.Lab import Lab
from Objects.Subject import Subject
# from datetime import date

class Table:

    def Make_table(self):
        ac = Abstract_Connect()
        con = ac.Get_connection()
        sc = Subject_controller(con)
        subject = sc.Get_all()

        lc = Lab_controller(con)

        x = 0
        l = []
        for s in subject:
            l.append(self.Fill_Table(s.SubID, lc))
            if(s.LabCount > x):
                x = s.LabCount

        con.close()

        return subject, x, l

    def Fill_Table(self, id : int, lc) -> list:
        l = lc.Get_all_by_subject(id)

        lll = []
        for ll in l:
            lll.append(ll.IsMaked)

        return lll

    def Update_square(self, number, subj_name, count):
        ac = Abstract_Connect()
        con = ac.Get_connection()
        sc = Subject_controller(con)
        lc = Lab_controller(con)

        subj = sc.Get_by_Name(subj_name)

        lab = lc.Get_by_Name(number+1, subj.SubID)
        if(lab.IsMaked == 0 | lab.IsMaked == None):
            lab.IsMaked = 0
        lab.IsMaked += count
        lc.Update(lab)
        con.close()

    # options

    def Add_new_Subject(self, name, lab_count):
        ac = Abstract_Connect()
        con = ac.Get_connection()
        sc = Subject_controller(con)
        lc = Lab_controller(con)

        sc.Add(Subject(1, name, lab_count))
        sub = sc.Get_by_Name(name)

        for i in range(lab_count):
            lc.Add(Lab(1,sub.SubID, i,0))

        con.close()

    def Delete_subject(self, name):
        ac = Abstract_Connect()
        con = ac.Get_connection()
        sc = Subject_controller(con)
        lc = Lab_controller(con)

        sub = sc.Get_by_Name(name)
        labs = lc.Get_all_by_subject(sub.SubID)

        for l in labs:
            lc.Delete(l.LabID)

        sc.Delete(sub.SubID)

        con.close()

    def Change_lab_count(self,  name, lab_count):
        ac = Abstract_Connect()
        con = ac.Get_connection()
        sc = Subject_controller(con)
        lc = Lab_controller(con)

        sub = sc.Get_by_Name(name)
        last_lc = sub.LabCount
        sub.LabCount = lab_count
        sc.Update(sub)

        if((last_lc - lab_count) > 0):
            for i in range(last_lc + 1, lab_count):
                lc.Add(Lab(1, sub.SubID, i, 0))
        else:
            for i in range(lab_count + 1, last_lc):
                lab = lc.Get_by_Name(i, sub.SubID)
                lc.Delete(lab.LabID)

        con.close()
