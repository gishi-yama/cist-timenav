import {Card, CardContent, TableContainer} from "@mui/material";
import TimeTableTitle from "./TimeTableTitle";
import TimeTableContents from "./TimeTableContents";


function TimeTable(props) {
    return (
        <Card>
            <CardContent>
                <TimeTableTitle direction={props.direction}/>
                <TableContainer>
                    <TimeTableContents direction={props.direction}/>
                </TableContainer>
            </CardContent>
        </Card>
    )
}

export default TimeTable;