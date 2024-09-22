/** @leewise-module */

import { IrMenuSelector } from "@spreadsheet_edition/bundle/ir_menu_selector/ir_menu_selector";
import { Domain } from "@web/core/domain";
import { DomainSelector } from "@web/core/domain_selector/domain_selector";
import { DomainSelectorDialog } from "@web/core/domain_selector_dialog/domain_selector_dialog";
import { useService } from "@web/core/utils/hooks";
import { _t } from "@web/core/l10n/translation";

import { Component, onWillStart, onWillUpdateProps } from "@leewise/owl";

export class CommonLeewiseChartConfigPanel extends Component {
    setup() {
        this.dialog = useService("dialog");
        const loadData = async (figureId) => {
            const dataSource = this.env.model.getters.getChartDataSource(figureId);
            this.modelDisplayName = await dataSource.getModelLabel();
        };
        onWillStart(() => loadData(this.props.figureId));
        onWillUpdateProps((nextProps) => loadData(nextProps.figureId));
    }

    get model() {
        const definition = this.env.model.getters.getChartDefinition(this.props.figureId);
        return definition.metaData.resModel;
    }

    get domain() {
        const definition = this.env.model.getters.getChartDefinition(this.props.figureId);
        return new Domain(definition.searchParams.domain).toString();
    }

    onNameChanged(title) {
        const definition = {
            ...this.env.model.getters.getChartDefinition(this.props.figureId),
            title,
        };
        this.env.model.dispatch("UPDATE_CHART", {
            id: this.props.figureId,
            sheetId: this.env.model.getters.getFigureSheetId(this.props.figureId),
            definition,
        });
    }

    /**
     * Get the last update date, formatted
     *
     * @returns {string} date formatted
     */
    getLastUpdate() {
        const dataSource = this.env.model.getters.getChartDataSource(this.props.figureId);
        const lastUpdate = dataSource.lastUpdate;
        if (lastUpdate) {
            return new Date(lastUpdate).toLocaleTimeString();
        }
        return _t("never");
    }

    /**
     * Refresh the cache of the current chart
     */
    refresh() {
        this.env.model.dispatch("REFRESH_LEEWISE_CHART", { chartId: this.props.figureId });
    }

    openDomainEdition() {
        this.dialog.add(DomainSelectorDialog, {
            resModel: this.model,
            domain: new Domain(this.domain).toString(),
            isDebugMode: !!this.env.debug,
            onConfirm: (domain) => {
                const definition = this.env.model.getters.getChartDefinition(this.props.figureId);
                const updatedDefinition = {
                    ...definition,
                    searchParams: {
                        ...definition.searchParams,
                        domain: new Domain(domain).toJson(),
                    },
                };
                this.env.model.dispatch("UPDATE_CHART", {
                    id: this.props.figureId,
                    sheetId: this.env.model.getters.getFigureSheetId(this.props.figureId),
                    definition: updatedDefinition,
                });
            },
        });
    }

    get leewiseMenuId() {
        const menu = this.env.model.getters.getChartLeewiseMenu(this.props.figureId);
        return menu ? menu.id : undefined;
    }
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
    }
}

CommonLeewiseChartConfigPanel.template = "spreadsheet_edition.CommonLeewiseChartConfigPanel";
CommonLeewiseChartConfigPanel.components = { IrMenuSelector, DomainSelector };
CommonLeewiseChartConfigPanel.props = {
    figureId: String,
    definition: Object,
    updateChart: Function,
    canUpdateChart: Function,
};
