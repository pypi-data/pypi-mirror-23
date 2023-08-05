"""This module shows a simple network topology where routers have set
custom ip(6)table rules, aka ACLs, to control traffic destinated to them
(hence why only INPUT rules are specified).

Only ICMP traffic will be allowed between the routers over
IPv4, whereas IPv6 traffic can only be made of TCP traffic (regularly
established, hence the use of CONNTRACK) or ICMP6 ND/NA."""
from ipmininet.iptopo import IPTopo
from ipmininet.router.config import IPTables, IP6Tables, RouterConfig
from ipmininet.router.config.iptables import Rule


class IPTablesTopo(IPTopo):
    """This is a simple 2-hosts topology with custom IPTable rules."""
    def build(self, *args, **kw):
        config = (RouterConfig, {'daemons': [
            (IPTables, {'rules': [
              Rule('-A INPUT -p icmp -j ACCEPT'),
              Rule('-A INPUT -j DROP')]}),
            (IP6Tables, {'rules': [
                Rule('-A INPUT -p icmpv6 -m icmpv6',
                     '--icmpv6-type neighbour-solicitation -j ACCEPT'),
                Rule('-A INPUT -p icmpv6 -m icmpv6 --icmpv6-type',
                     'neighbour-advertisement -j ACCEPT'),
                Rule('-A INPUT -m conntrack --ctstate RELATED,ESTABLISHED',
                     '-j ACCEPT'),
                Rule('-A INPUT -m conntrack --ctstate INVALID -j DROP'),
                Rule('-A INPUT -p tcp -m tcp --tcp-flags FIN,SYN,RST,ACK SYN',
                     '-m conntrack --ctstate NEW -j ACCEPT'),
                Rule('-A INPUT -j DROP')]})]})
        self.addLink(self.addRouter('r1', config=config),
                     self.addRouter('r2', config=config))
        super(IPTablesTopo, self).build(*args, **kw)
