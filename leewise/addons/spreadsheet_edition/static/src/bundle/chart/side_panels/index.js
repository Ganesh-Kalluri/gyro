/** @leewise-module */

import * as spreadsheet from "@leewise/o-spreadsheet";
import { CommonLeewiseChartConfigPanel } from "./common/config_panel";
import { LeewiseBarChartConfigPanel } from "./leewise_bar/leewise_bar_config_panel";
import { LeewiseLineChartConfigPanel } from "./leewise_line/leewise_line_config_panel";

const { chartSidePanelComponentRegistry } = spreadsheet.registries;
const { LineBarPieDesignPanel } = spreadsheet.components;

chartSidePanelComponentRegistry
    .add("leewise_line", {
        configuration: LeewiseLineChartConfigPanel,
        design: LineBarPieDesignPanel,
    })
    .add("leewise_bar", {
        configuration: LeewiseBarChartConfigPanel,
        design: LineBarPieDesignPanel,
    })
    .add("leewise_pie", {
        configuration: CommonLeewiseChartConfigPanel,
        design: LineBarPieDesignPanel,
    });
