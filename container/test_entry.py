#!/usr/bin/python2.7
import sys
sys.path.append("/rhvh-auto-ng")
from cases.fabric_run import FabricRun


if __name__ == "__main__":
    ksfile = sys.argv[1]
    host_string = sys.argv[2]
    beakername = sys.argv[3]

    fr = FabricRun()
    fr.host_string = host_string
    fr.ksfile = ksfile
    fr.beaker_name = beakername
    fr.host_user = 'root'
    fr.host_pass = 'redhat'

    cmd = "hostname"
    fr.run(cmd)

    cmd = "date"
    fr.run(cmd)
