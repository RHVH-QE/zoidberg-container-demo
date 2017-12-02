#!/usr/bin/python2.7

import sys
from container.container import Container


if __name__ == "__main__":
    host_ip1 = sys.argv[1]
    host_ip2 = sys.argv[2]

    image = "zoidberg:latest"

    ksfile1 = "atv_bondi_02.ks"
    beaker_name1 = "dell-per515-01.lab.eng.pek2.redhat.com"

    # Set docker run
    dr = Container()
    dr.image = image
    dr.ksfile = ksfile1
    dr.host_ip = host_ip1
    dr.beaker_name = beaker_name1

    # Run test
    dr.run_test()
    print "Running test1 in background..."

    # 
    # Run second test
    #
    ksfile2 = "atv_nfs_01.ks"
    beaker_name2 = "dguo-localhost.nay.redhat.com"

    # Set docker run
    dr2 = Container()
    dr2.image = image
    dr2.ksfile = ksfile2
    dr2.host_ip = host_ip2
    dr2.beaker_name = beaker_name2

    # Run test
    dr2.run_test()
    print "Running test2 in background..."
