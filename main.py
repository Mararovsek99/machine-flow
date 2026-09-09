import time

from src.machine_flow.simulator import MachineSimulator


simulator = MachineSimulator()

simulator.start_all()

for i in range(10):
    simulator.update_all()

    print(f"\n--- Simulation cycle {i + 1} ---")

    for machine_data in simulator.get_all_data():
        print(machine_data)

    time.sleep(1)

simulator.stop_all()