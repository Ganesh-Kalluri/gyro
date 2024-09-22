/** @leewise-module */

import * as spreadsheet from "@leewise/o-spreadsheet";
import { _t } from "@web/core/l10n/translation";
import { LeewiseChart } from "./leewise_chart";

const { chartRegistry } = spreadsheet.registries;

const { getDefaultChartJsRuntime, chartFontColor, ChartColors } = spreadsheet.helpers;

export class LeewiseBarChart extends LeewiseChart {
    constructor(definition, sheetId, getters) {
        super(definition, sheetId, getters);
        this.verticalAxisPosition = definition.verticalAxisPosition;
        this.stacked = definition.stacked;
    }

    getDefinition() {
        return {
            ...super.getDefinition(),
            verticalAxisPosition: this.verticalAxisPosition,
            stacked: this.stacked,
        };
    }
}

chartRegistry.add("leewise_bar", {
    match: (type) => type === "leewise_bar",
    createChart: (definition, sheetId, getters) => new LeewiseBarChart(definition, sheetId, getters),
    getChartRuntime: createLeewiseChartRuntime,
    validateChartDefinition: (validator, definition) =>
        LeewiseBarChart.validateChartDefinition(validator, definition),
    transformDefinition: (definition) => LeewiseBarChart.transformDefinition(definition),
    getChartDefinitionFromContextCreation: () => LeewiseBarChart.getDefinitionFromContextCreation(),
    name: _t("Bar"),
});

function createLeewiseChartRuntime(chart, getters) {
    const background = chart.background || "#FFFFFF";
    const { datasets, labels } = chart.dataSource.getData();
    const locale = getters.getLocale();
    const chartJsConfig = getBarConfiguration(chart, labels, locale);
    const colors = new ChartColors();
    for (const { label, data } of datasets) {
        const color = colors.next();
        const dataset = {
            label,
            data,
            borderColor: color,
            backgroundColor: color,
        };
        chartJsConfig.data.datasets.push(dataset);
    }

    return { background, chartJsConfig };
}

function getBarConfiguration(chart, labels, locale) {
    const fontColor = chartFontColor(chart.background);
    const config = getDefaultChartJsRuntime(chart, labels, fontColor, { locale });
    config.type = chart.type.replace("leewise_", "");
    const legend = {
        ...config.options.legend,
        display: chart.legendPosition !== "none",
        labels: { fontColor },
    };
    legend.position = chart.legendPosition;
    config.options.plugins = config.options.plugins || {};
    config.options.plugins.legend = legend;
    config.options.layout = {
        padding: { left: 20, right: 20, top: chart.title ? 10 : 25, bottom: 10 },
    };
    config.options.scales = {
        x: {
            ticks: {
                // x axis configuration
                maxRotation: 60,
                minRotation: 15,
                padding: 5,
                labelOffset: 2,
                color: fontColor,
            },
        },
        y: {
            position: chart.verticalAxisPosition,
            ticks: {
                color: fontColor,
                // y axis configuration
            },
            beginAtZero: true, // the origin of the y axis is always zero
        },
    };
    if (chart.stacked) {
        config.options.scales.x.stacked = true;
        config.options.scales.y.stacked = true;
    }
    return config;
}
