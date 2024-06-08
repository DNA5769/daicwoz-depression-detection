import os
import zipfile

for fn in os.listdir():
    if fn.endswith('.zip'):
        with zipfile.ZipFile(fn, 'r') as zip_ref:
            zip_ref.extractall('.')
        for fnn in os.listdir():
            wanted = False
            for suff in ['.py', '.zip', '.', 'TRANSCRIPT.csv', '.wav', '.fdmdownload']:
                if fnn.endswith(suff):
                    wanted = True
                    break
            if not wanted:
                os.remove(fnn)
        os.remove(fn)
