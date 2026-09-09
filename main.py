from src.machine_flow.machine import CNCMachine

machine = CNCMachine("CNC-01", "Machine 1")

print(machine.machine_id)
print(machine.name)
print(machine.status)
print(machine.temperature)