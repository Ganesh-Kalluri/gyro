/** @leewise-module */

import * as spreadsheet from "@leewise/o-spreadsheet";
import { _t } from "@web/core/l10n/translation";
import { LeewiseChart } from "./leewise_chart";

const { chartRegistry } = spreadsheet.registries;

const { getDefaultChartJsRuntime, chartFontColor, ChartColors } = spreadsheet.helpers;

chartRegistry.add("leewise_pie", {
    match: (type) => type === "leewise_pie",
    createChart: (definition, sheetId, getters) => new LeewiseChart(definition, sheetId, getters),
    getChartRuntime: createLeewiseChartRuntime,
    validateChartDefinition: (validator, definition) =>
        LeewiseChart.validateChartDefinition(validator, definition),
    transformDefinition: (definition) => LeewiseChart.transformDefinition(definition),
    getChartDefinitionFromContextCreation: () => LeewiseChart.getDefinitionFromContextCreation(),
    name: _t("Pie"),
});

function createLeewiseChartRuntime(chart, getters) {
    const background = chart.background || "#FFFFFF";
    const { datasets, labels } = chart.dataSource.getData();
    const locale = getters.getLocale();
    const chartJsConfig = getPieConfiguration(chart, labels, locale);
    const colors = new ChartColors();
    for (const { label, data } of datasets) {
        const backgroundColor = getPieColors(colors, datasets);
        const dataset = {
            label,
            data,
            borderColor: "#FFFFFF",
            backgroundColor,
        };
        chartJsConfig.data.datasets.push(dataset);
    }
    return { background, chartJsConfig };
}

function getPieConfiguration(chart, labels, locale) {
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
    config.options.plugins.tooltip = {
        callbacks: {
            title: function (tooltipItem) {
                return tooltipItem.label;
            },
        },
    };
    return config;
}

function getPieColors(colors, dataSetsValues) {
    const pieColors = [];
    const maxLength = Math.max(...dataSetsValues.map((ds) => ds.data.length));
    for (let i = 0; i <= maxLength; i++) {
        pieColors.push(colors.next());
    }

    return pieColors;
}
