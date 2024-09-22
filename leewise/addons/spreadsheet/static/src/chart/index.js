/** @leewise-module */

import * as spreadsheet from "@leewise/o-spreadsheet";

const { chartComponentRegistry } = spreadsheet.registries;
const { ChartJsComponent } = spreadsheet.components;

chartComponentRegistry.add("leewise_bar", ChartJsComponent);
chartComponentRegistry.add("leewise_line", ChartJsComponent);
chartComponentRegistry.add("leewise_pie", ChartJsComponent);

import { LeewiseChartCorePlugin } from "./plugins/leewise_chart_core_plugin";
import { ChartLeewiseMenuPlugin } from "./plugins/chart_leewise_menu_plugin";
import { LeewiseChartUIPlugin } from "./plugins/leewise_chart_ui_plugin";

export { LeewiseChartCorePlugin, ChartLeewiseMenuPlugin, LeewiseChartUIPlugin };
