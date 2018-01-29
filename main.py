import subprocess
from multiprocessing.dummy import Pool
pool = Pool(4)
urls =['you-get https://www.panda.tv/310667 -o c:\\code\\video','you-get https://www.panda.tv/1424867 -o c:\\code\\video',
       'you-get https://www.panda.tv/88888 -o c:\\code\\video','you-get https://www.panda.tv/727250 -o c:\\code\\video']
result = pool.map(subprocess.call,urls)