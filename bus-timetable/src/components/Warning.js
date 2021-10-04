import {Alert, AlertTitle} from "@mui/material";


function Warning() {
    return (
        <Alert severity="warning">
            <AlertTitle>注意</AlertTitle>
            このページでは今日0:00時点における<a href="https://www.chitose.ac.jp/info/access">大学へのアクセス</a>の一番上のPDFの内容を参照しています。PDFの更新状況によっては本日の時刻表を表示しない場合があります。
        </Alert>
    );
}

export default Warning;