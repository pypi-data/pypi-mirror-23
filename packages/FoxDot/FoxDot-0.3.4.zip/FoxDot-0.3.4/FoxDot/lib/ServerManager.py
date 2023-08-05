"""
    ServerManager.py

    Handles OSC messages being sent to SuperCollider.

"""

import os, socket
import signal
import subprocess 
from time import sleep
from Settings import *
from OSC import *
from Code import WarningMsg

class SCLangClient(OSCClient):
    def send(*args, **kwargs):
        try:
            OSCClient.send(*args, **kwargs)
        except Exception as e:
            print(e)

class SCLangServerManager:

    metro = None

    def __init__(self, addr, osc_port, sclang_port):

        self.addr = addr
        self.port = osc_port
        self.SCLang_port = sclang_port

        self.booted = False
        self.wait_time = 5
        self.count = 0

        self.client = SCLangClient()
        self.client.connect( (self.addr, self.port) )

        self.sclang = SCLangClient()
        self.sclang.connect( (self.addr, self.SCLang_port) )        

        self.node = 1000
        self.bus  = 4

        self.fx_setup_done = False
        self.fx_names = {}

        # Toggle debug
        # ------------

        self.dumpOSC(0)

    def __str__(self):
        return "FoxDot ServerManager Instance -> {}:{}".format(self.addr, self.port)

    def __repr__(self):
        return str(self)

    def nextnodeID(self):
        self.node += 1
        return self.node

    def query(self):
        self.client.send(OSCMessage("/status"))
        return

    def nextbusID(self):
        if self.bus > 100:
            self.bus = 4
        self.bus += 1
        return self.bus

    def sendOSC(self, packet):
        """ Compiles and sends an 's_new' OSC message for SuperCollider """
        message = OSCMessage("/s_new")
        node = packet[1] = self.nextnodeID()
        message.append(packet)
        self.client.send( message )        
        return

    def freeAllNodes(self):
        msg = OSCMessage("/g_freeAll")
        msg.append([1])
        self.client.send(msg)
        return

    def setFx(self, fx_list):
        self.fx_names = {name: fx.synthdef for name, fx in fx_list.items() }
        return

    def sendMidiMessage(self, event):
        pass

    def sendPlayerMessage(self, synthdef, packet, effects, player=None):

        ## todo -- should packet be a dict?

        ## todo -- make this more elegant

        if synthdef == "MidiOut":

            note    = packet[packet.index("midinote") + 1]
            vel     = min(127, (packet[packet.index("amp") + 1] * 128) - 1)
            sus     = packet[packet.index("sus") + 1]
            channel = packet[packet.index("channel") + 1]

            return [synthdef, note, vel, sus, channel]
        
        # Create a bundle
        bundle = OSCBundle()

        # Create a group for the note
        group_id = self.nextnodeID()
        msg = OSCMessage("/g_new")
        msg.append( [group_id, 1, 1] )
        bundle.append(msg)

        # Get the bus and SynthDef nodes
        this_bus  = self.nextbusID()
        this_node = self.nextnodeID()

        # Make sure messages release themselves after 8 * the duration at max (temp)
        i = packet.index('sus') + 1
        max_sus = float(packet[i] * 8)

        # Synth
        msg = OSCMessage("/s_new")

        new_packet = []

        for i in range(0, len(packet), 2):

            try:

                packet[i+1] = float(packet[i+1])

            except TypeError as e:

                WarningMsg( "Could not convert '{}' argument '{}' to float. Set to 0".format( packet[i], packet[i+1] ))
                packet[i+1] = 0.0
                
        packet = [synthdef, this_node, 0, group_id, 'bus', this_bus] + packet
        msg.append( packet )
        bundle.append(msg)

        # Effects
        for fx in effects:

            this_effect = effects[fx]

            # effects should not have 0 values for the first argument

            nonzero = True

            for i in range(0, len(this_effect), 2):

                try:

                    val = float(this_effect[i+1])

                except TypeError as e:

                    WarningMsg( "Could not convert '{}' argument '{}' to float. Set to 0".format( this_effect[i], this_effect[i+1] ))

                    val = 0

                if i == 0 and val == 0:

                    nonzero = False

                else:

                    this_effect[i+1] = val

            if nonzero:

                # Get next node ID
                this_node, last_node = self.nextnodeID(), this_node
                msg = OSCMessage("/s_new")
                packet = [self.fx_names[fx], this_node, 1, group_id, 'bus', this_bus] + this_effect
                msg.append(packet)
                bundle.append(msg)

        # Finally, output sound through end node "makeSound"
        msg = OSCMessage("/s_new")
        this_node, last_node = self.nextnodeID(), this_node
        packet = ['makeSound', this_node, 1, group_id, 'bus', this_bus, 'sus', max_sus]
        msg.append(packet)
        bundle.append(msg)
        
        return bundle        

    def send(self, address, message):
        """ Sends message (a list) to SuperCollider """
        msg = OSCMessage(address)
        msg.append(message)
        self.client.send(msg)
        return

    def free_node(self, node):
        message = OSCMessage("/n_free")
        message.append(node)
        self.client.send( message )
        return

    # Buffer Communiation
    # -------------------

    def bufferRead(self, path, bufnum):
        message = OSCMessage("/b_allocRead")
        message.append([bufnum, path])
        self.client.send( message )
        return

    # Midi Messages
    # -------------

    def sendMidi(self, data, cmd="/foxdot_midi"):
        msg = OSCMessage()
        msg.append(data)
        msg.setAddress(cmd)
        self.sclang.send(msg)
        return

    # SynthDef Commmunication
    # -----------------------

    def loadSynthDef(self, fn, cmd='/foxdot'):
        msg = OSCMessage()
        msg.setAddress(cmd)
        msg.append(fn)
        self.sclang.send(msg)
        return

    # Debug - Dumps OSC messages SCLang side
    # --------------------------------------

    def dumpOSC(self, value=1):
        msg = OSCMessage("/dumpOSC")
        msg.append(value)
        self.client.send(msg)
        return


    # Boot and Quit
    # -------------

    def start(self):
        """ Boots SuperCollider """

        if not self.booted:
            
            os.chdir(SC_DIRECTORY)
            
            print("Booting SuperCollider Server...")

            self.daemon = subprocess.Popen([SCLANG_EXEC, '-D', FOXDOT_STARTUP_FILE])

            os.chdir(USER_CWD)

            self.booted = True

        else:
            
            print("Warning: SuperCollider already running")
            
        return

    def makeStartupFile(self):
        ''' Boot SuperCollider and connect over OSC '''

        # 1. Compile startup file

        with open(FOXDOT_STARTUP_FILE, 'w') as startup:

            startup.write('''Routine.run {
            s.options.blockSize = 128;
            s.options.memSize = 131072;
            s.bootSync();\n''')

            files = [FOXDOT_OSC_FUNC, FOXDOT_BUFFERS_FILE]
            files = files + GET_SYNTHDEF_FILES() + GET_FX_FILES()
            
            for fn in files:

                f = open(fn)
                startup.write(f.read())
                startup.write("\n\n")

            startup.write("};")

        return

    def quit(self):
        if self.booted:
            self.client.send(OSCMessage("/quit"))
            sleep(1)
            self.daemon.terminate()
        return


if __name__ != "__main__":

    from Settings import ADDRESS, PORT, PORT2

    Server = SCLangServerManager(ADDRESS, PORT, PORT2)

        
