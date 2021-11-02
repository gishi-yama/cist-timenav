import React, {useEffect, useState} from "react";
import {
    CircularProgress, styled,
    Table,
    TableBody,
    TableCell, tableCellClasses,
    TableHead,
    TableRow
} from "@mui/material";


const StyledTableCell = styled(TableCell)(({ theme }) => ({
    [`&.${tableCellClasses.head}`]: {
        backgroundColor: theme.palette.primary.main,
        color: theme.palette.common.white,
    }
}))


function TimeTableContents(props) {
    const [error, setError] = useState(null);
    const [isLoaded, setIsLoaded] = useState(false);
    const [items, setItems] = useState({results: []})

    useEffect(() => {
        if (props.direction === "school") {
            fetch("/table/to/school/oldest")
                .then(res => res.json())
                .then(
                    (results) => {
                        setIsLoaded(true);
                        setItems(results);
                    }
                )
                .catch(
                    (error) => {
                        setIsLoaded(true);
                        setError(error);
                    }
                )
        } else if (props.direction === "chitose") {
            fetch("/table/to/chitose/oldest")
                .then(res => res.json())
                .then(
                    (results) => {
                        setIsLoaded(true);
                        setItems(results);
                    }
                )
                .catch(
                    (error) => {
                        setIsLoaded(true);
                        setError(error);
                    }
                )
        }
    }, [])

    if (error) {
        return <div>Error: {error.message}</div>
    } else if (!isLoaded) {
        return <CircularProgress/>
    } else {
        if (props.direction === "school") {
            return (
                <Table sx={{minWidth: 650}} aria-label="timetable">
                    <TableHead>
                        <TableRow>
                            <StyledTableCell>千歳駅発</StyledTableCell>
                            <StyledTableCell>南千歳駅発</StyledTableCell>
                            <StyledTableCell>研究実験棟発</StyledTableCell>
                            <StyledTableCell>本部棟着</StyledTableCell>
                            <StyledTableCell>備考</StyledTableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {items.results.map((item) => (
                            <TableRow>
                                <TableCell> {item.chitose} </TableCell>
                                <TableCell> {item.minamiChitose} </TableCell>
                                <TableCell> {item.studyBldg} </TableCell>
                                <TableCell> {item.mainBldg} </TableCell>
                                <TableCell> {item.note} </TableCell>
                            </TableRow>
                        ))}
                    </TableBody>
                </Table>
            )
        } else {
            return (
                <Table sx={{minWidth: 650}} aria-label="timetable">
                    <TableHead>
                        <TableRow>
                            <StyledTableCell>本部棟発</StyledTableCell>
                            <StyledTableCell>研究実験棟着</StyledTableCell>
                            <StyledTableCell>南千歳駅着</StyledTableCell>
                            <StyledTableCell>千歳駅着</StyledTableCell>
                            <StyledTableCell>備考</StyledTableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {items.results.map(item => (
                            <TableRow>
                                <TableCell> {item.mainBldg} </TableCell>
                                <TableCell> {item.studyBldg} </TableCell>
                                <TableCell> {item.minamiChitose} </TableCell>
                                <TableCell> {item.chitose} </TableCell>
                                <TableCell> {item.note} </TableCell>
                            </TableRow>
                        ))}
                    </TableBody>
                </Table>
            )
        }
    }
}

export default TimeTableContents;