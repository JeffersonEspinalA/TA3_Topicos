import sys
import threading
from PySide6.QtWidgets import QApplication
from pade.acl.aid import AID
from pade.behaviours.protocols import TimedBehaviour
from pade.misc.utility import start_loop
from fishagent import FishAgent
from pade.core.agent import Agent

from globals import Global
from gui import Gui

class FishTimedBehaviour(TimedBehaviour):
    def __init__(self, agent, time):
        super(FishTimedBehaviour, self).__init__(agent, time)
        self.agent = agent

    def on_time(self):
        super(FishTimedBehaviour, self).on_time()
        self.agent.updateStatus()
        self.agent.swim()

class MyTimedBehaviour(TimedBehaviour):
    def __init__(self, agent, time):
        super(MyTimedBehaviour, self).__init__(agent, time)
        self.agent = agent

    def on_time(self):
        super(MyTimedBehaviour, self).on_time()
        gui.update()

class YourTimedBehaviour(TimedBehaviour):
    def __init__(self, agent, time):
        super(YourTimedBehaviour, self).__init__(agent, time)
        self.agent = agent

    def on_time(self):
        super(YourTimedBehaviour, self).on_time()
        Global.x_center += 3
        print(Global.x_center)

class HostAgent(Agent):
    gui = None
    num_fishes = 1
    fish_list = []
    enabled = False

    def __init__(self, aid):
        super(HostAgent, self).__init__(aid=aid, debug=False)

        Global.x_center = 0

        for _ in range(self.num_fishes):
            self.fish_list.append(FishAgent())
            # TODO name it and launch it as an agent of chaos

        for fish in self.fish_list:
            self.behaviours.append(FishTimedBehaviour(fish, .2))
    
        mytimed = MyTimedBehaviour(self, .2)
        yourtimed = YourTimedBehaviour(self, 2)
        self.behaviours.append(mytimed)
        self.behaviours.append(yourtimed)

def agentsexec():
    start_loop(agents)

if __name__ == '__main__':
    num_hosts = 50
    agents = list()
    for i in range(num_hosts):
        port = int(sys.argv[1]) + i
        host_agent_name = 'host_agent_{}@localhost:{}'.format(port+1, port+1)
        host_agent = HostAgent(AID(name=host_agent_name))
        agents.append(host_agent)

    x = threading.Thread(target=agentsexec)
    x.start()
    app = QApplication([])
    
    gui = Gui(host_agent)
    host_agent.fish_list[0]
    gui.show()
    app.exec()
    x.join()
