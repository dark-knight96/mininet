"""
Creates a custom topology with  two switches and six hosts
"""
from mininet.topo import Topo

class custom(Topo):
    def __init__(self):
        Topo.__init__(self)
        hostNames = ["HOST1", "HOST2", "HOST3",
                     "HOST4", "HOST5", "HOST6"]

        switchNames = ["SWITCH1", "SWITCH2"]

        h1 = self.addHost(hostNames[0])
        h2 =  self.addHost(hostNames[1])
        h3 = self.addHost(hostNames[2])
        h4 = self.addHost(hostNames[3])
        h5 = self.addHost(hostNames[4])
        h6 = self.addHost(hostNames[5])

        switch1 = self.addSwitch(switchNames[0])
        switch2 = self.addSwitch(switchNames[1])

        self.addLink(h1, switch1)
        self.addLink(h2, switch1)
        self.addLink(h3, switch1)

        self.addLink(h4, switch2)
        self.addLink(h5, switch2)
        self.addLink(h6, switch2)

topos = {'custom': (lambda: custom())}