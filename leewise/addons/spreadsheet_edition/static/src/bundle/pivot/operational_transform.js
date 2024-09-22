/** @leewise-module */

import * as spreadsheet from "@leewise/o-spreadsheet";
const { otRegistry } = spreadsheet.registries;

otRegistry
    .addTransformation("INSERT_PIVOT", ["INSERT_PIVOT"], (toTransform) => ({
        ...toTransform,
        id: (parseInt(toTransform.id, 10) + 1).toString(),
    }))
    .addTransformation("REMOVE_PIVOT", ["RENAME_LEEWISE_PIVOT"], (toTransform, executed) => {
        if (toTransform.pivotId === executed.pivotId) {
            return undefined;
        }
        return toTransform;
    })
    .addTransformation("REMOVE_PIVOT", ["RE_INSERT_PIVOT"], (toTransform, executed) => {
        if (toTransform.id === executed.pivotId) {
            return undefined;
        }
        return toTransform;
    });
