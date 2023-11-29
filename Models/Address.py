import pika
import json
  
class AddressData:
  def __init__(self, state, city, street, houseNumber):
    self.State = state
    self.City = city
    self.Street = street
    self.HouseNumber = houseNumber

  # Define a custom encoder for AddressData
class AddressDataEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, AddressData):
            return obj.__dict__
        return super().default(obj)
