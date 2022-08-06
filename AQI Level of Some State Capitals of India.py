import matplotlib.pyplot as plt
#Source: Central Pollution Control Board (CPCB)
#Satisfactory=Green, Moderate=Yellow, Poor=Orange, Very Poor=Red, Severe=Dark Red
IndiaAQI={'Chennai':57,'Delhi':72,'Hyderabad':52,'Jaipur':56,'Kolkata':36,'Mumbai':71}
SomeStateCapitalsOfIndia=list(IndiaAQI.keys())
AQILevel=list(IndiaAQI.values())
plt.title('AQI Level of Some State Capitals of India')
plt.xlabel('State Capitals of India')
plt.ylabel('AQI Level')
plt.bar(range(len(IndiaAQI)), AQILevel, tick_label=SomeStateCapitalsOfIndia)
plt.grid(False)
plt.show()