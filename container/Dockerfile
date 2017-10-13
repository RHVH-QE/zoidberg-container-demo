FROM fedora:latest
MAINTAINER Daijie Guo <dguo@redhat.com>


# Install pip and third python module
RUN dnf install -y python-pip gcc redhat-rpm-config python2-devel\
    && pip install fabric attrs cffi click cryptography enum34 Flask \
    hiredis idna ipaddress itsdangerous Jinja2 MarkupSafe ordered-set paramiko \
    pyasn1 pycparser pykickstart PyYAML redis requests six Werkzeug

# Copy the files
COPY ./docker_entry.sh /usr/local/bin/docker_entry.sh 

COPY ./test_entry.py /usr/local/bin/test_entry.py

RUN chmod a+x /usr/local/bin/docker_entry.sh \
    && chmod a+x /usr/local/bin/test_entry.py

CMD ["test_entry.py"]

ENTRYPOINT ["/usr/local/bin/docker_entry.sh"]
