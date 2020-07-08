import numpy as np
from Slices import Slices, Slice
from UseCases import UseCases
import time


class IntraCalculations:
    capacity = 0
    new_thresh = 0
    handoff_thresh = 0
    handoff_rate = np.arange(10, 20, 1)
    holding_time1 = handoff_rate
    holding_time2 = handoff_rate

    eMBB_handoff_thresh = 0
    eMBB_newcall_thresh = 0
    uRLLC_handoff_thresh = 0
    uRLLC_newcall_thresh = 0
    uRLLC_capacity = 0
    eMBB_capacity = 0
    mMTC_capacity = 0
    uRLLC_capacity_inter = 0
    uRLLC_newcall_thresh_inter = 0
    uRLLC_handoff_thresh_inter = 0
    mMTC_thresh = 0

    def __init__(self):
        print('Intra Slice Handover Calculations Started\n')

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
        qh_1 = np.zeros(10)
        qn_1 = np.zeros(10)
        qn_2 = np.zeros(10)
        qh_2 = np.zeros(10)
        # Normalisation Constants
        G = np.zeros(10)
        G1 = np.zeros(10)
        G2 = np.zeros(10)
        G3 = np.zeros(10)
        # New Call arrival rates
        # callA = np.arange(3, 8, .5)  # eMBB, uRLLC, mMTC
        callA = np.ones(10)
        callA *= 2
        callAM = callA
        # Handoff Call Arrival rates
        handA = (callA * cls.handoff_rate) / 0.5
        # Initialise Available Bandwidth
        newB = np.ones(len(callA))
        handB = np.ones(len(handA))
        newBU = np.ones(len(callA))
        handBU = np.ones(len(handA))
        newBE = np.ones(len(callA))
        handBE = np.ones(len(handA))
        newBM = np.ones(len(callAM))

        # Initialise Loads
        newL = np.ones(len(newB))
        handL = np.ones(len(handB))
        newLU = np.ones(len(newBU))
        handLU = np.ones(len(handBU))
        newLE = np.ones(len(newBE))
        handLE = np.ones(len(handBE))
        newLM = np.ones(len(newBM))

        if slice_name == 'eMBB':
            required_bbu = UseCases()
            bbuN = required_bbu.allocate_bbu(slice_name)[0]  # eMBB new call bbU
            bbuH = required_bbu.allocate_bbu(slice_name)[1]  # eMBB handoff call bbu
            bbuNU = required_bbu.allocate_bbu('uRLLC')[0]  # uRLLC new call bbu
            bbuHU = required_bbu.allocate_bbu('uRLLC')[1]  # uRLLC handoff call bbu
            bbuNM = required_bbu.allocate_bbu('mMTC')  # mMTC bbu

            cls.capacity = params[0]  # slice capacity
            cls.new_thresh = params[1]  # new call threshold
            cls.handoff_thresh = params[2]  # handoff call threshold
            cls.uRLLC_handoff_thresh = params[2]
            cls.uRLLC_newcall_thresh = params[1]
            cls.uRLLC_capacity = params[0]
            cls.mMTC_capacity = params[1]
            cls.mMTC_thresh = params[1]

            # Available bandwidth
            newB *= (cls.capacity / cls.capacity) * callA
            handB *= (cls.capacity / cls.capacity) * handA
            newBM *= (cls.mMTC_capacity / cls.mMTC_capacity) * callAM
            newBU *= (cls.uRLLC_capacity / cls.uRLLC_capacity) * callA
            handBU *= (cls.uRLLC_capacity / cls.uRLLC_capacity) * handA

            # Load at each slice
            newL *= newB / cls.holding_time1
            handL *= handB / cls.holding_time2
            newLU *= newBU / cls.holding_time1
            handLU *= handBU / cls.holding_time2
            newLM *= newBM / cls.holding_time1

            # Number calls that can be accepted
            w = 0
            newNum = round((cls.new_thresh / bbuN) + 1)
            handNum = round((cls.handoff_thresh / bbuH) + 1)
            newNumU = round((cls.uRLLC_newcall_thresh / bbuNU) + 1)
            handNumU = round((cls.uRLLC_handoff_thresh / bbuHU) + 1)
            newNumM = round((cls.mMTC_thresh / bbuNM) + 1)
            e = 0

            for i in range(10):
                for newC in range(0, newNum, 1):
                    for handC in range(0, handNum, 1):
                        for newCM in range(0, newNumM, 1):
                            for newCU in range(0, newNumU, 1):
                                for handCU in range(0, handNumU, 1):

                                    # Admissible states
                                    if (bbuN * (newC + handC) <= cls.capacity) and \
                                            (bbuNM * newCM <= cls.mMTC_capacity) and \
                                            (bbuNU * (newCU + handCU) <= cls.uRLLC_capacity) and \
                                            (bbuN * newC <= cls.new_thresh) and \
                                            (bbuNU * newCU <= cls.uRLLC_newcall_thresh):
                                        for j in range(10):
                                            qn[j] = pow(newL[j], newC) / cls.factorial(newC)
                                            qh[j] = pow(handL[j], handC) / cls.factorial(handC)
                                            qn_1[j] = pow(newLU[j], newCU) / cls.factorial(newCU)
                                            qh_1[j] = pow(handLU[j], handCU) / cls.factorial(handCU)
                                            qn_2[j] = pow(newLM[j], newCM) / cls.factorial(newCM)
                                            # Normalisation Constant
                                            G[j] = G[j] + qn[j] + qh[j] + qh_1[j] + qn_1[j] + qn_2[j]

                                            # Condition for blocking new calls
                                            if (bbuN + bbuN * (newC + handC) > cls.capacity) or \
                                                    (bbuN + bbuN * newC > cls.new_thresh):
                                                G1[j] = G1[j] + qn[j] + qh[j] + qh_1[j] + qn_1[j] + qn_2[j]

                                            # Condition for dropping handoff calls
                                            if (bbuN + bbuN * (newC + handC) > cls.capacity) or \
                                                    bbuN + bbuN * handC > cls.handoff_thresh:
                                                G2[j] = G2[j] + qn[j] + qh[j] + qh_1[j] + qn_1[j] + qn_2[j]

            # return the probabilities
            blocking_prob = cls.probabilities(G1, G)
            dropping_prob = cls.probabilities(G2, G)
            return slice_name, blocking_prob, dropping_prob

        elif slice_name == 'uRLLC':
            required_bbu = UseCases()
            bbuN = required_bbu.allocate_bbu(slice_name)[0]  # new call bbU
            bbuH = required_bbu.allocate_bbu(slice_name)[1]  # handoff call bbu
            bbuNE = required_bbu.allocate_bbu('eMBB')[0]
            bbuHE = required_bbu.allocate_bbu('eMBB')[1]
            bbuNM = required_bbu.allocate_bbu('mMTC')

            cls.capacity = params[0]  # slice capacity
            cls.new_thresh = params[1]  # new call threshold
            cls.handoff_thresh = params[2]  # handoff call threshold
            cls.eMBB_handoff_thresh = params[2]
            cls.eMBB_newcall_thresh = params[1]
            cls.eMBB_capacity = params[0]
            cls.mMTC_capacity = params[1]
            cls.mMTC_thresh = params[1]

            # Available bandwidth
            newB *= (cls.capacity / cls.capacity) * callA
            handB *= (cls.capacity / cls.capacity) * handA
            newBM *= (cls.mMTC_capacity / cls.mMTC_capacity) * callAM
            newBE *= (cls.eMBB_capacity / cls.eMBB_capacity) * callA
            handBE *= (cls.eMBB_capacity / cls.eMBB_capacity) * handA

            # Load at each slice
            newL *= newB / cls.holding_time1
            handL *= handB / cls.holding_time2
            newLE *= newBE / cls.holding_time1
            handLE *= handBE / cls.holding_time2
            newLM *= newBM / cls.holding_time1

            # Number calls that can be accepted
            w = 0
            newNum = round((cls.new_thresh / bbuNE) + 1)
            handNum = round((cls.handoff_thresh / bbuHE) + 1)
            newNumU = round((cls.eMBB_newcall_thresh / bbuN) + 1)
            handNumU = round((cls.eMBB_handoff_thresh / bbuH) + 1)
            newNumM = round((cls.mMTC_thresh / bbuNM) + 1)
            e = 0

            for i in range(10):
                for newC in range(1, newNumU, 1):
                    for handC in range(1, handNumU, 1):
                        for newCM in range(1, newNumM, 1):
                            for newCE in range(1, newNum, 1):
                                for handCE in range(1, handNum, 1):

                                    # Admissible states
                                    if (bbuN * (newC + handC) <= cls.capacity) and \
                                            (bbuNM * newCM <= cls.mMTC_capacity) and \
                                            (bbuNE * (newCE + handCE) <= cls.eMBB_capacity) and \
                                            (bbuN * newC <= cls.new_thresh) and \
                                            (bbuNE * newCE <= cls.eMBB_newcall_thresh):
                                        e += 1
                                        for j in range(10):
                                            qn[j] = pow(newL[j], newC) / cls.factorial(newC)
                                            qh[j] = pow(handL[j], handC) / cls.factorial(handC)
                                            qn_1[j] = pow(newLE[j], newCE) / cls.factorial(newCE)
                                            qh_1[j] = pow(handLE[j], handCE) / cls.factorial(handCE)
                                            qn_2[j] = pow(newLM[j], newCM) / cls.factorial(newCM)
                                            # Normalisation Constant
                                            G[j] = G[j] + qn[j] + qh[j] + qh_1[j] + qn_1[j] + qn_2[j]

                                            # Condition for blocking new calls
                                            if (bbuN + bbuN * (newC + handC) > cls.capacity) or \
                                                    (bbuN + bbuN * newC > cls.new_thresh):
                                                G1[j] = G1[j] + qn[j] + qh[j] + qh_1[j] + qn_1[j] + qn_2[j]

                                            # Condition for dropping handoff calls
                                            if (bbuN + bbuN * (newC + handC) > cls.capacity) or \
                                                    bbuN + bbuN * handC > cls.handoff_thresh:
                                                G2[j] = G2[j] + qn[j] + qh[j] + qh_1[j] + qn_1[j] + qn_2[j]

            # return the probabilities
            blocking_prob = cls.probabilities(G1, G)
            dropping_prob = cls.probabilities(G2, G)
            return slice_name, blocking_prob, dropping_prob

        elif slice_name == 'mMTC':
            required_bbu = UseCases()
            bbuNM = required_bbu.allocate_bbu(slice_name)  # new call bbU
            bbuNE = required_bbu.allocate_bbu('eMBB')[0]
            bbuHE = required_bbu.allocate_bbu('eMBB')[1]
            bbuN = required_bbu.allocate_bbu('uRLLC')[0]

            cls.uRLLC_capacity = params[0] + 15  # slice capacity
            cls.uRLLC_newcall_thresh = params[1]  # new call threshold
            cls.uRLLC_handoff_thresh = params[0] + 15  # new call threshold
            cls.eMBB_handoff_thresh = params[0] + 15
            cls.eMBB_newcall_thresh = params[1]
            cls.eMBB_capacity = params[0] + 15
            cls.mMTC_capacity = params[0]
            cls.mMTC_thresh = params[1]

            # Available bandwidth
            newB *= (cls.uRLLC_capacity / cls.uRLLC_capacity) * callA
            handB *= (cls.uRLLC_capacity / cls.uRLLC_capacity) * handA
            newBM *= (cls.mMTC_capacity / cls.mMTC_capacity) * callAM
            newBE *= (cls.eMBB_capacity / cls.eMBB_capacity) * callA
            handBE *= (cls.eMBB_capacity / cls.eMBB_capacity) * handA

            # Load at each slice
            newL *= newB / cls.holding_time1
            handL *= handB / cls.holding_time2
            newLE *= newBE / cls.holding_time1
            handLE *= handBE / cls.holding_time2
            newLM *= newBM / cls.holding_time1

            # Possible Number of calls
            newNum = round((cls.eMBB_newcall_thresh / bbuNE) + 1)
            handNum = round((cls.eMBB_handoff_thresh / bbuHE) + 1)
            newNumU = round((cls.uRLLC_newcall_thresh / bbuN) + 1)
            handNumU = round((cls.uRLLC_handoff_thresh / bbuN) + 1)
            newNumM = round((cls.mMTC_thresh / bbuNM) + 1)

            k = 0

            for i in range(10):
                for newC in range(0, newNumU, 1):
                    for handC in range(0, handNumU, 1):
                        for newCM in range(0, newNumM, 1):
                            for newCE in range(0, newNum, 1):
                                for handCE in range(0, handNum, 1):

                                    # Admissible states
                                    if (bbuN * (newC + handC) <= cls.uRLLC_capacity) and \
                                            (bbuNM * newCM <= cls.mMTC_capacity) and \
                                            (bbuNE * (newCE + handCE) <= cls.eMBB_capacity) and \
                                            (bbuN * newC <= cls.uRLLC_newcall_thresh) and \
                                            (bbuNE * newCE <= cls.eMBB_newcall_thresh):

                                        for j in range(10):
                                            qn[j] = pow(newL[j], newC) / cls.factorial(newC)
                                            qh[j] = pow(handL[j], handC) / cls.factorial(handC)
                                            qn_1[j] = pow(newLE[j], newCE) / cls.factorial(newCE)
                                            qh_1[j] = pow(handLE[j], handCE) / cls.factorial(handCE)
                                            qn_2[j] = pow(newLM[j], newCM) / cls.factorial(newCM)
                                            # Normalisation Constant
                                            G[j] = G[j] + qn_2[j] + qn_1[j] + qn[j] + qh[j] + qh_1[j]

                                            # Condition for dropping new calls
                                            if bbuNM + bbuNM * newCM > cls.mMTC_capacity:
                                                G1[j] = G1[j] + qn_2[j] + qn_1[j] + qn[j] + qh[j] + qh_1[j]
                                                k += 1

            # return the probabilities
            blocking_prob = cls.probabilities(G1, G)
            return slice_name, blocking_prob


class InterCalculations(IntraCalculations):

    def __init__(self):
        print('Inter Slice Handover Calculations Started\n')

    @classmethod
    def calculations(cls, slice_name, params):
        # Blocking and Dropping Probabilities
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
        # callA = np.arange(3, 8, .5)  # eMBB, uRLLC, mMTC
        callA = np.ones(10)
        callA *= 2
        callAM = callA + 2
        # callA = np.ones(10)
        # callA *= 2

        # Handoff Call Arrival rates
        handA = (callA * cls.handoff_rate) / 0.5

        # Initialise Available Bandwidth
        newB = np.ones(len(callA))
        handB = np.ones(len(handA))
        newBU = np.ones(len(callA))
        handBU = np.ones(len(handA))
        newBE = np.ones(len(callA))
        handBE = np.ones(len(handA))
        newBM = np.ones(len(callAM))

        # Initialise Loads
        newL = np.ones(len(newB))
        handL = np.ones(len(handB))
        newLU = np.ones(len(newB))
        handLU = np.ones(len(handB))
        newLE = np.ones(len(newBE))
        handLE = np.ones(len(handBE))
        newLM = np.ones(len(newB))

        if slice_name == 'mMTC':
            required_bbu = UseCases()
            bbuN = required_bbu.allocate_bbu('eMBB')[0]  # new call bbU
            bbuHE = required_bbu.allocate_bbu('eMBB')[1]  # handoff call bbu
            bbuNU = required_bbu.allocate_bbu('uRLLC')[0]
            bbuHU = required_bbu.allocate_bbu('uRLLC')[1]
            bbuNM = required_bbu.allocate_bbu(slice_name)

            cls.capacity = params[0]
            cls.new_thresh = params[1]
            cls.uRLLC_handoff_thresh = params[0] + 15
            cls.uRLLC_newcall_thresh = params[1]
            cls.uRLLC_capacity = params[0] + 15
            cls.eMBB_handoff_thresh = params[0] + 15
            cls.eMBB_newcall_thresh = params[1]
            cls.eMBB_capacity = params[0] + 15

            # Available bandwidth
            newB *= (cls.capacity / cls.capacity) * callAM
            newBU *= (cls.uRLLC_capacity / cls.uRLLC_capacity) * callA
            newBE *= (cls.eMBB_capacity / cls.eMBB_capacity) * callA
            handBE *= (cls.eMBB_capacity / cls.eMBB_capacity) * handA
            handBU *= (cls.uRLLC_capacity / cls.uRLLC_capacity) * handA

            # Load at each slice
            newLM *= newB / cls.holding_time1
            newLU *= newBU / cls.holding_time1
            handLU *= handBU / cls.holding_time2
            newLE *= newBE / cls.holding_time1
            handLE *= handBE / cls.holding_time2

            # Number calls that can be accepted
            newNum = round((cls.new_thresh / bbuNM) + 1)
            newNumE = round((cls.eMBB_newcall_thresh / bbuN) + 1)
            handNumE = round((cls.eMBB_handoff_thresh / bbuHE) + 1)
            newNumU = round((cls.uRLLC_newcall_thresh / bbuNU) + 1)
            handNumU = round((cls.uRLLC_handoff_thresh / bbuHU) + 1)
            h = []

            for i in range(10):
                for newCE in range(0, newNumE, 1):
                    for newCM in range(0, newNum, 1):
                        for newCU in range(0, newNumU, 1):
                            for handCE in range(0, handNumE, 1):
                                for handCU in range(0, handNumU, 1):

                                    # Admissible state condition
                                    if (bbuNU * (newCU + handCU) + bbuNM * newCM + bbuN * (
                                            newCE + handCE) <= cls.uRLLC_capacity) and (
                                            bbuN * (newCE + handCE) + bbuNM * newCM <= cls.eMBB_capacity) and (
                                            bbuNM * newCM <= cls.capacity) and (
                                            bbuN * newCE + bbuNU * newCU + bbuNM * newCM <= cls.uRLLC_newcall_thresh) and (
                                            bbuNM * newCM + bbuN * newCE <= cls.eMBB_newcall_thresh):

                                        for j in range(10):
                                            qn[j] = pow(newLU[j], newCU) / cls.factorial(newCU)
                                            qh[j] = pow(handLU[j], handCU) / cls.factorial(handCU)
                                            qn_1[j] = pow(newLE[j], newCE) / cls.factorial(newCE)
                                            qh_1[j] = pow(handLE[j], handCE) / cls.factorial(handCE)
                                            qn_2[j] = pow(newLM[j], newCM) / cls.factorial(newCM)
                                            # Normalisation Constant
                                            G[j] = G[j] + qn[j] + qh[j] + qh_1[j] + qn_1[j] + qn_2[j]

                                            # Condition for blocking new calls
                                            if (bbuNM + bbuNM * newCM > cls.capacity) and \
                                                    ((bbuNM + bbuNU * (newCU + handCU) + bbuN * (newCE + handCE) +
                                                      bbuNM * newCM > cls.uRLLC_capacity) or
                                                     (bbuNM + bbuNU * newCU + bbuN * newCE +
                                                      bbuNM * newCM > cls.uRLLC_newcall_thresh)) and \
                                                    ((bbuNM + bbuN * (
                                                            newCE + handCE) + bbuNM * newCM > cls.eMBB_capacity)
                                                     or (
                                                             bbuNM + bbuN * newCE + bbuNM * newCM > cls.eMBB_newcall_thresh)):
                                                G1[j] = G1[j] + qn[j] + qh[j] + qh_1[j] + qn_1[j] + qn_2[j]

            blocking_prob = cls.probabilities(G1, G)
            return slice_name, blocking_prob

        elif slice_name == 'eMBB':

            required_bbu = UseCases()
            bbuN = required_bbu.allocate_bbu(slice_name)[0]  # new call bbU
            bbuHE = required_bbu.allocate_bbu(slice_name)[1]  # handoff call bbu
            bbuNU = required_bbu.allocate_bbu('uRLLC')[0]
            bbuHU = required_bbu.allocate_bbu('uRLLC')[1]
            bbuNM = required_bbu.allocate_bbu('mMTC')

            cls.capacity = params[0]
            cls.new_thresh = params[1]
            cls.handoff_thresh = params[2]
            cls.uRLLC_handoff_thresh = params[2]
            cls.uRLLC_newcall_thresh = params[1]
            cls.uRLLC_capacity = params[0]
            cls.mMTC_capacity = params[1]
            cls.mMTC_thresh = params[1]

            # Available bandwidth
            newBM *= (cls.mMTC_capacity / cls.mMTC_capacity) * callAM
            newBU *= (cls.uRLLC_capacity / cls.uRLLC_capacity) * callA
            newBE *= (cls.capacity / cls.capacity) * callA
            handBE *= (cls.capacity / cls.capacity) * handA
            handBU *= (cls.uRLLC_capacity / cls.uRLLC_capacity) * handA

            # Load at each slice
            newLM *= newBM / cls.holding_time1
            newLU *= newBU / cls.holding_time1
            handLU *= handBU / cls.holding_time2
            newLE *= newBE / cls.holding_time1
            handLE *= handBE / cls.holding_time2

            # Number calls that can be accepted
            newNum = round((cls.mMTC_thresh / bbuNM) + 1)
            newNumE = round((cls.new_thresh / bbuN) + 1)
            handNumE = round((cls.handoff_thresh / bbuHE) + 1)
            newNumU = round((cls.uRLLC_newcall_thresh / bbuNU) + 1)
            handNumU = round((cls.uRLLC_handoff_thresh / bbuHU) + 1)
            h = []

            for i in range(10):
                for newCE in range(0, newNumE, 1):
                    for newCM in range(0, newNum, 1):
                        for newCU in range(0, newNumU, 1):
                            for handCE in range(0, handNumE, 1):
                                for handCU in range(0, handNumU, 1):

                                    if (bbuNU * (newCU + handCU) + bbuNM * newCM + bbuN * (
                                            newCE + handCE) <= cls.uRLLC_capacity) and (
                                            bbuN * (newCE + handCE) + bbuNM * newCM <= cls.capacity) and (
                                            bbuNM * newCM <= cls.mMTC_capacity) and (
                                            bbuN * newCE + bbuNU * newCU + bbuNM * newCM <= cls.uRLLC_newcall_thresh) and (
                                            bbuNM * newCM + bbuN * newCE <= cls.new_thresh):

                                        for j in range(10):
                                            qn[j] = pow(newLU[j], newCU) / cls.factorial(newCU)
                                            qh[j] = pow(handLU[j], handCU) / cls.factorial(handCU)
                                            qn_1[j] = pow(newLE[j], newCE) / cls.factorial(newCE)
                                            qh_1[j] = pow(handLE[j], handCE) / cls.factorial(handCE)
                                            qn_2[j] = pow(newLM[j], newCM) / cls.factorial(newCM)
                                            # Normalisation Constant
                                            G[j] = G[j] + qn[j] + qh[j] + qh_1[j] + qn_1[j] + qn_2[j]

                                            # Condition for blocking new calls
                                            if ((bbuN + bbuN * (newCE + handCE) + bbuNM * newCM > cls.capacity) or
                                                (bbuN + bbuN * newCE + bbuNM * newCM > cls.new_thresh)) and \
                                                    ((bbuN + bbuNU * (newCU + handCU) + bbuN * (newCE + handCE) +
                                                      bbuNM * newCM > cls.uRLLC_capacity) or
                                                     (bbuN + bbuNU * newCU + bbuN * newCE +
                                                      bbuNM * newCM > cls.uRLLC_newcall_thresh)):
                                                G1[j] = G1[j] + qn[j] + qh[j] + qh_1[j] + qn_1[j] + qn_2[j]

                                            # Condition for dropping handoff calls
                                            if (bbuN + bbuNU * (newCU + handCU) + bbuN * (newCE + handCE) +
                                                bbuNM * newCM > cls.uRLLC_capacity) and \
                                                    (bbuN + bbuN * (newCE + handCE) + bbuNM * newCM > cls.capacity):
                                                G2[j] = G2[j] + qn[j] + qh[j] + qh_1[j] + qn_1[j] + qn_2[j]

            blocking_prob = cls.probabilities(G1, G)
            dropping_prob = cls.probabilities(G2, G)
            return slice_name, blocking_prob, dropping_prob

        elif slice_name == 'uRLLC':
            required_bbu = UseCases()
            bbuNU = required_bbu.allocate_bbu(slice_name)[0]  # new call bbU
            bbuHU = required_bbu.allocate_bbu(slice_name)[1]  # handoff call bbu
            bbuNE = required_bbu.allocate_bbu('eMBB')[0]
            bbuHE = required_bbu.allocate_bbu('eMBB')[1]
            bbuNM = required_bbu.allocate_bbu('mMTC')

            cls.capacity = params[0]
            cls.new_thresh = params[1]
            cls.handoff_thresh = params[2]
            cls.eMBB_handoff_thresh = params[2]
            cls.eMBB_newcall_thresh = params[1]
            cls.eMBB_capacity = params[0]
            cls.mMTC_capacity = params[1]
            cls.mMTC_thresh = params[1]

            # Available bandwidth
            newBM *= (cls.mMTC_capacity / cls.mMTC_capacity) * callAM
            newBU *= (cls.capacity / cls.capacity) * callA
            newBE *= (cls.eMBB_capacity / cls.eMBB_capacity) * callA
            handBE *= (cls.eMBB_capacity / cls.eMBB_capacity) * handA
            handBU *= (cls.capacity / cls.capacity) * handA

            # Load at each slice
            newLM *= newBM / cls.holding_time1
            newLU *= newBU / cls.holding_time1
            handLU *= handBU / cls.holding_time2
            newLE *= newBE / cls.holding_time1
            handLE *= handBE / cls.holding_time2

            # Number calls that can be accepted
            newNumM = round((cls.mMTC_thresh / bbuNM) + 1)
            newNumE = round((cls.eMBB_newcall_thresh / bbuNE) + 1)
            handNumE = round((cls.eMBB_handoff_thresh / bbuHE) + 1)
            newNumU = round((cls.new_thresh / bbuNU) + 1)
            handNumU = round((cls.handoff_thresh / bbuHU) + 1)
            h = []

            for i in range(10):
                for newCE in range(0, newNumE, 1):
                    for newCM in range(0, newNumM, 1):
                        for newCU in range(0, newNumU, 1):
                            for handCE in range(0, handNumE, 1):
                                for handCU in range(0, handNumU, 1):

                                    if (bbuNU * (newCU + handCU) + bbuNM * newCM + bbuNE * (
                                            newCE + handCE) <= cls.capacity) and (
                                            bbuNE * (newCE + handCE) + bbuNM * newCM <= cls.eMBB_capacity) and (
                                            bbuNM * newCM <= cls.mMTC_capacity) and (
                                            bbuNE * newCE + bbuNU * newCU + bbuNM * newCM <= cls.new_thresh) and (
                                            bbuNM * newCM + bbuNE * newCE <= cls.new_thresh):

                                        for j in range(10):
                                            qn[j] = pow(newLU[j], newCU) / cls.factorial(newCU)
                                            qh[j] = pow(handLU[j], handCU) / cls.factorial(handCU)
                                            qn_1[j] = pow(newLE[j], newCE) / cls.factorial(newCE)
                                            qh_1[j] = pow(handLE[j], handCE) / cls.factorial(handCE)
                                            qn_2[j] = pow(newLM[j], newCM) / cls.factorial(newCM)
                                            # Normalisation Constant
                                            G[j] = G[j] + qn[j] + qh[j] + qh_1[j] + qn_1[j] + qn_2[j]

                                            # condition for blocking new calls
                                            if (bbuNU + bbuNU * (newCU + handCU) + bbuNE * (newCE + handCE) +
                                                bbuNM * newCM > cls.capacity) or \
                                                    (
                                                            bbuNU + bbuNU * newCU + bbuNM * newCM +
                                                            bbuNE * newCE > cls.new_thresh):
                                                G1[j] = G1[j] + qn[j] + qh[j] + qh_1[j] + qn_1[j] + qn_2[j]

                                            # condition for dropping handoff calls
                                            if (bbuNU + bbuNU * (newCU + handCU) + bbuNE * (newCE + handCE) +
                                                    bbuNM * newCM > cls.capacity):
                                                G2[j] = G2[j] + qn[j] + qh[j] + qh_1[j] + qn_1[j] + qn_2[j]

            blocking_prob = cls.probabilities(G1, G)
            dropping_prob = cls.probabilities(G2, G)
            return slice_name, blocking_prob, dropping_prob
