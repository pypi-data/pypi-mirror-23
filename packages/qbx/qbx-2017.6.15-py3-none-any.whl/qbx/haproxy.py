import os
from docopt import docopt as docoptinit
import datetime

haproxy_doc = """
Usage:
    haproxy.py [options]

Options:
    --port=<port>
    --dest=<dest>
    --timeout_server=<t>         Timeout For Server [default: 86400000]

"""


# haproxy --port port --dest host:port
def haproxy(argv):
    docopt = docoptinit(haproxy_doc, argv)
    print(docopt)
    port = int(docopt['--port'])
    opt = {'dest': docopt['--dest'], 'timeout_server': docopt['--timeout_server']}
    cfg = """
    global
        debug
        log 127.0.0.1 local0
        maxconn 20480

    defaults
        mode tcp
        log     global
        option tcplog
        option tcp-check
        timeout connect 5000
        timeout client  86400000 # 1day 86400 * 1000 ms
        timeout server  {timeout_server}


    frontend shadow1
        bind :9998
        option tcplog
        default_backend haproxy-nodes

    backend haproxy-nodes
        server node-1 {dest} check

    """.format(**opt)
    print(cfg)
    filename = '/tmp/haproxy-{}.cfg'.format(str(int(datetime.datetime.now().timestamp() * 10e6)))
    fp = open(filename, 'w')
    fp.write(cfg)
    fp.close()
    cmd = 'sudo docker run -it --rm -v {}:/usr/local/etc/haproxy/haproxy.cfg -p {}:9998 haproxy'.format(filename, port)
    os.system(cmd)

if __name__ == '__main__':
    haproxy(['--port', '123'])
