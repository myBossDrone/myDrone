import spidev
import subprocess

swt_channel = 0
vrx_channel = 1
vry_channel = 2
spi = spidev.SpiDev()
spi.open(0,1)
userLogin = True

def readChannel(channel):
    val = spi.xfer2([1,(8 + channel) << 4,0])
    data = ((val[1]&3) << 8) + val[2]
    return data

def intToString(nr):
    word = str(nr)
    return word

#Wird ersetzt durch RFID
def logIn():
    userLogin = True
    return userLogin

#Wird ersetzt durch RFID
def logOut():
    userLogin = False
    return userLogin

while userLogin:
    code = readChannel(vrx_channel)
    tmp = subprocess.check_call(['/home/pi/Documents/433Utils/RPi_utils/./codesend',intToString(code)])
    print(tmp)
    code = readChannel(vry_channel)
    tmp = subprocess.check_call(['/home/pi/Documents/433Utils/RPi_utils/./codesend',intToString(code)])
    print(tmp)
    code = readChannel(swt_channel)
    tmp = subprocess.check_call(['/home/pi/Documents/433Utils/RPi_utils/./codesend',intToString(code)])
    print(tmp)
