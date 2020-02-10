from DAO.Lab_controller import Lab_controller
from DAO.Subject_controller import Subject_controller
from DAO.Abstract_connect import Abstract_Connect
from Objects.Lab import Lab
from datetime import date

class Table:

    def Make_table(self):
        ac = Abstract_Connect()
        con = ac.Get_connection()
        sc = Subject_controller(con)
        subject  = sc.Get_all()
        con.close()

        x = 0
        l = []
        for s in subject:
            l.append(self.Fill_Table(s.SubID))
            if(s.LabCount > x):
                x = s.LabCount

        return subject, x, l

    def Fill_Table(self, id : int) -> list:
        ac = Abstract_Connect()
        con = ac.Get_connection()
        lc = Lab_controller(con)

        l = lc.Get_all_by_subject(id)
        con.close()

        lll = []
        for ll in l:
            lll.append(ll.IsMaked)

        return lll


    # def Initialize_table(self, lab : Lab,  contr : Lab_controller):
    #     lab.IsMaked = 0
    #     contr.Update(lab)


    def Update_square(self, number, subj_name, count):
        ac = Abstract_Connect()
        con = ac.Get_connection()
        sc = Subject_controller(con)
        lc = Lab_controller(con)

        subj = sc.Get_by_Name(subj_name)

        lab = lc.Get_by_Name(number+1, subj.SubID)
        if(lab.IsMaked == 0 | lab.IsMaked == None):
            lab.IsMaked = 0
        elif(lab.IsMaked < 100):
            lab.IsMaked += count
        lc.Update(lab)







