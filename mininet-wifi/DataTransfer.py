#!/usr/bin/python

'Setting the position of nodes and providing mobility'

import sys

from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi


def topology(args):
    "Create a network."
    net = Mininet_wifi()

    info("*** Creating nodes\n")
    net.addStation('mn1', mac='00:00:00:00:00:01', ip='10.0.0.1/24', min_x=75, max_x=125, min_y=75, max_y=125, ConstantDistance=1, min_v=1, max_v=3)
    net.addStation('mn2', mac='00:00:00:00:00:02', ip='10.0.0.2/24', min_x=75, max_x=125, min_y=75, max_y=125, ConstantDistance=1, min_v=1, max_v=3)
    net.addStation('mn3', mac='00:00:00:00:00:03', ip='10.0.0.3/24', min_x=75, max_x=125, min_y=75, max_y=125, ConstantDistance=1, min_v=1, max_v=3)
    net.addStation('mn4', mac='00:00:00:00:00:04', ip='10.0.0.4/24', min_x=75, max_x=125, min_y=75, max_y=125, ConstantDistance=1, min_v=1, max_v=3)
   

    net.addStation('sn1', mac='00:00:00:00:01:00', ip='10.0.0.5/24', min_x=80, max_x=120, min_y=80, max_y=120, ConstantDistance=1, min_v=1, max_v=3)
    net.addStation('sn2', mac='00:00:00:00:02:00', ip='10.0.0.6/24', min_x=80, max_x=120, min_y=80, max_y=120, ConstantDistance=1, min_v=1, max_v=3)
    net.addStation('sn3', mac='00:00:00:00:03:00', ip='10.0.0.7/24', min_x=80, max_x=120, min_y=80, max_y=120, ConstantDistance=1, min_v=1, max_v=3)
    net.addStation('sn4', mac='00:00:00:00:04:00', ip='10.0.0.8/24', min_x=80, max_x=120, min_y=80, max_y=120, ConstantDistance=1, min_v=1, max_v=3)
    
    net.addStation('sn5', mac='00:00:00:00:05:00', ip='10.0.0.9/24', min_x=80, max_x=120, min_y=80, max_y=120, ConstantDistance=1, min_v=1, max_v=3)
    net.addStation('sn6', mac='00:00:00:00:06:00', ip='10.0.0.10/24', min_x=80, max_x=120, min_y=80, max_y=120, ConstantDistance=1, min_v=1, max_v=3)
    net.addStation('sn7', mac='00:00:00:00:07:00', ip='10.0.0.11/24', min_x=80, max_x=120, min_y=80, max_y=120, ConstantDistance=1, min_v=1, max_v=3)
    net.addStation('sn8', mac='00:00:00:00:08:00', ip='10.0.0.12/24', min_x=80, max_x=120, min_y=80, max_y=120, ConstantDistance=1, min_v=1, max_v=3)
    
    net.addStation('sn9', mac='00:00:00:00:09:00', ip='10.0.0.13/24', min_x=80, max_x=120, min_y=80, max_y=120, ConstantDistance=1, min_v=1, max_v=3)
    net.addStation('sn10', mac='00:00:00:00:10:00', ip='10.0.0.14/24', min_x=80, max_x=120, min_y=80, max_y=120, ConstantDistance=1, min_v=1, max_v=3)
    net.addStation('sn11', mac='00:00:00:00:11:00', ip='10.0.0.15/24', min_x=80, max_x=120, min_y=80, max_y=120, ConstantDistance=1, min_v=1, max_v=3)
    net.addStation('sn12', mac='00:00:00:00:12:00', ip='10.0.0.16/24', min_x=80, max_x=120, min_y=80, max_y=120, ConstantDistance=1, min_v=1, max_v=3)
  
    net.addStation('sn13', mac='00:00:00:00:13:00', ip='10.0.0.17/24', min_x=80, max_x=120, min_y=80, max_y=120, ConstantDistance=1, min_v=1, max_v=3)
    net.addStation('sn14', mac='00:00:00:00:14:00', ip='10.0.0.18/24', min_x=80, max_x=120, min_y=80, max_y=120, ConstantDistance=1, min_v=1, max_v=3)
    net.addStation('sn15', mac='00:00:00:00:15:00', ip='10.0.0.19/24', min_x=80, max_x=120, min_y=80, max_y=120, ConstantDistance=1, min_v=1, max_v=3)
    net.addStation('sn16', mac='00:00:00:00:16:00', ip='10.0.0.20/24', min_x=80, max_x=120, min_y=80, max_y=120, ConstantDistance=1, min_v=1, max_v=3)

    net.addStation('sn17', mac='00:00:00:00:17:00', ip='10.0.0.21/24', min_x=80, max_x=120, min_y=80, max_y=120, ConstantDistance=1, min_v=1, max_v=3)
    net.addStation('sn18', mac='00:00:00:00:18:00', ip='10.0.0.22/24', min_x=80, max_x=120, min_y=80, max_y=120, ConstantDistance=1, min_v=1, max_v=3)
    net.addStation('sn19', mac='00:00:00:00:19:00', ip='10.0.0.23/24', min_x=80, max_x=120, min_y=80, max_y=120, ConstantDistance=1, min_v=1, max_v=3)
    net.addStation('sn20', mac='00:00:00:00:20:00', ip='10.0.0.24/24', min_x=80, max_x=120, min_y=80, max_y=120, ConstantDistance=1, min_v=1, max_v=3)
    
    ap1 = net.addAccessPoint('ap1', ssid='new-ssid', mode='g', channel='1',
                             position='100,100,0')
    c1 = net.addController('c1')

    info("*** Configuring propagation model\n")
    net.setPropagationModel(model="logDistance", exp=5)

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

   
    if '-p' not in args:
        net.plotGraph(max_x=200, max_y=200)

    net.setMobilityModel(time=0, model='RandomWalk',
                         max_x=200, max_y=200, seed=5)



    info("*** Starting network\n")
    net.build()
    c1.start()
    ap1.start([c1])

    info("*** Running CLI\n")
    CLI(net)

    info("*** Stopping network\n")
    net.stop(time=1000)


if __name__ == '__main__':
    setLogLevel('info')
    topology(sys.argv)
