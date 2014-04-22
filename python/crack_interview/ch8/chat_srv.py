"""
Chat Server
"""
import time


class User():

    def __init__(self, username):
        self.username = username
        self.sessions = {}

    def send(self, session, msg):
        if session in self.sessions:
            session.add(self, msg)

    def get(self, session):
        tmp = session.get_after(self.sessions[session])
        self.sessions[session] = tmp[-1]['id']

    def display(self, msg):
        print '%s: %s' % (msg['user'], msg['msg'])


class Session():

    def __init__(self, participants):
        self.participants = participants
        self.log = []

    def add(self, user, msg):
        content = {
            'id': len(self.log),
            'user': user.username,
            'msg': msg,
            'time': time.time()
        }
        self.log.append(content)

    def push(self, content):
        pass

    def get_after(self, id):
        return self.log[id:]
