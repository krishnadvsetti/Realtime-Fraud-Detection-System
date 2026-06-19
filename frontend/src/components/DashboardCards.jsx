import { Grid, Card, CardContent, Typography } from "@mui/material";

export default function DashboardCards({
    metrics
}) {
    return (
        <Grid container spacing={3} sx={{ mt: 2 }}>

            <Grid item xs={12} md={3}>
                <Card>
                    <CardContent>
                        <Typography variant="h6">
                            Total Transactions
                        </Typography>

                        <Typography variant="h3">
                            {metrics.total_transactions ?? 0}
                        </Typography>
                    </CardContent>
                </Card>
            </Grid>

            <Grid item xs={12} md={3}>
                <Card>
                    <CardContent>
                        <Typography variant="h6">
                            Fraud Alerts
                        </Typography>

                        <Typography variant="h3">
                            {metrics.fraud_alerts ?? 0}
                        </Typography>
                    </CardContent>
                </Card>
            </Grid>

            <Grid item xs={12} md={3}>
                <Card>
                    <CardContent>
                        <Typography variant="h6">
                            Fraud Rate
                        </Typography>

                        <Typography variant="h3">
                            {metrics.fraud_rate ?? 0}%
                        </Typography>
                    </CardContent>
                </Card>
            </Grid>

            <Grid item xs={12} md={3}>
                <Card>
                    <CardContent>
                        <Typography variant="h6">
                            Avg Risk Score
                        </Typography>

                        <Typography variant="h3">
                            {metrics.avg_risk_score ?? 0}
                        </Typography>
                    </CardContent>
                </Card>
            </Grid>

        </Grid>
    );
}