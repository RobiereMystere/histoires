from DatabaseManager import DatabaseManager
from DictionaryUtils import DictionaryUtils as Du
from HistoireMaker import HistoireMaker

if __name__ == '__main__':
    dbm = DatabaseManager("database/Histoire.db")
    hm = HistoireMaker(dbm.dictionary)
    Du.print_dict(hm.protagoniste)
    Du.print_dict(hm.situation_initiale)
