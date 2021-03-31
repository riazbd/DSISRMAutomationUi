import os
import pathlib
from datetime import datetime
time = str(datetime.today().strftime('%Y-%m-%d'))
print(time)
path = pathlib.Path(__file__).parent / "new.txt"
fileToRead =open(path, 'r+')
data = int(fileToRead.read())
# print(type(data))

newData = (data + 1)

fileToRead.seek(0)
fileToRead.write(str(newData))
fileToRead.truncate()
fileToRead.close()

fileToReadForNewData = open(path, 'r')
readNewData = fileToReadForNewData.read()
fileToReadForNewData.close()
command = "pytest --alluredir=Reports/"+ time + "_" + readNewData + " " + "tests"
# print(command)
os.system(command)


os.system("allure serve "+"Reports/" + time + "_" + readNewData)