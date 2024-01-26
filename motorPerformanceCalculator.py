
import math

motorMaxRPM = int(input("Enter the max motor RPM: "))
maxVoltage = int(input("Enter the max voltage: "))
maxCurrent = int(input("Enter the max amperage your motor pulls on max current: "))
RPMatMaxLoad = int(input("Enter the RPM at max load (this should be quite low, if you do not know, a good guess if 0.05x max RPM): "))
kv = motorMaxRPM / maxVoltage
#the units on this are RPM/V

#they need to be converted to rad/s/V
kvRadians = kv * 2 * math.pi / 60
kt = 1 / kvRadians

maxTorque = kt * maxCurrent
#units are N*m
mechanicalPower = maxTorque * RPMatMaxLoad * 2 * math.pi / 60
print("kv: " + str(kv))
print("max torque: " + str(maxTorque) + " N*m")
print("mechanical power: " + str(mechanicalPower) + " W")
print("note, this result is probably correct to within 10-50%, use only for back of napkin/order of magnitude calculations")







