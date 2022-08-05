import uiautomator2 as u
import os
d=u.connect()
cmd=("adb shell am start com.android.chrome")
os.system(cmd)
l=[1,2,3,4]
l.append(5)
print(l)
print("the file executed successfully")