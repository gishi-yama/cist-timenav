import {Card, CardContent, CircularProgress, Table, Typography} from "@mui/material";
import {TableBody} from "@mui/material";
import {TableCell} from "@mui/material";
import {TableContainer} from "@mui/material";
import {TableHead} from "@mui/material";
import {TableRow} from "@mui/material";
import React, {useEffect, useState} from "react";

function ReturnTimeTable() {
    const [error, setError] = useState(null);
    const [isLoaded, setIsLoaded] = useState(false);
    const [items, setItems] = useState({return: []})

    useEffect(() => {
        fetch("/returns")
            .then(res => res.json())
            .then(
                (result) => {
                    setIsLoaded(true);
                    setItems(result);
                }
            )
            .catch(
                (error) => {
                    setIsLoaded(true);
                    setError(error);
                }
            )
    }, [])

    if (error) {
        return <div>Error: {error.message}</div>
    } else if (!isLoaded) {
        return <CircularProgress />
    } else {
        return (
            <Card>
                <CardContent>
                    <Typography variant="h5">復路</Typography>
                    <TableContainer>
                        <Table sx={{ minWidth: 650 }} aria-label="timetable">
                            <TableHead>
                                <TableRow>
                                    <TableCell>本部棟発</TableCell>
                                    <TableCell>研究実験棟着</TableCell>
                                    <TableCell>南千歳駅着</TableCell>
                                    <TableCell>千歳駅着</TableCell>
                                    <TableCell>備考</TableCell>
                                </TableRow>
                            </TableHead>
                            <TableBody>
                                {items.return.map(item => (
                                    <TableRow>
                                        <TableCell> {item.fromMainBldg} </TableCell>
                                        <TableCell> {item.toStudyBldg} </TableCell>
                                        <TableCell> {item.toMinamiChitoseSta} </TableCell>
                                        <TableCell> {item.toChitoseSta} </TableCell>
                                        <TableCell> {item.note} </TableCell>
                                    </TableRow>
                                ))}
                            </TableBody>
                        </Table>
                    </TableContainer>
                </CardContent>
            </Card>
        )
    }
}

export default ReturnTimeTable;