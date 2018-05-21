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
![image](https://user-images.githubusercontent.com/25040414/40320009-c4cfa43c-5d5c-11e8-8f04-201898020a90.png)

# 2
![image](https://user-images.githubusercontent.com/25040414/40320012-c893e6aa-5d5c-11e8-99ea-32815422f3ec.png)
(No hard feelings)

# 3
![image](https://user-images.githubusercontent.com/25040414/40320019-ccba5066-5d5c-11e8-8782-40a7b0a2dc38.png)

# 4
![image](https://user-images.githubusercontent.com/25040414/40320033-d19b4356-5d5c-11e8-9f6a-224a96e93267.png)

# 5
![image](https://user-images.githubusercontent.com/25040414/40320041-d667beaa-5d5c-11e8-8468-7df005b8fc02.png)

# 6
![image](https://user-images.githubusercontent.com/25040414/40320047-dbe1ea18-5d5c-11e8-9acf-2f4a90315842.png)

# 7
![image](https://user-images.githubusercontent.com/25040414/40320053-e0e252b4-5d5c-11e8-996b-87f0bb63d9b1.png)

# 8
![image](https://user-images.githubusercontent.com/25040414/40320057-e5b01e16-5d5c-11e8-95da-2508843a387b.png)


# Method

simple K-nn seemed sufficient for clean and clear data, and it indeed is. 100% ratios with k = 1 are achievable even with 
big cuts in the training / model part of dataset (useful for speeding up classification, crucial in it's usecase). 

Supplied in this repository is the full labeled dataset [FingerData.csv] + a short version for a big improvement in speed [FingerDataShort.csv], a script training the knn model and testing it [Assignment-3-gesture-recognition-knn-test.py], a script for routing the over UDP received sensor data to the classifier and routing it's output as a MIDI message [Live+Classifier.py], and the script running on the "glove" sending the sensor data [Glove.py].


