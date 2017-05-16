#!/usr/bin/python

"""
This example shows how to create a simulation with two roaming hosts and seven APs
"""
from subprocess import call, check_call, check_output
from mininet.net import Mininet
from mininet.node import Node, OVSKernelSwitch, Host, RemoteController, UserSwitch, Controller
from mininet.link import Link, Intf, TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from functools import partial
import sys
flush=sys.stdout.flush

def WifiNet(n, m, IP):

    net = Mininet(switch=OVSKernelSwitch)

    """ Uncomment following lines to add controller """
    # info( '*** Adding controller\n' )
    print(IP)
    #link=partial(TCLink,delay='2ms',bw=10)
    #net.addController('c0',controller=Controller,link=link)
    net.addController( 'c0', controller=RemoteController, ip=IP, port=6653 )

    """ Initialize WifiSegment
        Reference mininet/ns3.py for more detail of WIFISegment class """

    """ Node names """
    hosts = []
    switches = []
    links = []
    hosts.append('dest')
    for i in range(1, n+1):
        hosts.append('ship'+str(i))
    for i in range(1, n+m+1):
        switches.append('s'+str(i))
    #hosts = ['h1', 'h2']
    #switches = ['s1', 's2', 's3', 's4', 's5', 's6', 's7']
    """ Links between APs """
    for i in range(1, n+1):
        links.append([hosts[i], switches[i-1]])
        for j in range(n, n+m):
            links.append([switches[i-1], switches[j]])
        #links.append([switches[i-1],switches[i-1+n]])
    for i in range(n, m+n):
        links.append([hosts[0], switches[i]])
    print(links)



    nodes = {}

    """ Initialize Stations """
    for host in hosts:
        node = net.addHost(host)
        nodes[host] = node

    """ Initialize APs """
    for switch in switches:
        node = net.addSwitch(switch)
        nodes[switch] = node

    """ Add links between APs """
    for link in links:
        name1, name2 = link[0], link[1]
        node1, node2 = nodes[name1], nodes[name2]
        print(name1,name2)
        net.addLink(node1, node2)

    """ Start the simulation """
    info('*** Starting network\n')
    net.start()

    info( 'Testing network connectivity\n' )
    for i in range(1,n+1):
        nodes[hosts[i]].cmdPrint('ping 10.0.0.1 -c 3')

    dst=nodes[hosts[0]]

    ports=[]
    for i in range(n):
        ports.append(1010+i)
        dst.cmdPrint('iperf -s -i 2 -p '+str(ports[i])+' -t 100 >testiperf'+str(i)+'.txt &')

    for i in range(1,n+1):
        src, dst=nodes[hosts[i]],nodes[hosts[0]]
        info("testing",src.name,"<->",dst.name,'\n')
        src.cmdPrint('iperf -c 10.0.0.1 -t 10 -i 2 -p '+str(ports[i-1])+' >src'+str(i)+'.txt &')
        #serverbw,_clientbw=net.iperf([src,dst],seconds=10)
        #info(serverbw, '\n')
        #flush()

    CLI(net)

    net.stop()
    info( '*** net.stop()\n' )

if __name__ == '__main__':
    setLogLevel( 'info' )
    WifiNet(3,3,"131.179.210.194")
