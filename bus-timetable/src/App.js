import React from "react";
import {Container} from "@mui/material";
import {Box} from "@mui/material";
import Header from "./components/Header";
import {Typography} from "@mui/material";
import OutwardTimeTable from "./components/OutwardTimeTable";
import ReturnTimeTable from "./components/ReturnTimeTable";

function App() {
    return (
        <div className="App">
            <header className="App-header">
                <Header />
            </header>
            <Container maxWidth="xl">
                <Box sx={{ m: 2 }} />
                <Typography variant="h4">往路</Typography>
                <Box sx={{ m: 1 }} />
                <OutwardTimeTable />
                <Box sx={{ m: 2 }} />
                <Typography variant="h4">復路</Typography>
                <Box sx={{ m: 1 }} />
                {/*<ReturnTimeTable />*/}
            </Container>
        </div>
    );
}

export default App;
