class UseCases:
    bbuV = 3
    bbuS = 2
    bbuA = 2
    bbuAh = 3
    bbuVh = 4

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
