import json


class CatheterPosition:
    def __init__(self, x, y, z, yaw, pitch, roll):
        self.X = x
        self.Y = y
        self.Z = z
        self.Yaw = yaw
        self.Pitch = pitch
        self.Roll = roll

    def get_current_position(self):
        return self

    def move_catheter(self):
        self.X += 0.001
        self.Y += 0.001

    def reset_position(self):
        self.X = 0.0
        self.Y = 0.0
        self.Z = 0.0
        self.Yaw = 0.0
        self.Pitch = 0.0
        self.Roll = 0.0


class CatheterPositionEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, CatheterPosition):
            return obj.__dict__
        return super().default(obj)
