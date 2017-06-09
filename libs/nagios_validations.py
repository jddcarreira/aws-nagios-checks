class NagiosValidations(object):
    @staticmethod
    def high_is_bad(val, wrn, crt):
        if val >= crt:
            return 2
        elif val >= wrn:
            return 1
        elif val <= wrn:
            return 0
        else:
            return 3

    @staticmethod
    def high_is_good(val, wrn, crt):
        if val <= crt:
            return 2
        elif val <= wrn:
            return 1
        elif val >= wrn:
            return 0
        else:
            return 3
