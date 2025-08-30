import urllib.request
url = 'https://bootstrap.pypa.io/get-pip.py'
file_name = 'get-pip.py'
urllib.request.urlretrieve(url, file_name)
print("get-pip.py dosyası indirildi.")

# 2. İndirilen get-pip.py dosyasını çalıştır:
# Bu komut pip'i yükler

import os
os.system('python get-pip.py')  # veya 'python3 get-pip.py' kullandığınız sürüme göre

# 3. pip'in yüklendiğini doğrula
os.system('pip --version')  # veya 'pip3 --version'