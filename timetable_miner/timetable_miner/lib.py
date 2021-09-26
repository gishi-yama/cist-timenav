from typing import Union

import tabula

from timetable_miner import config


class PdfMiner:

    def __init__(self, path_or_buf: Union[str, bytes]):
        if type(path_or_buf) is bytes:
            buf = path_or_buf
            with open('tmp.pdf', 'wb') as f:
                f.write(buf)
            self.__dfs = tabula.read_pdf('tmp.pdf', lattice=True, pages='all')
        else:
            path = path_or_buf
            self.__dfs = tabula.read_pdf(path, lattice=True, pages='all')
        self.__outward_df = self.__dfs[0][config.outward_columns]
        self.__return_df = self.__dfs[1][config.return_columns]
        self.__outwards = self.__outward_df.to_dict(orient='records')
        self.__returns = self.__return_df.to_dict(orient='records')

    def outwards_and_returns(self) -> dict:
        return {'往路': self.__outwards, '復路': self.__returns}

    @property
    def outwards(self) -> dict:
        return self.__outwards

    @property
    def returns(self) -> dict:
        return self.__returns

