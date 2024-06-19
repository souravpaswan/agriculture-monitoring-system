from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from .models import SensorData
import threading
import serial
import time
import json

is_collecting = False


def read_from_arduino():
    ser = serial.Serial('COM3', 9600, timeout=1)  
    while is_collecting:
        try:
            line = ser.readline().decode('utf-8').strip()
            if line:
                data = json.loads(line)  # Parse JSON string to dictionary
                moisture_value = data["Moisture Value"]
                moisture_percentage = data["Moisture Percentage"]
                temperature = data["Temperature"]
                humidity = data["Humidity"]
                motor_status = data["LED"]
                SensorData.objects.create(
                    moisture_value=moisture_value,
                    moisture_percentage=moisture_percentage,
                    temperature=temperature,
                    humidity=humidity,
                    motor_status=motor_status
                )
                print(data)
            time.sleep(2)
        except Exception as e:
            print(e)
            break
    ser.close()

def start_data(request):
    global is_collecting
    is_collecting = True
    threading.Thread(target=read_from_arduino).start()
    return redirect('/')

def stop_data(request):
    global is_collecting
    is_collecting = False
    return redirect('/')

def display_data(request):
    data = SensorData.objects.all()
    return render(request, 'displaysite.html', {'data': data})

def sensor_data(request):
    latest_data = SensorData.objects.last()
    return JsonResponse({
        'humidity': latest_data.humidity,
        'temperature':latest_data.temperature,
        'moisture_value':latest_data.moisture_value,
        'moisture_percentage':latest_data.moisture_percentage,
        'motor_status':latest_data.motor_status
    })