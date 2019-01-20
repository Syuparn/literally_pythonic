class __:
    def __init__(self, n=0, codes=''):
        self.n = n
        self.codes = codes

    def __getattr__(self, name):
        return __(self.n * 4 + len(name) - 1, self.codes)

    def __call__(self):
        return __(0, self.codes + chr(self.n))

    def __str__(self):
        return self.codes

    def __neg__(self):
        exec(self.codes)


_ = __()
