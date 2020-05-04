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
        newBM = np.ones(len(callA))
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
        newLM = np.ones(len(newBM))

        required_bbu = UseCases()
        bbuN = required_bbu.allocate_bbu(slice_name)[0]  # new call bbU
        bbuH = required_bbu.allocate_bbu(slice_name)[1]  # handoff call bbu
        bbuNU = required_bbu.allocate_bbu('uRLLC')[0]
        bbuHU = required_bbu.allocate_bbu('uRLLC')[1]
        bbuNM = required_bbu.allocate_bbu('mMTC')

        cls.capacity = params[0]  # slice capacity
        cls.new_thresh = params[1]  # new call threshold
        cls.handoff_thresh = params[2]  # handoff call threshold
        cls.uRLLC_handoff_thresh = params[2]  # handoff threshold for uRLLC
        cls.uRLLC_newcall_thresh = params[1]  # newcall threshold for uRLLC
        cls.uRLLC_capacity = params[0]  # capacity for uRLLC
        cls.mMTC_capacity = params[0] - 15  # mMTC capacity
        cls.uRLLC_capacity_inter = 0.6 * cls.uRLLC_capacity
        cls.uRLLC_newcall_thresh_inter = 0.6 * cls.uRLLC_newcall_thresh
        cls.uRLLC_handoff_thresh_inter = 0.6 * cls.uRLLC_capacity

        # Available bandwidth
        newB *= (cls.capacity / (cls.capacity * 3)) * callA
        handB *= (cls.capacity / (cls.capacity * 3)) * handA
        newBU *= (cls.uRLLC_capacity / (cls.uRLLC_capacity * 3)) * callA
        handBU *= (cls.uRLLC_capacity / (cls.uRLLC_capacity * 3)) * handA
        newBM *= (cls.mMTC_capacity / (cls.mMTC_capacity * 3)) * callA

        # Load at each slice
        newL *= newB / cls.holding_time1
        handL *= handB / cls.holding_time2
        newLU *= newBU / cls.holding_time1
        handLU *= handBU / cls.holding_time2
        newLM *= newBM / cls.holding_time1

        # Number calls that can be accepted

        newNum = round((cls.new_thresh / bbuN) + 1)
        handNum = round((cls.handoff_thresh / bbuH) + 1)
        newNumU = round((cls.uRLLC_newcall_thresh / bbuNU) + 1)
        handNumU = round((cls.uRLLC_handoff_thresh / bbuHU) + 1)
        newNumM = round((cls.mMTC_capacity / bbuNM) + 1)
        n = 0
        l = []

        for i in range(10):
            for newC in range(1, newNumM, 1):
                for newCE in range(1, newNum, 1):
                    for newCU in range(1, newNumU, 1):
                        for handCE in range(1, handNum, 1):
                            for handCU in range(1, handNumU, 1):

                                # Admissible States

                                if (bbuNU * (newCU + handCU) + bbuNM * newC + bbuN * (
                                        newCE + handCE) <= cls.uRLLC_capacity) \
                                        and (bbuNM * newC + bbuN * (newCE + handCE) <= cls.capacity) and \
                                        bbuNM * newC <= cls.mMTC_capacity and \
                                        (bbuNU * newCU + bbuN * newCE + bbuNM * newC <= cls.uRLLC_newcall_thresh) and \
                                        (bbuN * newCE + bbuNM * newC <= cls.new_thresh) and \
                                        (bbuN * handCE + bbuNM * handCU <= cls.uRLLC_capacity) and \
                                        bbuN * handCE <= cls.capacity:
                                    n += 1

                                    for j in range(10):
                                        qn[j] = pow(newLM[j], newC) / cls.factorial(newC)
                                        qn_1[j] = pow(newL[j], newCE) / cls.factorial(newCE)
                                        qn_2[j] = pow(newLU[j], newCU) / cls.factorial(newCU)
                                        qh_1[j] = pow(handL[j], handCE) / cls.factorial(handCE)
                                        qh_2[j] = pow(handLU[j], handCU) / cls.factorial(handCU)
                                        G[j] = G[j] + qn[j] + qn_1[j] * qh_1[j] + qn_2[j] * qh_2[j]

                                        if slice_name == 'eMBB':
                                            if ((bbuN + bbuN * (newCE + handCE) + bbuNM * newC > cls.capacity) or
                                                (bbuN + bbuN * newCE + bbuNM * newC > cls.new_thresh)) and \
                                                    ((bbuN + bbuNU * (newCU + handCU) + bbuN * (
                                                            newCE + handCE) + bbuNM * newC > cls.uRLLC_capacity_inter)
                                                     or (bbuNM * newC + bbuN * newCE + bbuNU + bbuNU * newCU <
                                                         cls.uRLLC_newcall_thresh_inter)):
                                                G1[j] = G1[j] + qn[j] + qn_1[j] * qh_1[j] + qn_2[j] * qh_2[j]

                                            

        blocking_probabilities = cls.probabilities(G1, G)
        dropping_probabilities = cls.probabilities(G2, G)
        return slice_name, blocking_probabilities, dropping_probabilities