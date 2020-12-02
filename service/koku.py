from repository.database import *


class KokuService:
    def __init__(self):
        self.__koku = CONNECTION.collection["koku"]

    def add_koku(self, _id, koku: dict):
        ku = f"{_id}"
        self.__koku.add_by_id(ku, koku)
        return self.__koku.find_by_id(ku)

    def get_kokus(self):
        return self.__koku.find_all()

    def get_koku_by_id(self,_id):
        return self.__koku.find_by_id(_id)

    def get_koku_categories_by_id(self, _id):
        return self.__koku.find_by_id(_id)

    def get_koku_categories_items_by_id(self,_id, category_id):
        return self.__koku.find_by_id(_id)