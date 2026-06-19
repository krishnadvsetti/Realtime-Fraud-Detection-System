import {

    Chip

} from "@mui/material";

export default function LiveStatus() {

    return (

        <Chip

            label="🟢 LIVE"

            color="success"

            sx={{

                fontSize: 18,
                fontWeight: "bold",
                mt: 2

            }}

        />

    );

}