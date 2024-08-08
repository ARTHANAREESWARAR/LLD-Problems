from abc import ABC,abstractmethod

class Vending_Machine(ABC):
    def __init__(self,vending_machine):
        self.vending_machine = vending_machine

    @abstractmethod

    def select_product(self,product):
        pass

    @abstractmethod

    def insert_coin(self,coin):
        pass

    @abstractmethod

    def insert_note(self,note):
        pass

    @abstractmethod

    def dispense_product(slef):
        pass

    @abstractmethod

    def return_change(self):
        pass

