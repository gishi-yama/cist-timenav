# timetable_miner

PDFから時刻表を抜き出し、JSON形式で返す。現在は大学発着の時刻表のみを抜き出し、市営のバスの時刻表は抜き出さない。

### ベースURL

```
https://localhost:8081
```

#### `/info`
「大学へのアクセス」に表示されているPDFの数とタイトルを取得する。

#### `/table/to/school/<number>` (Timestamp対応)
「大学へのアクセス」の `<number>` 番目のPDFから往路を取得する。 `<number>` は0から数える。

#### `/table/to/chitose/<number>` (Timestamp対応)
「大学へのアクセス」の `<number>` 番目のPDFから復路を取得する。 `<number>` は0から数える。

#### `/date/<number>`
「大学へのアクセス」の `<number>` 番目のPDFのタイトルに含まれる日付部を取得する。 `<number>` は0から数える。

#### 備考

- (Timestamp対応)のものは、末尾に `/timestamp` を付与すると、Timestampの形式で取得する。
- `<number>` は `oldest` とすることで一番上のものを取得できる。