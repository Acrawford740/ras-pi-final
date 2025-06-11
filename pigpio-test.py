from gpiozero import Device
import os
os.environ["GPIOZERO_PIN_LIBRARY"] = "pigpio"
print(Device.pin_factory)