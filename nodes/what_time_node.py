#!/usr/bin/env python

import rospy

import datetime
import importlib
import os
import sys


def show_time(unix_time):
    dt = datetime.datetime.fromtimestamp(unix_time)
    sys.stdout.write('\r{0}\r'.format(' ' * 20))
    s = dt.strftime('%Y/%m/%d %H:%M:%S.%f')
    sys.stdout.write(s)
    sys.stdout.flush()

def callback(msg):
    try:
        show_time(msg.header.stamp.to_sec())
    except AttributeError:
        sys.stderr.write('header.stamp not found in message\n')
        os._exit(1)

def get_topic_class(tgt_topic_name):
    found_topic = False
    topics = rospy.get_published_topics()
    for topic_info in topics:
        topic_name, topic_pkg = topic_info
        topic_name = topic_name.lstrip('/')
        if topic_name != tgt_topic_name.lstrip('/'):
            continue

        found_topic = True
        pkg, class_name = topic_pkg.split('/')
        m = importlib.import_module(pkg + '.msg')
        return getattr(m, class_name)
    if not found_topic:
        err_msg = tgt_topic_name + ' not published yet?'
        raise ValueError(err_msg)

def spin():
    while not rospy.is_shutdown():
        show_time(rospy.Time.now().to_sec())
        rospy.sleep(0.1)

rospy.init_node('what_time_node')

if len(sys.argv) > 1:
    print('Showing timestamp of latest message received')
    topic_name = sys.argv[1]
    c = get_topic_class(topic_name)
    time_sub = rospy.Subscriber(topic_name, c, callback, queue_size=1)
    rospy.spin()
else:
    print('Showing rospy.Time.now()')
    spin()

print('')
print('Bye!')
