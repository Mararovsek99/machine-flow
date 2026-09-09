import time

from src.machine_flow.simulator import MachineSimulator


simulator = MachineSimulator()

simulator.start_all()

for i in range(10):
    simulator.update_all()

    print(f"\n--- Simulation cycle {i + 1} ---")

    for machine in simulator.machines:
        print(
            machine.machine_id,
            machine.status,
            f"RPM: {machine.rpm}",
            f"Load: {machine.spindle_load}%",
            f"Temp: {machine.temperature}°C",
            f"Parts: {machine.parts_produced}",
        )

    time.sleep(1)

simulator.stop_all()