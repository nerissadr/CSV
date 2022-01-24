import serial
import csv

f = open("dua.csv", "a", newline="")
writer = csv.writer(f)
ser = serial.Serial ('/dev/ttyACM0',9600) #memulai komunikasi serial dengan ttyUSB1, bisa diubah sesuai port yang terbaca

while True :
    try:
        read_serial=ser.readline().decode('utf-8').rstrip()
        print(read_serial)
        writer.writerow(read_serial)

    except Exception as err:
        print("Error: ".format(err.args))
        
f.close()
