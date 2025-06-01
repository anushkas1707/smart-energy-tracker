import { Line } from 'react-chartjs-2';

function EnergyChart({ data }) {
    return <Line data={data} options={{ responsive: true }} />;
}
