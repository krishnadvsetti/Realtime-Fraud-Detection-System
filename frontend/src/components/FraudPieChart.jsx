import {
    Card,
    CardContent,
    Typography
} from "@mui/material";

import {
    ResponsiveContainer,
    PieChart,
    Pie,
    Cell,
    Tooltip,
    Legend
} from "recharts";

const COLORS = [
    "#ef4444",
    "#22c55e"
];

export default function FraudPieChart({ summary }) {

    return (

        <Card sx={{ mt: 3 }}>

            <CardContent>

                <Typography
                    variant="h5"
                    gutterBottom
                >
                    Fraud Distribution
                </Typography>

                <ResponsiveContainer
                    width="100%"
                    height={400}
                >

                    <PieChart>

                        <Pie
                            data={summary}
                            dataKey="count"
                            nameKey="prediction"
                            outerRadius={150}
                            label
                        >

                            {
                                summary.map(
                                    (_, index) => (

                                        <Cell
                                            key={index}
                                            fill={
                                                COLORS[
                                                index %
                                                COLORS.length
                                                ]
                                            }
                                        />

                                    )
                                )
                            }

                        </Pie>

                        <Tooltip />

                        <Legend />

                    </PieChart>

                </ResponsiveContainer>

            </CardContent>

        </Card>

    );

}