import {AppBar} from "@mui/material";
import {Toolbar} from "@mui/material";
import {Typography} from "@mui/material";

function Header() {
    return (
        <AppBar position="static">
            <Toolbar>
                <Typography variant="h6" component="div">
                    公立千歳科学技術大学 非公式バス時刻表
                </Typography>
            </Toolbar>
        </AppBar>
    );
}

export default Header;