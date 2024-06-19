import serial
import time
import json 


def read_Data():
    ser=serial.Serial('COM3',9600,timeout=100)
    if ser:
        print("connection Success")
    line=ser.readline().decode('utf-8').strip()
    print(line)
    data = json.loads(line)  # Parse JSON string to dictionary
    moisture_value = data["Moisture Value"]
    moisture_percentage = data["Moisture Percentage"]
    temperature = data["Temperature"]
    humidity = data["Humidity"]
    print(moisture_percentage,moisture_value,temperature,humidity)
    # try:
    #     line = ser.readline().decode('utf-8').strip()
    #     if line:
    #         # Extract numeric values only
    #         values = [int(s) for s in line.split() if s.isdigit()]
    #         if len(values) == 2:
    #             humidity, temperature = values
    #             print(humidity,temperature)
    #     time.sleep(2)
    # except ValueError as e:
    #     print(f"Error occurred: {e}")
# import json

# def read_from_arduino():
#     ser = serial.Serial('COM3', 9600, timeout=1)  
#     while is_collecting:
#         try:
#             line = ser.readline().decode('utf-8').strip()
#             if line:
#                 data = json.loads(line)  # Parse JSON string to dictionary
#                 moisture_value = data["Moisture Value"]
#                 moisture_percentage = data["Moisture Percentage"]
#                 temperature = data["Temperature"]
#                 humidity = data["Humidity"]
#                 SensorData.objects.create(
#                     moisture_value=moisture_value,
#                     moisture_percentage=moisture_percentage,
#                     temperature=temperature,
#                     humidity=humidity
#                 )
#             time.sleep(2)
#         except Exception as e:
#             print(e)
#             break
#     ser.close()

read_Data()