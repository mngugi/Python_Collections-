<<<<<<< Tabnine <<<<<<<
import speedtest

#-
def checkNetSpeed():
#-
    speed = speedtest.Speedtest()#+
    print(f'Download speed is : {speed.download()/8000000:.2f}mb')
    print(f'Upload speed is : {speed.download()/8000000:.2f}mb')#-
    print(f'Upload speed is : {speed.upload()/8000000:.2f}mb')#+

#-
checkNetSpeed()
>>>>>>> Tabnine >>>>>>>
