from typing import List

import pandas as pd
import tabula

from timetable_miner import miner_util


class PDFMiner:

    def __init__(self, buffers: List[bytes]):
        self.__buffers = buffers
        self.__pdf_count = len(buffers)
        self.__target_dfs: list = []
        self.__target_df: pd.DataFrame = pd.DataFrame()

    def read(self, ordinal: int) -> 'PDFMiner':
        if 0 <= ordinal < self.__pdf_count:
            buffer = self.__buffers[ordinal]
            path = miner_util.bytes_to_pdf(buffer)
            self.__target_dfs = tabula.read_pdf(path, lattice=True, pages='all')
            return self
        else:
            raise IndexError(f'The ordinal {ordinal} is not enable.')

    def replace(self, mappers: dict) -> 'PDFMiner':
        for df in self.__target_dfs:
            df.replace(mappers, inplace=True)
        return self

    def mine_to_school(self, columns: list = ['千歳駅発', '南千歳駅発', '研究実験棟発', '本部棟着', '備考']) -> pd.DataFrame:
        return self.__target_dfs[0][columns]

    def mine_to_chitose(self, columns: list = ['本部棟発', '研究実験棟着', '南千歳駅着', '千歳駅着', '備考']) -> pd.DataFrame:
        return self.__target_dfs[1][columns]
