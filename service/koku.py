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

    def get_koku_by_id(self, _id):
        return self.__koku.find_by_id(_id)

    def get_koku_categories_by_id(self, _id):
        return self.__koku.find_by_id(_id)

    def get_item_of_category_by_id(self, _id, _item_id):
        return self.__koku.find_by_children(_id, _item_id)

    def update_category_picture(self, _id, _category_id):
        return self.__koku.find_by_id(_id)

    def remote_list_of_items(self, _id, _category_id, item_list):
        category_items = self.__koku.find_by_children(_id, _category_id)
        c_items = category_items['items']
        updated_items = []
        for j in c_items:

            if j['title'] in item_list:
                updated_items.append(j)

        category_items['items'] = updated_items
        new_list = self.__koku.find_by_id(_id)['categories']
        for index, k in enumerate(new_list):
            if k['_id'] == _category_id:
                new_list[index] = category_items
                break
        self.__koku.update_by_id(_id, key="categories", value=new_list)
        return self.__koku.find_by_id(_id)

    def update_all_categories(self, _id, category_list):
        self.__koku.update_by_id(_id, key="categories", value=category_list['categories'])
        return self.__koku.find_by_id(_id)
        # return category_list['categories']

    def put_new_category(self, _id, new_category):
        self.__koku.update_by_id(_id, key="categories", value=new_category, aggregate=PUSH)
        return self.__koku.find_by_id(_id)
