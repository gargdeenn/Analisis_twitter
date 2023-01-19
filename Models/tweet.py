from dataclasses import dataclass

@dataclass
class tweet:
    pub_day: str
    pub_month: str
    pub_year: str
    tema: str
    id_city: str
    
    def __init__(self, pubday, pubmonth, pubyear, tema_description, idcity) :
        self.pub_day = pubday
        self.pub_month = pubmonth
        self.pub_year = pubyear
        self.tema = tema_description
        self.id_city = idcity