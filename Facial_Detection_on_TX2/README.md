Faces stored to IBM Cloud object store: http://s3.us-south.cloud-object-storage.appdomain.cloud/piercecogginsfaces

The goal of this project was to build a lightweight IoT application pipeline with components running both on the edge (your Nvidia Jetson TX2) and the cloud (a VM in Softlayer). Additionally, I wrote the application in a modular way such that it could be run on pretty much any low power edge device or hub (e.g. Raspberry Pi or Raspberry Pi Zero) and a cheap Cloud VM or another low power edge device connected to some kind of storage instead of a Cloud VM.

The overall goal is to be able to capture faces in a video stream coming from the edge in real time, transmit them to the cloud in real time, and save these faces in the cloud for long term storage.

All components are packaged within Docker containers, encapsulating each element of the project into portable microservices. On the TX2, we used Alpine Linux as the base OS for your containers as it is frugal in terms of storage. (Jetson TX2 devices and Raspberry Pis are both based on the ARM v8 architecture.)

For the edge face detector component, I used OpenCV to write an application that scans video frames gathered from the connected USB camera for faces. When one or more faces are detected in the frame, the application cut them out of the frame and sent them to a Cloud VM for storage purposes.

I used an MQTT client to send and receive messages, and MQTT broker as the server component of this architecture.

The local MQTT broker was installed on my TX2, and the face detector sent messages through this local broker to a remote MQTT client where the message was converted and saved to object store in the cloud.

![this](Face_detection.png)
