import numpy as np
import tabula

from timetable_miner import miner_util


class PDFMiner:

    def __init__(self, buffer: bytes):
        path = miner_util.bytes_to_pdf(buffer)
        dfs = tabula.read_pdf(path, lattice=True, pages='all')
        self.__to_school_df = dfs[0].replace({'―': None, '-': None, ' ': None, '　': None, np.nan: None})
        self.__to_home_df = dfs[1].replace({'―': None, '-': None, ' ': None, '　': None, np.nan: None})

    @property
    def to_school_df(self):
        return self.__to_school_df

    @property
    def to_home_df(self):
        return self.__to_home_df
