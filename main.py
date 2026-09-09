import time

from src.machine_flow.machine import CNCMachine


machine = CNCMachine("CNC-01", "Machine 1")

machine.start()

for i in range(10):
    machine.update_data()

    print(
        machine.machine_id,
        machine.status,
        machine.rpm,
        machine.spindle_load,
        machine.temperature,
        machine.parts_produced,
    )

    time.sleep(1)