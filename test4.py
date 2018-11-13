"""Custom topology example
RING Topology(Loop),
Switch1-----Switch2------Switch3-----Switch4-----Switch1
Switch1-----Host1
Switch2-----Host2
Switch3-----Host3
Switch4-----Host4
MAC,IP, Controller, CLI stuff configured
"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import OVSSwitch, Controller, RemoteController

class SingleSwitchTopo(Topo):
    "Single switch connected to n hosts."
    def build(self):
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')


        h1 = self.addHost('h1')
        h2 = self.addHost('h2')


        self.addLink(h1, s1)
        self.addLink(h2, s2)



        self.addLink(s1, s2)


topos = { 'mytopo': ( lambda: SingleSwitchTopo() ) }

if __name__ == '__main__':
    setLogLevel('info')
    topo = SingleSwitchTopo()
    c1 = RemoteController('c1', ip='127.0.0.1')
    net = Mininet(topo=topo, controller=c1)
    net.start()
    #net.pingAll()
    CLI(net)
    net.stop()

