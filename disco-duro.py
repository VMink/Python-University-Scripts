gigabyte = float(input("Ingrese la capacidad de su disco en Gigabytes: "))
megabyte = gigabyte * 1024
kilobyte = megabyte * 1024
byte = kilobyte * 1024
print("Su disco duro tiene: \n",
      gigabyte, "Gigabytes \n",
      megabyte, "Megabytes \n",
      kilobyte, "Kilobytes \n",
      byte, "Bytes")