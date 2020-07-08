class UseCases:
    bbuV = 4  # new call bbu for eMBB
    bbuS = bbuV - 2  # new call bbu for mMTC
    bbuA = bbuV - 1  # new call bbu for uRLLC
    bbuAh = bbuA  # handoff call bbu for uRLLC
    bbuVh = bbuV  # handoff call bbu for eMBB

    @classmethod
    def allocate_bbu(cls, names):
        if 'mMTC' in names:
            return cls.bbuS
        elif 'eMBB' in names:
            return cls.bbuV, cls.bbuVh
        elif 'uRLLC' in names:
            return cls.bbuA, cls.bbuAh
        else:
            return None
