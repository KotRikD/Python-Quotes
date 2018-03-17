from database import *
import random
from datetime import datetime


class MQuo():
    def get_random_quote():
        allq = Quotes.select().dicts()
        if not allq:
            return None
        else:
            q = random.choice(allq)
            return q

    def get_quote(ida):
        q = Quotes.select().where(Quotes.id == ida).dicts()
        try:
            return q.get()
        except:
            return MQuo.get_random_quote()

    def get_count():
        q = Quotes.select()
        return len(q)

    def add_quote(text):
        d = Quotes.create(textqoute=text, date=datetime.today().timestamp())
