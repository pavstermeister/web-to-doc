import time
import progressbar

with progressbar.ProgressBar(max_value=27) as bar:
    for i in range(11):
        time.sleep(0.1)
        bar.update(i)
