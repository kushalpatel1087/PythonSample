from abc import ABCMeta, abstractmethod

class MasterClass:
    __MetaClass__ = ABCMeta

    @abstractmethod
    def setUp():
        pass

    @abstractmethod
    def tearDown():
        pass