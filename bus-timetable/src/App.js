import React from "react";
import Container from "@mui/material/Container";
import AppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";

function App() {
    return (
        <div className="App">
            <header className="App-header">
                <AppBar>
                    <Toolbar>
                        <Typography variant="h6" component="div">
                            公立千歳科学技術大学 非公式バス時刻表
                        </Typography>
                    </Toolbar>
                </AppBar>
            </header>
            <Container maxWidth="lg">
                
            </Container>
        </div>
    );
}

export default App;
