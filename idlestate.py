from vending_machine_state import VendingMachineState
from coin import Coin
from product import Product
from note import Note

class IdleState( VendingMachineState):
    def __init__(self,vending_machine):
        self.vending_machine = vending_machine

    def select_product(self,product : Product):
        if self.vending_machine.inventory.is_available(product):
            self.vending_machine.selected_product = product
            self.vending_machine.set_state(self.vending_machine.ready_state)
            print(f"product selected : {product.name}")

        else:
            print(f"poduct not available{product.name}")

    def insert_coins(self,coin : Coin)
        print("first select product")

    def insert_note(self,note:Note):
        print("first select product")


    def dispense_product(self):
        print("Please select a product and make payment.")

    def return_change(self):
        print("No change to return.")

