# -*- coding: utf-8 -*-

MOCK_USERS = {'test@example.com': '123'}

class MockDBHelper:

    def get_user(self, email):
        if email in MOCK_USERS:
            return MOCK_USERS[email]
        return None
