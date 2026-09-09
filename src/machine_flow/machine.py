class CNCMachine:
    def __init__(self, machine_id, name):
        self.machine_id = machine_id
        self.name = name
        self.status = "IDLE"
        self.rpm = 0
        self.spindle_load = 0
        self.temperature = 20.0
        self.parts_produced = 0