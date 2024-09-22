/** @leewise-module */

import { AbstractChart, CommandResult } from "@leewise/o-spreadsheet";
import { ChartDataSource } from "../data_source/chart_data_source";

/**
 * @typedef {import("@web/search/search_model").SearchParams} SearchParams
 *
 * @typedef MetaData
 * @property {Array<Object>} domains
 * @property {Array<string>} groupBy
 * @property {string} measure
 * @property {string} mode
 * @property {string} [order]
 * @property {string} resModel
 * @property {boolean} stacked
 *
 * @typedef LeewiseChartDefinition
 * @property {string} type
 * @property {MetaData} metaData
 * @property {SearchParams} searchParams
 * @property {string} title
 * @property {string} background
 * @property {string} legendPosition
 * @property {boolean} cumulative
 *
 * @typedef LeewiseChartDefinitionDataSource
 * @property {MetaData} metaData
 * @property {SearchParams} searchParams
 *
 */

export class LeewiseChart extends AbstractChart {
    /**
     * @param {LeewiseChartDefinition} definition
     * @param {string} sheetId
     * @param {Object} getters
     */
    constructor(definition, sheetId, getters) {
        super(definition, sheetId, getters);
        this.type = definition.type;
        this.metaData = {
            ...definition.metaData,
            mode: this.type.replace("leewise_", ""),
            cumulated: definition.cumulative,
            // if a chart is cumulated, the first data point should take into
            // account past data, even if a domain on a specific period is applied
            cumulatedStart: definition.cumulative,
        };
        this.searchParams = definition.searchParams;
        this.legendPosition = definition.legendPosition;
        this.background = definition.background;
        this.dataSource = undefined;
    }

    static transformDefinition(definition) {
        return definition;
    }

    static validateChartDefinition(validator, definition) {
        return CommandResult.Success;
    }

    static getDefinitionFromContextCreation() {
        throw new Error("It's not possible to convert an Leewise chart to a native chart");
    }

    /**
     * @returns {LeewiseChartDefinitionDataSource}
     */
    getDefinitionForDataSource() {
        return {
            metaData: this.metaData,
            searchParams: this.searchParams,
        };
    }

    /**
     * @returns {LeewiseChartDefinition}
     */
    getDefinition() {
        return {
            //@ts-ignore Defined in the parent class
            title: this.title,
            background: this.background,
            legendPosition: this.legendPosition,
            metaData: this.metaData,
            searchParams: this.searchParams,
            type: this.type,
        };
    }

    getDefinitionForExcel() {
        // Export not supported
        return undefined;
    }

    /**
     * @returns {LeewiseChart}
     */
    updateRanges() {
        // No range on this graph
        return this;
    }

    /**
     * @returns {LeewiseChart}
     */
    copyForSheetId() {
        return this;
    }

    /**
     * @returns {LeewiseChart}
     */
    copyInSheetId() {
        return this;
    }

    getContextCreation() {
        return {};
    }

    getSheetIdsUsedInChartRanges() {
        return [];
    }

    setDataSource(dataSource) {
        if (dataSource instanceof ChartDataSource) {
            this.dataSource = dataSource;
        } else {
            throw new Error("Only ChartDataSources can be added.");
        }
    }
}
