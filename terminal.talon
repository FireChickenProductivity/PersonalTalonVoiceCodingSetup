app: MobaXterm
app: WindowsTerminal.exe
app: Terminal
app: Google Chrome
and title: /jupyterlab/i
and not tag: user.exam_mode
app: Code
and tag: user.terminal_chicken
app: Visual Studio Code
and tag: user.terminal_chicken
app: VMware Fusion
-
g c c: 'gcc *.c'
move: 'cd '
show: 'ls '
a out: './a.out'
gedit: 'gedit '
here: './'
above: '../'
make: 'mk'
dir: 'dir '
remove: 'rm '
recurse|recursively: '-r '

cat: 'cat '

(H D F S|hadoop) start: 'start-dfs.sh'
(H D F S|hadoop) stop: 'stop-dfs.sh'
hadoop home: '$HADOOP_HOME'
#Only do this when you first use your cluster
(H D F S|hadoop) initialize: 'hdfs namenode -format'
yarn start: 'start-yarn.sh'
yarn stop: 'stop-yarn.sh'
stand alone yarn start: '$HADOOP_HOME/sbin/start-yarn.sh'
stand alone yarn stop: '$HADOOP_HOME/sbin/stop-yarn.sh'
hadoop config: 'hadoopConf'
hadoop show: 'hadoop fs -ls /'
hadoop (new folder|make Durr): 'hadoop fs -mkdir /'
hadoop (upload|put): 'hadoop fs -put '
hadoop remove: 'hadoop fs -rm -r /'
hadoop jar: 'hadoop jar '
hadoop java: 'hadoop com.sun.tools.javac.Main '
hadoop compile: 'hadoop com.sun.tools.javac.Main *.java'
class move: 'mv ./*.class ./'
hadoop daemon: '$HADOOP_HOME/sbin/hadoop-daemon.sh '
hadoop f s: 'hadoop fs -'
hadoop copy to local: 'hadoop fs -copyToLocal '
stop data node: 'hadoop --daemon stop datanode'
start data node: 'hadoop --daemon start datanode'
yarn job: ' -D mapreduce.framework.name=yarn '
untar: 'tar xvf '
tar: 'tar -cvf '
jar (new|create): 'jar cf '
part are: 'part-r-00000'

spark start:
    insert('start-dfs.sh\n')
    insert('start-master.sh\n')
    insert('start-workers.sh\n')

spark stop:
    insert('stop-master.sh\n')
    insert('stop-workers.sh\n')
    insert('stop-dfs.sh\n')

conda activate [python] environment: 'conda activate '
conda deactivate [python] environment: 'conda deactivate'
conda: 'conda '
[create] python environment [create|new]: 'python -m venv '
python environment source [activate]: 'source .venv/bin/activate'
python environment deactivate: 'deactivate\n'
pip install: 'pip install '
pip install [jupiter] notebook: 'pip install notebook'
pip install mat plot lib: 'pip install matplotlib'
pip install from requirements: "pip install -r requirements.txt"
jupiter [notebook]: 'jupyter notebook'
source: 'source '
venv ben activate: '.venv/bin/activate'

user [home]: '~/'
bash rc: 'bashrc'
main bash rc: '~/.bashrc'
s s h: 'ssh '
exit: 'exit'
apt get: 'apt-get '
apt install: 'apt-get install '
pseudo: 'sudo '


change mod: 'chmod '
lookup: 'nslookup'
lookup experiment:
    insert('nslookup jsonlint.com\n')
    sleep(5)
    insert('nslookup www.mathematicalgemstones.com\n')
    sleep(5)
    insert('nslookup www.diagrams.net\n')


