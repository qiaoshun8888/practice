"""
Cal center
with 3 levels of employees:
    respondent, manager, director
    implement dispathCall()
"""
import random


class Staff()

    def __init__(self, name, rank, callcenter):
        if rank in ['respondent', 'manager', 'director']:
            self.rank = rank
        else:
            raise ValueError
        self.name = name
        self.callcenter = callcenter
        self.free()

    def pickup(self, call):
        self.busy = True
        self.call = call
        self.callcenter.free_staffs[self.rank].remove(self)

    def cannot_handle(self):
        self.call_queue[self.rank].append(self.call)
        self.free()

    def free(self):
        self.call = None
        self.busy = False
        self.callcenter.free_staffs[self.rank].append(self)


class CallCenter():

    def __init__(self):
        self.call_queue = {}

        for rank in ['none', 'respondent', 'manager']:
            self.hand_queue[rank] = []

        self.free_staffs = {}
        for rank in ['respondent', 'manager', 'director']:
            self.free_staffs[rank] = []

    def callin(self, call):
        self.call_queue['none'].append(call)

    def _dispath(self, staff, queue):
        if len(self.free_staffs[staff]) and self.call_queue[queue]:
            call = self.call_queue[queue].pop(0)
            r = self.free_staffs[staff][
                radom.randrange(len(self.free_staffs[staff]))]
            r.pickup(call)

    def dispatchCall(self):
        self._dispath('respondent', 'none')
        self._dispath('manager', 'respondent')
        self._dispath('director', 'manager')
