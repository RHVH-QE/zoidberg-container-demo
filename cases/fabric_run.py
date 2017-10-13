from fabric.api import settings, run


def loginfo(message):
    print "INFO:{}".format(message)


def logerror(message):
    print "ERROR:{}".format(message)


class FabricRun(object):

    def __int__(self):
        self.ksfile = None
        self.host_string = None
        self.beaker_name = None
        self.host_user = None
        self.host_pass = None

    @property
    def host_string(self):
        return self._host_string

    @host_string.setter
    def host_string(self, val):
        # TODO check val
        self._host_string = val

    @property
    def host_user(self):
        return self._host_user

    @host_user.setter
    def host_user(self, val):
        self._host_user = val

    @property
    def host_pass(self):
        return self._host_pass

    @host_pass.setter
    def host_pass(self, val):
        self._host_pass = val

    @property
    def beaker_name(self):
        return self._beaker_name

    @beaker_name.setter
    def beaker_name(self, val):
        self._beaker_name = val

    @property
    def ksfile(self):
        return self._ksfile

    @ksfile.setter
    def ksfile(self, val):
        self._ksfile = val

    def run(self, cmd):
        ret = self._run_cmd(cmd)
        loginfo(ret[1])

    def _run_cmd(self, cmd, timeout=60):
        ret = None
        try:
            with settings(
                    host_string=self.host_string,
                    user=self.host_user,
                    password=self.host_pass,
                    disable_known_hosts=True,
                    connection_attempts=60):
                ret = run(cmd, quiet=True, timeout=timeout)
                if ret.succeeded:
                    loginfo('Run cmd "%s" succeeded' % cmd)
                    return True, ret
                else:
                    logerror('Run cmd "%s" failed' % cmd)
                    return False, ret
        except Exception as e:
            logerror('Run cmd "%s" failed with exception "%s"' % (cmd, e))
            return False, e
