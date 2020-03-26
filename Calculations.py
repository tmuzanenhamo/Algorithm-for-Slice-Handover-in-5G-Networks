import numpy as np
from Slices import Slices, Slice
from UseCases import UseCases


class Calculations:
    capacity = 0
    new_thresh = 0
    handoff_thresh = 0
    handoff_rate = 0.5
    holding_time1 = handoff_rate + 0.5
    holding_time2 = handoff_rate + 0.5

    def __init__(self):
        print('Calculations started\n')

    @classmethod
    def factorial(cls, num):
        if num == 1 or num == 0:
            return 1
        else:
            return num * cls.factorial(num - 1)

    @classmethod
    def power(cls, num, power):
        if power == 0:
            return 1
        elif power == 1:
            return num
        else:
            value = 1
            for i in range(power):
                value *= num
            return value

    @classmethod
    def probabilities(cls, numerator, denominator):
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
            bbuN = required_bbu.allocate_bbu(slice_name)[0]
            bbuH = required_bbu.allocate_bbu(slice_name)[1]
            cls.capacity = params[0]
            cls.new_thresh = params[1]
            cls.handoff_thresh = params[2]
            # Available bandwidth
            newB *= (cls.capacity / (cls.capacity * 3)) * callA
            handB *= (cls.capacity / (cls.capacity * 3)) * handA
            # Load at each slice
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
