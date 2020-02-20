
class Lab:
    def __init__(self, LabID, SubID, Number, IsMaked):
        self.LabID = LabID
        self.Number = Number
        self.SubID = SubID
        self.IsMaked = IsMaked

    def __repr__(self):
        return "<History('%s','%s', '%s', '%s')>" % (self.LabID, self.SubID, self.Number, self.IsMaked)
