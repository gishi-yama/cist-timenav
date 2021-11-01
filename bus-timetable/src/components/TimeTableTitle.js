import {useEffect, useState} from "react";
import {CircularProgress, Typography} from "@mui/material";


function TimeTableTitle(props) {
    const [error, setError] = useState(null);
    const [isLoaded, setIsLoaded] = useState(false);
    const [item, setItem] = useState({})

    useEffect(() => {
        fetch("/date/oldest")
            .then(res => res.json())
            .then(
                (results) => {
                    setIsLoaded(true);
                    setItem(results);
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
        if (props.direction === "school") {
            return <Typography variant="h6">往路（{ item.results }）</Typography>
        } else {
            return <Typography variant="h6">復路（{ item.results }）</Typography>
        }
    }
}

export default TimeTableTitle;