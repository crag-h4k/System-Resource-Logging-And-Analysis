import subprocess as sp
import pandas as pd

#cmd = "top -l 1 -stats pid,command,mem,cpu"
cmd = "ps -o pid,command,%mem,%cpu -m -e"
#"top","-l" "1" "-stats pid,command,mem,cpu"

def getStats(cmd):

    sysStats = sp.check_output(cmd,shell=True)
    sysStats = str(sysStats).split("\n")
    
    return sysStats

sysStats = getStats(cmd)
print sysStats
df = pd.DataFrame(sysStats)
df1 = df[0].str.extract('\s+-\s+', expand=True)
#"pid","cmd","mem","cpu"
