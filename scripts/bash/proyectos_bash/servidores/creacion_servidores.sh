for i in `seq 1 40`; do sudo virt-clone --original alpine_template --name server$i --file /var/lib/libvirt/images/server$i.qcow2 ; done
