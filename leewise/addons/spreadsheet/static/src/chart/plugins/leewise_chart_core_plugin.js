/** @leewise-module */
import * as spreadsheet from "@leewise/o-spreadsheet";
import { globalFiltersFieldMatchers } from "@spreadsheet/global_filters/plugins/global_filters_core_plugin";
import { checkFilterFieldMatching } from "@spreadsheet/global_filters/helpers";
import { CommandResult } from "../../o_spreadsheet/cancelled_reason";
import { Domain } from "@web/core/domain";

const { CorePlugin } = spreadsheet;

/**
 * @typedef {Object} Chart
 * @property {Object} fieldMatching
 *
 * @typedef {import("@spreadsheet/global_filters/plugins/global_filters_core_plugin").FieldMatching} FieldMatching
 */

export class LeewiseChartCorePlugin extends CorePlugin {
    constructor(config) {
        super(config);

        /** @type {Object.<string, Chart>} */
        this.charts = {};

        globalFiltersFieldMatchers["chart"] = {
            getIds: () => this.getters.getLeewiseChartIds(),
            getDisplayName: (chartId) => this.getters.getLeewiseChartDisplayName(chartId),
            getFieldMatching: (chartId, filterId) =>
                this.getLeewiseChartFieldMatching(chartId, filterId),
            getModel: (chartId) =>
                this.getters.getChart(chartId).getDefinitionForDataSource().metaData.resModel,
        };
    }

    allowDispatch(cmd) {
        switch (cmd.type) {
            case "ADD_GLOBAL_FILTER":
            case "EDIT_GLOBAL_FILTER":
                if (cmd.chart) {
                    return checkFilterFieldMatching(cmd.chart);
                }
        }
        return CommandResult.Success;
    }

    /**
     * Handle a spreadsheet command
     *
     * @param {Object} cmd Command
     */
    handle(cmd) {
        switch (cmd.type) {
            case "CREATE_CHART": {
                switch (cmd.definition.type) {
                    case "leewise_pie":
                    case "leewise_bar":
                    case "leewise_line":
                        this._addLeewiseChart(cmd.id);
                        break;
                }
                break;
            }
            case "DELETE_FIGURE": {
                const charts = { ...this.charts };
                delete charts[cmd.id];
                this.history.update("charts", charts);
                break;
            }
            case "REMOVE_GLOBAL_FILTER":
                this._onFilterDeletion(cmd.id);
                break;
            case "ADD_GLOBAL_FILTER":
            case "EDIT_GLOBAL_FILTER":
                if (cmd.chart) {
                    this._setLeewiseChartFieldMatching(cmd.filter.id, cmd.chart);
                }
                break;
        }
    }

    // -------------------------------------------------------------------------
    // Getters
    // -------------------------------------------------------------------------

    /**
     * Get all the leewise chart ids
     * @returns {Array<string>}
     */
    getLeewiseChartIds() {
        return Object.keys(this.charts);
    }

    /**
     * @param {string} chartId
     * @returns {string}
     */
    getChartFieldMatch(chartId) {
        return this.charts[chartId].fieldMatching;
    }

    /**
     *
     * @param {string} chartId
     * @returns {string}
     */
    getLeewiseChartDisplayName(chartId) {
        return `(#${this.getLeewiseChartIds().indexOf(chartId) + 1}) ${
            this.getters.getChart(chartId).title
        }`;
    }

    /**
     * Import the charts
     *
     * @param {Object} data
     */
    import(data) {
        for (const sheet of data.sheets) {
            if (sheet.figures) {
                for (const figure of sheet.figures) {
                    if (figure.tag === "chart" && figure.data.type.startsWith("leewise_")) {
                        this._addLeewiseChart(figure.id, figure.data.fieldMatching);
                    }
                }
            }
        }
    }
    /**
     * Export the chart
     *
     * @param {Object} data
     */
    export(data) {
        for (const sheet of data.sheets) {
            if (sheet.figures) {
                for (const figure of sheet.figures) {
                    if (figure.tag === "chart" && figure.data.type.startsWith("leewise_")) {
                        figure.data.fieldMatching = this.getChartFieldMatch(figure.id);
                        figure.data.searchParams.domain = new Domain(
                            figure.data.searchParams.domain
                        ).toJson();
                    }
                }
            }
        }
    }
    // -------------------------------------------------------------------------
    // Private
    // -------------------------------------------------------------------------

    /**
     * Get the current leewiseChartFieldMatching of a chart
     *
     * @param {string} chartId
     * @param {string} filterId
     */
    getLeewiseChartFieldMatching(chartId, filterId) {
        return this.charts[chartId].fieldMatching[filterId];
    }

    /**
     * Sets the current leewiseChartFieldMatching of a chart
     *
     * @param {string} filterId
     * @param {Record<string,FieldMatching>} chartFieldMatches
     */
    _setLeewiseChartFieldMatching(filterId, chartFieldMatches) {
        const charts = { ...this.charts };
        for (const [chartId, fieldMatch] of Object.entries(chartFieldMatches)) {
            charts[chartId].fieldMatching[filterId] = fieldMatch;
        }
        this.history.update("charts", charts);
    }

    _onFilterDeletion(filterId) {
        const charts = { ...this.charts };
        for (const chartId in charts) {
            this.history.update("charts", chartId, "fieldMatching", filterId, undefined);
        }
    }

    /**
     * @param {string} chartId
     * @param {Object} fieldMatching
     */
    _addLeewiseChart(chartId, fieldMatching = undefined) {
        const charts = { ...this.charts };
        if (!fieldMatching) {
            const model = this.getters.getChartDefinition(chartId).metaData.resModel;
            fieldMatching = this.getters.getFieldMatchingForModel(model);
        }
        charts[chartId] = {
            fieldMatching,
        };
        this.history.update("charts", charts);
    }
}

LeewiseChartCorePlugin.getters = [
    "getLeewiseChartIds",
    "getChartFieldMatch",
    "getLeewiseChartDisplayName",
    "getLeewiseChartFieldMatching",
];
