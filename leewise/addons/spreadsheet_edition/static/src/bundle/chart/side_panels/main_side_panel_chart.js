/** @leewise-module **/

import { patch } from "@web/core/utils/patch";
import * as spreadsheet from "@leewise/o-spreadsheet";

const { chartRegistry } = spreadsheet.registries;
const { ChartPanel } = spreadsheet.components;

/**
 * This patch is necessary to ensure that the chart type cannot be changed
 * between leewise charts and spreadsheet charts.
 */

patch(ChartPanel.prototype, {
    get chartTypes() {
        const definition = this.getChartDefinition();
        const isLeewise = definition.type.startsWith("leewise_");
        return this.getChartTypes(isLeewise);
    },

    /**
     * @param {boolean} isLeewise
     */
    getChartTypes(isLeewise) {
        const result = {};
        for (const key of chartRegistry.getKeys()) {
            if ((isLeewise && key.startsWith("leewise_")) || (!isLeewise && !key.startsWith("leewise_"))) {
                result[key] = chartRegistry.get(key).name;
            }
        }
        return result;
    },

    onTypeChange(type) {
        if (this.getChartDefinition().type.startsWith("leewise_")) {
            const definition = {
                stacked: false,
                verticalAxisPosition: "left",
                ...this.env.model.getters.getChartDefinition(this.figureId),
                type,
            };
            this.env.model.dispatch("UPDATE_CHART", {
                definition,
                id: this.figureId,
                sheetId: this.env.model.getters.getActiveSheetId(),
            });
        } else {
            super.onTypeChange(type);
        }
    },
});
