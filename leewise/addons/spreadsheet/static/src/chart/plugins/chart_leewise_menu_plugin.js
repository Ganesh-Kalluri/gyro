/** @leewise-module */

import { coreTypes, CorePlugin } from "@leewise/o-spreadsheet";

/** Plugin that link charts with Leewise menus. It can contain either the Id of the leewise menu, or its xml id. */
export class ChartLeewiseMenuPlugin extends CorePlugin {
    constructor(config) {
        super(config);
        this.leewiseMenuReference = {};
    }

    /**
     * Handle a spreadsheet command
     * @param {Object} cmd Command
     */
    handle(cmd) {
        switch (cmd.type) {
            case "LINK_LEEWISE_MENU_TO_CHART":
                this.history.update("leewiseMenuReference", cmd.chartId, cmd.leewiseMenuId);
                break;
            case "DELETE_FIGURE":
                this.history.update("leewiseMenuReference", cmd.id, undefined);
                break;
        }
    }

    /**
     * Get leewise menu linked to the chart
     *
     * @param {string} chartId
     * @returns {object | undefined}
     */
    getChartLeewiseMenu(chartId) {
        const menuId = this.leewiseMenuReference[chartId];
        return menuId ? this.getters.getIrMenu(menuId) : undefined;
    }

    import(data) {
        if (data.chartLeewiseMenusReferences) {
            this.leewiseMenuReference = data.chartLeewiseMenusReferences;
        }
    }

    export(data) {
        data.chartLeewiseMenusReferences = this.leewiseMenuReference;
    }
}
ChartLeewiseMenuPlugin.getters = ["getChartLeewiseMenu"];

coreTypes.add("LINK_LEEWISE_MENU_TO_CHART");
