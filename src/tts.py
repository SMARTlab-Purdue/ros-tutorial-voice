#!/usr/bin/env python
import rospy
import os
from std_msgs.msg import String
from std_msgs.msg import Bool
from tts_watson.TtsWatson import TtsWatson
import anyconfig
import bunch


class TtsWatsonRos:
    CONFIG_FILE = "config.sample.yml"

    def __init__(self):
        currentDir = os.path.dirname(os.path.realpath(__file__))
        configFile = currentDir + "/../" + self.CONFIG_FILE
        conf = anyconfig.load(configFile)
        bconf = bunch.bunchify(conf)
        self.ttsWatson = TtsWatson(bconf.user, bconf.password, bconf.voice, bconf.url, bconf.chunk)


    def playSound(self, data):
        if data.data == True:
            self.ttsWatson.play("Requested action executed")
        else:
            self.ttsWatson.play("No command to execute")


def listen():
    ttsWatsonRos = TtsWatsonRos()
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("voice_command", Bool, ttsWatsonRos.playSound)
    print 'Ready to transform text into sound'
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    listen()
