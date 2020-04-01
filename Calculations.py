import numpy as np
from Slices import Slices, Slice
from UseCases import UseCases
import time


class IntraCalculations:
    capacity = 0
    new_thresh = 0
    handoff_thresh = 0
    handoff_rate = 0.5
    holding_time1 = handoff_rate + 0.5
    holding_time2 = handoff_rate + 0.5
    eMBB_handoff_thresh = 0
    eMBB_newcall_thresh = 0
    uRLLC_handoff_thresh = 0
    uRLLC_newcall_thresh = 0
    uRLLC_capacity = 0
    eMBB_capacity = 0

    def __init__(self):
        print('Calculations started\n')

    @classmethod
    def factorial(cls, num):
        """Function that calculates the Factorial of a given number"""
        if num == 1 or num == 0:
            return 1
        else:
            return num * cls.factorial(num - 1)

    @classmethod
    def probabilities(cls, numerator: object, denominator: object) -> object:
        """Function that calculates the probabilities"""
        probability = numerator / denominator
        return probability

    @classmethod
    def calculations(cls, slice_name, params):
        # blocking probabilities
        Dp = np.zeros(10)
        Bp = np.zeros(10)
        qn = np.zeros(10)
        qh = np.zeros(10)
        # Normalisation Constants
        G = np.zeros(10)
        G1 = np.zeros(10)
        G2 = np.zeros(10)
        G3 = np.zeros(10)
        # New Call arrival rates
        callA = np.arange(1.0, 6, 0.5)  # eMBB, uRLLC, mMTC
        # Handoff Call Arrival rates
        handA = (callA * cls.handoff_rate) / 0.5
        # Initialise Available Bandwidth
        newB = np.ones(len(callA))
        handB = np.ones(len(handA))
        # Initialise Loads
        newL = np.ones(len(newB))
        handL = np.ones(len(handB))

        if slice_name == 'eMBB':
            required_bbu = UseCases()
            bbuN = required_bbu.allocate_bbu(slice_name)[0]  # new call bbU
            bbuH = required_bbu.allocate_bbu(slice_name)[1]  # handoff call bbu
            cls.capacity = params[0]  # slice capacity
            cls.new_thresh = params[1]  # new call threshold
            cls.handoff_thresh = params[2]  # handoff call threshold
            # Available bandwidth
            newB *= (cls.capacity / (cls.capacity * 3)) * callA
            handB *= (cls.capacity / (cls.capacity * 3)) * handA
            # Load at each slice
            newL *= newB / cls.holding_time1
            handL *= handB / cls.holding_time2

            # Number calls that can be accepted
            w = 0
            newNum = round((cls.new_thresh / bbuN) + 1)
            handNum = round((cls.handoff_thresh / bbuH) + 1)

            for i in range(10):
                for newC in range(1, newNum, 1):
                    for handC in range(1, handNum, 1):
                        # Admissible states
                        if bbuN * (
                                newC + handC) <= cls.capacity and bbuN * newC <= cls.new_thresh and \
                                bbuH * handC <= cls.handoff_thresh:
                            for j in range(10):
                                qn[j] = pow(newL[j], newC) / cls.factorial(newC)
                                qh[j] = pow(handL[j], handC) / cls.factorial(handC)
                                G[j] = G[j] + qn[j] * qh[j]  # Normalisation Constant

                                # Condition for blocking new calls
                                if bbuN + (
                                        bbuN * newC + bbuH * handC) > cls.capacity or bbuN + bbuN * newC > \
                                        cls.new_thresh:
                                    G1[j] = G1[j] + qn[j] * qh[j]

                                # Condition for dropping handoff calls

                                if bbuN + (
                                        bbuN * newC + bbuH * handC) > cls.capacity or bbuH + bbuH * handC > \
                                        cls.handoff_thresh:
                                    w += 1
                                    G2[j] = G2[j] + qn[j] * qh[j]

            # return the probabilities
            print('####################################')
            print(w)
            print('####################################')
            blocking_prob = cls.probabilities(G1, G)
            dropping_prob = cls.probabilities(G2, G)
            return slice_name, blocking_prob, dropping_prob

        elif slice_name == 'uRLLC':
            required_bbu = UseCases()
            bbuN = required_bbu.allocate_bbu(slice_name)[0]
            bbuH = required_bbu.allocate_bbu(slice_name)[1]
            cls.capacity = params[0]
            cls.new_thresh = params[1]
            cls.handoff_thresh = params[2]

            # Available Bandwidth
            newB *= (cls.capacity / (cls.capacity * 3)) * callA
            handB *= (cls.capacity / (cls.capacity * 3)) * handA

            # Load at the slice
            newL *= newB / cls.holding_time1
            handL *= handB / cls.holding_time2

            # Number calls that can be accepted
            newNum = round((cls.new_thresh / bbuN) + 1)
            handNum = round((cls.handoff_thresh / bbuH) + 1)

            for i in range(10):
                for newC in range(1, newNum, 1):
                    for handC in range(1, handNum, 1):
                        # Admissible states
                        if bbuN * (
                                newC + handC) <= cls.capacity and bbuN * newC <= cls.new_thresh and \
                                bbuH * handC <= cls.handoff_thresh:
                            for j in range(10):
                                qn[j] = pow(newL[j], newC) / cls.factorial(newC)
                                qh[j] = pow(handL[j], handC) / cls.factorial(handC)
                                G[j] = G[j] + qn[j] * qh[j]  # Normalisation Constant

                                # Condition for blocking new calls
                                if bbuN + (
                                        bbuN * newC + bbuH * handC) > cls.capacity or bbuN + bbuN * newC > \
                                        cls.new_thresh:
                                    G1[j] = G1[j] + qn[j] * qh[j]

                                # Condition for dropping handoff calls
                                if bbuN + (
                                        bbuN * newC + bbuH * handC) > cls.capacity or bbuH + bbuH * handC > \
                                        cls.handoff_thresh:
                                    G2[j] = G2[j] + qn[j] * qh[j]

            # return the probabilities
            blocking_prob = cls.probabilities(G1, G)
            dropping_prob = cls.probabilities(G2, G)
            return slice_name, blocking_prob, dropping_prob

        elif slice_name == 'mMTC':
            required_bbu = UseCases()
            bbuN = required_bbu.allocate_bbu(slice_name)
            cls.capacity = params[0]
            cls.new_thresh = params[1]
            # Available bandwidth
            newB *= (cls.capacity / (cls.capacity * 3)) * callA
            # Load at the slice
            newL *= newB / cls.holding_time1

            # Number calls that can be accepted
            newNum = round((cls.new_thresh / bbuN) + 1)
            y = 0
            for i in range(10):
                for newC in range(1, newNum, 1):
                    # Admissible states
                    if bbuN * newC <= cls.capacity and bbuN * newC <= cls.new_thresh:
                        for j in range(10):
                            qn[j] = pow(newL[j], newC) / cls.factorial(newC)
                            G[j] += qn[j]

                            # Condition for blocking new calls
                            if bbuN * newC > cls.capacity or bbuN + bbuN * newC > cls.new_thresh:
                                G3[j] += qn[j]

            # return the probabilities
            blocking_prob = cls.probabilities(G3, G)
            return slice_name, blocking_prob


class InterCalculations(IntraCalculations):

    def __init__(self):
        print('Calculations Started\n')

    @classmethod
    def calculations(cls, slice_name, params):
        # blocking probabilities
        Dp = np.zeros(10)
        Bp = np.zeros(10)
        qn = np.zeros(10)
        qh = np.zeros(10)
        qn_1 = np.zeros(10)
        qh_1 = np.zeros(10)
        qn_2 = np.zeros(10)
        qh_2 = np.zeros(10)

        # Normalisation Constants
        G = np.zeros(10)
        G1 = np.zeros(10)
        G2 = np.zeros(10)
        G3 = np.zeros(10)
        # New Call arrival rates
        callA = np.arange(1.0, 6, 0.5)  # eMBB, uRLLC, mMTC
        # Handoff Call Arrival rates
        handA = (callA * cls.handoff_rate) / 0.5
        # Initialise Available Bandwidth
        newB = np.ones(len(callA))
        handB = np.ones(len(handA))
        newBU = np.ones(len(callA))
        handBU = np.ones(len(handA))
        newBE = np.ones(len(callA))
        handBE = np.ones(len(handA))

        # Initialise Loads
        newL = np.ones(len(newB))
        handL = np.ones(len(handB))
        newLU = np.ones(len(newB))
        handLU = np.ones(len(handB))
        newLE = np.ones(len(newBE))
        handLE = np.ones(len(handBE))

        if slice_name == 'eMBB':
            required_bbu = UseCases()
            bbuN = required_bbu.allocate_bbu(slice_name)[0]  # new call bbU
            bbuH = required_bbu.allocate_bbu(slice_name)[1]  # handoff call bbu
            bbuNU = required_bbu.allocate_bbu('uRLLC')[0]
            bbuHU = required_bbu.allocate_bbu('uRLLC')[1]
            cls.capacity = params[0]  # slice capacity
            cls.new_thresh = params[1]  # new call threshold
            cls.handoff_thresh = params[2]  # handoff call threshold
            cls.uRLLC_handoff_thresh = params[2]  # handoff threshold for uRLLC
            cls.uRLLC_newcall_thresh = params[1]  # newcall threshold for uRLLC
            cls.uRLLC_capacity = params[0]  # capacity for uRLLC

            # Available bandwidth
            newB *= (cls.capacity / (cls.capacity * 3)) * callA
            handB *= (cls.capacity / (cls.capacity * 3)) * handA
            newBU *= (cls.uRLLC_capacity / (cls.uRLLC_capacity * 3)) * callA
            handBU *= (cls.uRLLC_capacity / (cls.uRLLC_capacity * 3)) * handA

            # Load at each slice
            newL *= newB / cls.holding_time1
            handL *= handB / cls.holding_time2
            newLU *= newBU / cls.holding_time1
            handLU *= handBU / cls.holding_time2

            # Number calls that can be accepted
            g = 0
            newNum = round((cls.new_thresh / bbuN) + 1)
            handNum = round((cls.handoff_thresh / bbuH) + 1)
            handNumU = round((cls.uRLLC_handoff_thresh / bbuHU) + 1)
            newNumu = round((cls.uRLLC_newcall_thresh / bbuNU) + 1)
            for i in range(10):
                for newC in range(1, newNum, 1):
                    for handC in range(1, handNum, 1):
                        for newCU in range(1, newNumu, 1):
                            for handCU in range(1, handNumU, 1):

                                # Admissible States
                                if bbuN * (newC + handC) <= cls.capacity and bbuN * newC <= cls.new_thresh and \
                                        bbuN * handC <= cls.handoff_thresh or bbuNU * (
                                        newCU + handCU) <= cls.uRLLC_capacity and \
                                        bbuNU * newCU <= cls.uRLLC_newcall_thresh and \
                                        bbuNU * handCU <= cls.uRLLC_handoff_thresh:

                                    for j in range(10):
                                        # Normalisation Constant
                                        qn[j] = pow(newL[j], newC) / cls.factorial(newC)
                                        qh[j] = pow(handL[j], handC) / cls.factorial(handC)
                                        qn_1[j] = pow(newLU[j], newCU) / cls.factorial(newCU)
                                        qh_1[j] = pow(handLU[j], handCU) / cls.factorial(handCU)

                                        G[j] = G[j] + qn[j] * qh[j] + qh_1[j] * qn_1[j]
                                        # Condition for blocking new calls
                                        if bbuN + bbuN * (newC + handC) > cls.capacity or \
                                                bbuN + bbuN * newC > cls.new_thresh and bbuNU + bbuNU * (
                                                newCU + handCU) > cls.uRLLC_capacity or \
                                                bbuNU + bbuNU * newCU > cls.uRLLC_newcall_thresh:
                                            G1[j] = G1[j] + qn[j] * qh[j] + qn_1[j] * qh_1[j]
                                            # g += 1
                                        if bbuN + bbuN * (newC + handC) > cls.capacity or \
                                                bbuN + bbuN * handC > cls.handoff_thresh and \
                                                bbuNU + bbuNU * (newCU + handCU) > cls.uRLLC_capacity or \
                                                bbuNU + bbuNU * handCU > cls.uRLLC_handoff_thresh:
                                            G2[j] = G2[j] + qn[j] * qh[j] * qn_1[j] * qh_1[j]
                                            g += 1

            blocking_prob = cls.probabilities(G1, G)
            dropping_prob = cls.probabilities(G2, G)
            return slice_name, blocking_prob, dropping_prob

        elif slice_name == 'uRLLC':
            required_bbu = UseCases()
            bbuN = required_bbu.allocate_bbu(slice_name)[0]
            bbuH = required_bbu.allocate_bbu(slice_name)[1]
            cls.capacity = params[0]
            cls.new_thresh = params[1]
            cls.handoff_thresh = params[2]

            # Available Bandwidth
            newB *= (cls.capacity / (cls.capacity * 3)) * callA
            handB *= (cls.capacity / (cls.capacity * 3)) * handA

            # Load at the slice
            newL *= newB / cls.holding_time1
            handL *= handB / cls.holding_time2

            # Number calls that can be accepted
            newNum = round((cls.new_thresh / bbuN) + 1)
            handNum = round((cls.handoff_thresh / bbuH) + 1)
            for i in range(10):
                for newC in range(1, newNum, 1):
                    for handC in range(1, handNum, 1):
                        # Admissible states
                        if bbuN * (
                                newC + handC) <= cls.capacity and bbuN * newC <= cls.new_thresh and \
                                bbuH * handC <= cls.handoff_thresh:
                            for j in range(10):
                                qn[j] = pow(newL[j], newC) / cls.factorial(newC)
                                qh[j] = pow(handL[j], handC) / cls.factorial(handC)
                                G[j] = G[j] + qn[j] * qh[j]  # Normalisation Constant

                                # Condition for blocking new calls
                                if bbuN + (
                                        bbuN * newC + bbuH * handC) > cls.capacity or bbuN + bbuN * newC > \
                                        cls.new_thresh:
                                    G1[j] = G1[j] + qn[j] * qh[j]

                                # Condition for dropping handoff calls
                                if bbuN + (
                                        bbuN * newC + bbuH * handC) > cls.capacity or bbuH + bbuH * handC > \
                                        cls.handoff_thresh:
                                    G2[j] = G2[j] + qn[j] * qh[j]

            # return the probabilities
            blocking_prob = cls.probabilities(G1, G)
            dropping_prob = cls.probabilities(G2, G)
            return slice_name, blocking_prob, dropping_prob

        elif slice_name == 'mMTC':
            d = time.time()
            required_bbu = UseCases()
            bbuN = required_bbu.allocate_bbu(slice_name)
            bbuHE = required_bbu.allocate_bbu('eMBB')[1]
            bbuHU = required_bbu.allocate_bbu('uRLLC')[1]
            bbuNE = required_bbu.allocate_bbu('eMBB')[0]
            bbuNU = required_bbu.allocate_bbu('uRLLC')[0]
            cls.capacity = params[0]
            cls.new_thresh = params[1]
            cls.uRLLC_handoff_thresh = params[0] + 10
            cls.uRLLC_newcall_thresh = params[1] + 5
            cls.uRLLC_capacity = params[0] + 10
            cls.eMBB_handoff_thresh = params[0] + 15
            cls.eMBB_newcall_thresh = params[1] + 5
            cls.eMBB_capacity = params[0] + 15
            k = 0
            # Available bandwidth
            newB *= (cls.capacity / (cls.capacity * 3)) * callA
            newBU *= (cls.uRLLC_capacity / (cls.uRLLC_capacity * 3)) * callA
            newBE *= (cls.eMBB_capacity / (cls.eMBB_capacity * 3)) * callA
            handBE *= (cls.eMBB_capacity / (cls.eMBB_capacity * 3)) * handA
            handBU *= (cls.uRLLC_capacity / (cls.uRLLC_capacity * 3)) * handA
            # Load at the slice
            newL *= newB / cls.holding_time1
            newLU *= newBU / cls.holding_time1
            handLU *= handBU / cls.holding_time2
            newLE *= newBE / cls.holding_time1
            handLE *= handBE / cls.holding_time2

            # Number calls that can be accepted
            newNum = round((cls.new_thresh / bbuN) + 1)
            newNumE = round((cls.eMBB_newcall_thresh / bbuNE) + 1)
            handNumE = round((cls.eMBB_handoff_thresh / bbuHE) + 1)
            newNumU = round((cls.uRLLC_newcall_thresh / bbuNU) + 1)
            handNumU = round((cls.uRLLC_handoff_thresh / bbuHU) + 1)
            for i in range(10):
                for newC in range(1, newNum, 1):
                    for newCE in range(1, newNumE, 1):
                        for handCE in range(1, handNumE, 1):
                            for newCU in range(1, newNumU, 1):
                                for handCU in range(1, handNumU, 1):
                                    # Admissible States
                                    if bbuN * newC <= cls.capacity and bbuN * newC <= cls.new_thresh or bbuNE * (
                                            newCE + handCE) <= cls.eMBB_capacity and \
                                            bbuNE * newCE <= cls.eMBB_newcall_thresh and \
                                            bbuHE * handCE <= cls.eMBB_handoff_thresh or \
                                            bbuNU * (newCU + handCU) <= cls.uRLLC_capacity and \
                                            bbuNU * newCU <= cls.uRLLC_newcall_thresh and \
                                            bbuHU * handCU <= cls.uRLLC_handoff_thresh:

                                        for j in range(10):
                                            # Normalisation Constant
                                            qn[j] = pow(newL[j], newC) / cls.factorial(newC)
                                            qn_1[j] = pow(newLU[j], newCU) / cls.factorial(newCU)
                                            qh_1[j] = pow(handLU[j], handCU) / cls.factorial(handCU)
                                            qn_2[j] = pow(newLE[j], newCE) / cls.factorial(newCE)
                                            qh_2[j] = pow(handLE[j], handCE) / cls.factorial(handCE)

                                            G[j] = G[j] + qn[j] + qh_1[j] * qn_1[j] * qh_2[j] * qn_2[j]

                                            if bbuN + bbuN * newC > cls.capacity or\
                                                    bbuN + bbuN * newC > cls.new_thresh and \
                                                    (bbuNE + bbuNE * (newCE + handCE)) > cls.eMBB_capacity or \
                                                    bbuNE + bbuNE * newCE > cls.eMBB_newcall_thresh and \
                                                    (bbuNU + bbuNU * (newCU + handCU)) > cls.uRLLC_capacity or \
                                                    bbuNU + bbuNU * newCU > cls.uRLLC_newcall_thresh:
                                                G1[j] = G1[j] + qn[j] * qn_1[j] * qh_1[j] * qh_2[j] * qn_2[j]
                                                k += 1

        l = time.time()
        print(f'it took {l-d} to finish')

        print(k)
        blocking_prob = cls.probabilities(G1, G)
        return slice_name, blocking_prob
