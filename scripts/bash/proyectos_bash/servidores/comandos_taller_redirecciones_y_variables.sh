for i in `seq -w 01 40`; do echo alpine$i; done >servers.txt
for SERVER in `seq -w 01 40`; do sudo virt-clone --original plantilla_alpine --name alpine$SERVER --auto-clone; done
for SERVER in `seq -w 01 40`;do sudo virsh start alpine$SERVER;done
for renault in `cat servers.txt`; do echo "`sudo virsh domifaddr $renault|grep 192.168|awk '{print $4}'|cut -d"/" -f1` $renault"; done |sudo tee -a /etc/hosts
for i in `cat servers.txt`; do ssh -o StrictHostKeyChecking=no root@$i hostname $i; done
for i in `cat servers.txt`; do sudo virsh destroy $i; done
for i in `cat servers.txt`; do sudo virsh undefine $i; done
for i in `cat servers.txt`; do sudo virsh vol-delete $i.qcow2 --pool default; done
for SERVER in `cat server_names`; do sudo virsh vol-delete  $SERVER.qcow2 --pool default; done
