import React from "react";
import {Container} from "@mui/material";
import {Box} from "@mui/material";
import Header from "./components/Header";
import Warning from "./components/Warning";
import TimeTable from "./components/TimeTable";

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
                <TimeTable direction="school" />
                <Box sx={{ m: 2 }} />
                <TimeTable direction="chitose" />
                <Box sx={{ m: 2 }} />
            </Container>
        </div>
    );
}

export default App;
