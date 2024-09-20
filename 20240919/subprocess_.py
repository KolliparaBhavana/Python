import subprocess
result1=subprocess.run(['dir'],shell=True,capture_output=True,text=True)
if result1.returncode == 0:
    print(result1.stdout)
else:
    print('Error in running command')
import subprocess
result2=subprocess.run(['python','-c','print(2**8)'],shell=True,capture_output=True,text=True)
print(result2.stdout)