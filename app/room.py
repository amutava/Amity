import random


class Room(object):
    def __init__(self, room_name, room_capacity):
        self.room_name = room_name

        self.room_capacity = room_capacity
        self.room_occupants = []

    def get_room_name(self):
        return self.room_name

    def get_room_capacity(self):
        return self.room_capacity


class Office(Room):
    def __init__(self, room_name):
        super(Office, self).__init__(room_name, room_capacity=6)
        self.room_occupants = []

    def allocate_office_space(self, person):
        pass

    def is_full(self):
        if len(self.room_occupants) == self.room_capacity:
            return True

    # def get_room_name(self):
        # return self.room_name

    def get_room_capacity(self):
        return self.room_capacity


class LivingSpace(Room):
    def __init__(self, room_name):
        super(LivingSpace, self).__init__(room_name, room_capacity=6)
        self.room_occupants = []

    def is_full(self):
        if len(self.room_occupants) == self.room_capacity:
            return True
        return len(self.room_capacity)

    def get_room_name(self):
        return self.room_name

    def get_room_capacity(self):
        return self.room_capacity
