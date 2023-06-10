import shutil #module for disk analysics
import psutil



du = shutil.disk_usage("/")
print(du)
print(du.free / du.total *100)

cpu_use = psutil.cpu_percent(0.2)
print(cpu_use)