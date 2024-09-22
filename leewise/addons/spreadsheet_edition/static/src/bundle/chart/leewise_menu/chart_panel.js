/** @leewise-module **/

import { patch } from "@web/core/utils/patch";
import * as spreadsheet from "@leewise/o-spreadsheet";
import { IrMenuSelector } from "@spreadsheet_edition/bundle/ir_menu_selector/ir_menu_selector";

const { LineBarPieConfigPanel, ScorecardChartConfigPanel, GaugeChartConfigPanel } =
    spreadsheet.components;

/**
 * Patch the chart configuration panel to add an input to
 * link the chart to an Leewise menu.
 */
function patchChartPanelWithMenu(PanelComponent) {
    patch(PanelComponent.prototype, {
        get leewiseMenuId() {
            const menu = this.env.model.getters.getChartLeewiseMenu(this.props.figureId);
            return menu ? menu.id : undefined;
        },
        /**
         * @param {number | undefined} leewiseMenuId
         */
        updateLeewiseLink(leewiseMenuId) {
            if (!leewiseMenuId) {
                this.env.model.dispatch("LINK_LEEWISE_MENU_TO_CHART", {
                    chartId: this.props.figureId,
                    leewiseMenuId: undefined,
                });
                return;
            }
            const menu = this.env.model.getters.getIrMenu(leewiseMenuId);
            this.env.model.dispatch("LINK_LEEWISE_MENU_TO_CHART", {
                chartId: this.props.figureId,
                leewiseMenuId: menu.xmlid || menu.id,
            });
        },
    });
    PanelComponent.components = {
        ...PanelComponent.components,
        IrMenuSelector,
    };
}
patchChartPanelWithMenu(LineBarPieConfigPanel);
patchChartPanelWithMenu(GaugeChartConfigPanel);
patchChartPanelWithMenu(ScorecardChartConfigPanel);
