/** @leewise-module */

import { CommonLeewiseChartConfigPanel } from "../common/config_panel";

export class LeewiseBarChartConfigPanel extends CommonLeewiseChartConfigPanel {
    onUpdateStacked(ev) {
        this.props.updateChart(this.props.figureId, {
            stacked: ev.target.checked,
        });
    }
}

LeewiseBarChartConfigPanel.template = "spreadsheet_edition.LeewiseBarChartConfigPanel";
