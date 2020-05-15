class UseCases:
    bbuV = 3
    bbuS = bbuV-1
    bbuA = bbuV-1
    bbuAh = bbuV-1
    bbuVh = bbuV

    @classmethod
    def allocate_bbu(cls, names):
        if 'mMTC' in names:
            return cls.bbuS
        elif 'eMBB' in names:
            return cls.bbuV, cls.bbuVh
        elif 'uRLLC' in names:
            return cls.bbuA, cls.bbuAh
        else:
            return 'Use Case not defined'
