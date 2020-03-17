"""
Creates a custom mesh topology with  two switches and six hosts
"""
from mininet.topo import Topo

class custom(Topo):
    def __init__(self):
        Topo.__init__(self)
        hostNames = ["HOST1", "HOST2", "HOST3",
                     "HOST4", "HOST5", "HOST6"]

        switchNames = ["SWITCH1", "SWITCH2", "SWITCH3", "SWITCH4", "SWITCH5", "SWITCH6"]

        h1 = self.addHost(hostNames[0])
        h2 =  self.addHost(hostNames[1])
        h3 = self.addHost(hostNames[2])
        h4 = self.addHost(hostNames[3])
        h5 = self.addHost(hostNames[4])
        h6 = self.addHost(hostNames[5])

        switch1 = self.addSwitch(switchNames[0])
        switch2 = self.addSwitch(switchNames[1])
        switch3 = self.addSwitch(switchNames[2])
        switch4 = self.addSwitch(switchNames[3])
        switch5 = self.addSwitch(switchNames[4])
        switch6 = self.addSwitch(switchNames[5])

        self.addLink(h1, switch1)
        self.addLink(h2, switch2)
        self.addLink(h3, switch3)

        self.addLink(h4, switch4)
        self.addLink(h5, switch5)
        self.addLink(h6, switch6)

        #Adding links between switches
        i = 0;
        while i< len(switchNames):
            j =0
            while j< len(switchNames) and j != i:
                self.addLink(switchNames[i], switchNames[j])
                j = j+1
            i = i+1

topos = {'custom': (lambda: custom())}