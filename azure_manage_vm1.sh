#!/usr/bin/bash

vmname=${1}
action=${2}
loginout=`az login --service-principal --username "6c371b21-5bd7-4f62-99f5-94d9b6c91440" --password "rSdTsGYOrtIJ6q1V9RW_Q4nC1tVr6CHnkK" --tenant "a8fe4acc-1aab-4b3e-a05d-c33b5c88f39a"`
wait
vmstatus=`az vm $action -g "mscoedevopscollection" -n $vmname`
wait
echo "vmName: $vmname"
echo "actionPerformed: $action"
