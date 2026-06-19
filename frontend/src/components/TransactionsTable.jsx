import {

    Card,
    CardContent,
    Typography,
    Table,
    TableBody,
    TableCell,
    TableContainer,
    TableHead,
    TableRow,
    Paper

} from "@mui/material";

export default function TransactionsTable({

    transactions

}) {

    return (

        <Card sx={{ mt: 3 }}>

            <CardContent>

                <Typography
                    variant="h5"
                    gutterBottom
                >
                    Recent Transactions
                </Typography>

                <TableContainer
                    component={Paper}
                >

                    <Table>

                        <TableHead>

                            <TableRow>

                                <TableCell>ID</TableCell>
                                <TableCell>Amount</TableCell>
                                <TableCell>Merchant</TableCell>
                                <TableCell>Hour</TableCell>
                                <TableCell>Risk</TableCell>
                                <TableCell>Status</TableCell>

                            </TableRow>

                        </TableHead>

                        <TableBody>

                            {
                                transactions.map(

                                    (tx) => (

                                        <TableRow
                                            key={tx.id}
                                        >

                                            <TableCell>
                                                {tx.id}
                                            </TableCell>

                                            <TableCell>
                                                ${tx.amount}
                                            </TableCell>

                                            <TableCell>
                                                {tx.merchant_id}
                                            </TableCell>

                                            <TableCell>
                                                {tx.hour}
                                            </TableCell>

                                            <TableCell>
                                                {tx.risk_score}
                                            </TableCell>

                                            <TableCell
                                                sx={{
                                                    color:
                                                        tx.prediction ===
                                                        "FRAUD"
                                                            ? "red"
                                                            : "green",
                                                    fontWeight:
                                                        "bold"
                                                }}
                                            >

                                                {tx.prediction}

                                            </TableCell>

                                        </TableRow>

                                    )

                                )
                            }

                        </TableBody>

                    </Table>

                </TableContainer>

            </CardContent>

        </Card>

    );

}