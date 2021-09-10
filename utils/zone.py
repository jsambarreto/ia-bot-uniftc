from datetime import date,datetime,tzinfo,timedelta

hora = datetime.now().strftime('%H:%M')

class Zone(tzinfo):
    def __init__(self,offset,isdst,name):
        self.offset = offset
        self.isdst = isdst
        self.name = name
    def utcoffset(self, dt):
        return timedelta(hours=self.offset) + self.dst(dt)
    def dst(self, dt):
            return timedelta(hours=1) if self.isdst else timedelta(0)
    def tzname(self,dt):
         return self.name
    def hora():
        BRA = Zone(-3, False, 'BRA')
        hora = datetime.now(BRA).strftime('%H:%M')
        return hora
