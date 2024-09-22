/** @leewise-module */

/**
 * This file is meant to load the different subparts of the module
 * to guarantee their plugins are loaded in the right order
 *
 * dependency:
 *             other plugins
 *                   |
 *                  ...
 *                   |
 *                filters
 *                /\    \
 *               /  \    \
 *           pivot  list  Leewise chart
 */

/** TODO: Introduce a position parameter to the plugin registry in order to load them in a specific order */
import * as spreadsheet from "@leewise/o-spreadsheet";
const { corePluginRegistry, coreViewsPluginRegistry } = spreadsheet.registries;

import { GlobalFiltersCorePlugin, GlobalFiltersUIPlugin } from "@spreadsheet/global_filters/index";
import { PivotCorePlugin, PivotUIPlugin } from "@spreadsheet/pivot/index"; // list depends on filter for its getters
import { ListCorePlugin, ListUIPlugin } from "@spreadsheet/list/index"; // pivot depends on filter for its getters
import {
    ChartLeewiseMenuPlugin,
    LeewiseChartCorePlugin,
    LeewiseChartUIPlugin,
} from "@spreadsheet/chart/index"; // Leewisechart depends on filter for its getters

corePluginRegistry.add("LeewiseGlobalFiltersCorePlugin", GlobalFiltersCorePlugin);
corePluginRegistry.add("LeewisePivotCorePlugin", PivotCorePlugin);
corePluginRegistry.add("LeewiseListCorePlugin", ListCorePlugin);
corePluginRegistry.add("leewiseChartCorePlugin", LeewiseChartCorePlugin);
corePluginRegistry.add("chartLeewiseMenuPlugin", ChartLeewiseMenuPlugin);

coreViewsPluginRegistry.add("LeewiseGlobalFiltersUIPlugin", GlobalFiltersUIPlugin);
coreViewsPluginRegistry.add("LeewisePivotUIPlugin", PivotUIPlugin);
coreViewsPluginRegistry.add("LeewiseListUIPlugin", ListUIPlugin);
coreViewsPluginRegistry.add("leewiseChartUIPlugin", LeewiseChartUIPlugin);
