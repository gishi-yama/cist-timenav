# pdf_retriever

公立千歳科学技術大学の[大学へのアクセス](https://www.chitose.ac.jp/info/access) からPDFを取得する。このプロジェクトはAPIを提供する。

### ベースURL

```
https://localhost:8082
```

#### `/info`
「大学へのアクセス」に表示されているPDFの数とタイトルを取得する。


#### `/url/<number>`
「大学へのアクセス」の上から `<number>` 番目に表示されているPDFのURLを取得する。 `<number>` は0から数える。


#### `/name/<number>`
「大学へのアクセス」の上から `<number>` 番目に表示されているPDFの表示名を取得する。 `<number>` は0から数える。


#### `/title/<number>`
「大学へのアクセス」の上から `<number>` 番目に表示されているPDFファイルの名称を取得する。 `<number>` は0から数える。


#### `/bytes/<number>`
「大学へのアクセス」の上から `<number>` 番目のPDFファイルを取得する。 `<number>` は0から数える。