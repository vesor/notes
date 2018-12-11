import subprocess
import json
import time
import signal, sys

runningInstanceId = None

def run_sslocal(ipaddr, passwd):
    subprocess.call(['/usr/local/bin/sslocal', '-s', ipaddr, '-p', '1733', '-l', '3128', '-k', passwd, '-m', 'aes-256-cfb'])

def start_instance(instanceId):
    subprocess.call(['aws', 'ec2', 'start-instances', '--instance-ids', instanceId])

def stop_instance(instanceId):
    subprocess.call(['aws', 'ec2', 'stop-instances', '--instance-ids', instanceId])


def signal_handler(signal, frame):
    global runningInstanceId
    print('Ctrl+C pressed')
    if runningInstanceId is not None:
        print('stopping instance', runningInstanceId)
        stop_instance(runningInstanceId)
    sys.exit(0)

def main(passwd):
    global runningInstanceId

    jsonstr = subprocess.check_output(['aws', 'ec2', 'describe-instances'])

    if len(jsonstr) <= 0:
        return

    data = json.loads(jsonstr)
    for resrv in data["Reservations"]:
        instances = resrv["Instances"]
        for instance in instances:
            state = instance["State"]["Name"]
            if state == "running":
                ipaddr = instance["PublicIpAddress"]
                runningInstanceId = instance["InstanceId"]
                print 'find running instance', ipaddr
                run_sslocal(ipaddr, passwd)
                break
            elif state == "stopped":
                instanceId = instance["InstanceId"]
                print "find stopped instance",instanceId
                start_instance(instanceId)
                time.sleep(6)
                print "instance starting, call main() recursively"
                main(passwd)
                break
            else:
                print "waiting for state", state
                time.sleep(2)
                print "call main() recursively"
                main(passwd)


with open('sspasswd') as f:
    lines = f.read().splitlines()
    if len(lines) <= 0:
        print('no passwd found')
        quit()
    passwd = lines[0]

signal.signal(signal.SIGINT, signal_handler)
main(passwd)
