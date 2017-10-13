#!/usr/bin/python2.7

from container.container import Container


if __name__ == "__main__":
    image = "new:latest"
    ksfile = "atv_bondi_02.ks"
    host_ip = "10.73.73.17"
    beaker_name = "dell-per515-01.lab.eng.pek2.redhat.com"

    # Set docker run
    dr = Container()
    dr.image = image
    dr.ksfile = ksfile
    dr.host_ip = host_ip
    dr.beaker_name = beaker_name

    # Run test
    dr.run_test()
    print "Running test1 in background..."

    # 
    # Run second test
    #
    ksfile2 = "atv_nfs_01.ks"
    host_ip2 = "10.66.8.109"
    beaker_name = "dguo-localhost.nay.redhat.com"

    # Set docker run
    dr2 = Container()
    dr2.image = image
    dr2.ksfile = ksfile2
    dr2.host_ip = host_ip2
    dr2.beaker_name = beaker_name

    # Run test
    dr2.run_test()
    print "Running test2 in background..."
