# what_time

Shows the current time or the time in `header.stamp`. Useful when you want to
show what time a sensor data was obtained at.

```
# Current ROS time
$ rosrun what_time what_time_node.py
# Time recorded in the header.stamp field
$ rosrun what_time what_time_node.py /some/sensor/topic
```

The program exits out when the given topic does not exist or no `header.stamp`
field is found in the class.


## License

MIT


## Author

Naoki Mizuno (mizuno.naoki@rm.is.tohoku.ac.jp)
