# timetable_miner

PDFから時刻表を抜き出し、JSON形式で返す。現在は大学発着の時刻表のみを抜き出し、市営のバスの時刻表は抜き出さない。

## API

APIを呼び出すには、以下のパターンのURLにアクセスする。

```
http://localhost:8080/<route>
```

### `/outwards`

往路の時刻表をJSONで取得する。

### `/returns`

復路の時刻表をJSONで取得する。