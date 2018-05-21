# Gesture recognition with simple finger bend data
Assignment P for COMP3314

# Motivation 
For another class, ELEC3542 (Advanced Programming and Application Development) I made a device to track hand movements, using a raspberry pi, a sensehat and flex sensors. My goal was to create something to interface with sounds using your hands in an intuitive way. It's relatively straightforward to map sensor values of the bend of the fingers to parameters in a digital audio workstation, but it seemed more interesting to me to apply gesture recognition to e.g. gate between different mappings of the other sensors or different instruments. Machine learning seemed a very feasable method for achieving this goal.

# Background
Flex sensors are generally analog sensors, but the Raspberry Pi doesn't have any ADC's so I used an external one for that job. The Pi sends the data over UDP to my laptop, where I can record it for model training. 

This is what the prototype looks like:

![image](https://user-images.githubusercontent.com/25040414/40318550-8d280998-5d57-11e8-9760-06a94c75e14e.png)

![image](https://user-images.githubusercontent.com/25040414/40318476-57ab21ec-5d57-11e8-9e1a-a2f2237d2607.png)

The gestures I wanted to train my model on:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8


# Method

simple K-nn seemed very sufficient for clean and clear data, and it indeed is. 100% ratios with k = 1 are achievable even with 
big cuts in the full dataset 

Preliminary experiments: Describe the experiments that you've run, the outcomes, and any err
