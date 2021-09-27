from typing import Union

import numpy as np
import tabula

from timetable_miner import config


class PdfMiner:

    def __init__(self, buf: bytes):
        path = self.__buf_to_file(buf)
        self.__dfs = tabula.read_pdf(path, lattice=True, pages='all')
        self.__outward_df = self.__dfs[0][config.outward_columns]
        self.__outward_df = self.__outward_df.rename(
            columns={'千歳駅発': 'fromChitoseSta', '南千歳駅発': 'fromMinamiChitoseSta',
                     '研究実験棟発': 'fromStudyBldg', '本部棟着': 'toMainBldg', '備考': 'note'})
        self.__return_df = self.__dfs[1][config.return_columns]
        self.__return_df = self.__return_df.rename(
            columns={'千歳駅着': 'toChitoseSta', '南千歳駅着': 'toMinamiChitoseSta',
                     '研究実験棟着': 'toStudyBldg', '本部棟発': 'fromMainBldg', '備考': 'note'})
        self.__outwards = self.__outward_df.replace(np.nan, 'null').to_dict(orient='records')
        self.__returns = self.__return_df.replace(np.nan, 'null').to_dict(orient='records')

    def __buf_to_file(self, buf: Union[str, bytes]) -> str:
        with open('tmp.pdf', 'wb') as f:
            f.write(buf)
        return f.name

    def outwards_and_returns(self) -> dict:
        return {'outward': self.__outwards, 'return': self.__returns}

    @property
    def outwards(self) -> dict:
        return {"outward": self.__outwards}

    @property
    def returns(self) -> dict:
        return {"return": self.__returns}
