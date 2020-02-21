from mininet.topo import Topo
import constants as cn

class customTopo(Topo):
    def __init__(self):
        """
        Creates a tree topology with two switches and four hosts with each switch connected to two hosts.
        """
        Topo.__init__(self)

        host1 = self.addHost(cn.HOST1)
        host2 = self.addHost(cn.HOST2)
        host3 = self.addHost(cn.HOST3)
        host4 = self.addHost(cn.HOST4)

        switch1 = self.addSwitch(cn.SWITCH1)
        switch2 = self.addSwitch(cn.SWITCH2)

        self.addLink(host1, switch1)
        self.addLink(host2, switch1)
        self.addLink(host3, switch2)
        self.addLink(host4, switch2)

topos = {'customtopo' : ( lambda: customTopo())}