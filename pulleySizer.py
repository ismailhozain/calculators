
import math

maxMotorStallTorque = float(input("Enter the max motor stall torque (N*m): "))
pulleyDiameter = float(input("Enter the pulley diameter (m): "))
pulleyRadius = pulleyDiameter / 2
desiredForce = maxMotorStallTorque / pulleyRadius
print("The driving force from the pulley is " + str(desiredForce) + " N")



