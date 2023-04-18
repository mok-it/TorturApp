class Team:
    nextId = 0;
    def __init__(self, next_challange_id, is_block_end):
        self.id = self.nextId
        self.nextId = self.nextId + 1
        self.nextChallangeId = next_challange_id
        self.isBlockEnd = is_block_end

    ##change the nextChallangeId
    def changeNextChallangeId(self):
        if(self.nextChallangeId == 5 or self.nextChallangeId==9 or self.nextChallangeId == 12 or self.nextChallangeId == 14):
            is_block_end = True
        else:
            self.nextChallangeId = self.nextChallangeId + 1


    ##write to csv



