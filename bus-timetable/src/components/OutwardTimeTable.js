import {Card, CardContent, CircularProgress, Table, Typography} from "@mui/material";
import {TableBody} from "@mui/material";
import {TableCell} from "@mui/material";
import {TableContainer} from "@mui/material";
import {TableHead} from "@mui/material";
import {TableRow} from "@mui/material";
import React, {useEffect, useState} from "react";

function OutwardTimeTable() {
    const [error, setError] = useState(null);
    const [isLoaded, setIsLoaded] = useState(false);
    const [items, setItems] = useState({outward: []})

    useEffect(() => {
        fetch("/to/school")
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
                    <Typography variant="h5">往路</Typography>
                    <TableContainer>
                        <Table sx={{ minWidth: 650 }} aria-label="timetable">
                            <TableHead>
                                <TableRow>
                                    <TableCell>千歳駅発</TableCell>
                                    <TableCell>南千歳駅発</TableCell>
                                    <TableCell>研究実験棟発</TableCell>
                                    <TableCell>本部棟着</TableCell>
                                    <TableCell>備考</TableCell>
                                </TableRow>
                            </TableHead>
                            <TableBody>
                                {items.outward.map(item => (
                                    <TableRow>
                                        <TableCell> {item.fromChitoseSta} </TableCell>
                                        <TableCell> {item.fromMinamiChitoseSta} </TableCell>
                                        <TableCell> {item.fromStudyBldg} </TableCell>
                                        <TableCell> {item.toMainBldg} </TableCell>
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

export default OutwardTimeTable;