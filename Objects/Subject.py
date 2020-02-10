
class Subject():
    def __init__(self, SubID, Name, LabCount):
        self.SubID = SubID
        self.LabCount = LabCount
        self.Name = Name

    def __repr__(self):
        return "<History('%s','%s', '%s')>" % (self.SubID, self.Name, self.LabCount)
