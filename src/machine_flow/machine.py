import random


class CNCMachine:
    def __init__(self, machine_id, name):
        self.machine_id = machine_id
        self.name = name
        self.status = "IDLE"
        self.rpm = 0
        self.spindle_load = 0
        self.temperature = 20.0
        self.parts_produced = 0

    def start(self):
        self.status = "RUNNING"
        self.rpm = 3500

    def stop(self):
        self.status = "IDLE"
        self.rpm = 0
        self.spindle_load = 0

    def update_data(self):
        if self.status == "RUNNING":
            self.rpm = random.randint(3200, 3800)
            self.spindle_load = random.randint(40, 80)
            self.temperature = round(random.uniform(35.0, 55.0), 1)

            if random.random() < 0.3:
                self.parts_produced += 1

    def get_data(self):
        return {
            "machine_id": self.machine_id,
            "name": self.name,
            "status": self.status,
            "rpm": self.rpm,
            "spindle_load": self.spindle_load,
            "temperature": self.temperature,
            "parts_produced": self.parts_produced,
        }