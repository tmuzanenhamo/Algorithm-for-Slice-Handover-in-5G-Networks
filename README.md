# Final Year Project
Bsc (Eng) Electrical and Computer Engineering, University of Cape Town `Passed with a Distinction`
## Project Title 

Design of An Algorithm for 5G Sliced Networks

## What's Here

This repo contains all the Python code used in this project, the results obtained from the simulations and graphs, the project report, and the project poster.

## Abstract

<p align="justify"><i>5G wireless networks are envisioned to meet the rising demand for network services from users. User devices have evolved and demand different services from the network. The user demands can be categorized based on latency, reliability and bandwidth required. In order to meet the diverse requirements of users in a cost-effective manner whilst ensuring network resources are efficiently allocated to users, 5G networks are expected to utilise technologies like Software Defined Networks (SDN), Network Function Virtualization (NFV) and Network Slicing.
With the introduction of diverse 5G application scenarios, new mobility management schemes must be implemented in Sliced 5G networks in order to guarantee seamless handover between network slices. Mobility management allows users to move from one coverage area to another without losing network connection. 5G networks follow the heterogenous networks architecture meaning different network slices can co-exist with each slice providing services tailored for specific Quality of Service (QoS) demands. Therefore, when users move from one coverage area to another, the call can be handed over to a slice catering for the same demands or a slice catering for different demands.
The aim of this project is to design an algorithm for making handover decisions in sliced 5G networks and evaluate the performance of the algorithm. The chosen network model for this project consist of three slices namely Enhanced Mobile Broadband, Massive Machine Type Communication (mMTC) and Ultra Reliable Low Latency Communication (uRLLC). An analytical model based on the Markov chain is used to model the call admission control algorithm in the network model.
This report details the design of the network model and the implementation of the vertical handover decision making algorithm . The algorithm performance is evaluated using connection level QoS metrics namely ne call blocking probability and handoff call dropping probability. The simulations are carried out to determine how the QoS metrics are affected by variations in different metrics like call arrival rate, capacity, new call threshold, required basic bandwidth unit and call departure rate. From the simulation results it is concluded that in overall, the implemented algorithms provide good QoS levels with the handoff call dropping probability being less than the new call blocking probability in all scenarios and the inter slice handover algorithm provides better QoS in the eMBB and mMTC slice whilst the intra slice handover algorithm provide better QoS in the uRLLC slice.</i></p>

