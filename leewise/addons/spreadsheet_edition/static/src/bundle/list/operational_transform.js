/** @leewise-module */

import * as spreadsheet from "@leewise/o-spreadsheet";
const { otRegistry } = spreadsheet.registries;

otRegistry

    .addTransformation("INSERT_LEEWISE_LIST", ["INSERT_LEEWISE_LIST"], (toTransform) => ({
        ...toTransform,
        id: (parseInt(toTransform.id, 10) + 1).toString(),
    }))
    .addTransformation("REMOVE_LEEWISE_LIST", ["RENAME_LEEWISE_LIST"], (toTransform, executed) => {
        if (toTransform.listId === executed.listId) {
            return undefined;
        }
        return toTransform;
    })
    .addTransformation("REMOVE_LEEWISE_LIST", ["RE_INSERT_LEEWISE_LIST"], (toTransform, executed) => {
        if (toTransform.id === executed.listId) {
            return undefined;
        }
        return toTransform;
    });
