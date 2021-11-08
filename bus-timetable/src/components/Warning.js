import {Alert, AlertTitle} from "@mui/material";


function Warning() {
    return (
        <Alert severity="warning">
            <AlertTitle>注意</AlertTitle>
            本システムは、AM/PM0:00の<a href="https://www.chitose.ac.jp/info/access">大学へのアクセス</a>の一番上のPDFの内容を表示しています。PDFの更新状況によっては本日の時刻表を表示しません。特に週明けの朝は更新されない傾向にあります。ご注意ください。
        </Alert>
    );
}

export default Warning;