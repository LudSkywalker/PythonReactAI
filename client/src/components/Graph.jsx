import { Fragment } from "react";
import Plot from "react-plotly.js";
export const Graph = (props) => {
	let layout = {
		autosize: false,
		width: 700,
		height: 700,
		xaxis: {
			fixedrange: true,
			range: [-1.5, 1.5],
		},
		yaxis: {
			fixedrange: true,
			range: [-1.5, 1.5],
		},
	};
	let { X: XY, Y: Z } = props.data;
	let blueDataset = [];
	let redDataset = [];
	for (let i = 0; i < Z.length; i++) {
		if (Z[i][0] == 1) {
			redDataset.push({
				x: XY[i][0],
				y: XY[i][1],
			});
		} else {
			blueDataset.push({
				x: XY[i][0],
				y: XY[i][1],
			});
		}
	}
	let data = [
		{
			x: blueDataset.map((xy) => xy.x),
			y: blueDataset.map((xy) => xy.y),
			mode: "markers",
			type: "scatter",
			marker: {
				size: 12,
				color: "skyblue",
			},
		},
		{
			x: Array.from(redDataset, (xy) => xy.x),
			y: Array.from(redDataset, (xy) => xy.y),
			mode: "markers",
			type: "scatter",
			marker: {
				size: 12,
				color: "salmon",
			},
		},
	];
	console.log(data);
	return (
		<Fragment>
			<div>
				<h3>La Grafica va aqui</h3>
				<Plot layout={layout} data={data} config={{displayModeBar: false }} />
			</div>
		</Fragment>
	);
};
