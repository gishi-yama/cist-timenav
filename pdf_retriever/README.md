# pdf_retriever

公立千歳科学技術大学の[大学へのアクセス](https://www.chitose.ac.jp/info/access)からPDFを取得する。現在はHTML上で最古のPDFを取得する。

## API

APIを呼び出すには、以下のパターンのURLにアクセスする。

```
http://localhost:8081/<route>
```

### `/pdf_url`

HTML上で最古のPDFのURLを取得する。

### `/pdf/bytes`

HTML上で最古のPDFをbytes型で取得する。