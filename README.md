# cist-timenav

本プロジェクトは以下の3つのサービスで構成されている。

1. pdf_retriever
2. timetable_miner
3. bus-timetable

## [pdf_retriever](https://github.com/k-oketa/cist-timenav/tree/develop/pdf_retriever)

公立千歳科学技術大学の[大学へのアクセス](https://www.chitose.ac.jp/info/access)からPDFを取得する。現在はHTML上で最古のPDFを取得する。

## [timetable_miner](https://github.com/k-oketa/cist-timenav/tree/develop/timetable_miner)

PDFから時刻表を抜き出し、JSON形式で返す。現在は大学発着の時刻表のみを抜き出し、市営のバスの時刻表は抜き出さない。

## [bus-timetable](https://github.com/k-oketa/cist-timenav/tree/develop/bus-timetable)

公立千歳科学技術大学のバスの時刻表を表示する。