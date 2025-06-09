from simple_pid import PID
from pymodbus.client import ModbusTcpClient
from time import sleep

client = ModbusTcpClient('plc', port=5020)
pid = PID(2.1, 0.8, 0.05, setpoint=180, sample_time=1.0, output_limits=(0, 100))

while True:
    pv = client.read_holding_registers(0, 1).registers[0] / 10
    cv = pid(pv)
    client.write_register(10, int(cv*10))  # válvula de combustível
    sleep(1)
    
    