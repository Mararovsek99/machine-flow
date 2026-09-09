from src.machine_flow.machine import CNCMachine


class MachineSimulator:
    def __init__(self):
        self.machines = [
            CNCMachine("CNC-01", "Machine 1"),
            CNCMachine("CNC-02", "Machine 2"),
            CNCMachine("CNC-03", "Machine 3"),
            CNCMachine("CNC-04", "Machine 4"),
            CNCMachine("CNC-05", "Machine 5"),
        ]

    def start_all(self):
        for machine in self.machines:
            machine.start()

    def update_all(self):
        for machine in self.machines:
            machine.update_data()

    def stop_all(self):
        for machine in self.machines:
            machine.stop()