/** @leewise-module */

import { CommonLeewiseChartConfigPanel } from "../common/config_panel";

export class LeewiseLineChartConfigPanel extends CommonLeewiseChartConfigPanel {
    onUpdateStacked(ev) {
        this.props.updateChart(this.props.figureId, {
            stacked: ev.target.checked,
        });
    }
    onUpdateCumulative(ev) {
        this.props.updateChart(this.props.figureId, {
            cumulative: ev.target.checked,
        });
    }
}

LeewiseLineChartConfigPanel.template = "spreadsheet_edition.LeewiseLineChartConfigPanel";
