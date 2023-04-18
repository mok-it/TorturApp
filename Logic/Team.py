class Team:
    nextId = 0;

    def __init__(self, id, nextChallangeId, isBlockEnd):
        self.id = self.nextId
        self.nextId = self.nextId + 1
        self.nextChallangeId = nextChallangeId
        self.isBlockEnd = isBlockEnd

    

