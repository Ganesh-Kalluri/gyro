/** @leewise-module */

import { getLeewiseFunctions } from "../helpers/leewise_functions_helpers";

/** @typedef {import("@spreadsheet/helpers/leewise_functions_helpers").Token} Token */

/**
 * Parse a spreadsheet formula and detect the number of LIST functions that are
 * present in the given formula.
 *
 * @param {Token[]} tokens
 *
 * @returns {number}
 */
export function getNumberOfListFormulas(tokens) {
    return getLeewiseFunctions(tokens, ["LEEWISE.LIST", "LEEWISE.LIST.HEADER"]).length;
}

/**
 * Get the first List function description of the given formula.
 *
 * @param {Token[]} tokens
 *
 * @returns {import("../helpers/leewise_functions_helpers").LeewiseFunctionDescription|undefined}
 */
export function getFirstListFunction(tokens) {
    return getLeewiseFunctions(tokens, ["LEEWISE.LIST", "LEEWISE.LIST.HEADER"])[0];
}
