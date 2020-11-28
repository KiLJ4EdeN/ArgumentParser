import sys
from typing import List


class ArgumentParser(object):
    def __init__(self, verbose: bool = True):
        self.verbose = verbose
        self.__argc: int = self.__set_argc
        self.__argv: List[str] = self.__set_argv

    @property
    def __set_argc(self) -> int:
        argc = len(sys.argv)
        if self.verbose:
            print(f"[INFO]: there are: {argc - 1} argument(s).")
        return argc

    @property
    def __set_argv(self) -> List[str]:
        argv = []
        for i, arg in enumerate(sys.argv):
            if i > 0:
                if self.verbose:
                    print(f"[INFO]: the {i} arg is: {arg}.")
                argv.append(arg)
        return argv

    def parse_arg(self, idx: int) -> str:
        assert len(self.__argv) >= idx, 'the entered idx is higher than the argument count'
        return self.__argv[idx]
