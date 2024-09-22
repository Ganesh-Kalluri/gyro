/** @leewise-module */

import * as spreadsheet from "@leewise/o-spreadsheet";
const { inverseCommandRegistry, otRegistry } = spreadsheet.registries;

function identity(cmd) {
    return [cmd];
}

otRegistry.addTransformation(
    "DELETE_FIGURE",
    ["LINK_LEEWISE_MENU_TO_CHART"],
    (toTransform, executed) => {
        if (executed.id === toTransform.chartId) {
            return undefined;
        }
        return toTransform;
    }
);

inverseCommandRegistry.add("LINK_LEEWISE_MENU_TO_CHART", identity);
