import { Fragment } from "react";
import { Graph } from "./components/Graph";
import data from "./data/data.json";
export const App = () => {
	return (
		<Fragment>
			La App aqui
			<Graph data={data[0]} />
		</Fragment>
	);
};
