import React from "react";
import {Container} from "@mui/material";
import {Box} from "@mui/material";
import Header from "./components/Header";
import OutwardTimeTable from "./components/OutwardTimeTable";
import ReturnTimeTable from "./components/ReturnTimeTable";
import Warning from "./components/Warning";

function App() {
    return (
        <div className="App">
            <header className="App-header">
                <Header />
            </header>
            <Container maxWidth="xl">
                <Box sx={{ m: 2}} />
                <Warning />
                <Box sx={{ m: 2 }} />
                <OutwardTimeTable />
                <Box sx={{ m: 2 }} />
                <ReturnTimeTable />
                <Box sx={{ m: 2 }} />
            </Container>
        </div>
    );
}

export default App;
