/** @leewise-module */

import * as spreadsheet from "@leewise/o-spreadsheet";
import { Domain } from "@web/core/domain";
import { globalFiltersFieldMatchers } from "@spreadsheet/global_filters/plugins/global_filters_core_plugin";
import { ChartDataSource } from "../data_source/chart_data_source";
import { sprintf } from "@web/core/utils/strings";
import { _t } from "@web/core/l10n/translation";

const { UIPlugin } = spreadsheet;

export class LeewiseChartUIPlugin extends UIPlugin {
    constructor(config) {
        super(config);
        this.dataSources = config.custom.dataSources;

        globalFiltersFieldMatchers["chart"] = {
            ...globalFiltersFieldMatchers["chart"],
            getTag: async (chartId) => {
                const model = await this.getChartDataSource(chartId).getModelLabel();
                return sprintf(_t("Chart - %s"), model);
            },
            waitForReady: () => this._getLeewiseChartsWaitForReady(),
            getFields: (chartId) => this.getChartDataSource(chartId).getFields(),
        };
    }

    beforeHandle(cmd) {
        switch (cmd.type) {
            case "START":
                for (const chartId of this.getters.getLeewiseChartIds()) {
                    this._setupChartDataSource(chartId);
                }

                // make sure the domains are correctly set before
                // any evaluation
                this._addDomains();
                break;
        }
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
                        this._setupChartDataSource(cmd.id);
                        break;
                }
                break;
            }
            case "UPDATE_CHART": {
                switch (cmd.definition.type) {
                    case "leewise_pie":
                    case "leewise_bar":
                    case "leewise_line": {
                        const dataSource = this.getChartDataSource(cmd.id);
                        if (
                            dataSource.getInitialDomainString() !==
                            new Domain(cmd.definition.searchParams.domain).toString()
                        ) {
                            this._resetChartDataSource(cmd.id);
                        }
                        this._setChartDataSource(cmd.id);
                        break;
                    }
                }
                break;
            }
            case "ADD_GLOBAL_FILTER":
            case "EDIT_GLOBAL_FILTER":
            case "REMOVE_GLOBAL_FILTER":
            case "SET_GLOBAL_FILTER_VALUE":
            case "CLEAR_GLOBAL_FILTER_VALUE":
                this._addDomains();
                break;
            case "UNDO":
            case "REDO": {
                if (
                    cmd.commands.find((command) =>
                        [
                            "ADD_GLOBAL_FILTER",
                            "EDIT_GLOBAL_FILTER",
                            "REMOVE_GLOBAL_FILTER",
                        ].includes(command.type)
                    )
                ) {
                    this._addDomains();
                }

                const domainEditionCommands = cmd.commands.filter(
                    (cmd) => cmd.type === "UPDATE_CHART" || cmd.type === "CREATE_CHART"
                );
                for (const cmd of domainEditionCommands) {
                    if (!this.getters.getLeewiseChartIds().includes(cmd.id)) {
                        continue;
                    }
                    const dataSource = this.getChartDataSource(cmd.id);
                    if (
                        dataSource.getInitialDomainString() !==
                        new Domain(cmd.definition.searchParams.domain).toString()
                    ) {
                        this._resetChartDataSource(cmd.id);
                    }
                }
                break;
            }
            case "REFRESH_LEEWISE_CHART":
                this._refreshLeewiseChart(cmd.chartId);
                break;
            case "REFRESH_ALL_DATA_SOURCES":
                this._refreshLeewiseCharts();
                break;
        }
    }

    /**
     * @param {string} chartId
     * @returns {ChartDataSource|undefined}
     */
    getChartDataSource(chartId) {
        const dataSourceId = this._getLeewiseChartDataSourceId(chartId);
        return this.dataSources.get(dataSourceId);
    }

    // -------------------------------------------------------------------------
    // Private
    // -------------------------------------------------------------------------

    /**
     * Add an additional domain to a chart
     *
     * @private
     *
     * @param {string} chartId chart id
     */
    _addDomain(chartId) {
        const domainList = [];
        for (const [filterId, fieldMatch] of Object.entries(
            this.getters.getChartFieldMatch(chartId)
        )) {
            domainList.push(this.getters.getGlobalFilterDomain(filterId, fieldMatch));
        }
        const domain = Domain.combine(domainList, "AND").toString();
        this.getChartDataSource(chartId).addDomain(domain);
    }

    /**
     * Add an additional domain to all chart
     *
     * @private
     *
     */
    _addDomains() {
        for (const chartId of this.getters.getLeewiseChartIds()) {
            this._addDomain(chartId);
        }
    }

    /**
     * @param {string} chartId
     * @param {string} dataSourceId
     */
    _setupChartDataSource(chartId) {
        const dataSourceId = this._getLeewiseChartDataSourceId(chartId);
        if (!this.dataSources.contains(dataSourceId)) {
            this._resetChartDataSource(chartId);
        }
        this._setChartDataSource(chartId);
    }

    /**
     * Sets the datasource on the corresponding chart
     * @param {string} chartId
     */
    _resetChartDataSource(chartId) {
        const definition = this.getters.getChart(chartId).getDefinitionForDataSource();
        const dataSourceId = this._getLeewiseChartDataSourceId(chartId);
        this.dataSources.add(dataSourceId, ChartDataSource, definition);
    }

    /**
     * Sets the datasource on the corresponding chart
     * @param {string} chartId
     */
    _setChartDataSource(chartId) {
        const chart = this.getters.getChart(chartId);
        chart.setDataSource(this.getChartDataSource(chartId));
    }

    /**
     *
     * @return {Promise[]}
     */
    _getLeewiseChartsWaitForReady() {
        return this.getters
            .getLeewiseChartIds()
            .map((chartId) => this.getChartDataSource(chartId).loadMetadata());
    }

    _getLeewiseChartDataSourceId(chartId) {
        return `chart-${chartId}`;
    }

    /**
     * Refresh the cache of a chart
     * @param {string} chartId Id of the chart
     */
    _refreshLeewiseChart(chartId) {
        this.getChartDataSource(chartId).load({ reload: true });
    }

    /**
     * Refresh the cache of all the charts
     */
    _refreshLeewiseCharts() {
        for (const chartId of this.getters.getLeewiseChartIds()) {
            this._refreshLeewiseChart(chartId);
        }
    }
}

LeewiseChartUIPlugin.getters = ["getChartDataSource"];
