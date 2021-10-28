#set term type if needed (vt100 for Nexus)
#export TERM=vt00

# Rotate logs
timestamp=`date +%Y%m%d%H%M`
 
# Archive last config log
logfile=config.log
newlogfile=$logfile.$timestamp
cp $logfile $newlogfile

image=test.txt
#user=xcg6761
user=admin

# Get SSH and enable passwords
 echo -n "Enter your SSH password "
 read -s -e password
 echo -ne '\n'
 echo -n "Enter your enable password "
 read -s -e enable
 echo -ne '\n'

# Pull in device list and passwords
for device in `cat router_test_list.txt`; do
    test=(./config.exp $user $device $password $enable | grep Failed) ;
    echo "Test"
    echo $test
    echo "Test2"
    #./scp_trans.exp $user $device $password $enable $image ;
    #./verify.exp $user $device $password $enable $image ;
    #./last_expect.exp $user $device $password $enable $image ;
done
