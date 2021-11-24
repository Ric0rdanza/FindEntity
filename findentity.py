import re

#Usage:
#    result = FindEntity(text, entity_start_pos, entity_end_pos).foundin

class FindEntity(object):
    def __init__(self, text, start, end):
        __period_pos = self.__helper(text)
        __index_start = self.__bisearch(start, __period_pos)
        __index_end = self.__bisearch(end, __period_pos)
        self.foundin = text[__index_start + 1: __period_pos[__period_pos.index(__index_end) + 1]].strip()
        
    def __helper(self, text):
        period_pos = [-1]
        a = -1
        while True:
            a = text.find(".", a + 1)
            if a == -1:
                break
            else:
                period_pos.append(a)
        return period_pos
        
    def __bisearch(self, target, candidate: list()):
        if len(candidate) == 1:
            return candidate[0]
        index = int(len(candidate) / 2)
        if target < candidate[index]:
            index = self.__bisearch(target, candidate[0: index])
        else:
            index = self.__bisearch(target, candidate[index: len(candidate)])
        return index
    

