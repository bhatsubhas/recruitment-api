import uuid


class Project:
    __id = None
    __name = None
    __start_date = None
    __end_date = None
    __description = None

    #
    #   Constructor
    #

    def __init__(self, name, start_date, end_date, description):
        self.__id = uuid.uuid4()
        self.__name = name
        self.__start_date = start_date
        self.__end_date = end_date
        self.__description = description

    #
    # Properties
    #

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def start_date(self):
        return self.__start_date

    @start_date.setter
    def start_date(self, value):
        self.__start_date = value

    @property
    def end_date(self):
        return self.__end_date

    @end_date.setter
    def end_date(self, value):
        self.__end_date = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    #
    # Methods
    #
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "description": self.description
        }
