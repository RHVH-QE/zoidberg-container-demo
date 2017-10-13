import docker
import time
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
client = docker.from_env()


class Container(object):
    """Module for manage container lifecycle such as run/rm etc
    """
    def __init__(self):
        self._image = None
        self._ksfile = None
        self._host_ip = None
        self._beaker_name = None
        self._container = None

    @property
    def image(self):
        # To do check if image exist
        return self._image

    @image.setter
    def image(self, val):
        self._image = val

    @property
    def ksfile(self):
        return self._ksfile

    @ksfile.setter
    def ksfile(self, val):
        self._ksfile = val
        
    @property
    def host_ip(self):
        return self._host_ip

    @host_ip.setter
    def host_ip(self, val):
        self._host_ip = val

    @property
    def beaker_name(self):
        return self._beaker_name

    @beaker_name.setter
    def beaker_name(self, val):
        self._beaker_name = val

    def _get_test_cmd(self):
        cmd = "/rhvh-auto-ng/container/test_entry.py"
        cmd_list = [cmd, self.ksfile, self.host_ip, self.beaker_name]
        return " ".join(cmd_list)

    def _check_image(self):
        # TO DO check image exists
        return True

    def _check_requirement(self):
        if not self._ksfile: 
            return False

        if not self._host_ip:
            return False

        if not self._check_image():
            return False
        
        return True

    def _get_mount_volumes(self):
        volumes_to_mount = [':'.join([PROJECT_ROOT, '/rhvh-auto-ng'])]
        return volumes_to_mount

    def _get_extra_host(self):
        extra_hosts = {"rhvm41-vdsm-auto.lab.eng.pek2.redhat.com": "10.73.75.48"}
        return extra_hosts

    def _finish_notify(self):
        # TO DO
        pass

    def run_test(self):
        """Run container from image"""
        # Check requirement
        if not self._check_requirement():
            return

        # Run command for container
        test_cmd = self._get_test_cmd()

        # Mount volumes
        volumes = self._get_mount_volumes()

        # Extra hosts to resolve
        extra_hosts = self._get_extra_host()

        try:
            self._container = client.containers.run(
                image=self.image,
                command=test_cmd,
                volumes=volumes,
                extra_hosts=extra_hosts,
                privileged=True,
                detach=True,
                remove=False)
        except Exception as e:
            print e

        # Notify framework after test
        self._finish_notify()
