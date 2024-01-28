import inspect

from SimpleSql.Core.Controller.Controller import Application


class SimpleBaseTable:

    def __init__(self, pre_struct):
        try:
            self.struct = self.__get_structure(pre_struct)
            # check structure for errors
            # send self to the controller singleton
            self.__send_table_to_control()

        except Exception as e:
            raise Exception(f"Exectpion occured while initializing {type(self)}: {e}")

    def __send_table_to_control(self):
        app = Application()
        app.add_table(self)
        # Send table object to the controller singleton

    def __get_structure(self, pre_struct):
        structure = []
        for i in inspect.getmembers(pre_struct):
            if not i[0].startswith('_'):
                if not inspect.ismethod(i[1]):
                    structure.append(i)
        return structure

