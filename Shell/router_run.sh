#set term type if needed (vt100 for Nexus)
#export TERM=vt00

# Rotate logs
timestamp=`date +%Y%m%d%H%M`
 
# Archive last config log
logfile=config.log
newlogfile=$logfile.$timestamp
cp $logfile $newlogfile

user=xcg6761
image=c800-universalk9-mz.SPA.158-3.M5.bin
#user=admin
#image=test.txt

# Get SSH and enable passwords
 echo -n "Enter your SSH password "
 read -s -e password
 echo -ne '\n'
 echo -n "Enter your enable password "
 read -s -e enablepwd
 echo -ne '\n'

# Pull in device list and passwords
for device in `cat router_test_list.txt`; do
    ./config.exp $user $device $password $enablepwd ;
    ./scp_trans.exp $user $device $password $image ;
    check=$(./verify.exp $user $device $password $image | grep check );
    echo "test0"
    echo $check
    echo "test1"
    echo $check | grep OK
    echo "test2"
    echo $check | grep FAILED
    echo "test3"

    checked=$check | grep OK
    echo $checked
    if [ -z $checked ]
    then
        echo "Image OK, continue."
        #./last_expect.exp $user $device $password $enablepwd $image ;
    else
        echo "Image verification failed!"
        ## save hostname to file.
    fi

done
