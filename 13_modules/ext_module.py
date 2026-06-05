# External Modules 
# r = requests.get('https://www.python.org/') # NameError: name 'requests' is not defined
# print("HTTP Status Code: ",r.status_code)

# import requests # ModuleNotFoundError: No module named 'requests'
# r = requests.get('https://www.python.org/') # NameError: name 'requests' is not defined
# print("HTTP Status Code: ",r.status_code)

import requests # First Install Module(pip install requests), then you can use it 
r = requests.get('https://www.python.org/') # NameError: name 'requests' is not defined
print("HTTP Status Code: ",r.status_code)

r = requests.get('https://www.python.org/ravi') 
print("HTTP Status Code: ",r.status_code)